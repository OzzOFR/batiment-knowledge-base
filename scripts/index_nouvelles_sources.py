import os
import sys
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Charger les variables d'environnement
load_dotenv()

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

def chunk_text(text: str, max_chars: int = 1500) -> list[str]:
    """Découpe un texte en chunks par paragraphes."""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for p in paragraphs:
        if len(current_chunk) + len(p) < max_chars:
            current_chunk += p + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = p + "\n\n"
            
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
        
    return chunks

def get_embedding(text: str) -> list[float]:
    """Obtient l'embedding via OpenRouter."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": text
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

def index_file(filepath: str, corps_etat: str, source: str):
    """Indexe un fichier dans Supabase."""
    print(f"\n[INDEXATION] {os.path.basename(filepath)}")
    print(f"  Corps d'état: {corps_etat}")
    print(f"  Source: {source}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    chunks = chunk_text(content)
    print(f"  -> {len(chunks)} chunks à indexer")
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    success_count = 0
    for i, chunk in enumerate(chunks):
        try:
            emb = get_embedding(chunk)
            
            data = {
                "content": chunk,
                "embedding": emb,
                "corps_etat": corps_etat,
                "source": source
            }
            
            r = requests.post(f"{SUPABASE_URL}/rest/v1/batiment_chunks", headers=headers, json=data, timeout=15)
            r.raise_for_status()
            success_count += 1
            
        except Exception as e:
            print(f"  Erreur sur le chunk {i+1}: {e}")
            
    print(f"  -> {success_count}/{len(chunks)} chunks indexés avec succès")
    return success_count

if __name__ == "__main__":
    print("=== Indexation des nouvelles sources dans Supabase ===")
    
    base_dir = "/home/ubuntu/batiment-knowledge-base/corpus/nouvelles_sources"
    
    files_to_index = [
        ("fiche_electricite_installations.md", "electricite", "Synthèse technique / Manuel de l'électricien"),
        ("fiche_plomberie_chauffage.md", "plomberie-chauffage", "Synthèse technique / Traité de plomberie"),
        ("fiche_isolation_thermique.md", "isolation-etancheite", "Synthèse technique / Ministère de la Culture"),
        ("fiche_maconnerie_precheur.md", "maconnerie", "Synthèse technique / Manuel du Maçon / Rondelet")
    ]
    
    total_chunks = 0
    for filename, corps_etat, source in files_to_index:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            chunks_indexed = index_file(filepath, corps_etat, source)
            total_chunks += chunks_indexed
        else:
            print(f"Fichier non trouvé: {filepath}")
            
    print(f"\n=== Terminé ! ===")
    print(f"  Nouveaux chunks indexés: {total_chunks}")
