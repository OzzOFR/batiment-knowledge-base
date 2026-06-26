"""
Script de ré-indexation des fiches techniques avec le chunker sémantique amélioré.

Ce script :
1. Supprime les anciens chunks des fiches nouvelles_sources dans Supabase
2. Les ré-indexe avec le nouveau chunker sémantique (par sections H2/H3)
3. Chaque chunk est préfixé par son titre de section pour le contexte

Usage : python3 scripts/reindex_with_semantic_chunker.py
"""

import os
import sys
import time
import requests

# Ajouter le répertoire scripts au PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semantic_chunker import SemanticChunker

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

# Fiches à ré-indexer avec le chunker sémantique
FICHES = [
    {
        "file": "corpus/nouvelles_sources/fiche_maconnerie_precheur.md",
        "corps_etat": "maconnerie",
        "source": "Fiche maçonnerie - Manuel du Maçon (Prêcheur/Eyrolles) et Rondelet",
        "source_title": "Maçonnerie — Manuel du Maçon"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_electricite_installations.md",
        "corps_etat": "electricite",
        "source": "Fiche électricité - Installations électriques du bâtiment",
        "source_title": "Électricité — Installations du bâtiment"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_plomberie_chauffage.md",
        "corps_etat": "plomberie-chauffage",
        "source": "Fiche plomberie et chauffage - Installations sanitaires et thermiques",
        "source_title": "Plomberie et Chauffage"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_isolation_thermique.md",
        "corps_etat": "isolation-etancheite",
        "source": "Fiche isolation thermique - Techniques et matériaux",
        "source_title": "Isolation Thermique"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_charpente_couverture.md",
        "corps_etat": "charpente-couverture",
        "source": "Fiche charpente et couverture - Techniques et matériaux",
        "source_title": "Charpente et Couverture"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_pathologies.md",
        "corps_etat": "pathologies",
        "source": "Fiche pathologies du bâtiment - Désordres et remèdes",
        "source_title": "Pathologies du Bâtiment"
    },
    {
        "file": "corpus/nouvelles_sources/fiche_normes_reglements.md",
        "corps_etat": "normes-reglements",
        "source": "Fiche normes et réglements - RE2020, PMR, sécurité incendie",
        "source_title": "Normes et Réglements"
    },
]

def get_embedding(text: str) -> list:
    """Obtient l'embedding via OpenRouter."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": text[:8000]
    }
    
    for attempt in range(3):
        try:
            r = requests.post("https://openrouter.ai/api/v1/embeddings", headers=headers, json=payload, timeout=20)
            r.raise_for_status()
            return r.json()["data"][0]["embedding"]
        except Exception as e:
            print(f"    Erreur embedding (tentative {attempt+1}/3): {e}")
            time.sleep(2)
    
    raise Exception("Échec de l'obtention de l'embedding après 3 tentatives")

def delete_chunks_by_source(source: str) -> int:
    """Supprime tous les chunks d'une source donnée dans Supabase."""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    
    # D'abord compter
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"source": f"eq.{source}", "select": "id", "limit": 1000}
    )
    
    if r.status_code != 200:
        print(f"  Erreur lors de la récupération: {r.status_code}")
        return 0
    
    existing = r.json()
    count = len(existing)
    
    if count == 0:
        print(f"  Aucun chunk existant pour cette source")
        return 0
    
    # Supprimer
    r = requests.delete(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"source": f"eq.{source}"}
    )
    
    if r.status_code in (200, 204):
        print(f"  {count} anciens chunks supprimés")
        return count
    else:
        print(f"  Erreur suppression: {r.status_code} - {r.text[:100]}")
        return 0

def index_fiche(fiche: dict, chunker: SemanticChunker, base_dir: str) -> int:
    """Indexe une fiche avec le chunker sémantique."""
    filepath = os.path.join(base_dir, fiche["file"])
    
    if not os.path.exists(filepath):
        print(f"  [MANQUANT] {fiche['file']}")
        return 0
    
    print(f"\n[FICHE] {os.path.basename(filepath)}")
    print(f"  Corps d'état: {fiche['corps_etat']}")
    
    # Supprimer les anciens chunks
    print(f"  Suppression des anciens chunks...")
    delete_chunks_by_source(fiche["source"])
    
    # Lire le fichier
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chunker sémantiquement
    chunks = chunker.chunk_markdown(content, source_title=fiche["source_title"])
    print(f"  -> {len(chunks)} chunks sémantiques")
    
    # Indexer dans Supabase
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    success_count = 0
    for i, chunk in enumerate(chunks):
        if i % 5 == 0 and i > 0:
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
            success_count += 1
        
        except Exception as e:
            print(f"  Erreur sur le chunk {i+1}: {e}")
    
    print(f"  -> {success_count}/{len(chunks)} chunks indexés")
    return success_count

if __name__ == "__main__":
    print("=== Ré-indexation avec le chunker sémantique ===\n")
    
    if not OPENROUTER_API_KEY:
        print("ERREUR: OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    base_dir = "/home/ubuntu/batiment-knowledge-base"
    chunker = SemanticChunker(max_chars=1500, min_chars=150, overlap_chars=200)
    
    total_new = 0
    for fiche in FICHES:
        new_chunks = index_fiche(fiche, chunker, base_dir)
        total_new += new_chunks
    
    print(f"\n=== Terminé ! ===")
    print(f"  Total nouveaux chunks (chunking sémantique): {total_new}")
