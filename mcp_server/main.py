"""
Serveur MCP (Model Context Protocol) pour la base de connaissances Bâtiment.
Expose les outils de recherche sémantique via le protocole MCP standard.
Déployable sur Railway, Render, ou tout serveur Python.
"""

import os
import json
import requests
from typing import Any
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# ─── Configuration ────────────────────────────────────────────────────────────
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://humvcalhznukzdbkninw.supabase.co")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
MCP_API_KEY = os.environ.get("MCP_API_KEY", "batiment-kb-secret-2024")
EMBEDDING_MODEL = "openai/text-embedding-3-small"
OPENROUTER_EMBED_URL = "https://openrouter.ai/api/v1/embeddings"

app = FastAPI(
    title="Batiment Knowledge Base MCP Server",
    description="Serveur MCP pour la base de connaissances sur les métiers du bâtiment",
    version="1.0.0"
)

# ─── Définition des outils MCP ────────────────────────────────────────────────

MCP_TOOLS = [
    {
        "name": "search_batiment",
        "description": (
            "Recherche sémantique dans la base de connaissances sur les métiers du bâtiment. "
            "Retourne les passages les plus pertinents issus d'ouvrages techniques (Champly, "
            "Dictionnaire du BTP, etc.). Utiliser pour répondre à des questions sur les techniques "
            "de construction, les matériaux, les corps d'état, les méthodes de travail."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "La question ou le sujet à rechercher (ex: 'comment poser un enduit de façade', 'assemblage tenon mortaise')"
                },
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état (optionnel). Valeurs: maconnerie, charpente-couverture, plomberie-chauffage, electricite, menuiserie, platrerie-peinture, isolation-etancheite, gros-oeuvre, encyclopedie-generale",
                    "enum": ["maconnerie", "charpente-couverture", "plomberie-chauffage", "electricite", "menuiserie", "platrerie-peinture", "isolation-etancheite", "gros-oeuvre", "encyclopedie-generale"]
                },
                "nb_resultats": {
                    "type": "integer",
                    "description": "Nombre de résultats à retourner (défaut: 5, max: 10)",
                    "default": 5,
                    "minimum": 1,
                    "maximum": 10
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "list_sources",
        "description": "Liste toutes les sources documentaires indexées dans la base de connaissances bâtiment, avec leurs métadonnées.",
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
        "description": "Retourne les statistiques de la base de connaissances (nombre de chunks, sources, corps d'état couverts).",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

# ─── Fonctions utilitaires ────────────────────────────────────────────────────

def get_embedding(text: str) -> list[float]:
    """Génère un embedding via OpenRouter (text-embedding-3-small)."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"model": EMBEDDING_MODEL, "input": [text]}
    r = requests.post(OPENROUTER_EMBED_URL, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    return data["data"][0]["embedding"]


def search_in_supabase(query: str, corps_etat: str = None, nb_resultats: int = 5) -> list[dict]:
    """Effectue une recherche sémantique dans Supabase."""
    embedding = get_embedding(query)
    
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query_embedding": embedding,
        "match_count": nb_resultats,
        "filter_corps_etat": corps_etat
    }
    
    url = f"{SUPABASE_URL}/rest/v1/rpc/search_batiment"
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


def get_sources_from_supabase(corps_etat: str = None) -> list[dict]:
    """Liste les sources uniques dans la base."""
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    }
    
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    params = {
        "select": "titre_document,auteur,corps_etat,source,date_document",
        "order": "corps_etat",
        "limit": "100"
    }
    if corps_etat:
        params["corps_etat"] = f"eq.{corps_etat}"
    
    r = requests.get(url, headers=headers, params=params, timeout=20)
    r.raise_for_status()
    
    # Dédupliquer par titre_document
    seen = set()
    sources = []
    for row in r.json():
        key = row.get("titre_document", "")
        if key not in seen:
            seen.add(key)
            sources.append(row)
    return sources


def get_stats_from_supabase() -> dict:
    """Récupère les statistiques de la base."""
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    }
    
    # Nombre total de chunks
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers={**headers, "Prefer": "count=exact"},
        params={"select": "id", "limit": "1"},
        timeout=20
    )
    total = int(r.headers.get("content-range", "0/0").split("/")[-1])
    
    # Répartition par corps d'état
    r2 = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"select": "corps_etat", "limit": "1000"},
        timeout=20
    )
    corps_etats = {}
    for row in r2.json():
        ce = row.get("corps_etat", "inconnu")
        corps_etats[ce] = corps_etats.get(ce, 0) + 1
    
    return {"total_chunks": total, "repartition_corps_etat": corps_etats}


# ─── Endpoints MCP ────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"name": "batiment-kb-mcp", "version": "1.0.0", "status": "ok"}


@app.get("/mcp/tools")
def list_tools():
    """Liste les outils MCP disponibles."""
    return {"tools": MCP_TOOLS}


class ToolCallRequest(BaseModel):
    name: str
    arguments: dict = {}


@app.post("/mcp/tools/call")
def call_tool(request: ToolCallRequest):
    """Exécute un outil MCP."""
    
    if request.name == "search_batiment":
        query = request.arguments.get("query", "")
        corps_etat = request.arguments.get("corps_etat")
        nb_resultats = min(request.arguments.get("nb_resultats", 5), 10)
        
        if not query:
            raise HTTPException(status_code=400, detail="Le paramètre 'query' est requis")
        
        try:
            results = search_in_supabase(query, corps_etat, nb_resultats)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur de recherche: {str(e)}")
        
        if not results:
            content = "Aucun résultat trouvé pour cette recherche dans la base de connaissances bâtiment."
        else:
            parts = [f"**{len(results)} résultat(s) trouvé(s) pour : \"{query}\"**\n"]
            for i, r in enumerate(results, 1):
                similarity_pct = round(r.get("similarity", 0) * 100, 1)
                parts.append(
                    f"\n---\n**[{i}] {r.get('titre_document', 'Document')}**  \n"
                    f"Corps d'état : `{r.get('corps_etat', 'N/A')}` | "
                    f"Auteur : {r.get('auteur', 'N/A')} | "
                    f"Pertinence : {similarity_pct}%\n\n"
                    f"{r.get('content', '')[:800]}..."
                )
            content = "\n".join(parts)
        
        return {"content": [{"type": "text", "text": content}]}
    
    elif request.name == "list_sources":
        corps_etat = request.arguments.get("corps_etat")
        try:
            sources = get_sources_from_supabase(corps_etat)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        lines = ["**Sources indexées dans la base de connaissances bâtiment :**\n"]
        for s in sources:
            lines.append(
                f"- **{s.get('titre_document', 'N/A')}**  \n"
                f"  Auteur : {s.get('auteur', 'N/A')} | "
                f"Corps d'état : `{s.get('corps_etat', 'N/A')}` | "
                f"Date : {s.get('date_document', 'N/A')} | "
                f"Source : {s.get('source', 'N/A')}"
            )
        
        return {"content": [{"type": "text", "text": "\n".join(lines)}]}
    
    elif request.name == "get_stats":
        try:
            stats = get_stats_from_supabase()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        lines = [
            f"**Statistiques de la base de connaissances bâtiment**\n",
            f"- Total chunks indexés : **{stats['total_chunks']}**",
            f"- Répartition par corps d'état :"
        ]
        for ce, count in sorted(stats["repartition_corps_etat"].items()):
            lines.append(f"  - `{ce}` : {count} chunk(s)")
        
        return {"content": [{"type": "text", "text": "\n".join(lines)}]}
    
    else:
        raise HTTPException(status_code=404, detail=f"Outil '{request.name}' non trouvé")


# ─── Point d'entrée ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
