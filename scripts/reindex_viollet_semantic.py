"""
Script de ré-indexation des volumes Viollet-le-Duc avec le SemanticChunker.

Les fichiers Viollet sont des OCR DjVu (texte brut), donc on utilise
un chunker adapté aux textes sans structure Markdown.
"""

import os
import sys
import time
import requests
import re

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

VIOLLET_VOLUMES = [
    {
        "file": "corpus/encyclopedie-generale/viollet/dictionnairerai01viol.txt",
        "source": "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 1)",
        "source_title": "Viollet-le-Duc — Dict. raisonné Vol.1",
        "corps_etat": "encyclopedie-generale",
        "max_chars": 250000
    },
    {
        "file": "corpus/encyclopedie-generale/viollet/dictionnairerais05viol.txt",
        "source": "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 5)",
        "source_title": "Viollet-le-Duc — Dict. raisonné Vol.5",
        "corps_etat": "encyclopedie-generale",
        "max_chars": 250000
    },
    {
        "file": "corpus/encyclopedie-generale/viollet/dictionnairerais07violuoft.txt",
        "source": "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 7)",
        "source_title": "Viollet-le-Duc — Dict. raisonné Vol.7",
        "corps_etat": "encyclopedie-generale",
        "max_chars": 250000
    },
    {
        "file": "corpus/encyclopedie-generale/viollet/dictionnairerais08viol_0.txt",
        "source": "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 8)",
        "source_title": "Viollet-le-Duc — Dict. raisonné Vol.8",
        "corps_etat": "encyclopedie-generale",
        "max_chars": 250000
    },
    {
        "file": "corpus/encyclopedie-generale/viollet/dictionnaireraison09viol.txt",
        "source": "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 9)",
        "source_title": "Viollet-le-Duc — Dict. raisonné Vol.9",
        "corps_etat": "encyclopedie-generale",
        "max_chars": 250000
    },
]


def clean_ocr_text(text: str) -> str:
    """Nettoie le texte OCR DjVu."""
    text = text.replace('\x0c', '\n\n')
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) > 3 or stripped == '':
            cleaned.append(line)
    text = '\n'.join(cleaned)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def detect_article_boundaries(text: str) -> list:
    """
    Détecte les entrées du dictionnaire (articles en majuscules).
    Ex: "ABSIDE", "ARCADE", "ARC-BOUTANT", etc.
    Retourne une liste de (titre, contenu).
    """
    # Pattern : ligne avec un mot en majuscules (entrée de dictionnaire)
    pattern = re.compile(r'\n([A-ZÀÂÉÈÊËÎÏÔÙÛÜÇ][A-ZÀÂÉÈÊËÎÏÔÙÛÜÇ\s\-]{2,})\n', re.MULTILINE)
    
    matches = list(pattern.finditer(text))
    
    if len(matches) < 5:
        # Pas assez d'entrées détectées - retourner le texte entier en chunks
        return [("", text)]
    
    articles = []
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        content = text[start:end].strip()
        if len(content) > 100:
            articles.append((title, content))
    
    return articles


def chunk_article(title: str, content: str, source_title: str, max_chars: int = 1500) -> list:
    """Découpe un article en chunks avec préfixe de titre."""
    prefix = f"[{source_title}]"
    if title:
        prefix = f"[{source_title} — {title}]"
    
    if len(content) <= max_chars:
        return [f"{prefix}\n\n{content}"]
    
    # Découper par paragraphes
    paragraphs = re.split(r'\n{2,}', content)
    chunks = []
    current = prefix
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 2 <= max_chars:
            current = current + "\n\n" + para
        else:
            if len(current) > len(prefix) + 10:
                chunks.append(current.strip())
            current = f"{prefix}\n\n{para}"
    
    if len(current) > len(prefix) + 10:
        chunks.append(current.strip())
    
    return chunks


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


def index_volume(vol: dict, base_dir: str) -> int:
    filepath = os.path.join(base_dir, vol["file"])
    if not os.path.exists(filepath):
        print(f"  [MANQUANT] {vol['file']}")
        return 0
    
    print(f"\n[VOLUME] {os.path.basename(filepath)}")
    
    # Supprimer les anciens chunks
    deleted = delete_chunks_by_source(vol["source"])
    if deleted > 0:
        print(f"  {deleted} anciens chunks supprimés")
    
    # Lire et nettoyer
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    max_chars = vol.get("max_chars", 250000)
    if len(text) > max_chars:
        print(f"  Texte tronqué à {max_chars} chars (original: {len(text)} chars)")
        text = text[:max_chars]
    
    text = clean_ocr_text(text)
    
    # Détecter les articles du dictionnaire
    articles = detect_article_boundaries(text)
    print(f"  {len(articles)} articles détectés")
    
    # Créer les chunks
    all_chunks = []
    for title, content in articles:
        chunks = chunk_article(title, content, vol["source_title"], max_chars=1500)
        all_chunks.extend(chunks)
    
    print(f"  -> {len(all_chunks)} chunks à indexer")
    
    # Indexer dans Supabase
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    success = 0
    for i, chunk in enumerate(all_chunks):
        if i % 20 == 0 and i > 0:
            print(f"  ... {i}/{len(all_chunks)} traités")
        try:
            emb = get_embedding(chunk)
            data = {
                "content": chunk,
                "embedding": emb,
                "corps_etat": vol["corps_etat"],
                "source": vol["source"]
            }
            r = requests.post(f"{SUPABASE_URL}/rest/v1/batiment_chunks", headers=headers, json=data, timeout=15)
            r.raise_for_status()
            success += 1
        except Exception as e:
            print(f"  Erreur chunk {i+1}: {e}")
    
    print(f"  -> {success}/{len(all_chunks)} chunks indexés")
    return success


if __name__ == "__main__":
    print("=== Ré-indexation Viollet-le-Duc avec détection d'articles ===\n")
    
    if not OPENROUTER_API_KEY:
        print("ERREUR: OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    base_dir = "/home/ubuntu/batiment-knowledge-base"
    total = 0
    
    for vol in VIOLLET_VOLUMES:
        n = index_volume(vol, base_dir)
        total += n
    
    print(f"\n=== Terminé ! Total: {total} nouveaux chunks Viollet-le-Duc ===")
