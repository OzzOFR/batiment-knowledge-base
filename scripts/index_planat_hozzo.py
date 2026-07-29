#!/usr/bin/env python3
"""
Indexation des 6 volumes de l'Encyclopédie de l'architecture et de la construction
de P. Planat (1888) dans PostgreSQL HOZZO via tunnel SSH.

Utilise le SemanticChunker pour un découpage par sections.
"""

import os
import sys
import re
import time
import psycopg2
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('/tmp/indexation_planat.log'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# Configuration
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
EMBEDDING_MODEL = "openai/text-embedding-3-small"
EMBEDDING_DIM = 1536
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
BATCH_SIZE = 5

# Connexion PostgreSQL via tunnel SSH (port 15432)
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 15432,
    'dbname': 'batiment_knowledge',
    'user': 'createk',
    'password': 'Forge2026Hozzo!',
    'connect_timeout': 10
}

# Métadonnées des volumes Planat
PLANAT_VOLUMES = [
    {
        'file': 'corpus/planat/planat_vol01_architecture-generale.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.1',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.1 (Archive.org encyclopediedela11unse)'
    },
    {
        'file': 'corpus/planat/planat_vol02_materiaux-construction.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.2',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.2 (Archive.org encyclopediedela21unse)'
    },
    {
        'file': 'corpus/planat/planat_vol03_gros-oeuvre.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.3',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'gros-oeuvre',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.3 (Archive.org encyclopediedela31unse)'
    },
    {
        'file': 'corpus/planat/planat_vol04_architecture-religieuse.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.4',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.4 (Archive.org encyclopediedela41unse)'
    },
    {
        'file': 'corpus/planat/planat_vol05_architecture-civile.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.5',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.5 (Archive.org encyclopediedela51unse)'
    },
    {
        'file': 'corpus/planat/planat_vol06_construction-moderne.txt',
        'titre': 'Encyclopédie de l\'architecture et de la construction — Vol.6',
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': 'Planat — Encyclopédie architecture Vol.6 (Archive.org encyclopediedela61unse)'
    },
]


def clean_ocr_text(text: str) -> str:
    """Nettoie le texte OCR des artefacts courants."""
    # Supprimer les lignes de séparation DjVu
    text = re.sub(r'\x0c', '\n\n', text)  # form feed -> double newline
    # Supprimer les numéros de page isolés
    text = re.sub(r'^\s*\d{1,4}\s*$', '', text, flags=re.MULTILINE)
    # Réparer les césures de mots (mot- \n suite)
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    # Supprimer les lignes vides multiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Supprimer les caractères parasites isolés
    text = re.sub(r'(?<!\w)[|}{\\^~`](?!\w)', ' ', text)
    # Normaliser les espaces
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def detect_article_sections(text: str, titre_ouvrage: str) -> list:
    """
    Détecte les articles dans un texte encyclopédique.
    Les encyclopédies du XIXe siècle ont des articles en MAJUSCULES.
    Retourne une liste de (titre_section, contenu).
    """
    sections = []
    
    # Pattern pour les titres d'articles en majuscules (au moins 4 chars)
    article_pattern = re.compile(
        r'\n([A-ZÉÈÊËÀÂÙÛÎÏÔŒÆÇ][A-ZÉÈÊËÀÂÙÛÎÏÔŒÆÇ\s\-]{3,50})\s*\n',
        re.MULTILINE
    )
    
    matches = list(article_pattern.finditer(text))
    
    if len(matches) < 3:
        # Pas assez d'articles détectés — chunking par paragraphes
        return chunk_by_paragraphs(text, titre_ouvrage)
    
    log.info(f"  {len(matches)} articles détectés dans {titre_ouvrage}")
    
    for i, match in enumerate(matches):
        titre_article = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        contenu = text[start:end].strip()
        
        if len(contenu) > 100:  # Ignorer les articles trop courts
            sections.append((titre_article, contenu))
    
    return sections


def chunk_by_paragraphs(text: str, titre_ouvrage: str) -> list:
    """Découpe le texte en chunks par paragraphes."""
    paragraphs = re.split(r'\n\n+', text)
    sections = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 50:
            continue
        
        if current_size + len(para) > CHUNK_SIZE and current_chunk:
            sections.append(('', '\n\n'.join(current_chunk)))
            current_chunk = [para]
            current_size = len(para)
        else:
            current_chunk.append(para)
            current_size += len(para)
    
    if current_chunk:
        sections.append(('', '\n\n'.join(current_chunk)))
    
    return sections


def split_section_into_chunks(titre_section: str, contenu: str, titre_ouvrage: str) -> list:
    """Découpe une section en chunks de taille CHUNK_SIZE avec overlap."""
    prefix = f"[{titre_ouvrage}]"
    if titre_section:
        prefix = f"[{titre_ouvrage} — {titre_section}]"
    
    if len(contenu) <= CHUNK_SIZE:
        return [f"{prefix}\n\n{contenu}"]
    
    # Découper par phrases
    sentences = re.split(r'(?<=[.!?])\s+', contenu)
    chunks = []
    current = []
    current_size = 0
    
    for sent in sentences:
        if current_size + len(sent) > CHUNK_SIZE and current:
            chunk_text = ' '.join(current)
            chunks.append(f"{prefix}\n\n{chunk_text}")
            # Overlap : garder les 2 dernières phrases
            overlap = current[-2:] if len(current) >= 2 else current[-1:]
            current = overlap + [sent]
            current_size = sum(len(s) for s in current)
        else:
            current.append(sent)
            current_size += len(sent)
    
    if current:
        chunk_text = ' '.join(current)
        chunks.append(f"{prefix}\n\n{chunk_text}")
    
    return chunks


def get_embedding(text: str) -> list:
    """Obtient l'embedding d'un texte via OpenRouter."""
    response = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": EMBEDDING_MODEL,
            "input": text[:8000]
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()['data'][0]['embedding']


def insert_chunks(conn, chunks_data: list):
    """Insère des chunks dans PostgreSQL."""
    with conn.cursor() as cur:
        for chunk in chunks_data:
            cur.execute("""
                INSERT INTO batiment_chunks 
                    (content, embedding, corps_etat, source, auteur, titre_ouvrage, annee_publication, fiabilite)
                VALUES (%s, %s::vector, %s, %s, %s, %s, %s, %s)
            """, (
                chunk['content'],
                '[' + ','.join(map(str, chunk['embedding'])) + ']',
                chunk['corps_etat'],
                chunk['source'],
                chunk['auteur'],
                chunk['titre_ouvrage'],
                chunk['annee'],
                chunk['fiabilite']
            ))
    conn.commit()


def index_volume(conn, vol_info: dict, base_dir: str):
    """Indexe un volume Planat complet."""
    filepath = os.path.join(base_dir, vol_info['file'])
    
    if not os.path.exists(filepath):
        log.warning(f"Fichier non trouvé : {filepath}")
        return 0
    
    log.info(f"\n=== Indexation : {vol_info['titre']} ===")
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        raw_text = f.read()
    
    # Nettoyage OCR
    text = clean_ocr_text(raw_text)
    log.info(f"  Texte nettoyé : {len(text):,} caractères")
    
    # Détection des sections/articles
    sections = detect_article_sections(text, vol_info['titre'])
    log.info(f"  Sections détectées : {len(sections)}")
    
    # Génération des chunks
    all_chunks_text = []
    for titre_section, contenu in sections:
        sub_chunks = split_section_into_chunks(titre_section, contenu, vol_info['titre'])
        all_chunks_text.extend(sub_chunks)
    
    log.info(f"  Chunks à indexer : {len(all_chunks_text)}")
    
    # Vérifier si déjà indexé
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE source = %s", (vol_info['source'],))
        existing = cur.fetchone()[0]
    
    if existing > 0:
        log.info(f"  Déjà indexé ({existing} chunks) — suppression et ré-indexation")
        with conn.cursor() as cur:
            cur.execute("DELETE FROM batiment_chunks WHERE source = %s", (vol_info['source'],))
        conn.commit()
    
    # Indexation par batches
    batch = []
    total_indexed = 0
    
    for i, chunk_text in enumerate(all_chunks_text):
        if len(chunk_text.strip()) < 100:
            continue
        
        try:
            embedding = get_embedding(chunk_text)
            batch.append({
                'content': chunk_text,
                'embedding': embedding,
                'corps_etat': vol_info['corps_etat'],
                'source': vol_info['source'],
                'auteur': vol_info['auteur'],
                'titre_ouvrage': vol_info['titre'],
                'annee': vol_info['annee'],
                'fiabilite': vol_info['fiabilite']
            })
            
            if len(batch) >= BATCH_SIZE:
                insert_chunks(conn, batch)
                total_indexed += len(batch)
                log.info(f"  Progression : {total_indexed}/{len(all_chunks_text)} chunks")
                batch = []
                time.sleep(0.2)  # Rate limiting
                
        except Exception as e:
            log.error(f"  Erreur chunk {i}: {e}")
            time.sleep(2)
            continue
    
    # Insérer le dernier batch
    if batch:
        insert_chunks(conn, batch)
        total_indexed += len(batch)
    
    log.info(f"  ✓ {total_indexed} chunks indexés pour {vol_info['titre']}")
    return total_indexed


def main():
    base_dir = '/home/ubuntu/batiment-knowledge-base'
    
    log.info("Connexion à PostgreSQL HOZZO...")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        log.info("✓ Connexion établie")
    except Exception as e:
        log.error(f"Erreur de connexion : {e}")
        sys.exit(1)
    
    total = 0
    for vol_info in PLANAT_VOLUMES:
        try:
            n = index_volume(conn, vol_info, base_dir)
            total += n
        except Exception as e:
            log.error(f"Erreur sur {vol_info['titre']}: {e}")
            import traceback
            traceback.print_exc()
    
    conn.close()
    log.info(f"\n=== TERMINÉ : {total} chunks Planat indexés au total ===")


if __name__ == '__main__':
    main()
