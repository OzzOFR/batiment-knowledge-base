#!/usr/bin/env python3
"""
Agent IA Bâtiment — RAG spécialisé architecture et construction.

v1.0 — Agent RAG avec :
  - Recherche sémantique dans la base PostgreSQL (768 dims, sentence-transformers)
  - Pondération par fiabilité (normes > technique moderne > XIXe > patrimoine)
  - Mémoire de conversation (contexte de projet)
  - Synthèse LLM via OpenRouter (multi-modèles : Mistral, Llama, GPT-4o-mini)
  - Détection et signalement des divergences sources anciennes/modernes
  - API REST exposée sur /chat, /ask, /health
  - Mode standalone (sans OpenRouter) avec réponse par passages bruts

Architecture :
  [Utilisateur] → [Agent API] → [Recherche sémantique PostgreSQL]
                              → [Pondération + reranking]
                              → [Synthèse LLM (OpenRouter)]
                              → [Réponse structurée + sources]
"""

import os
import json
import time
import uuid
import hashlib
import psycopg2
import psycopg2.extras
import requests
from contextlib import contextmanager
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ─── Configuration ────────────────────────────────────────────────────────────
PG_HOST     = os.environ.get("PG_HOST", "forge-postgres")
PG_PORT     = int(os.environ.get("PG_PORT", "5432"))
PG_DB       = os.environ.get("PG_DB", "batiment_knowledge")
PG_USER     = os.environ.get("PG_USER", "createk")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "Forge2026Hozzo!")

EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
EMBEDDING_DIMS = 768

# OpenRouter — multi-modèles avec fallback
OPENROUTER_API_KEY  = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

# Modèles par ordre de préférence (coût croissant, qualité croissante)
LLM_MODELS = [
    "mistralai/mistral-7b-instruct",       # open source, rapide, économique
    "meta-llama/llama-3.1-8b-instruct",    # open source, bon rapport qualité/prix
    "openai/gpt-4o-mini",                   # fallback commercial
]

PORT = int(os.environ.get("AGENT_PORT", "8200"))

# ─── Pondération par fiabilité ────────────────────────────────────────────────
# Plus le score est élevé, plus la source est prioritaire dans le reranking
FIABILITE_WEIGHTS = {
    "norme-en-vigueur":  1.30,   # DTU, NF, RE 2020 — priorité maximale
    "technique-moderne": 1.15,   # Guides CSTB, ADEME post-1970
    "technique_xix_xx":  1.00,   # Ouvrages XIXe-XXe siècle (base)
    "patrimoine_xix":    0.90,   # Patrimoine XIXe (restauration)
    "patrimoine":        0.90,
    "technique-ancien":  1.00,
}

FIABILITE_LABELS = {
    "norme-en-vigueur":  "Norme en vigueur",
    "technique-moderne": "Technique moderne",
    "technique_xix_xx":  "Technique XIXe-XXe s.",
    "patrimoine_xix":    "Patrimoine XIXe s.",
    "patrimoine":        "Patrimoine XIXe s.",
    "technique-ancien":  "Technique XIXe-XXe s.",
}

# ─── Mémoire de conversation (en mémoire, sessions TTL 2h) ───────────────────
_sessions: dict = {}
SESSION_TTL = 7200  # 2 heures

def get_session(session_id: str) -> dict:
    """Récupère ou crée une session de conversation."""
    now = time.time()
    # Nettoyer les sessions expirées
    expired = [k for k, v in _sessions.items() if now - v["last_activity"] > SESSION_TTL]
    for k in expired:
        del _sessions[k]
    
    if session_id not in _sessions:
        _sessions[session_id] = {
            "id": session_id,
            "history": [],
            "context": {},  # contexte de projet (type bâtiment, époque, etc.)
            "created_at": now,
            "last_activity": now,
        }
    else:
        _sessions[session_id]["last_activity"] = now
    return _sessions[session_id]


def add_to_history(session: dict, role: str, content: str):
    """Ajoute un message à l'historique de la session."""
    session["history"].append({"role": role, "content": content})
    # Garder les 10 derniers échanges (20 messages)
    if len(session["history"]) > 20:
        session["history"] = session["history"][-20:]


# ─── Modèle d'embedding (singleton) ──────────────────────────────────────────
_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        from sentence_transformers import SentenceTransformer
        print(f"[Agent] Chargement modèle embedding : {EMBEDDING_MODEL_NAME}")
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        print(f"[Agent] Modèle chargé — {_embedding_model.get_sentence_embedding_dimension()} dims")
    return _embedding_model


def embed_query(text: str) -> list[float]:
    """Génère l'embedding d'une requête."""
    model = get_embedding_model()
    return model.encode(text).tolist()


# ─── Base de données ──────────────────────────────────────────────────────────
@contextmanager
def get_db():
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASSWORD,
        connect_timeout=10
    )
    conn.cursor_factory = psycopg2.extras.RealDictCursor
    try:
        yield conn
    finally:
        conn.close()


def search_passages(
    query: str,
    corps_etat: Optional[str] = None,
    nb_results: int = 6,
    min_similarity: float = 0.25,
) -> list[dict]:
    """
    Recherche sémantique avec pondération par fiabilité.
    
    Stratégie :
    1. Récupérer nb_results * 2 candidats par similarité cosinus pure
    2. Appliquer le score pondéré : score_final = similarity * weight_fiabilite
    3. Retourner les nb_results meilleurs
    """
    embedding = embed_query(query)
    emb_str = "[" + ",".join(map(str, embedding)) + "]"
    
    fetch_n = nb_results * 3  # sursampling pour le reranking
    
    with get_db() as conn:
        with conn.cursor() as cur:
            if corps_etat:
                cur.execute("""
                    SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                           annee_publication, fiabilite,
                           1 - (embedding <=> %s::vector) AS similarity
                    FROM batiment_chunks
                    WHERE embedding IS NOT NULL
                      AND corps_etat = %s
                      AND 1 - (embedding <=> %s::vector) > %s
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s
                """, (emb_str, corps_etat, emb_str, min_similarity, emb_str, fetch_n))
            else:
                cur.execute("""
                    SELECT id, content, corps_etat, source, auteur, titre_ouvrage,
                           annee_publication, fiabilite,
                           1 - (embedding <=> %s::vector) AS similarity
                    FROM batiment_chunks
                    WHERE embedding IS NOT NULL
                      AND 1 - (embedding <=> %s::vector) > %s
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s
                """, (emb_str, emb_str, min_similarity, emb_str, fetch_n))
            
            rows = [dict(r) for r in cur.fetchall()]
    
    # Reranking avec pondération fiabilité
    for row in rows:
        fiabilite = row.get("fiabilite", "")
        weight = FIABILITE_WEIGHTS.get(fiabilite, 1.0)
        row["score_final"] = float(row["similarity"]) * weight
    
    rows.sort(key=lambda x: x["score_final"], reverse=True)
    return rows[:nb_results]


def detect_divergences(passages: list[dict]) -> str:
    """Détecte les divergences entre sources d'époques différentes."""
    if len(passages) < 2:
        return ""
    
    anciens  = [p for p in passages if p.get("fiabilite") in ("patrimoine", "patrimoine_xix", "technique-ancien", "technique_xix_xx")]
    modernes = [p for p in passages if p.get("fiabilite") in ("technique-moderne", "norme-en-vigueur")]
    
    if anciens and modernes:
        annees_a = [p["annee_publication"] for p in anciens  if p.get("annee_publication")]
        annees_m = [p["annee_publication"] for p in modernes if p.get("annee_publication")]
        
        if annees_a and annees_m and (min(annees_m) - max(annees_a)) > 50:
            noms_a = list(set(p.get("auteur", "?") for p in anciens  if p.get("auteur")))[:2]
            noms_m = list(set(p.get("auteur", "?") for p in modernes if p.get("auteur")))[:2]
            return (
                f"\n\n> ⚠️ **Sources d'époques différentes** : "
                f"sources anciennes ({', '.join(noms_a)}, ~{max(annees_a)}) "
                f"et sources modernes ({', '.join(noms_m)}, ~{min(annees_m)}). "
                f"En cas de contradiction, privilégier les sources modernes pour les pratiques actuelles, "
                f"les sources anciennes pour la restauration du patrimoine."
            )
    return ""


# ─── Synthèse LLM ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """Tu es HERMES, un expert en architecture, construction et techniques du bâtiment.
Tu travailles pour Createk Engineering / OzzO, spécialisé dans la rénovation et la construction en France.

Tes domaines d'expertise couvrent tous les corps d'état :
- Gros œuvre (maçonnerie, béton armé, fondations, charpente)
- Second œuvre (plomberie, électricité, menuiserie, plâtrerie, peinture)
- Isolation et étanchéité
- Pathologies du bâtiment (humidité, fissures, désordres structurels)
- Réglementation française (DTU, RT/RE 2020, normes NF, diagnostics)
- Restauration du patrimoine bâti ancien

Tu réponds en te basant UNIQUEMENT sur les passages fournis de la base de connaissances.
Chaque passage est annoté avec son auteur, son année et son niveau de fiabilité.

Règles de réponse :
1. Structurer avec des titres si la réponse est longue
2. Citer les sources (Auteur, année) pour chaque information technique importante
3. Distinguer clairement les pratiques actuelles (normes, DTU) des pratiques historiques
4. Signaler si les informations sont insuffisantes pour répondre complètement
5. Toujours répondre en français
6. Être précis et technique, éviter les généralités vagues
7. Pour les questions de sécurité (incendie, structure, électricité), recommander de consulter un professionnel qualifié"""


def build_context(passages: list[dict], max_chars_per_passage: int = 1000) -> str:
    """Construit le contexte à partir des passages."""
    parts = []
    for i, p in enumerate(passages, 1):
        auteur    = p.get("auteur") or p.get("source", "Source inconnue")
        annee     = p.get("annee_publication")
        fiabilite = p.get("fiabilite", "")
        label     = FIABILITE_LABELS.get(fiabilite, fiabilite)
        corps     = p.get("corps_etat", "")
        score     = p.get("score_final", p.get("similarity", 0))
        
        header = f"[Source {i}: {auteur}"
        if annee:
            header += f" ({annee})"
        header += f" — {label} — {corps}] (pertinence: {score:.1%})"
        
        content = p.get("content", "")[:max_chars_per_passage]
        parts.append(f"{header}\n{content}")
    
    return "\n\n---\n\n".join(parts)


def call_llm(
    messages: list[dict],
    model: str = None,
    max_tokens: int = 1500,
    temperature: float = 0.3,
) -> str:
    """Appelle le LLM via OpenRouter avec fallback multi-modèles."""
    if not OPENROUTER_API_KEY:
        raise ValueError("Clé OpenRouter non configurée")
    
    models_to_try = [model] + LLM_MODELS if model else LLM_MODELS
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://createk.engineering",
        "X-Title": "Hermes Agent Batiment",
    }
    
    last_error = None
    for m in models_to_try:
        try:
            payload = {
                "model": m,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
            r = requests.post(OPENROUTER_CHAT_URL, headers=headers, json=payload, timeout=60)
            r.raise_for_status()
            return r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            last_error = e
            print(f"[Agent] Modèle {m} échoué: {e}")
            continue
    
    raise RuntimeError(f"Tous les modèles LLM ont échoué. Dernière erreur: {last_error}")


def synthesize_answer(
    question: str,
    passages: list[dict],
    history: list[dict] = None,
    context: dict = None,
) -> str:
    """Génère une réponse synthétisée à partir des passages et de l'historique."""
    
    kb_context = build_context(passages)
    divergence_note = detect_divergences(passages)
    
    # Construire le prompt utilisateur
    context_info = ""
    if context:
        if context.get("type_batiment"):
            context_info += f"\nContexte de projet : {context['type_batiment']}"
        if context.get("epoque"):
            context_info += f", époque : {context['epoque']}"
        if context.get("localisation"):
            context_info += f", localisation : {context['localisation']}"
    
    user_content = f"""Question : {question}{context_info}

Passages de la base de connaissances bâtiment :

{kb_context}

Réponds à la question en citant les sources (auteur + année) pour chaque information importante.{divergence_note}"""
    
    # Construire les messages avec historique
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    if history:
        # Inclure les 6 derniers échanges de l'historique
        for msg in history[-12:]:
            messages.append(msg)
    
    messages.append({"role": "user", "content": user_content})
    
    return call_llm(messages)


# ─── Réponse sans LLM (mode dégradé) ─────────────────────────────────────────
def format_passages_response(question: str, passages: list[dict]) -> str:
    """Formate les passages bruts quand le LLM n'est pas disponible."""
    if not passages:
        return f"Aucune information trouvée dans la base de connaissances pour : *{question}*"
    
    lines = [f"**{len(passages)} résultat(s) trouvé(s) pour : \"{question}\"**\n"]
    
    for i, p in enumerate(passages, 1):
        auteur    = p.get("auteur") or p.get("source", "N/A")
        annee     = p.get("annee_publication")
        fiabilite = p.get("fiabilite", "")
        label     = FIABILITE_LABELS.get(fiabilite, fiabilite)
        corps     = p.get("corps_etat", "")
        score     = p.get("score_final", p.get("similarity", 0))
        titre     = p.get("titre_ouvrage") or ""
        content   = p.get("content", "")[:600]
        
        header = f"**[{i}]** `{corps}` | **{auteur}"
        if annee:
            header += f" ({annee})"
        header += f" — *{label}***"
        if titre:
            header += f"\n*{titre}*"
        header += f"\nPertinence : {score:.1%}"
        
        lines.append(f"---\n{header}\n{content}\n")
    
    lines.append(detect_divergences(passages))
    return "\n".join(lines)


# ─── Application FastAPI ──────────────────────────────────────────────────────
app = FastAPI(
    title="Hermes — Agent IA Bâtiment",
    description="Agent RAG spécialisé architecture et construction — Createk Engineering",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    corps_etat: Optional[str] = None
    nb_sources: int = 6
    use_llm: bool = True
    model: Optional[str] = None
    context: Optional[dict] = None  # {"type_batiment": "maison 1900", "epoque": "XIXe", ...}


class ChatResponse(BaseModel):
    session_id: str
    answer: str
    sources: list[dict]
    nb_sources_used: int
    model_used: Optional[str]
    processing_time_ms: int


class AskRequest(BaseModel):
    question: str
    corps_etat: Optional[str] = None
    nb_sources: int = 5
    use_llm: bool = True


@app.get("/health")
def health():
    """Vérification de l'état du service."""
    try:
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) as total FROM batiment_chunks WHERE embedding IS NOT NULL")
                row = cur.fetchone()
                total = row["total"] if row else 0
        return {
            "status": "healthy",
            "chunks_indexed": total,
            "embedding_model": EMBEDDING_MODEL_NAME,
            "llm_available": bool(OPENROUTER_API_KEY),
            "active_sessions": len(_sessions),
        }
    except Exception as e:
        return {"status": "degraded", "error": str(e)}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    Endpoint principal de conversation avec mémoire de session.
    
    Supporte le contexte de projet (type de bâtiment, époque, localisation).
    Utilise le LLM si disponible, sinon retourne les passages bruts.
    """
    start = time.time()
    
    # Gérer la session
    session_id = req.session_id or str(uuid.uuid4())
    session = get_session(session_id)
    
    # Mettre à jour le contexte de projet si fourni
    if req.context:
        session["context"].update(req.context)
    
    # Recherche sémantique
    try:
        passages = search_passages(
            query=req.message,
            corps_etat=req.corps_etat,
            nb_results=req.nb_sources,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur recherche: {str(e)}")
    
    # Synthèse
    model_used = None
    if req.use_llm and OPENROUTER_API_KEY and passages:
        try:
            answer = synthesize_answer(
                question=req.message,
                passages=passages,
                history=session["history"],
                context=session["context"],
            )
            model_used = req.model or LLM_MODELS[0]
        except Exception as e:
            print(f"[Agent] LLM échoué, mode dégradé: {e}")
            answer = format_passages_response(req.message, passages)
    else:
        answer = format_passages_response(req.message, passages)
    
    # Sauvegarder dans l'historique
    add_to_history(session, "user", req.message)
    add_to_history(session, "assistant", answer[:2000])  # tronquer pour l'historique
    
    # Formater les sources pour la réponse
    sources_out = []
    seen = set()
    for p in passages:
        key = f"{p.get('auteur')}_{p.get('annee_publication')}"
        if key not in seen:
            seen.add(key)
            sources_out.append({
                "auteur": p.get("auteur"),
                "annee": p.get("annee_publication"),
                "titre": p.get("titre_ouvrage"),
                "corps_etat": p.get("corps_etat"),
                "fiabilite": FIABILITE_LABELS.get(p.get("fiabilite", ""), p.get("fiabilite", "")),
                "pertinence": round(p.get("score_final", p.get("similarity", 0)), 3),
            })
    
    elapsed_ms = int((time.time() - start) * 1000)
    
    return ChatResponse(
        session_id=session_id,
        answer=answer,
        sources=sources_out,
        nb_sources_used=len(passages),
        model_used=model_used,
        processing_time_ms=elapsed_ms,
    )


@app.post("/ask")
def ask(req: AskRequest):
    """
    Endpoint simple sans session — question/réponse directe.
    Compatible avec l'interface MCP existante.
    """
    start = time.time()
    
    passages = search_passages(
        query=req.question,
        corps_etat=req.corps_etat,
        nb_results=req.nb_sources,
    )
    
    if req.use_llm and OPENROUTER_API_KEY and passages:
        try:
            answer = synthesize_answer(question=req.question, passages=passages)
        except Exception as e:
            answer = format_passages_response(req.question, passages)
    else:
        answer = format_passages_response(req.question, passages)
    
    elapsed_ms = int((time.time() - start) * 1000)
    
    return {
        "answer": answer,
        "nb_sources": len(passages),
        "processing_time_ms": elapsed_ms,
        "sources": [
            {
                "auteur": p.get("auteur"),
                "annee": p.get("annee_publication"),
                "corps_etat": p.get("corps_etat"),
                "pertinence": round(p.get("score_final", 0), 3),
            }
            for p in passages
        ]
    }


@app.get("/sessions/{session_id}")
def get_session_info(session_id: str):
    """Récupère les informations d'une session."""
    if session_id not in _sessions:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    s = _sessions[session_id]
    return {
        "session_id": session_id,
        "nb_messages": len(s["history"]),
        "context": s["context"],
        "created_at": s["created_at"],
        "last_activity": s["last_activity"],
    }


@app.delete("/sessions/{session_id}")
def clear_session(session_id: str):
    """Efface une session (réinitialise la mémoire de conversation)."""
    if session_id in _sessions:
        del _sessions[session_id]
    return {"status": "cleared", "session_id": session_id}


@app.get("/stats")
def get_stats():
    """Statistiques de la base de connaissances."""
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) as total FROM batiment_chunks WHERE embedding IS NOT NULL")
            total = cur.fetchone()["total"]
            
            cur.execute("""
                SELECT corps_etat, COUNT(*) as nb
                FROM batiment_chunks
                GROUP BY corps_etat
                ORDER BY nb DESC
            """)
            by_corps = {r["corps_etat"]: r["nb"] for r in cur.fetchall()}
            
            cur.execute("""
                SELECT fiabilite, COUNT(*) as nb
                FROM batiment_chunks
                GROUP BY fiabilite
                ORDER BY nb DESC
            """)
            by_fiabilite = {
                FIABILITE_LABELS.get(r["fiabilite"], r["fiabilite"]): r["nb"]
                for r in cur.fetchall()
            }
    
    return {
        "total_chunks": total,
        "by_corps_etat": by_corps,
        "by_fiabilite": by_fiabilite,
        "embedding_model": EMBEDDING_MODEL_NAME,
        "embedding_dims": EMBEDDING_DIMS,
        "active_sessions": len(_sessions),
    }


# ─── Point d'entrée ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    print(f"[Agent] Démarrage Hermes Agent Bâtiment v1.0 sur port {PORT}")
    print(f"[Agent] LLM disponible: {bool(OPENROUTER_API_KEY)}")
    get_embedding_model()  # Pré-charger le modèle
    uvicorn.run(app, host="0.0.0.0", port=PORT)
