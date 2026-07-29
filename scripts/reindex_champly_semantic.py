"""
Script de ré-indexation des volumes Champly avec le SemanticChunker.

Ce script :
1. Supprime les anciens chunks Champly dans Supabase
2. Les ré-indexe avec le nouveau chunker sémantique (par sections H2/H3)
3. Chaque chunk est préfixé par son titre de section pour le contexte

Usage : python3 scripts/reindex_champly_semantic.py
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

# Mapping des volumes Champly
CHAMPLY_VOLUMES = [
    {
        "file": "corpus/champly/champly_vol01_arpentage-fondations.md",
        "corps_etat": "gros-oeuvre",
        "source": "Gallica BnF ark:/12148/bpt6k9774323q",
        "source_title": "Champly Vol.1 — Arpentage, Fondations"
    },
    {
        "file": "corpus/champly/champly_vol02_maconnerie-brique.md",
        "corps_etat": "maconnerie",
        "source": "Gallica BnF ark:/12148/bpt6k97743229",
        "source_title": "Champly Vol.2 — Maçonnerie, Pierre, Brique"
    },
    {
        "file": "corpus/champly/champly_vol03_beton-arme.md",
        "corps_etat": "gros-oeuvre",
        "source": "Gallica BnF ark:/12148/bpt6k9774321w",
        "source_title": "Champly Vol.3 — Béton Armé"
    },
    {
        "file": "corpus/champly/champly_vol04_charpente-bois.md",
        "corps_etat": "charpente-couverture",
        "source": "Gallica BnF ark:/12148/bpt6k938852q",
        "source_title": "Champly Vol.4 — Charpente Bois"
    },
    {
        "file": "corpus/champly/champly_vol05_charpentes-metalliques.md",
        "corps_etat": "charpente-couverture",
        "source": "Gallica BnF ark:/12148/bpt6k97744284",
        "source_title": "Champly Vol.5 — Charpentes Métalliques"
    },
    {
        "file": "corpus/champly/champly_vol06_couvertures-toitures.md",
        "corps_etat": "charpente-couverture",
        "source": "Gallica BnF ark:/12148/bpt6k9774427q",
        "source_title": "Champly Vol.6 — Couvertures et Toitures"
    },
    {
        "file": "corpus/champly/champly_vol07_menuiserie-parquets.md",
        "corps_etat": "menuiserie",
        "source": "Gallica BnF ark:/12148/bpt6k65806792",
        "source_title": "Champly Vol.7 — Menuiserie et Parquets"
    },
    {
        "file": "corpus/champly/champly_vol08_serrurerie-fermetures.md",
        "corps_etat": "menuiserie",
        "source": "Gallica BnF ark:/12148/bpt6k6580680q",
        "source_title": "Champly Vol.8 — Serrurerie et Fermetures"
    },
    {
        "file": "corpus/champly/champly_vol09_pavages-carrelages-peintures.md",
        "corps_etat": "platrerie-peinture",
        "source": "Gallica BnF ark:/12148/bpt6k65806814",
        "source_title": "Champly Vol.9 — Pavages, Carrelages, Peintures"
    },
    {
        "file": "corpus/champly/champly_vol10_vitrerie-chauffage-ventilation.md",
        "corps_etat": "plomberie-chauffage",
        "source": "Gallica BnF ark:/12148/bpt6k6580763j",
        "source_title": "Champly Vol.10 — Vitrerie, Chauffage, Ventilation"
    },
    {
        "file": "corpus/champly/champly_vol11_plomberie-chauffage.md",
        "corps_etat": "plomberie-chauffage",
        "source": "Gallica BnF ark:/12148/bpt6k6580764z",
        "source_title": "Champly Vol.11 — Plomberie et Chauffage"
    },
    {
        "file": "corpus/champly/champly_vol12_plomberie-eau-assainissement.md",
        "corps_etat": "plomberie-chauffage",
        "source": "Gallica BnF ark:/12148/bpt6k65807655",
        "source_title": "Champly Vol.12 — Plomberie, Eau, Assainissement"
    },
    {
        "file": "corpus/champly/champly_vol13_salubrite-sonneries.md",
        "corps_etat": "electricite",
        "source": "Gallica BnF ark:/12148/bpt6k6580766r",
        "source_title": "Champly Vol.13 — Salubrité, Sonneries, Téléphonie"
    },
    {
        "file": "corpus/champly/champly_vol14_escaliers-ascenseurs.md",
        "corps_etat": "menuiserie",
        "source": "Gallica BnF ark:/12148/bpt6k6580767z",
        "source_title": "Champly Vol.14 — Escaliers et Ascenseurs"
    },
    {
        "file": "corpus/champly/champly_vol15_architecture-plans.md",
        "corps_etat": "encyclopedie-generale",
        "source": "Gallica BnF ark:/12148/bpt6k6580768d",
        "source_title": "Champly Vol.15 — Architecture et Plans"
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
            r = requests.post("https://openrouter.ai/api/v1/embeddings", headers=headers, json=payload, timeout=25)
            r.raise_for_status()
            return r.json()["data"][0]["embedding"]
        except Exception as e:
            print(f"    Erreur embedding (tentative {attempt+1}/3): {e}")
            time.sleep(3)
    raise Exception("Échec embedding après 3 tentatives")


def delete_chunks_by_source(source: str) -> int:
    """Supprime tous les chunks d'une source donnée."""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    # Compter d'abord
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"source": f"eq.{source}", "select": "id", "limit": 1000}
    )
    if r.status_code != 200:
        return 0
    count = len(r.json())
    if count == 0:
        return 0
    # Supprimer
    r = requests.delete(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers={**headers, "Content-Type": "application/json"},
        params={"source": f"eq.{source}"}
    )
    if r.status_code in (200, 204):
        return count
    return 0


def index_volume(vol: dict, chunker: SemanticChunker, base_dir: str) -> int:
    """Indexe un volume Champly avec le chunker sémantique."""
    filepath = os.path.join(base_dir, vol["file"])
    
    if not os.path.exists(filepath):
        print(f"  [MANQUANT] {vol['file']}")
        return 0
    
    print(f"\n[VOLUME] {os.path.basename(filepath)}")
    print(f"  Corps d'état: {vol['corps_etat']}")
    
    # Supprimer les anciens chunks
    deleted = delete_chunks_by_source(vol["source"])
    if deleted > 0:
        print(f"  {deleted} anciens chunks supprimés")
    
    # Lire le fichier
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chunker sémantiquement
    chunks = chunker.chunk_markdown(content, source_title=vol["source_title"])
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
        if i % 10 == 0 and i > 0:
            print(f"  ... {i}/{len(chunks)} traités")
        
        try:
            emb = get_embedding(chunk.content)
            data = {
                "content": chunk.content,
                "embedding": emb,
                "corps_etat": vol["corps_etat"],
                "source": vol["source"]
            }
            r = requests.post(f"{SUPABASE_URL}/rest/v1/batiment_chunks", headers=headers, json=data, timeout=15)
            r.raise_for_status()
            success_count += 1
        except Exception as e:
            print(f"  Erreur chunk {i+1}: {e}")
    
    print(f"  -> {success_count}/{len(chunks)} chunks indexés")
    return success_count


if __name__ == "__main__":
    print("=== Ré-indexation Champly avec SemanticChunker ===\n")
    
    if not OPENROUTER_API_KEY:
        print("ERREUR: OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    base_dir = "/home/ubuntu/batiment-knowledge-base"
    chunker = SemanticChunker(max_chars=1500, min_chars=150, overlap_chars=200)
    
    total_new = 0
    for vol in CHAMPLY_VOLUMES:
        n = index_volume(vol, chunker, base_dir)
        total_new += n
    
    print(f"\n=== Terminé ! ===")
    print(f"  Total nouveaux chunks Champly (sémantique): {total_new}")
