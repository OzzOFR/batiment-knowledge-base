"""
Serveur MCP (Model Context Protocol) pour la base de connaissances Bâtiment.
Expose les outils de recherche sémantique via le protocole MCP standard.

v5.0 — Embeddings locaux avec sentence-transformers (paraphrase-multilingual-mpnet-base-v2, 768 dims)
       Suppression de la dépendance OpenRouter pour les embeddings
       Synthèse LLM via OpenRouter (gpt-4o-mini) — optionnelle
       Métadonnées de publication (auteur, année, fiabilité) + confrontation des sources divergentes
"""

import os
import json
import requests
import psycopg2
import psycopg2.extras
from contextlib import contextmanager
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# ─── Configuration ────────────────────────────────────────────────────────────
# PostgreSQL HOZZO
PG_HOST     = os.environ.get("PG_HOST", "forge-postgres")
PG_PORT     = int(os.environ.get("PG_PORT", "5432"))
PG_DB       = os.environ.get("PG_DB", "batiment_knowledge")
PG_USER     = os.environ.get("PG_USER", "createk")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "Forge2026Hozzo!")

# Modèle d'embedding local (sentence-transformers)
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
EMBEDDING_DIMS = 768

# LLM pour la synthèse (OpenRouter — optionnel)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
SYNTHESIS_MODEL    = "openai/gpt-4o-mini"
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

# Serveur
PORT = int(os.environ.get("PORT", "8100"))

app = FastAPI(
    title="Batiment Knowledge Base MCP Server",
    description="Serveur MCP pour la base de connaissances sur les métiers du bâtiment",
    version="5.0.0"
)

# ─── Labels de fiabilité ──────────────────────────────────────────────────────
FIABILITE_LABELS = {
    "patrimoine":        "Patrimoine XIXe s.",
    "technique-ancien":  "Technique XIXe-XXe s.",
    "technique-moderne": "Technique moderne",
    "norme-en-vigueur":  "Norme en vigueur",
}

# ─── Modèle d'embedding (chargé une seule fois au démarrage) ─────────────────
_embedding_model = None

def get_embedding_model():
    """Charge le modèle d'embedding (singleton)."""
    global _embedding_model
    if _embedding_model is None:
        from sentence_transformers import SentenceTransformer
        print(f"[MCP] Chargement du modèle d'embedding : {EMBEDDING_MODEL_NAME}")
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        print(f"[MCP] Modèle chargé — {_embedding_model.get_sentence_embedding_dimension()} dims")
    return _embedding_model


# ─── Connexion PostgreSQL ─────────────────────────────────────────────────────
@contextmanager
def get_db():
    """Gestionnaire de contexte pour les connexions PostgreSQL."""
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASSWORD,
        connect_timeout=10
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
            "Rondelet, Barberot, Viollet-le-Duc, Planat, guides ADEME, etc.). Utiliser pour répondre "
            "à des questions sur les techniques de construction, les matériaux, les corps d'état, "
            "les méthodes de travail. Retourne les passages bruts avec leur source et leur date."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "La question ou le sujet à rechercher"
                },
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
            "par un LLM à partir des sources de la base de connaissances. Contrairement à "
            "search_batiment qui retourne des passages bruts, ask_batiment retourne une réponse "
            "structurée et directement utilisable. Signale automatiquement les divergences "
            "entre sources d'époques différentes."
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
        "description": "Liste toutes les sources indexées dans la base de connaissances bâtiment, avec auteur, année et niveau de fiabilité.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel)"
                }
            }
        }
    },
    {
        "name": "get_stats",
        "description": "Retourne les statistiques de la base de connaissances (nombre de chunks par corps d'état, sources, etc.)",
        "inputSchema": {"type": "object", "properties": {}}
    }
]


# ─── Fonctions utilitaires ────────────────────────────────────────────────────

def get_embedding(text: str) -> list[float]:
    """Génère un embedding via le modèle local sentence-transformers."""
    model = get_embedding_model()
    embedding = model.encode(text, show_progress_bar=False)
    return embedding.tolist()


def search_in_db(query: str, corps_etat: str = None, nb_resultats: int = 5) -> list[dict]:
    """Recherche sémantique dans PostgreSQL via pgvector."""
    embedding = get_embedding(query)
    embedding_str = "[" + ",".join(str(x) for x in embedding) + "]"
    
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        if corps_etat:
            cur.execute("""
                SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                       annee_publication, fiabilite,
                       1 - (embedding <=> %s::vector) AS similarity
                FROM batiment_chunks
                WHERE corps_etat = %s
                  AND embedding IS NOT NULL
                  AND 1 - (embedding <=> %s::vector) > 0.2
                ORDER BY embedding <=> %s::vector
                LIMIT %s
            """, (embedding_str, corps_etat, embedding_str, embedding_str, nb_resultats))
        else:
            cur.execute("""
                SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                       annee_publication, fiabilite,
                       1 - (embedding <=> %s::vector) AS similarity
                FROM batiment_chunks
                WHERE embedding IS NOT NULL
                  AND 1 - (embedding <=> %s::vector) > 0.2
                ORDER BY embedding <=> %s::vector
                LIMIT %s
            """, (embedding_str, embedding_str, embedding_str, nb_resultats))
        
        return [dict(row) for row in cur.fetchall()]


def format_source_badge(result: dict) -> str:
    """Formate un badge de source avec auteur, année et fiabilité."""
    auteur = result.get("auteur")
    annee = result.get("annee_publication")
    fiabilite = result.get("fiabilite", "")
    source = result.get("source", "N/A")
    
    if auteur and annee:
        label = FIABILITE_LABELS.get(fiabilite, fiabilite)
        return f"{auteur} ({annee}) — *{label}*"
    return source


def detect_divergences(passages: list[dict]) -> str:
    """Détecte et signale les divergences potentielles entre sources d'époques différentes."""
    if len(passages) < 2:
        return ""
    
    anciens  = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    
    if anciens and modernes:
        annees_anciens  = [p["annee_publication"] for p in anciens  if p.get("annee_publication")]
        annees_modernes = [p["annee_publication"] for p in modernes if p.get("annee_publication")]
        
        if annees_anciens and annees_modernes:
            ecart = min(annees_modernes) - max(annees_anciens)
            if ecart > 50:
                noms_anciens  = list(set(p.get("auteur", "?") for p in anciens  if p.get("auteur")))
                noms_modernes = list(set(p.get("auteur", "?") for p in modernes if p.get("auteur")))
                return (
                    f"\n\n> ⚠️ **Sources d'époques différentes** : "
                    f"les sources anciennes ({', '.join(noms_anciens[:2])}, ~{max(annees_anciens)}) "
                    f"et les sources modernes ({', '.join(noms_modernes[:2])}, ~{min(annees_modernes)}) "
                    f"peuvent présenter des divergences. "
                    f"En cas de contradiction, privilégier les sources modernes pour les pratiques actuelles, "
                    f"et les sources anciennes pour la restauration du patrimoine."
                )
    return ""


def synthesize_with_llm(question: str, passages: list[dict]) -> str:
    """Synthétise une réponse à partir des passages trouvés via un LLM."""
    context_parts = []
    for i, p in enumerate(passages, 1):
        auteur   = p.get("auteur") or p.get("source", "Source inconnue")
        annee    = p.get("annee_publication")
        fiabilite = p.get("fiabilite", "")
        label    = FIABILITE_LABELS.get(fiabilite, fiabilite)
        source_header = f"{auteur} ({annee}) [{label}]" if annee else auteur
        content  = p.get("content", "")[:1200]
        context_parts.append(f"[Source {i}: {source_header}]\n{content}")
    
    context = "\n\n---\n\n".join(context_parts)
    
    anciens  = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    divergence_instruction = ""
    if anciens and modernes:
        divergence_instruction = (
            "\nATTENTION : Les sources fournies couvrent des époques différentes. "
            "Si des informations divergent entre sources anciennes et modernes, "
            "signale-le explicitement et précise que les sources modernes reflètent les pratiques actuelles, "
            "tandis que les sources anciennes sont pertinentes pour la restauration du patrimoine."
        )
    
    system_prompt = (
        "Tu es un expert en techniques du bâtiment et construction. "
        "Tu réponds aux questions techniques en te basant UNIQUEMENT sur les passages fournis. "
        "Chaque passage est annoté avec son auteur, son année de publication et son niveau de fiabilité. "
        "Ta réponse doit être :\n"
        "- Structurée avec des titres et sous-titres si nécessaire\n"
        "- Précise et technique\n"
        "- Sourcée (mentionner auteur + année pour chaque information clé)\n"
        "- En français\n"
        "Si les passages ne contiennent pas assez d'information pour répondre, indique-le clairement."
        + divergence_instruction
    )
    
    user_prompt = f"""Question : {question}

Passages de la base de connaissances bâtiment (avec auteur et année) :

{context}

Réponds à la question en citant les sources (auteur + année) pour chaque information importante."""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": SYNTHESIS_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ],
        "max_tokens": 1500,
        "temperature": 0.3
    }
    r = requests.post(OPENROUTER_CHAT_URL, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def get_sources_from_db(corps_etat: str = None) -> list[dict]:
    """Liste les sources uniques dans la base."""
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if corps_etat:
            cur.execute("""
                SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage,
                                annee_publication, fiabilite
                FROM batiment_chunks
                WHERE corps_etat = %s
                ORDER BY corps_etat, annee_publication NULLS LAST
                LIMIT 300
            """, (corps_etat,))
        else:
            cur.execute("""
                SELECT DISTINCT source, corps_etat, auteur, titre_ouvrage,
                                annee_publication, fiabilite
                FROM batiment_chunks
                ORDER BY corps_etat, annee_publication NULLS LAST
                LIMIT 300
            """)
        return [dict(row) for row in cur.fetchall()]


def get_stats_from_db() -> dict:
    """Récupère les statistiques de la base directement via SQL."""
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        # Total
        cur.execute("SELECT COUNT(*) AS total FROM batiment_chunks")
        total = cur.fetchone()["total"]
        
        # Répartition par corps d'état
        cur.execute("""
            SELECT corps_etat, COUNT(*) AS nb_chunks
            FROM batiment_chunks
            GROUP BY corps_etat
            ORDER BY nb_chunks DESC
        """)
        corps_etats = {row["corps_etat"]: row["nb_chunks"] for row in cur.fetchall()}
        
        # Répartition par niveau de fiabilité
        cur.execute("""
            SELECT fiabilite, COUNT(*) AS nb_chunks
            FROM batiment_chunks
            WHERE fiabilite IS NOT NULL
            GROUP BY fiabilite
            ORDER BY nb_chunks DESC
        """)
        fiabilites = {row["fiabilite"]: row["nb_chunks"] for row in cur.fetchall()}
        
        # Nombre d'auteurs uniques
        cur.execute("SELECT COUNT(DISTINCT auteur) AS nb_auteurs FROM batiment_chunks WHERE auteur IS NOT NULL")
        nb_auteurs = cur.fetchone()["nb_auteurs"]
        
        # Embeddings
        cur.execute("""
            SELECT 
                COUNT(*) FILTER (WHERE embedding IS NOT NULL) as avec_embedding,
                COUNT(*) FILTER (WHERE embedding IS NULL) as sans_embedding
            FROM batiment_chunks
        """)
        row = cur.fetchone()
        
        return {
            "total_chunks": total,
            "repartition_corps_etat": corps_etats,
            "repartition_fiabilite": fiabilites,
            "nb_auteurs_uniques": nb_auteurs,
            "avec_embedding": row["avec_embedding"],
            "sans_embedding": row["sans_embedding"],
            "embedding_model": EMBEDDING_MODEL_NAME,
            "embedding_dims": EMBEDDING_DIMS
        }


# ─── Endpoints MCP ────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "name": "batiment-kb-mcp",
        "version": "5.0.0",
        "status": "ok",
        "backend": "PostgreSQL HOZZO",
        "embedding_model": EMBEDDING_MODEL_NAME,
        "embedding_dims": EMBEDDING_DIMS
    }


@app.get("/health")
def health():
    try:
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM batiment_chunks")
            count = cur.fetchone()[0]
        return {
            "status": "healthy",
            "chunks": count,
            "backend": "PostgreSQL HOZZO",
            "embedding_model": EMBEDDING_MODEL_NAME
        }
    except Exception as e:
        return JSONResponse(status_code=503, content={"status": "unhealthy", "error": str(e)})


@app.get("/mcp/tools")
def list_tools():
    return {"tools": MCP_TOOLS}


class ToolCallRequest(BaseModel):
    name: str
    arguments: dict = {}


@app.post("/mcp/tools/call")
def call_tool(request: ToolCallRequest):
    """Exécute un outil MCP."""
    
    if request.name == "search_batiment":
        query       = request.arguments.get("query", "")
        corps_etat  = request.arguments.get("corps_etat")
        nb_resultats = min(request.arguments.get("nb_resultats", 5), 10)
        
        if not query:
            raise HTTPException(status_code=400, detail="Le paramètre 'query' est requis")
        
        try:
            results = search_in_db(query, corps_etat, nb_resultats)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur de recherche: {str(e)}")
        
        if not results:
            content = "Aucun résultat trouvé pour cette recherche dans la base de connaissances bâtiment."
        else:
            parts = [f"**{len(results)} résultat(s) trouvé(s) pour : \"{query}\"**\n"]
            for i, r in enumerate(results, 1):
                similarity_pct = round(float(r.get("similarity", 0)) * 100, 1)
                corps          = r.get("corps_etat", "N/A")
                content_text   = r.get("content", "")
                source_badge   = format_source_badge(r)
                
                # Extraire le préfixe de section si présent
                section_info = ""
                if content_text.startswith("[") and "]" in content_text[:200]:
                    bracket_end  = content_text.index("]")
                    section_info = content_text[1:bracket_end]
                    content_preview = content_text[bracket_end+2:bracket_end+802]
                else:
                    content_preview = content_text[:800]
                
                parts.append(
                    f"\n---\n**[{i}]** `{corps_etat or corps}` | **{source_badge}**  \n"
                    + (f"*Section : {section_info}*  \n" if section_info else "")
                    + f"Pertinence : {similarity_pct}%\n\n"
                    + f"{content_preview}..."
                )
            
            divergence_note = detect_divergences(results)
            content = "\n".join(parts) + divergence_note
        
        return {"content": [{"type": "text", "text": content}]}
    
    elif request.name == "ask_batiment":
        question   = request.arguments.get("question", "")
        corps_etat = request.arguments.get("corps_etat")
        nb_sources = min(request.arguments.get("nb_sources", 5), 8)
        
        if not question:
            raise HTTPException(status_code=400, detail="Le paramètre 'question' est requis")
        
        if not OPENROUTER_API_KEY:
            raise HTTPException(status_code=503, detail="Clé API OpenRouter non configurée pour la synthèse LLM")
        
        try:
            passages = search_in_db(question, corps_etat, nb_sources)
            
            if not passages:
                return {"content": [{"type": "text", "text": "Aucune information trouvée dans la base de connaissances pour répondre à cette question."}]}
            
            answer = synthesize_with_llm(question, passages)
            
            seen_sources = set()
            sources_lines = []
            for p in passages:
                auteur    = p.get("auteur") or p.get("source", "N/A")
                annee     = p.get("annee_publication")
                fiabilite = p.get("fiabilite", "")
                label     = FIABILITE_LABELS.get(fiabilite, fiabilite)
                titre     = p.get("titre_ouvrage") or p.get("source", "N/A")
                key = f"{auteur}_{annee}"
                if key not in seen_sources:
                    seen_sources.add(key)
                    if annee:
                        sources_lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}")
                    else:
                        sources_lines.append(f"- {titre}")
            
            divergence_note = detect_divergences(passages)
            full_response = (
                f"{answer}\n\n---\n**Sources consultées :**\n"
                + "\n".join(sources_lines[:6])
                + divergence_note
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur lors de la synthèse: {str(e)}")
        
        return {"content": [{"type": "text", "text": full_response}]}
    
    elif request.name == "list_sources":
        corps_etat = request.arguments.get("corps_etat")
        try:
            sources = get_sources_from_db(corps_etat)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        lines = ["**Sources indexées dans la base de connaissances bâtiment :**\n"]
        current_corps = None
        for s in sources:
            ce = s.get("corps_etat", "N/A")
            if ce != current_corps:
                lines.append(f"\n### {ce}")
                current_corps = ce
            auteur    = s.get("auteur")
            annee     = s.get("annee_publication")
            fiabilite = s.get("fiabilite", "")
            label     = FIABILITE_LABELS.get(fiabilite, "")
            titre     = s.get("titre_ouvrage") or s.get("source", "N/A")
            if auteur and annee:
                lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}")
            else:
                lines.append(f"- {titre}")
        
        return {"content": [{"type": "text", "text": "\n".join(lines)}]}
    
    elif request.name == "get_stats":
        try:
            stats = get_stats_from_db()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        lines = [
            f"**Statistiques de la base de connaissances bâtiment (PostgreSQL HOZZO)**\n",
            f"- Total chunks indexés : **{stats['total_chunks']}**",
            f"- Auteurs uniques : **{stats['nb_auteurs_uniques']}**",
            f"- Embeddings générés : **{stats.get('avec_embedding', 'N/A')}**",
            f"- Modèle d'embedding : `{stats.get('embedding_model', 'N/A')}` ({stats.get('embedding_dims', 'N/A')} dims)",
            "",
            "**Répartition par corps d'état :**"
        ]
        for ce, nb in sorted(stats["repartition_corps_etat"].items(), key=lambda x: -x[1]):
            lines.append(f"  - `{ce}` : {nb} chunks")
        
        lines += ["", "**Répartition par niveau de fiabilité :**"]
        for fid, nb in stats["repartition_fiabilite"].items():
            label = FIABILITE_LABELS.get(fid, fid)
            lines.append(f"  - *{label}* : {nb} chunks")
        
        return {"content": [{"type": "text", "text": "\n".join(lines)}]}
    
    else:
        raise HTTPException(status_code=404, detail=f"Outil inconnu : {request.name}")


# ─── Point d'entrée ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    # Pré-charger le modèle d'embedding au démarrage
    get_embedding_model()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
