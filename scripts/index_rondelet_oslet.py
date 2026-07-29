"""
Script d'indexation des corpus Rondelet et Oslet dans Supabase.
Ces textes sont des OCR DjVu, donc on utilise le chunker plain_text.
"""

import os
import sys
import time
import requests
import re

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

# Fichiers à indexer
CORPUS = [
    {
        "file": "corpus/rondelet/traitthoriqueet01rondgoog.txt",
        "corps_etat": "gros-oeuvre",
        "source": "Traité théorique et pratique de l'art de bâtir - Vol.1 (Rondelet, 1834)",
        "source_title": "Rondelet — Art de bâtir Vol.1",
        "max_chars": 200000  # Limiter pour les gros volumes
    },
    {
        "file": "corpus/rondelet/traitetheoriquee02rond.txt",
        "corps_etat": "maconnerie",
        "source": "Traité théorique et pratique de l'art de bâtir - Vol.2 (Rondelet, 1834)",
        "source_title": "Rondelet — Art de bâtir Vol.2",
        "max_chars": 200000
    },
    {
        "file": "corpus/rondelet/traitetheoriquee03rond.txt",
        "corps_etat": "maconnerie",
        "source": "Traité théorique et pratique de l'art de bâtir - Vol.3 (Rondelet, 1834)",
        "source_title": "Rondelet — Art de bâtir Vol.3",
        "max_chars": 200000
    },
    {
        "file": "corpus/rondelet/traitetheoriquee04rond.txt",
        "corps_etat": "charpente-couverture",
        "source": "Traité théorique et pratique de l'art de bâtir - Vol.4 (Rondelet, 1834)",
        "source_title": "Rondelet — Art de bâtir Vol.4",
        "max_chars": 200000
    },
    {
        "file": "corpus/rondelet/traitetheoriquee05rond.txt",
        "corps_etat": "gros-oeuvre",
        "source": "Traité théorique et pratique de l'art de bâtir - Vol.5 (Rondelet, 1834)",
        "source_title": "Rondelet — Art de bâtir Vol.5",
        "max_chars": 200000
    },
    {
        "file": "corpus/oslet/oslet_charpente_bois.txt",
        "corps_etat": "charpente-couverture",
        "source": "Traité de charpente en bois (Oslet, Gustave)",
        "source_title": "Oslet — Charpente en bois",
        "max_chars": 300000
    },
]


def clean_ocr_text(text: str) -> str:
    """Nettoie le texte OCR DjVu."""
    # Supprimer les sauts de page DjVu
    text = text.replace('\x0c', '\n\n')
    # Supprimer les lignes très courtes (artefacts OCR)
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        # Garder les lignes de plus de 3 caractères ou les lignes vides
        if len(stripped) > 3 or stripped == '':
            cleaned_lines.append(line)
    text = '\n'.join(cleaned_lines)
    # Normaliser les espaces multiples
    text = re.sub(r'[ \t]{2,}', ' ', text)
    # Normaliser les sauts de ligne multiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def chunk_text(text: str, max_chars: int = 1500, overlap: int = 200) -> list:
    """Découpe le texte en chunks avec chevauchement."""
    paragraphs = re.split(r'\n{2,}', text)
    paragraphs = [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 30]
    
    chunks = []
    current = ""
    
    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_chars:
            current = (current + "\n\n" + para).strip()
        else:
            if current and len(current) >= 100:
                chunks.append(current)
                # Overlap
                tail = current[-overlap:]
                dot = tail.find('. ')
                if dot != -1:
                    tail = tail[dot+2:]
                current = (tail + "\n\n" + para).strip() if tail else para
            else:
                current = (current + "\n\n" + para).strip() if current else para
    
    if current and len(current) >= 100:
        chunks.append(current)
    
    return chunks


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


def check_already_indexed(source: str) -> bool:
    """Vérifie si une source est déjà indexée."""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers=headers,
        params={"source": f"eq.{source}", "select": "id", "limit": 1}
    )
    if r.status_code == 200:
        return len(r.json()) > 0
    return False


def index_corpus(item: dict, base_dir: str) -> int:
    """Indexe un corpus dans Supabase."""
    filepath = os.path.join(base_dir, item["file"])
    
    if not os.path.exists(filepath):
        print(f"  [MANQUANT] {item['file']}")
        return 0
    
    print(f"\n[INDEXATION] {os.path.basename(filepath)}")
    print(f"  Corps d'état: {item['corps_etat']}")
    print(f"  Source: {item['source']}")
    
    # Vérifier si déjà indexé
    if check_already_indexed(item["source"]):
        print(f"  -> Déjà indexé, on passe")
        return 0
    
    # Lire et nettoyer le texte
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Limiter la taille si nécessaire
    max_chars = item.get("max_chars", 300000)
    if len(text) > max_chars:
        print(f"  -> Texte tronqué à {max_chars} chars (original: {len(text)} chars)")
        text = text[:max_chars]
    
    # Nettoyer l'OCR
    text = clean_ocr_text(text)
    
    # Préfixer avec le titre source
    source_title = item.get("source_title", "")
    
    # Chunker
    chunks = chunk_text(text, max_chars=1500, overlap=200)
    
    # Ajouter le préfixe de source à chaque chunk
    if source_title:
        chunks = [f"[{source_title}]\n\n{c}" for c in chunks]
    
    print(f"  -> {len(chunks)} chunks à indexer")
    
    # Indexer dans Supabase
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    success_count = 0
    for i, chunk in enumerate(chunks):
        if i % 20 == 0 and i > 0:
            print(f"  ... {i}/{len(chunks)} traités")
        
        try:
            emb = get_embedding(chunk)
            data = {
                "content": chunk,
                "embedding": emb,
                "corps_etat": item["corps_etat"],
                "source": item["source"]
            }
            r = requests.post(f"{SUPABASE_URL}/rest/v1/batiment_chunks", headers=headers, json=data, timeout=15)
            r.raise_for_status()
            success_count += 1
        except Exception as e:
            print(f"  Erreur chunk {i+1}: {e}")
    
    print(f"  -> {success_count}/{len(chunks)} chunks indexés")
    return success_count


if __name__ == "__main__":
    print("=== Indexation Rondelet + Oslet dans Supabase ===\n")
    
    if not OPENROUTER_API_KEY:
        print("ERREUR: OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    base_dir = "/home/ubuntu/batiment-knowledge-base"
    total = 0
    
    for item in CORPUS:
        n = index_corpus(item, base_dir)
        total += n
    
    print(f"\n=== Terminé ! Total: {total} nouveaux chunks ===")
