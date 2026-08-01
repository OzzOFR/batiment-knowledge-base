"""
Serveur MCP (Model Context Protocol) pour la base de connaissances Bâtiment.
Protocole : MCP 2025-03-26 — JSON-RPC 2.0 sur HTTP Streamable (compatible Claude.ai)

v6.0 — Réécriture complète en protocole MCP standard
       JSON-RPC 2.0 sur POST /mcp (Streamable HTTP transport)
       Authentification Bearer token
       Embeddings locaux sentence-transformers (768 dims)
       Synthèse LLM via OpenRouter (gpt-4o-mini)
"""

import os
import json
import uuid
import requests
import psycopg2
import psycopg2.extras
from contextlib import contextmanager
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
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

MCP_API_KEY = os.environ.get("MCP_API_KEY", "t-63pCvruQiQGxX8d3qQnqjVB-RwT7FEQth0jmFBrj8")
PORT        = int(os.environ.get("PORT", "8100"))

MCP_VERSION      = "2025-03-26"
SERVER_NAME      = "batiment-knowledge"
SERVER_VERSION   = "6.0.0"

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
        print(f"[MCP] Modèle chargé — {_embedding_model.get_embedding_dimension()} dims")
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

# ─── Définition des outils MCP ────────────────────────────────────────────────
MCP_TOOLS = [
    {
        "name": "search_batiment",
        "description": (
            "Recherche sémantique dans la base de connaissances sur les métiers du bâtiment. "
            "Retourne les passages les plus pertinents issus d'ouvrages techniques (Champly, "
            "Rondelet, Barberot, Viollet-le-Duc, Planat, etc.). Utiliser pour répondre "
            "à des questions sur les techniques de construction, les matériaux, les corps d'état."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "La question ou le sujet à rechercher"},
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel)",
                    "enum": ["maconnerie", "charpente-couverture", "plomberie-chauffage",
                             "electricite", "menuiserie", "platrerie-peinture",
                             "isolation-etancheite", "gros-oeuvre", "encyclopedie-generale",
                             "pathologies", "normes-reglements", "materiaux"]
                },
                "nb_resultats": {
                    "type": "integer",
                    "description": "Nombre de résultats (défaut: 5, max: 10)",
                    "default": 5, "minimum": 1, "maximum": 10
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "ask_batiment",
        "description": (
            "Pose une question sur les métiers du bâtiment et obtient une réponse synthétisée "
            "par un LLM à partir des sources de la base de connaissances. "
            "Signale automatiquement les divergences entre sources d'époques différentes."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "La question technique à poser"},
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel)",
                    "enum": ["maconnerie", "charpente-couverture", "plomberie-chauffage",
                             "electricite", "menuiserie", "platrerie-peinture",
                             "isolation-etancheite", "gros-oeuvre", "encyclopedie-generale",
                             "pathologies", "normes-reglements", "materiaux"]
                },
                "nb_sources": {
                    "type": "integer",
                    "description": "Nombre de sources à consulter (défaut: 5, max: 8)",
                    "default": 5, "minimum": 1, "maximum": 8
                }
            },
            "required": ["question"]
        }
    },
    {
        "name": "list_sources",
        "description": "Liste toutes les sources indexées dans la base de connaissances bâtiment.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "corps_etat": {"type": "string", "description": "Filtrer par corps d'état (optionnel)"}
            }
        }
    },
    {
        "name": "get_stats",
        "description": "Retourne les statistiques de la base de connaissances bâtiment.",
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
    auteur   = r.get("auteur")
    annee    = r.get("annee_publication")
    fiabilite = r.get("fiabilite", "")
    if auteur and annee:
        label = FIABILITE_LABELS.get(fiabilite, fiabilite)
        return f"{auteur} ({annee}) — *{label}*"
    return r.get("source", "N/A")


def detect_divergences(passages: list) -> str:
    if len(passages) < 2:
        return ""
    anciens   = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
    modernes  = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    syntheses = [p for p in passages if p.get("fiabilite") == "synthese-ia"]
    notes = []
    if syntheses:
        notes.append(
            "⚠️ **Synthèse IA** : certains résultats proviennent de fiches synthétiques rédigées par IA "
            "(OzzO Knowledge Base), non issues de sources primaires. À vérifier avant usage professionnel."
        )
    if anciens and modernes:
        aa = [p["annee_publication"] for p in anciens  if p.get("annee_publication")]
        am = [p["annee_publication"] for p in modernes if p.get("annee_publication")]
        if aa and am and (min(am) - max(aa)) > 50:
            na = list(set(p.get("auteur", "?") for p in anciens  if p.get("auteur")))
            nm = list(set(p.get("auteur", "?") for p in modernes if p.get("auteur")))
            notes.append(
                f"⚠️ **Sources d'époques différentes** : "
                f"sources anciennes ({', '.join(na[:2])}, ~{max(aa)}) "
                f"vs sources modernes ({', '.join(nm[:2])}, ~{min(am)}). "
                f"En cas de contradiction, privilégier les sources modernes."
            )
    return ("\n\n> " + "\n> ".join(notes)) if notes else ""


def synthesize_with_llm(question: str, passages: list) -> str:
    context_parts = []
    for i, p in enumerate(passages, 1):
        auteur   = p.get("auteur") or p.get("source", "Source inconnue")
        annee    = p.get("annee_publication")
        fiabilite = p.get("fiabilite", "")
        label    = FIABILITE_LABELS.get(fiabilite, fiabilite)
        header   = f"{auteur} ({annee}) [{label}]" if annee else auteur
        context_parts.append(f"[Source {i}: {header}]\n{p.get('content', '')[:1200]}")
    context = "\n\n---\n\n".join(context_parts)
    anciens  = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    div_instr = ""
    if anciens and modernes:
        div_instr = (
            "\nATTENTION : Les sources couvrent des époques différentes. "
            "Si des informations divergent, signale-le et précise que les sources modernes "
            "reflètent les pratiques actuelles, les sources anciennes la restauration du patrimoine."
        )
    system_prompt = (
        "Tu es un expert en techniques du bâtiment. "
        "Réponds UNIQUEMENT à partir des passages fournis. "
        "Réponse structurée, précise, sourcée (auteur + année), en français. "
        "Si les passages sont insuffisants, indique-le clairement." + div_instr
    )
    user_prompt = (
        f"Question : {question}\n\nPassages :\n\n{context}\n\n"
        "Réponds en citant les sources (auteur + année) pour chaque information importante."
    )
    r = requests.post(
        OPENROUTER_CHAT_URL,
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"},
        json={"model": SYNTHESIS_MODEL, "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ], "max_tokens": 1500, "temperature": 0.3},
        timeout=60
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def get_sources_from_db(corps_etat: str = None) -> list:
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if corps_etat:
            cur.execute("""
                SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage, annee_publication, fiabilite
                FROM batiment_chunks WHERE corps_etat = %s
                ORDER BY corps_etat, annee_publication NULLS LAST LIMIT 300
            """, (corps_etat,))
        else:
            cur.execute("""
                SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage, annee_publication, fiabilite
                FROM batiment_chunks
                ORDER BY corps_etat, annee_publication NULLS LAST LIMIT 300
            """)
        return [dict(row) for row in cur.fetchall()]


def get_stats_from_db() -> dict:
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS total FROM batiment_chunks")
        total = cur.fetchone()["total"]
        cur.execute("SELECT corps_etat, COUNT(*) AS n FROM batiment_chunks GROUP BY corps_etat ORDER BY n DESC")
        corps_etats = {r["corps_etat"]: r["n"] for r in cur.fetchall()}
        cur.execute("SELECT fiabilite, COUNT(*) AS n FROM batiment_chunks WHERE fiabilite IS NOT NULL GROUP BY fiabilite ORDER BY n DESC")
        fiabilites = {r["fiabilite"]: r["n"] for r in cur.fetchall()}
        cur.execute("SELECT COUNT(DISTINCT auteur) AS n FROM batiment_chunks WHERE auteur IS NOT NULL")
        nb_auteurs = cur.fetchone()["n"]
        return {
            "total_chunks": total,
            "repartition_corps_etat": corps_etats,
            "repartition_fiabilite": fiabilites,
            "nb_auteurs_uniques": nb_auteurs,
            "embedding_model": EMBEDDING_MODEL_NAME,
            "embedding_dims": EMBEDDING_DIMS
        }

# ─── Exécution des outils ─────────────────────────────────────────────────────

def execute_tool(name: str, arguments: dict) -> list:
    """Exécute un outil et retourne une liste de content blocks MCP."""

    if name == "search_batiment":
        query        = arguments.get("query", "")
        corps_etat   = arguments.get("corps_etat")
        nb_resultats = min(int(arguments.get("nb_resultats", 5)), 10)
        if not query:
            return [{"type": "text", "text": "Erreur : le paramètre 'query' est requis."}]
        results = search_in_db(query, corps_etat, nb_resultats)
        if not results:
            return [{"type": "text", "text": "Aucun résultat trouvé pour cette recherche."}]
        parts = [f"**{len(results)} résultat(s) pour : \"{query}\"**\n"]
        for i, r in enumerate(results, 1):
            sim   = round(float(r.get("similarity", 0)) * 100, 1)
            corps = r.get("corps_etat", "N/A")
            txt   = r.get("content", "")
            badge = format_source_badge(r)
            section = ""
            if txt.startswith("[") and "]" in txt[:200]:
                end = txt.index("]")
                section = txt[1:end]
                preview = txt[end+2:end+802]
            else:
                preview = txt[:800]
            parts.append(
                f"\n---\n**[{i}]** `{corps_etat or corps}` | **{badge}**  \n"
                + (f"*Section : {section}*  \n" if section else "")
                + f"Pertinence : {sim}%\n\n{preview}..."
            )
        text = "\n".join(parts) + detect_divergences(results)
        return [{"type": "text", "text": text}]

    elif name == "ask_batiment":
        question   = arguments.get("question", "")
        corps_etat = arguments.get("corps_etat")
        nb_sources = min(int(arguments.get("nb_sources", 5)), 8)
        if not question:
            return [{"type": "text", "text": "Erreur : le paramètre 'question' est requis."}]
        if not OPENROUTER_API_KEY:
            return [{"type": "text", "text": "Erreur : clé API OpenRouter non configurée."}]
        passages = search_in_db(question, corps_etat, nb_sources)
        if not passages:
            return [{"type": "text", "text": "Aucune information trouvée pour cette question."}]
        answer = synthesize_with_llm(question, passages)
        seen, sources_lines = set(), []
        for p in passages:
            auteur = p.get("auteur") or p.get("source", "N/A")
            annee  = p.get("annee_publication")
            label  = FIABILITE_LABELS.get(p.get("fiabilite", ""), "")
            titre  = p.get("titre_ouvrage") or p.get("source", "N/A")
            key    = f"{auteur}_{annee}"
            if key not in seen:
                seen.add(key)
                sources_lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}" if annee else f"- {titre}")
        full = (
            f"{answer}\n\n---\n**Sources consultées :**\n"
            + "\n".join(sources_lines[:6])
            + detect_divergences(passages)
        )
        return [{"type": "text", "text": full}]

    elif name == "list_sources":
        corps_etat = arguments.get("corps_etat")
        sources    = get_sources_from_db(corps_etat)
        lines      = ["**Sources indexées dans la base de connaissances bâtiment :**\n"]
        current    = None
        for s in sources:
            ce = s.get("corps_etat", "N/A")
            if ce != current:
                lines.append(f"\n### {ce}")
                current = ce
            auteur = s.get("auteur")
            annee  = s.get("annee_publication")
            label  = FIABILITE_LABELS.get(s.get("fiabilite", ""), "")
            titre  = s.get("titre_ouvrage") or s.get("source", "N/A")
            lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}" if auteur and annee else f"- {titre}")
        return [{"type": "text", "text": "\n".join(lines)}]

    elif name == "get_stats":
        stats = get_stats_from_db()
        lines = [
            f"**Statistiques de la base de connaissances bâtiment (PostgreSQL HOZZO)**\n",
            f"- Total chunks indexés : **{stats['total_chunks']}**",
            f"- Auteurs uniques : **{stats['nb_auteurs_uniques']}**",
            f"- Modèle d'embedding : `{stats['embedding_model']}` ({stats['embedding_dims']} dims)",
            "", "**Répartition par corps d'état :**"
        ]
        for ce, nb in sorted(stats["repartition_corps_etat"].items(), key=lambda x: -x[1]):
            lines.append(f"  - `{ce}` : {nb} chunks")
        lines += ["", "**Répartition par niveau de fiabilité :**"]
        for fid, nb in stats["repartition_fiabilite"].items():
            lines.append(f"  - *{FIABILITE_LABELS.get(fid, fid)}* : {nb} chunks")
        return [{"type": "text", "text": "\n".join(lines)}]

    else:
        raise ValueError(f"Outil inconnu : {name}")


# ─── Helpers JSON-RPC ─────────────────────────────────────────────────────────

def jsonrpc_result(req_id, result: dict) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}

def jsonrpc_error(req_id, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}

def check_auth(request: Request):
    """Vérifie le Bearer token. Lève HTTPException 401 si invalide."""
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer ") or auth[7:] != MCP_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Clé API invalide ou manquante",
            headers={"WWW-Authenticate": "Bearer"}
        )

# ─── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "name": SERVER_NAME,
        "version": SERVER_VERSION,
        "status": "ok",
        "protocol": MCP_VERSION,
        "backend": "PostgreSQL HOZZO",
        "embedding_model": EMBEDDING_MODEL_NAME,
        "embedding_dims": EMBEDDING_DIMS,
        "mcp_endpoint": "/mcp",
        "auth": "Bearer token required"
    }


@app.get("/health")
def health():
    try:
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM batiment_chunks")
            count = cur.fetchone()[0]
        return {"status": "healthy", "chunks": count, "backend": "PostgreSQL HOZZO"}
    except Exception as e:
        return JSONResponse(status_code=503, content={"status": "unhealthy", "error": str(e)})


# ─── Endpoint MCP principal (JSON-RPC 2.0 Streamable HTTP) ───────────────────

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    """
    Endpoint MCP standard — JSON-RPC 2.0 Streamable HTTP Transport (2025-03-26).
    Gère initialize, tools/list, tools/call.
    """
    check_auth(request)

    body = await request.json()

    # Support batch (liste) et requête unique
    is_batch = isinstance(body, list)
    requests_list = body if is_batch else [body]

    responses = []
    for rpc in requests_list:
        req_id = rpc.get("id")
        method = rpc.get("method", "")
        params = rpc.get("params", {})

        try:
            if method == "initialize":
                result = {
                    "protocolVersion": MCP_VERSION,
                    "capabilities": {
                        "tools": {"listChanged": False}
                    },
                    "serverInfo": {
                        "name": SERVER_NAME,
                        "version": SERVER_VERSION
                    }
                }
                responses.append(jsonrpc_result(req_id, result))

            elif method == "notifications/initialized":
                # Notification — pas de réponse
                continue

            elif method == "tools/list":
                responses.append(jsonrpc_result(req_id, {"tools": MCP_TOOLS}))

            elif method == "tools/call":
                tool_name = params.get("name", "")
                arguments = params.get("arguments", {})
                content   = execute_tool(tool_name, arguments)
                responses.append(jsonrpc_result(req_id, {"content": content}))

            elif method == "ping":
                responses.append(jsonrpc_result(req_id, {}))

            else:
                if req_id is not None:
                    responses.append(jsonrpc_error(req_id, -32601, f"Méthode inconnue : {method}"))

        except ValueError as e:
            responses.append(jsonrpc_error(req_id, -32602, str(e)))
        except Exception as e:
            responses.append(jsonrpc_error(req_id, -32603, f"Erreur interne : {str(e)}"))

    if not responses:
        return JSONResponse(status_code=202, content={})

    if is_batch:
        return JSONResponse(content=responses)
    return JSONResponse(content=responses[0])


# ─── Compatibilité ancienne API REST ─────────────────────────────────────────

@app.get("/mcp/tools")
def list_tools_compat(request: Request):
    check_auth(request)
    return {"tools": MCP_TOOLS}


@app.post("/mcp/tools/call")
async def call_tool_compat(request: Request):
    check_auth(request)
    body = await request.json()
    name      = body.get("name", "")
    arguments = body.get("arguments", {})
    try:
        content = execute_tool(name, arguments)
        return {"content": content}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── Point d'entrée ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    # Précharger le modèle au démarrage
    get_embedding_model()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
