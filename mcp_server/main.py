"""
Serveur MCP (Model Context Protocol) pour la base de connaissances Bâtiment.
Expose les outils de recherche sémantique via le protocole MCP standard.
Déployable sur Railway, Render, ou tout serveur Python.

v3.0 — Métadonnées de publication (auteur, année, fiabilité) + confrontation des sources divergentes
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
SYNTHESIS_MODEL = "openai/gpt-4o-mini"
OPENROUTER_EMBED_URL = "https://openrouter.ai/api/v1/embeddings"
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

app = FastAPI(
    title="Batiment Knowledge Base MCP Server",
    description="Serveur MCP pour la base de connaissances sur les métiers du bâtiment",
    version="3.0.0"
)

# ─── Définition des outils MCP ────────────────────────────────────────────────

MCP_TOOLS = [
    {
        "name": "search_batiment",
        "description": (
            "Recherche sémantique dans la base de connaissances sur les métiers du bâtiment. "
            "Retourne les passages les plus pertinents issus d'ouvrages techniques (Champly, "
            "Rondelet, Barberot, Viollet-le-Duc, guides ADEME, etc.). Utiliser pour répondre "
            "à des questions sur les techniques de construction, les matériaux, les corps d'état, "
            "les méthodes de travail. Retourne les passages bruts avec leur source."
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
                    "description": "Filtrer par corps d'état (optionnel). Valeurs: maconnerie, charpente-couverture, plomberie-chauffage, electricite, menuiserie, platrerie-peinture, isolation-etancheite, gros-oeuvre, encyclopedie-generale, pathologies, normes-reglements",
                    "enum": ["maconnerie", "charpente-couverture", "plomberie-chauffage", "electricite", "menuiserie", "platrerie-peinture", "isolation-etancheite", "gros-oeuvre", "encyclopedie-generale", "pathologies", "normes-reglements"]
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
        "name": "ask_batiment",
        "description": (
            "Pose une question sur les métiers du bâtiment et obtient une réponse synthétisée "
            "par un LLM à partir des sources de la base de connaissances. Contrairement à "
            "search_batiment qui retourne des passages bruts, ask_batiment retourne une réponse "
            "structurée et directement utilisable. Idéal pour des questions précises nécessitant "
            "une synthèse (ex: 'Quelles sont les étapes de pose d'un plancher chauffant ?', "
            "'Comment diagnostiquer des remontées capillaires ?')."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "La question technique à poser sur les métiers du bâtiment"
                },
                "corps_etat": {
                    "type": "string",
                    "description": "Filtrer par corps d'état pour cibler la recherche (optionnel)",
                    "enum": ["maconnerie", "charpente-couverture", "plomberie-chauffage", "electricite", "menuiserie", "platrerie-peinture", "isolation-etancheite", "gros-oeuvre", "encyclopedie-generale", "pathologies", "normes-reglements"]
                },
                "nb_sources": {
                    "type": "integer",
                    "description": "Nombre de passages sources à utiliser pour la synthèse (défaut: 5, max: 8)",
                    "default": 5,
                    "minimum": 2,
                    "maximum": 8
                }
            },
            "required": ["question"]
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


FIABILITE_LABELS = {
    "patrimoine": "Patrimoine XIXe s.",
    "technique-ancien": "Manuel technique ancien",
    "technique-moderne": "Guide technique moderne",
    "norme-en-vigueur": "Norme/Réglementation en vigueur",
}


def search_in_supabase(query: str, corps_etat: str = None, nb_resultats: int = 5) -> list[dict]:
    """Effectue une recherche sémantique dans Supabase, retourne aussi les métadonnées."""
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
    results = r.json()
    
    # Enrichir avec les métadonnées si elles ne sont pas déjà dans les résultats RPC
    if results and "auteur" not in results[0]:
        ids = [str(row.get("id", "")) for row in results if row.get("id")]
        if ids:
            r_meta = requests.get(
                f"{SUPABASE_URL}/rest/v1/batiment_chunks",
                headers=headers,
                params={
                    "select": "id,auteur,titre_ouvrage,annee_publication,fiabilite",
                    "id": f"in.({','.join(ids)})",
                    "limit": str(len(ids))
                },
                timeout=15
            )
            if r_meta.status_code == 200:
                meta_map = {str(row["id"]): row for row in r_meta.json()}
                for row in results:
                    row_id = str(row.get("id", ""))
                    if row_id in meta_map:
                        row.update(meta_map[row_id])
    
    return results


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
    
    anciens = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    
    if anciens and modernes:
        annees_anciens = [p["annee_publication"] for p in anciens if p.get("annee_publication")]
        annees_modernes = [p["annee_publication"] for p in modernes if p.get("annee_publication")]
        
        if annees_anciens and annees_modernes:
            ecart = min(annees_modernes) - max(annees_anciens)
            if ecart > 50:
                noms_anciens = list(set(p.get("auteur", "?") for p in anciens if p.get("auteur")))
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
    """Synthétise une réponse à partir des passages trouvés via un LLM, en tenant compte des époques."""
    context_parts = []
    for i, p in enumerate(passages, 1):
        auteur = p.get("auteur") or p.get("source", "Source inconnue")
        annee = p.get("annee_publication")
        fiabilite = p.get("fiabilite", "")
        label = FIABILITE_LABELS.get(fiabilite, fiabilite)
        source_header = f"{auteur} ({annee}) [{label}]" if annee else auteur
        content = p.get("content", "")[:1200]
        context_parts.append(f"[Source {i}: {source_header}]\n{content}")
    
    context = "\n\n---\n\n".join(context_parts)
    
    anciens = [p for p in passages if p.get("fiabilite") in ("patrimoine", "technique-ancien")]
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
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": 1500,
        "temperature": 0.3
    }
    
    r = requests.post(OPENROUTER_CHAT_URL, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def get_sources_from_supabase(corps_etat: str = None) -> list[dict]:
    """Liste les sources uniques dans la base."""
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    }
    
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    params = {
        "select": "source,corps_etat",
        "order": "corps_etat",
        "limit": "200"
    }
    if corps_etat:
        params["corps_etat"] = f"eq.{corps_etat}"
    
    r = requests.get(url, headers=headers, params=params, timeout=20)
    r.raise_for_status()
    
    # Dédupliquer par source
    seen = set()
    sources = []
    for row in r.json():
        key = row.get("source", "")
        if key not in seen:
            seen.add(key)
            sources.append(row)
    return sources


def get_stats_from_supabase() -> dict:
    """Récupère les statistiques de la base via une requête RPC SQL agrégée."""
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
        "Content-Type": "application/json",
    }
    
    # Nombre total de chunks (count exact)
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers={**headers, "Prefer": "count=exact"},
        params={"select": "id", "limit": "1"},
        timeout=20
    )
    total = int(r.headers.get("content-range", "0/0").split("/")[-1])
    
    # Répartition par corps d'état via RPC SQL (évite la limite de 1000 lignes)
    r2 = requests.post(
        f"{SUPABASE_URL}/rest/v1/rpc/get_stats_corps_etat",
        headers=headers,
        json={},
        timeout=20
    )
    corps_etats = {}
    if r2.status_code == 200:
        for row in r2.json():
            corps_etats[row["corps_etat"]] = row["nb_chunks"]
    else:
        # Fallback : requête paginée si la fonction RPC n'existe pas
        offset = 0
        page_size = 1000
        while True:
            r_page = requests.get(
                f"{SUPABASE_URL}/rest/v1/batiment_chunks",
                headers=headers,
                params={"select": "corps_etat", "limit": str(page_size), "offset": str(offset)},
                timeout=20
            )
            rows = r_page.json()
            if not rows:
                break
            for row in rows:
                ce = row.get("corps_etat", "inconnu")
                corps_etats[ce] = corps_etats.get(ce, 0) + 1
            if len(rows) < page_size:
                break
            offset += page_size
    
    return {"total_chunks": total, "repartition_corps_etat": corps_etats}


# ─── Endpoints MCP ────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"name": "batiment-kb-mcp", "version": "3.0.0", "status": "ok"}


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
                corps = r.get("corps_etat", "N/A")
                content_text = r.get("content", "")
                
                # Badge source avec métadonnées
                source_badge = format_source_badge(r)
                
                # Extraire le préfixe de section si présent (format [Source — Section])
                section_info = ""
                if content_text.startswith("[") and "]" in content_text[:200]:
                    bracket_end = content_text.index("]")
                    section_info = content_text[1:bracket_end]
                    content_preview = content_text[bracket_end+2:bracket_end+802]
                else:
                    content_preview = content_text[:800]
                
                parts.append(
                    f"\n---\n**[{i}]** `{corps_etat or corps}` | **{source_badge}**  \n"
                    + (f"*Section : {section_info}*  \n" if section_info else "")
                    + f"Pertinence : {similarity_pct}%\n\n"
                    f"{content_preview}..."
                )
            
            # Avertissement si sources d'époques différentes
            divergence_note = detect_divergences(results)
            content = "\n".join(parts) + divergence_note
        
        return {"content": [{"type": "text", "text": content}]}
    
    elif request.name == "ask_batiment":
        question = request.arguments.get("question", "")
        corps_etat = request.arguments.get("corps_etat")
        nb_sources = min(request.arguments.get("nb_sources", 5), 8)
        
        if not question:
            raise HTTPException(status_code=400, detail="Le paramètre 'question' est requis")
        
        if not OPENROUTER_API_KEY:
            raise HTTPException(status_code=503, detail="Clé API OpenRouter non configurée")
        
        try:
            # Rechercher les passages pertinents
            passages = search_in_supabase(question, corps_etat, nb_sources)
            
            if not passages:
                return {"content": [{"type": "text", "text": "Aucune information trouvée dans la base de connaissances pour répondre à cette question."}]}
            
            # Synthétiser avec le LLM
            answer = synthesize_with_llm(question, passages)
            
            # Ajouter les sources en bas avec métadonnées
            seen_sources = set()
            sources_lines = []
            for p in passages:
                auteur = p.get("auteur") or p.get("source", "N/A")
                annee = p.get("annee_publication")
                fiabilite = p.get("fiabilite", "")
                label = FIABILITE_LABELS.get(fiabilite, fiabilite)
                titre = p.get("titre_ouvrage") or p.get("source", "N/A")
                key = f"{auteur}_{annee}"
                if key not in seen_sources:
                    seen_sources.add(key)
                    if annee:
                        sources_lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}")
                    else:
                        sources_lines.append(f"- {titre}")
            
            divergence_note = detect_divergences(passages)
            full_response = f"{answer}\n\n---\n**Sources consultées :**\n" + "\n".join(sources_lines[:6]) + divergence_note
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur lors de la synthèse: {str(e)}")
        
        return {"content": [{"type": "text", "text": full_response}]}
    
    elif request.name == "list_sources":
        corps_etat = request.arguments.get("corps_etat")
        try:
            sources = get_sources_from_supabase(corps_etat)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        # Enrichir avec les métadonnées
        headers_meta = {
            "apikey": SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
        }
        try:
            params_meta = {
                "select": "source,corps_etat,auteur,annee_publication,fiabilite,titre_ouvrage",
                "order": "corps_etat,annee_publication",
                "limit": "300"
            }
            if corps_etat:
                params_meta["corps_etat"] = f"eq.{corps_etat}"
            r_meta = requests.get(
                f"{SUPABASE_URL}/rest/v1/batiment_chunks",
                headers=headers_meta,
                params=params_meta,
                timeout=20
            )
            if r_meta.status_code == 200:
                seen = set()
                sources = []
                for row in r_meta.json():
                    key = (row.get("source", ""), row.get("corps_etat", ""))
                    if key not in seen:
                        seen.add(key)
                        sources.append(row)
        except Exception:
            pass
        
        lines = ["**Sources indexées dans la base de connaissances bâtiment :**\n"]
        current_corps = None
        for s in sources:
            ce = s.get("corps_etat", "N/A")
            if ce != current_corps:
                lines.append(f"\n### {ce}")
                current_corps = ce
            auteur = s.get("auteur")
            annee = s.get("annee_publication")
            fiabilite = s.get("fiabilite", "")
            label = FIABILITE_LABELS.get(fiabilite, "")
            titre = s.get("titre_ouvrage") or s.get("source", "N/A")
            if auteur and annee:
                lines.append(f"- **{auteur}** ({annee}) — *{label}* — {titre}")
            else:
                lines.append(f"- {titre}")
        
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
        for ce, count in sorted(stats["repartition_corps_etat"].items(), key=lambda x: -x[1]):
            lines.append(f"  - `{ce}` : {count} chunk(s)")
        
        return {"content": [{"type": "text", "text": "\n".join(lines)}]}
    
    else:
        raise HTTPException(status_code=404, detail=f"Outil '{request.name}' non trouvé")


# ─── Point d'entrée ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
