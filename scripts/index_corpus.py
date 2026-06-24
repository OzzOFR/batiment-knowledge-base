"""
Pipeline d'indexation de la base de connaissances bâtiment.
Lit les fichiers Markdown du corpus, les découpe en chunks,
génère les embeddings OpenAI et les insère dans Supabase (pgvector).
"""

import os
import json
import time
import re
import requests
from pathlib import Path
from typing import Generator

# ─── Configuration ────────────────────────────────────────────────────────────
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
EMBEDDING_MODEL = "gte-small"  # Modèle natif Supabase via Edge Function
EMBEDDING_DIM = 384
SUPABASE_EMBED_URL = f"{SUPABASE_URL}/functions/v1/generate-embeddings"

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
CHUNK_SIZE = 800       # Nombre de tokens approximatif par chunk
CHUNK_OVERLAP = 100    # Chevauchement entre chunks

# ─── Découpage en chunks ──────────────────────────────────────────────────────

def split_text_into_chunks(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Découpe un texte en chunks de taille approximative avec chevauchement."""
    # Découper d'abord par paragraphes (double saut de ligne)
    paragraphs = re.split(r'\n{2,}', text)
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 20:
            continue
        
        # Estimation grossière : 1 token ≈ 4 caractères
        para_tokens = len(para) // 4
        
        if current_size + para_tokens > chunk_size and current_chunk:
            # Sauvegarder le chunk courant
            chunks.append('\n\n'.join(current_chunk))
            # Garder les derniers paragraphes pour le chevauchement
            overlap_tokens = 0
            overlap_paras = []
            for p in reversed(current_chunk):
                overlap_tokens += len(p) // 4
                if overlap_tokens > overlap:
                    break
                overlap_paras.insert(0, p)
            current_chunk = overlap_paras
            current_size = sum(len(p) // 4 for p in current_chunk)
        
        current_chunk.append(para)
        current_size += para_tokens
    
    # Dernier chunk
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks


def extract_metadata_from_md(content: str) -> dict:
    """Extrait les métadonnées du front-matter YAML d'un fichier Markdown."""
    meta = {}
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            yaml_block = content[3:end].strip()
            for line in yaml_block.split('\n'):
                if ':' in line:
                    key, _, val = line.partition(':')
                    meta[key.strip()] = val.strip()
    return meta


def clean_markdown_for_indexing(content: str) -> str:
    """Nettoie le Markdown pour l'indexation (supprime front-matter, balises)."""
    # Supprimer le front-matter YAML
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            content = content[end+3:].strip()
    # Supprimer les titres Markdown (#)
    content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)
    # Supprimer les balises Markdown de formatage
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
    content = re.sub(r'\*(.+?)\*', r'\1', content)
    # Normaliser les espaces
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


# ─── Embeddings OpenAI ────────────────────────────────────────────────────────

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Génère les embeddings via la Edge Function Supabase (modèle gte-small)."""
    headers = {
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"input": texts}
    
    r = requests.post(SUPABASE_EMBED_URL, headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    return data["embeddings"]


# ─── Insertion dans Supabase ──────────────────────────────────────────────────

def insert_chunks_to_supabase(chunks_data: list[dict]) -> bool:
    """Insère des chunks avec leurs embeddings dans Supabase via l'API REST."""
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    r = requests.post(url, headers=headers, json=chunks_data, timeout=30)
    if r.status_code in (200, 201):
        return True
    else:
        print(f"  [ERREUR Supabase] {r.status_code}: {r.text[:200]}")
        return False


# ─── Pipeline principal ───────────────────────────────────────────────────────

def process_markdown_file(md_path: Path) -> list[dict]:
    """Traite un fichier Markdown : extrait, découpe, prépare les chunks."""
    content = md_path.read_text(encoding='utf-8')
    meta = extract_metadata_from_md(content)
    clean_content = clean_markdown_for_indexing(content)
    
    chunks_text = split_text_into_chunks(clean_content)
    
    chunks_data = []
    for i, chunk_text in enumerate(chunks_text):
        if len(chunk_text.strip()) < 50:
            continue
        chunks_data.append({
            "content": chunk_text,
            "corps_etat": meta.get("corps_etat", md_path.parent.name),
            "source": meta.get("source", "Archive.org / Gallica BnF"),
            "titre_document": meta.get("titre", md_path.stem),
            "auteur": meta.get("auteur", "Inconnu"),
            "date_document": meta.get("date", "N/A"),
            "type_contenu": "technique",
            "libre_droits": True,
            "url_source": None,
            "chunk_index": i,
            "total_chunks": len(chunks_text),
        })
    
    return chunks_data


def index_all_corpus(batch_size: int = 20):
    """Pipeline complet : lit le corpus, génère les embeddings, indexe dans Supabase."""
    print("=" * 65)
    print("Pipeline d'indexation — Base de connaissances Bâtiment")
    print("=" * 65)
    
    # Collecter tous les fichiers Markdown du corpus
    md_files = list(CORPUS_DIR.rglob("*.md"))
    print(f"\nFichiers trouvés : {len(md_files)}")
    
    all_chunks = []
    for md_path in md_files:
        print(f"\n  Traitement : {md_path.relative_to(CORPUS_DIR)}")
        chunks = process_markdown_file(md_path)
        print(f"  → {len(chunks)} chunks générés")
        all_chunks.extend(chunks)
    
    print(f"\nTotal chunks à indexer : {len(all_chunks)}")
    
    # Traitement par lots
    total_indexed = 0
    for batch_start in range(0, len(all_chunks), batch_size):
        batch = all_chunks[batch_start:batch_start + batch_size]
        batch_texts = [c["content"] for c in batch]
        
        print(f"\n  Lot {batch_start//batch_size + 1}/{(len(all_chunks)-1)//batch_size + 1} "
              f"({len(batch)} chunks) — génération embeddings...")
        
        try:
            embeddings = get_embeddings(batch_texts)
        except Exception as e:
            print(f"  [ERREUR embedding] {e}")
            time.sleep(5)
            continue
        
        # Ajouter les embeddings aux chunks
        for chunk, embedding in zip(batch, embeddings):
            chunk["embedding"] = embedding
        
        # Insérer dans Supabase
        print(f"  Insertion dans Supabase...")
        success = insert_chunks_to_supabase(batch)
        if success:
            total_indexed += len(batch)
            print(f"  [OK] {total_indexed}/{len(all_chunks)} chunks indexés")
        
        time.sleep(0.5)  # Rate limit
    
    print(f"\n{'=' * 65}")
    print(f"Indexation terminée : {total_indexed}/{len(all_chunks)} chunks dans Supabase")
    print(f"URL Supabase : {SUPABASE_URL}")
    print(f"Table : batiment_chunks")


if __name__ == "__main__":
    index_all_corpus()
