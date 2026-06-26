"""
Script d'indexation des nouvelles fiches techniques spécialisées.
Utilise le SemanticChunker pour un découpage par sections H2/H3.
"""

import os
import sys
import time
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semantic_chunker import SemanticChunker

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

FICHES = [
    {
        "file": "corpus/plomberie/fiche_plomberie_chauffage_complet.md",
        "corps_etat": "plomberie-chauffage",
        "source": "Fiche technique plomberie-chauffage (OzzO Knowledge Base)",
        "source_title": "Plomberie, Chauffage et Installations Sanitaires"
    },
    {
        "file": "corpus/electricite2/fiche_electricite_batiment_complet.md",
        "corps_etat": "electricite",
        "source": "Fiche technique électricité bâtiment (OzzO Knowledge Base)",
        "source_title": "Installations Électriques du Bâtiment"
    },
    {
        "file": "corpus/pathologies/fiche_pathologies_batiment_complet.md",
        "corps_etat": "pathologies",
        "source": "Fiche technique pathologies bâtiment (OzzO Knowledge Base)",
        "source_title": "Pathologies du Bâtiment"
    },
]


def get_embedding(text: str) -> list:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"model": "text-embedding-3-small", "input": text[:8000]}
    for attempt in range(3):
        try:
            r = requests.post("https://openrouter.ai/api/v1/embeddings", headers=headers, json=payload, timeout=25)
            r.raise_for_status()
            return r.json()["data"][0]["embedding"]
        except Exception as e:
            print(f"    Erreur embedding (tentative {attempt+1}/3): {e}")
            time.sleep(3)
    raise Exception("Échec embedding")


def delete_chunks_by_source(source: str) -> int:
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"source": f"eq.{source}", "select": "id", "limit": 1000}
    )
    count = len(r.json()) if r.status_code == 200 else 0
    if count > 0:
        requests.delete(
            f"{SUPABASE_URL}/rest/v1/batiment_chunks",
            headers={**headers, "Content-Type": "application/json"},
            params={"source": f"eq.{source}"}
        )
    return count


def index_fiche(fiche: dict, chunker: SemanticChunker, base_dir: str) -> int:
    filepath = os.path.join(base_dir, fiche["file"])
    if not os.path.exists(filepath):
        print(f"  [MANQUANT] {fiche['file']}")
        return 0
    
    print(f"\n[FICHE] {os.path.basename(filepath)}")
    
    # Supprimer les anciens chunks
    deleted = delete_chunks_by_source(fiche["source"])
    if deleted > 0:
        print(f"  {deleted} anciens chunks supprimés")
    
    # Lire et chunker
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chunks = chunker.chunk_markdown(content, source_title=fiche["source_title"])
    print(f"  -> {len(chunks)} chunks sémantiques")
    
    # Indexer
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    success = 0
    for i, chunk in enumerate(chunks):
        if i % 10 == 0 and i > 0:
            print(f"  ... {i}/{len(chunks)} traités")
        try:
            emb = get_embedding(chunk.content)
            data = {
                "content": chunk.content,
                "embedding": emb,
                "corps_etat": fiche["corps_etat"],
                "source": fiche["source"]
            }
            r = requests.post(f"{SUPABASE_URL}/rest/v1/batiment_chunks", headers=headers, json=data, timeout=15)
            r.raise_for_status()
            success += 1
        except Exception as e:
            print(f"  Erreur chunk {i+1}: {e}")
    
    print(f"  -> {success}/{len(chunks)} chunks indexés")
    return success


if __name__ == "__main__":
    print("=== Indexation des fiches techniques spécialisées ===\n")
    
    if not OPENROUTER_API_KEY:
        print("ERREUR: OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    base_dir = "/home/ubuntu/batiment-knowledge-base"
    chunker = SemanticChunker(max_chars=1500, min_chars=150, overlap_chars=200)
    
    total = 0
    for fiche in FICHES:
        n = index_fiche(fiche, chunker, base_dir)
        total += n
    
    print(f"\n=== Terminé ! Total: {total} nouveaux chunks ===")
