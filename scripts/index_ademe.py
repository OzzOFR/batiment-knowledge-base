import os
import sys
import time
import requests

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

def chunk_text(text: str, max_chars: int = 1500) -> list:
    """Découpe un texte en chunks sémantiques."""
    # Nettoyer le texte
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    cleaned = '\n'.join(lines)
    
    # Séparer par doubles sauts de ligne ou par sections
    paragraphs = cleaned.split('\n\n')
    if len(paragraphs) < 5:
        paragraphs = cleaned.split('\n')
    
    chunks = []
    current_chunk = ""
    
    for p in paragraphs:
        p = p.strip()
        if not p or len(p) < 20:
            continue
        
        if len(current_chunk) + len(p) < max_chars:
            current_chunk += p + "\n\n"
        else:
            if current_chunk.strip() and len(current_chunk.strip()) > 100:
                chunks.append(current_chunk.strip())
            current_chunk = p + "\n\n"
    
    if current_chunk.strip() and len(current_chunk.strip()) > 100:
        chunks.append(current_chunk.strip())
    
    return chunks

def get_embedding(text: str) -> list:
    """Obtient l'embedding via OpenRouter."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": text[:8000]  # Limiter à 8000 chars
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
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
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
        if i % 10 == 0 and i > 0:
            print(f"  ... {i}/{len(chunks)} traités")
        
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
    print("=== Indexation des guides ADEME dans Supabase ===")
    
    base_dir = "/home/ubuntu/batiment-knowledge-base/corpus/ademe"
    
    files_to_index = [
        ("guide_isolation_maison.txt", "isolation-etancheite", "Guide ADEME - Isoler sa maison (Ministère Transition Écologique, 2020)"),
        ("guide_materiaux_isolants.txt", "isolation-etancheite", "Guide des matériaux isolants (ADEME/AGEDEN, 2020)"),
        ("fiche_energies_renouvelables.txt", "normes-reglements", "Fiches ADEME - Énergies renouvelables (Ministère Transition Énergétique, 2023)"),
        ("fiche_isolation_renovation.txt", "normes-reglements", "Fiche réglementation isolation en rénovation (Ministère Transition Écologique)"),
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
