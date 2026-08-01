"""
Serveur MCP (Model Context Protocol) — Base de connaissances Bâtiment
Protocole : MCP 2025-06-18 — JSON-RPC 2.0 Streamable HTTP + OAuth 2.1 complet

v7.0 — OAuth 2.1 complet compatible Claude.ai
       RFC 9728 : Protected Resource Metadata
       RFC 8414 : Authorization Server Metadata
       RFC 7591 : Dynamic Client Registration
       OAuth 2.1 + PKCE S256 obligatoire
       Pages HTML login + consentement
"""

import os
import json
import uuid
import hashlib
import base64
import secrets
import time
import requests
import psycopg2
import psycopg2.extras
from contextlib import contextmanager
from urllib.parse import urlencode, urlparse, parse_qs
from fastapi import FastAPI, Request, HTTPException, Form, Query
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# ─── Configuration ────────────────────────────────────────────────────────────
PG_HOST      = os.environ.get("PG_HOST", "forge-postgres")
PG_PORT      = int(os.environ.get("PG_PORT", "5432"))
PG_DB        = os.environ.get("PG_DB", "batiment_knowledge")
PG_USER      = os.environ.get("PG_USER", "createk")
PG_PASSWORD  = os.environ.get("PG_PASSWORD", "Forge2026Hozzo!")

EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
EMBEDDING_DIMS       = 768

OPENROUTER_API_KEY  = os.environ.get("OPENROUTER_API_KEY", "")
SYNTHESIS_MODEL     = "openai/gpt-4o-mini"
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

# URL publique du serveur (sans slash final)
SERVER_BASE_URL = os.environ.get("SERVER_BASE_URL", "https://knowledge.ozzo.fr")
PORT            = int(os.environ.get("PORT", "8100"))

MCP_VERSION    = "2025-03-26"
SERVER_NAME    = "batiment-knowledge"
SERVER_VERSION = "7.0.0"

# Credentials admin pour la page de login
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "ozzo")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Batiment2026!")

# ─── Stockage en mémoire (OAuth state) ───────────────────────────────────────
# En production on utiliserait Redis/DB, mais pour un usage mono-user c'est suffisant
_oauth_clients: dict  = {}   # client_id -> client_data
_auth_codes: dict     = {}   # code -> {client_id, redirect_uri, code_challenge, scope, expires}
_access_tokens: dict  = {}   # token -> {client_id, scope, expires}
_sessions: dict       = {}   # session_id -> {initialized}

# ─── App FastAPI ──────────────────────────────────────────────────────────────
app = FastAPI(title="Batiment Knowledge MCP", version=SERVER_VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Labels de fiabilité ──────────────────────────────────────────────────────
FIABILITE_LABELS = {
    "patrimoine":        "Patrimoine XIXe s.",
    "technique-ancien":  "Technique XIXe-XXe s.",
    "technique-moderne": "Technique moderne",
    "norme-en-vigueur":  "Norme en vigueur",
    "synthese-ia":       "Synthèse IA (non sourcée)",
}

# ─── Modèle d'embedding ───────────────────────────────────────────────────────
_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        from sentence_transformers import SentenceTransformer
        print(f"[MCP] Chargement du modèle : {EMBEDDING_MODEL_NAME}")
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        print(f"[MCP] Modèle chargé — {_embedding_model.get_sentence_embedding_dimension()} dims")
    return _embedding_model

# ─── PostgreSQL ───────────────────────────────────────────────────────────────
@contextmanager
def get_db():
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASSWORD, connect_timeout=10
    )
    try:
        yield conn
    finally:
        conn.close()

# ─── Outils MCP ───────────────────────────────────────────────────────────────
MCP_TOOLS = [
    {
        "name": "search_batiment",
        "title": "Recherche dans la base bâtiment",
        "description": (
            "Recherche sémantique dans la base de connaissances sur les métiers du bâtiment. "
            "Retourne les passages les plus pertinents issus d'ouvrages techniques (Champly, "
            "Rondelet, Barberot, Viollet-le-Duc, Planat, etc.)."
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False},
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "La question ou le sujet à rechercher"},
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel)",
                    "enum": ["maconnerie","charpente-couverture","plomberie-chauffage",
                             "electricite","menuiserie","platrerie-peinture",
                             "isolation-etancheite","gros-oeuvre","encyclopedie-generale",
                             "pathologies","normes-reglements","materiaux"]
                },
                "nb_resultats": {"type": "integer", "description": "Nombre de résultats (défaut: 5, max: 10)", "default": 5, "minimum": 1, "maximum": 10}
            },
            "required": ["query"]
        }
    },
    {
        "name": "ask_batiment",
        "title": "Question technique bâtiment",
        "description": (
            "Pose une question sur les métiers du bâtiment et obtient une réponse synthétisée "
            "par un LLM à partir des sources de la base de connaissances."
        ),
        "annotations": {"readOnlyHint": True, "destructiveHint": False},
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "La question technique à poser"},
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel)",
                    "enum": ["maconnerie","charpente-couverture","plomberie-chauffage",
                             "electricite","menuiserie","platrerie-peinture",
                             "isolation-etancheite","gros-oeuvre","encyclopedie-generale",
                             "pathologies","normes-reglements","materiaux"]
                },
                "nb_sources": {"type": "integer", "description": "Nombre de sources (défaut: 5, max: 8)", "default": 5, "minimum": 1, "maximum": 8}
            },
            "required": ["question"]
        }
    },
    {
        "name": "list_sources",
        "title": "Lister les sources indexées",
        "description": "Liste toutes les sources indexées dans la base de connaissances bâtiment.",
        "annotations": {"readOnlyHint": True, "destructiveHint": False},
        "inputSchema": {
            "type": "object",
            "properties": {
                "corps_etat": {"type": "string", "description": "Filtrer par corps d'état (optionnel)"}
            }
        }
    },
    {
        "name": "get_stats",
        "title": "Statistiques de la base",
        "description": "Retourne les statistiques de la base de connaissances bâtiment.",
        "annotations": {"readOnlyHint": True, "destructiveHint": False},
        "inputSchema": {"type": "object", "properties": {}}
    }
]

# ─── Fonctions métier ─────────────────────────────────────────────────────────

def get_embedding(text: str) -> list:
    model = get_embedding_model()
    return model.encode(text, show_progress_bar=False).tolist()

def search_in_db(query: str, corps_etat: str = None, nb_resultats: int = 5) -> list:
    embedding = get_embedding(query)
    emb_str = "[" + ",".join(str(x) for x in embedding) + "]"
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if corps_etat:
            cur.execute("""
                SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                       annee_publication, fiabilite,
                       1 - (embedding <=> %s::vector) AS similarity
                FROM batiment_chunks
                WHERE corps_etat = %s AND embedding IS NOT NULL
                  AND 1 - (embedding <=> %s::vector) > 0.2
                ORDER BY embedding <=> %s::vector LIMIT %s
            """, (emb_str, corps_etat, emb_str, emb_str, nb_resultats))
        else:
            cur.execute("""
                SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                       annee_publication, fiabilite,
                       1 - (embedding <=> %s::vector) AS similarity
                FROM batiment_chunks
                WHERE embedding IS NOT NULL
                  AND 1 - (embedding <=> %s::vector) > 0.2
                ORDER BY embedding <=> %s::vector LIMIT %s
            """, (emb_str, emb_str, emb_str, nb_resultats))
        return [dict(row) for row in cur.fetchall()]

def format_source_badge(r: dict) -> str:
    auteur = r.get("auteur"); annee = r.get("annee_publication"); fiabilite = r.get("fiabilite", "")
    if auteur and annee:
        return f"{auteur} ({annee}) — *{FIABILITE_LABELS.get(fiabilite, fiabilite)}*"
    return r.get("source", "N/A")

def detect_divergences(passages: list) -> str:
    if len(passages) < 2: return ""
    anciens   = [p for p in passages if p.get("fiabilite") in ("patrimoine","technique-ancien")]
    modernes  = [p for p in passages if p.get("fiabilite") in ("technique-moderne","norme-en-vigueur")]
    syntheses = [p for p in passages if p.get("fiabilite") == "synthese-ia"]
    notes = []
    if syntheses:
        notes.append("⚠️ **Synthèse IA** : certains résultats proviennent de fiches synthétiques rédigées par IA (OzzO Knowledge Base), non issues de sources primaires.")
    if anciens and modernes:
        aa = [p["annee_publication"] for p in anciens  if p.get("annee_publication")]
        am = [p["annee_publication"] for p in modernes if p.get("annee_publication")]
        if aa and am and (min(am) - max(aa)) > 50:
            na = list(set(p.get("auteur","?") for p in anciens  if p.get("auteur")))
            nm = list(set(p.get("auteur","?") for p in modernes if p.get("auteur")))
            notes.append(f"⚠️ **Sources d'époques différentes** : sources anciennes ({', '.join(na[:2])}, ~{max(aa)}) vs modernes ({', '.join(nm[:2])}, ~{min(am)}). Privilégier les sources modernes pour les pratiques actuelles.")
    return ("\n\n> " + "\n> ".join(notes)) if notes else ""

def synthesize_with_llm(question: str, passages: list) -> str:
    ctx = "\n\n---\n\n".join(
        f"[Source {i}: {p.get('auteur','?')} ({p.get('annee_publication','?')}) [{FIABILITE_LABELS.get(p.get('fiabilite',''),'')}]]\n{p.get('content','')[:1200]}"
        for i, p in enumerate(passages, 1)
    )
    anciens  = [p for p in passages if p.get("fiabilite") in ("patrimoine","technique-ancien")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne","norme-en-vigueur")]
    div = ("\nATTENTION : sources d'époques différentes. Signale les divergences." if anciens and modernes else "")
    r = requests.post(
        OPENROUTER_CHAT_URL,
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"},
        json={"model": SYNTHESIS_MODEL, "messages": [
            {"role": "system", "content": "Tu es un expert en techniques du bâtiment. Réponds UNIQUEMENT à partir des passages fournis. Réponse structurée, précise, sourcée (auteur + année), en français." + div},
            {"role": "user", "content": f"Question : {question}\n\nPassages :\n\n{ctx}\n\nRéponds en citant les sources."}
        ], "max_tokens": 1500, "temperature": 0.3},
        timeout=60
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def get_sources_from_db(corps_etat=None):
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if corps_etat:
            cur.execute("SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage, annee_publication, fiabilite FROM batiment_chunks WHERE corps_etat = %s ORDER BY corps_etat, annee_publication NULLS LAST LIMIT 300", (corps_etat,))
        else:
            cur.execute("SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage, annee_publication, fiabilite FROM batiment_chunks ORDER BY corps_etat, annee_publication NULLS LAST LIMIT 300")
        return [dict(r) for r in cur.fetchall()]

def get_stats_from_db():
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS total FROM batiment_chunks"); total = cur.fetchone()["total"]
        cur.execute("SELECT corps_etat, COUNT(*) AS n FROM batiment_chunks GROUP BY corps_etat ORDER BY n DESC")
        corps = {r["corps_etat"]: r["n"] for r in cur.fetchall()}
        cur.execute("SELECT fiabilite, COUNT(*) AS n FROM batiment_chunks WHERE fiabilite IS NOT NULL GROUP BY fiabilite ORDER BY n DESC")
        fids = {r["fiabilite"]: r["n"] for r in cur.fetchall()}
        cur.execute("SELECT COUNT(DISTINCT auteur) AS n FROM batiment_chunks WHERE auteur IS NOT NULL")
        nb_a = cur.fetchone()["n"]
        return {"total_chunks": total, "repartition_corps_etat": corps, "repartition_fiabilite": fids, "nb_auteurs_uniques": nb_a, "embedding_model": EMBEDDING_MODEL_NAME, "embedding_dims": EMBEDDING_DIMS}

def execute_tool(name: str, arguments: dict) -> list:
    if name == "search_batiment":
        query = arguments.get("query",""); corps_etat = arguments.get("corps_etat"); nb = min(int(arguments.get("nb_resultats",5)),10)
        if not query: return [{"type":"text","text":"Erreur : 'query' requis."}]
        results = search_in_db(query, corps_etat, nb)
        if not results: return [{"type":"text","text":"Aucun résultat trouvé."}]
        parts = [f"**{len(results)} résultat(s) pour : \"{query}\"**\n"]
        for i, r in enumerate(results, 1):
            sim = round(float(r.get("similarity",0))*100,1); txt = r.get("content",""); badge = format_source_badge(r)
            if txt.startswith("[") and "]" in txt[:200]:
                end = txt.index("]"); section = txt[1:end]; preview = txt[end+2:end+802]
            else:
                section = ""; preview = txt[:800]
            parts.append(f"\n---\n**[{i}]** `{corps_etat or r.get('corps_etat','N/A')}` | **{badge}**  \n" + (f"*Section : {section}*  \n" if section else "") + f"Pertinence : {sim}%\n\n{preview}...")
        return [{"type":"text","text":"\n".join(parts) + detect_divergences(results)}]

    elif name == "ask_batiment":
        question = arguments.get("question",""); corps_etat = arguments.get("corps_etat"); nb = min(int(arguments.get("nb_sources",5)),8)
        if not question: return [{"type":"text","text":"Erreur : 'question' requis."}]
        if not OPENROUTER_API_KEY: return [{"type":"text","text":"Erreur : clé OpenRouter non configurée."}]
        passages = search_in_db(question, corps_etat, nb)
        if not passages: return [{"type":"text","text":"Aucune information trouvée."}]
        answer = synthesize_with_llm(question, passages)
        seen, lines = set(), []
        for p in passages:
            auteur = p.get("auteur") or p.get("source","N/A"); annee = p.get("annee_publication"); label = FIABILITE_LABELS.get(p.get("fiabilite",""),""); titre = p.get("titre_ouvrage") or p.get("source","N/A")
            key = f"{auteur}_{annee}"
            if key not in seen:
                seen.add(key); lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}" if annee else f"- {titre}")
        return [{"type":"text","text":f"{answer}\n\n---\n**Sources :**\n" + "\n".join(lines[:6]) + detect_divergences(passages)}]

    elif name == "list_sources":
        sources = get_sources_from_db(arguments.get("corps_etat"))
        lines = ["**Sources indexées :**\n"]; current = None
        for s in sources:
            ce = s.get("corps_etat","N/A")
            if ce != current: lines.append(f"\n### {ce}"); current = ce
            auteur = s.get("auteur"); annee = s.get("annee_publication"); label = FIABILITE_LABELS.get(s.get("fiabilite",""),""); titre = s.get("titre_ouvrage") or s.get("source","N/A")
            lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}" if auteur and annee else f"- {titre}")
        return [{"type":"text","text":"\n".join(lines)}]

    elif name == "get_stats":
        stats = get_stats_from_db()
        lines = [f"**Statistiques base bâtiment (PostgreSQL HOZZO)**\n", f"- Total chunks : **{stats['total_chunks']}**", f"- Auteurs uniques : **{stats['nb_auteurs_uniques']}**", f"- Modèle : `{stats['embedding_model']}` ({stats['embedding_dims']} dims)", "", "**Par corps d'état :**"]
        for ce, nb in sorted(stats["repartition_corps_etat"].items(), key=lambda x: -x[1]): lines.append(f"  - `{ce}` : {nb}")
        lines += ["","**Par fiabilité :**"]
        for fid, nb in stats["repartition_fiabilite"].items(): lines.append(f"  - *{FIABILITE_LABELS.get(fid,fid)}* : {nb}")
        return [{"type":"text","text":"\n".join(lines)}]

    else:
        raise ValueError(f"Outil inconnu : {name}")

# ─── Helpers JSON-RPC ─────────────────────────────────────────────────────────
def jrpc_ok(req_id, result): return {"jsonrpc":"2.0","id":req_id,"result":result}
def jrpc_err(req_id, code, msg): return {"jsonrpc":"2.0","id":req_id,"error":{"code":code,"message":msg}}

def verify_token(request: Request) -> bool:
    auth = request.headers.get("Authorization","")
    if not auth.startswith("Bearer "): return False
    token = auth[7:]
    entry = _access_tokens.get(token)
    if not entry: return False
    if entry["expires"] < time.time(): del _access_tokens[token]; return False
    return True

def unauthorized_response():
    """Retourne 401 avec WWW-Authenticate pointant vers le resource metadata (RFC 9728)."""
    resource_metadata_url = f"{SERVER_BASE_URL}/.well-known/oauth-protected-resource"
    return JSONResponse(
        status_code=401,
        content={"error": "unauthorized", "error_description": "Bearer token required"},
        headers={"WWW-Authenticate": f'Bearer resource_metadata="{resource_metadata_url}"'}
    )

# ─── OAuth 2.1 — Discovery documents ─────────────────────────────────────────

@app.get("/.well-known/oauth-protected-resource")
@app.get("/.well-known/oauth-protected-resource/mcp")
def oauth_protected_resource():
    """RFC 9728 — Protected Resource Metadata."""
    return JSONResponse({
        "resource": SERVER_BASE_URL,
        "authorization_servers": [SERVER_BASE_URL],
        "bearer_methods_supported": ["header"],
        "scopes_supported": ["mcp"],
        "resource_documentation": f"{SERVER_BASE_URL}/docs"
    })

@app.get("/.well-known/oauth-authorization-server")
def oauth_authorization_server():
    """RFC 8414 — Authorization Server Metadata."""
    return JSONResponse({
        "issuer": SERVER_BASE_URL,
        "authorization_endpoint": f"{SERVER_BASE_URL}/authorize",
        "token_endpoint": f"{SERVER_BASE_URL}/token",
        "registration_endpoint": f"{SERVER_BASE_URL}/register",
        "scopes_supported": ["mcp"],
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code"],
        "code_challenge_methods_supported": ["S256"],
        "token_endpoint_auth_methods_supported": ["none"],
        "service_documentation": f"{SERVER_BASE_URL}/docs"
    })

# ─── OAuth 2.1 — Dynamic Client Registration (RFC 7591) ──────────────────────

@app.post("/register")
async def register_client(request: Request):
    """RFC 7591 — Dynamic Client Registration."""
    try:
        body = await request.json()
    except Exception:
        body = {}
    client_id     = str(uuid.uuid4())
    client_name   = body.get("client_name", "MCP Client")
    redirect_uris = body.get("redirect_uris", [])
    _oauth_clients[client_id] = {
        "client_id": client_id,
        "client_name": client_name,
        "redirect_uris": redirect_uris,
        "grant_types": ["authorization_code"],
        "response_types": ["code"],
        "token_endpoint_auth_method": "none",
        "created_at": time.time()
    }
    return JSONResponse(status_code=201, content={
        "client_id": client_id,
        "client_name": client_name,
        "redirect_uris": redirect_uris,
        "grant_types": ["authorization_code"],
        "response_types": ["code"],
        "token_endpoint_auth_method": "none"
    })

# ─── OAuth 2.1 — Authorization endpoint ──────────────────────────────────────

LOGIN_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Connexion — Base de connaissances Bâtiment</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f5f0; display: flex; align-items: center; justify-content: center; min-height: 100vh; }}
  .card {{ background: white; border-radius: 12px; padding: 40px; width: 100%; max-width: 400px; box-shadow: 0 4px 24px rgba(0,0,0,0.08); }}
  .logo {{ text-align: center; margin-bottom: 24px; }}
  .logo-icon {{ font-size: 48px; }}
  h1 {{ font-size: 22px; font-weight: 600; color: #1a1a1a; text-align: center; margin-bottom: 6px; }}
  .subtitle {{ font-size: 14px; color: #666; text-align: center; margin-bottom: 28px; }}
  .app-info {{ background: #f8f9fa; border-radius: 8px; padding: 12px 16px; margin-bottom: 24px; font-size: 13px; color: #444; }}
  .app-info strong {{ color: #1a1a1a; }}
  label {{ display: block; font-size: 13px; font-weight: 500; color: #333; margin-bottom: 6px; }}
  input {{ width: 100%; padding: 10px 14px; border: 1px solid #ddd; border-radius: 8px; font-size: 15px; outline: none; transition: border-color 0.2s; }}
  input:focus {{ border-color: #2563eb; }}
  .field {{ margin-bottom: 16px; }}
  button {{ width: 100%; padding: 12px; background: #2563eb; color: white; border: none; border-radius: 8px; font-size: 15px; font-weight: 600; cursor: pointer; margin-top: 8px; transition: background 0.2s; }}
  button:hover {{ background: #1d4ed8; }}
  .error {{ background: #fef2f2; color: #dc2626; padding: 10px 14px; border-radius: 8px; font-size: 13px; margin-bottom: 16px; }}
  .footer {{ text-align: center; font-size: 12px; color: #999; margin-top: 20px; }}
</style>
</head>
<body>
<div class="card">
  <div class="logo"><span class="logo-icon">🏗️</span></div>
  <h1>Base de connaissances Bâtiment</h1>
  <p class="subtitle">Connectez-vous pour autoriser l'accès</p>
  <div class="app-info">
    <strong>{client_name}</strong> demande l'accès à la base de connaissances bâtiment (lecture seule).
  </div>
  {error_html}
  <form method="post" action="/authorize">
    <input type="hidden" name="client_id" value="{client_id}">
    <input type="hidden" name="redirect_uri" value="{redirect_uri}">
    <input type="hidden" name="state" value="{state}">
    <input type="hidden" name="code_challenge" value="{code_challenge}">
    <input type="hidden" name="code_challenge_method" value="{code_challenge_method}">
    <input type="hidden" name="scope" value="{scope}">
    <div class="field">
      <label for="username">Identifiant</label>
      <input type="text" id="username" name="username" placeholder="Identifiant" required autofocus>
    </div>
    <div class="field">
      <label for="password">Mot de passe</label>
      <input type="password" id="password" name="password" placeholder="Mot de passe" required>
    </div>
    <button type="submit">Se connecter et autoriser</button>
  </form>
  <p class="footer">OzzO Knowledge Base · Accès sécurisé</p>
</div>
</body>
</html>"""

@app.get("/authorize")
def authorize_get(
    response_type: str = Query(...),
    client_id: str = Query(...),
    redirect_uri: str = Query(...),
    code_challenge: str = Query(...),
    code_challenge_method: str = Query("S256"),
    scope: str = Query("mcp"),
    state: str = Query("")
):
    """Affiche la page de login OAuth."""
    client = _oauth_clients.get(client_id)
    client_name = client["client_name"] if client else "Application MCP"
    html = LOGIN_HTML.format(
        client_name=client_name,
        client_id=client_id,
        redirect_uri=redirect_uri,
        state=state,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        scope=scope,
        error_html=""
    )
    return HTMLResponse(html)

@app.post("/authorize")
async def authorize_post(
    username: str = Form(...),
    password: str = Form(...),
    client_id: str = Form(...),
    redirect_uri: str = Form(...),
    state: str = Form(""),
    code_challenge: str = Form(...),
    code_challenge_method: str = Form("S256"),
    scope: str = Form("mcp")
):
    """Traite le formulaire de login et émet un authorization code."""
    # Vérification des credentials
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        client = _oauth_clients.get(client_id)
        client_name = client["client_name"] if client else "Application MCP"
        html = LOGIN_HTML.format(
            client_name=client_name,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            scope=scope,
            error_html='<div class="error">Identifiant ou mot de passe incorrect.</div>'
        )
        return HTMLResponse(html, status_code=401)

    # Émettre un authorization code
    code = secrets.token_urlsafe(32)
    _auth_codes[code] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge,
        "code_challenge_method": code_challenge_method,
        "scope": scope,
        "expires": time.time() + 300  # 5 minutes
    }

    # Rediriger vers le client avec le code
    params = {"code": code}
    if state:
        params["state"] = state
    redirect_url = redirect_uri + ("&" if "?" in redirect_uri else "?") + urlencode(params)
    return RedirectResponse(url=redirect_url, status_code=302)

# ─── OAuth 2.1 — Token endpoint ───────────────────────────────────────────────

@app.post("/token")
async def token_endpoint(request: Request):
    """Échange un authorization code contre un access token (PKCE S256)."""
    content_type = request.headers.get("content-type","")
    if "application/x-www-form-urlencoded" in content_type:
        form = await request.form()
        data = dict(form)
    else:
        try:
            data = await request.json()
        except Exception:
            data = {}

    grant_type    = data.get("grant_type","")
    code          = data.get("code","")
    redirect_uri  = data.get("redirect_uri","")
    code_verifier = data.get("code_verifier","")
    client_id     = data.get("client_id","")

    if grant_type != "authorization_code":
        return JSONResponse(status_code=400, content={"error":"unsupported_grant_type"})

    code_entry = _auth_codes.get(code)
    if not code_entry:
        return JSONResponse(status_code=400, content={"error":"invalid_grant","error_description":"Code invalide ou expiré"})
    if code_entry["expires"] < time.time():
        del _auth_codes[code]
        return JSONResponse(status_code=400, content={"error":"invalid_grant","error_description":"Code expiré"})
    if code_entry["redirect_uri"] != redirect_uri:
        return JSONResponse(status_code=400, content={"error":"invalid_grant","error_description":"redirect_uri ne correspond pas"})

    # Vérification PKCE S256
    challenge = code_entry["code_challenge"]
    digest = hashlib.sha256(code_verifier.encode()).digest()
    computed = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    if computed != challenge:
        return JSONResponse(status_code=400, content={"error":"invalid_grant","error_description":"PKCE invalide"})

    # Supprimer le code (usage unique)
    del _auth_codes[code]

    # Émettre un access token (24h)
    access_token = secrets.token_urlsafe(48)
    _access_tokens[access_token] = {
        "client_id": client_id,
        "scope": code_entry["scope"],
        "expires": time.time() + 86400
    }

    return JSONResponse({
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 86400,
        "scope": code_entry["scope"]
    })

# ─── Endpoints publics ────────────────────────────────────────────────────────

@app.post("/")
async def mcp_root(request: Request):
    """MCP endpoint sur / — Claude.ai envoie les requêtes JSON-RPC à la racine."""
    return await mcp_endpoint(request)

@app.get("/")
def root():
    return {
        "name": SERVER_NAME,
        "version": SERVER_VERSION,
        "status": "ok",
        "protocol": MCP_VERSION,
        "backend": "PostgreSQL HOZZO",
        "mcp_endpoint": "/mcp",
        "auth": "OAuth 2.1 (RFC 9728 + RFC 8414 + RFC 7591 + PKCE S256)"
    }

@app.get("/health")
def health():
    try:
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM batiment_chunks")
            count = cur.fetchone()[0]
        return {"status": "healthy", "chunks": count}
    except Exception as e:
        return JSONResponse(status_code=503, content={"status": "unhealthy", "error": str(e)})

@app.get("/docs")
def docs():
    return HTMLResponse("""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Batiment Knowledge MCP</title>
<style>body{font-family:sans-serif;max-width:700px;margin:40px auto;padding:0 20px;color:#333}
h1{color:#1a1a1a}code{background:#f4f4f4;padding:2px 6px;border-radius:4px;font-size:13px}
</style></head><body>
<h1>🏗️ Batiment Knowledge MCP</h1>
<p>Base de connaissances sur les métiers du bâtiment — 13 000+ chunks issus d'ouvrages techniques.</p>
<h2>Connexion depuis Claude.ai</h2>
<p>URL du serveur : <code>https://knowledge.ozzo.fr</code></p>
<p>Credentials : <code>ozzo</code> / voir documentation interne</p>
<h2>Outils disponibles</h2>
<ul>
<li><strong>search_batiment</strong> — Recherche sémantique</li>
<li><strong>ask_batiment</strong> — Question avec synthèse LLM</li>
<li><strong>list_sources</strong> — Liste des sources indexées</li>
<li><strong>get_stats</strong> — Statistiques de la base</li>
</ul>
</body></html>""")

# ─── Endpoint MCP principal (JSON-RPC 2.0) ───────────────────────────────────

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    """MCP Streamable HTTP Transport — JSON-RPC 2.0."""
    if not verify_token(request):
        return unauthorized_response()

    body = await request.json()
    is_batch = isinstance(body, list)
    reqs = body if is_batch else [body]
    responses = []

    for rpc in reqs:
        req_id = rpc.get("id")
        method = rpc.get("method","")
        params = rpc.get("params",{})
        try:
            if method == "initialize":
                # Gérer la session
                session_id = str(uuid.uuid4())
                _sessions[session_id] = {"initialized": True}
                result = {
                    "protocolVersion": MCP_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION}
                }
                resp = jrpc_ok(req_id, result)
                # Ajouter le session ID dans les headers (géré via response custom si besoin)
                responses.append(resp)

            elif method == "notifications/initialized":
                continue  # notification, pas de réponse

            elif method == "tools/list":
                responses.append(jrpc_ok(req_id, {"tools": MCP_TOOLS}))

            elif method == "tools/call":
                tool_name = params.get("name","")
                arguments = params.get("arguments",{})
                content   = execute_tool(tool_name, arguments)
                responses.append(jrpc_ok(req_id, {"content": content}))

            elif method == "ping":
                responses.append(jrpc_ok(req_id, {}))

            else:
                if req_id is not None:
                    responses.append(jrpc_err(req_id, -32601, f"Méthode inconnue : {method}"))

        except ValueError as e:
            responses.append(jrpc_err(req_id, -32602, str(e)))
        except Exception as e:
            responses.append(jrpc_err(req_id, -32603, f"Erreur interne : {str(e)}"))

    if not responses:
        return JSONResponse(status_code=202, content={})
    return JSONResponse(content=responses[0] if not is_batch else responses)

# ─── Point d'entrée ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    get_embedding_model()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
