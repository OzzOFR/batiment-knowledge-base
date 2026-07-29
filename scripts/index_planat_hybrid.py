#!/usr/bin/env python3
"""
Indexation hybride des volumes Planat :
- Génération des embeddings depuis le sandbox (qui a la clé OpenRouter)
- Insertion dans PostgreSQL HOZZO via SSH + psql

Stratégie : générer les chunks + embeddings localement, puis les insérer
directement via SSH en utilisant psql avec des COPY ou INSERT.
"""

import os
import sys
import re
import time
import json
import subprocess
import requests
import logging
import tempfile

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('/tmp/indexation_planat_hybrid.log'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# Configuration
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
EMBEDDING_MODEL = "openai/text-embedding-3-small"
CHUNK_SIZE = 800
BATCH_SIZE = 5

# SSH config pour le VPS
SSH_KEY = os.path.expanduser('~/.ssh/id_ed25519')
SSH_HOST = 'ubuntu@213.32.71.18'
PG_CONTAINER = 'forge-postgres'
PG_USER = 'createk'
PG_DB = 'batiment_knowledge'

# Métadonnées des volumes Planat
PLANAT_VOLUMES = [
    {
        'file': 'corpus/planat/planat_vol01_architecture-generale.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.1",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.1 (Archive.org encyclopediedela11unse)"
    },
    {
        'file': 'corpus/planat/planat_vol02_materiaux-construction.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.2",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.2 (Archive.org encyclopediedela21unse)"
    },
    {
        'file': 'corpus/planat/planat_vol03_gros-oeuvre.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.3",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'gros-oeuvre',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.3 (Archive.org encyclopediedela31unse)"
    },
    {
        'file': 'corpus/planat/planat_vol04_architecture-religieuse.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.4",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.4 (Archive.org encyclopediedela41unse)"
    },
    {
        'file': 'corpus/planat/planat_vol05_architecture-civile.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.5",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.5 (Archive.org encyclopediedela51unse)"
    },
    {
        'file': 'corpus/planat/planat_vol06_construction-moderne.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.6",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.6 (Archive.org encyclopediedela61unse)"
    },
]


def clean_ocr_text(text: str) -> str:
    """Nettoie le texte OCR des artefacts courants."""
    text = re.sub(r'\x0c', '\n\n', text)
    text = re.sub(r'^\s*\d{1,4}\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'(?<!\w)[|}{\\^~`](?!\w)', ' ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def detect_article_sections(text: str, titre_ouvrage: str) -> list:
    """Détecte les articles dans un texte encyclopédique."""
    article_pattern = re.compile(
        r'\n([A-ZÉÈÊËÀÂÙÛÎÏÔŒÆÇ][A-ZÉÈÊËÀÂÙÛÎÏÔŒÆÇ\s\-]{3,50})\s*\n',
        re.MULTILINE
    )
    matches = list(article_pattern.finditer(text))
    
    if len(matches) < 3:
        return chunk_by_paragraphs(text, titre_ouvrage)
    
    log.info(f"  {len(matches)} articles détectés")
    sections = []
    for i, match in enumerate(matches):
        titre_article = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        contenu = text[start:end].strip()
        if len(contenu) > 100:
            sections.append((titre_article, contenu))
    return sections


def chunk_by_paragraphs(text: str, titre_ouvrage: str) -> list:
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
    prefix = f"[{titre_ouvrage}]"
    if titre_section:
        prefix = f"[{titre_ouvrage} — {titre_section}]"
    
    if len(contenu) <= CHUNK_SIZE:
        return [f"{prefix}\n\n{contenu}"]
    
    sentences = re.split(r'(?<=[.!?])\s+', contenu)
    chunks = []
    current = []
    current_size = 0
    
    for sent in sentences:
        if current_size + len(sent) > CHUNK_SIZE and current:
            chunk_text = ' '.join(current)
            chunks.append(f"{prefix}\n\n{chunk_text}")
            overlap = current[-2:] if len(current) >= 2 else current[-1:]
            current = overlap + [sent]
            current_size = sum(len(s) for s in current)
        else:
            current.append(sent)
            current_size += len(sent)
    
    if current:
        chunks.append(f"{prefix}\n\n{' '.join(current)}")
    
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


def insert_via_ssh(chunks_data: list):
    """Insère des chunks dans PostgreSQL via SSH + psql."""
    if not chunks_data:
        return 0
    
    # Construire les requêtes SQL
    sql_lines = []
    for chunk in chunks_data:
        content = chunk['content'].replace("'", "''")
        source = chunk['source'].replace("'", "''")
        auteur = chunk['auteur'].replace("'", "''")
        titre = chunk['titre_ouvrage'].replace("'", "''")
        embedding_str = '[' + ','.join(map(str, chunk['embedding'])) + ']'
        
        sql = (
            f"INSERT INTO batiment_chunks "
            f"(content, embedding, corps_etat, source, auteur, titre_ouvrage, annee_publication, fiabilite) "
            f"VALUES ('{content}', '{embedding_str}'::vector, '{chunk['corps_etat']}', "
            f"'{source}', '{auteur}', '{titre}', {chunk['annee']}, '{chunk['fiabilite']}');"
        )
        sql_lines.append(sql)
    
    # Écrire dans un fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', suffix='.sql', delete=False, encoding='utf-8') as f:
        f.write('\n'.join(sql_lines))
        tmp_path = f.name
    
    try:
        # Copier le fichier SQL sur le VPS
        remote_path = f'/tmp/planat_batch_{int(time.time())}.sql'
        subprocess.run(
            ['scp', '-o', 'StrictHostKeyChecking=no', '-i', SSH_KEY,
             tmp_path, f'{SSH_HOST}:{remote_path}'],
            check=True, capture_output=True
        )
        
        # Exécuter le SQL sur le VPS
        result = subprocess.run(
            ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', SSH_KEY, SSH_HOST,
             f"docker exec -i {PG_CONTAINER} psql -U {PG_USER} -d {PG_DB} < {remote_path} && rm {remote_path}"],
            check=True, capture_output=True, text=True
        )
        
        return len(chunks_data)
    except subprocess.CalledProcessError as e:
        log.error(f"Erreur SSH/psql: {e.stderr}")
        raise
    finally:
        os.unlink(tmp_path)


def check_already_indexed(source: str) -> int:
    """Vérifie si une source est déjà indexée."""
    source_escaped = source.replace("'", "''")
    result = subprocess.run(
        ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', SSH_KEY, SSH_HOST,
         f"docker exec {PG_CONTAINER} psql -U {PG_USER} -d {PG_DB} -t -c "
         f"\"SELECT COUNT(*) FROM batiment_chunks WHERE source = '{source_escaped}';\""],
        capture_output=True, text=True
    )
    try:
        return int(result.stdout.strip())
    except:
        return 0


def delete_source(source: str):
    """Supprime tous les chunks d'une source."""
    source_escaped = source.replace("'", "''")
    subprocess.run(
        ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', SSH_KEY, SSH_HOST,
         f"docker exec {PG_CONTAINER} psql -U {PG_USER} -d {PG_DB} -c "
         f"\"DELETE FROM batiment_chunks WHERE source = '{source_escaped}';\""],
        capture_output=True
    )


def index_volume(vol_info: dict, base_dir: str):
    """Indexe un volume Planat complet."""
    filepath = os.path.join(base_dir, vol_info['file'])
    
    if not os.path.exists(filepath):
        log.warning(f"Fichier non trouvé : {filepath}")
        return 0
    
    log.info(f"\n=== Indexation : {vol_info['titre']} ===")
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        raw_text = f.read()
    
    text = clean_ocr_text(raw_text)
    log.info(f"  Texte nettoyé : {len(text):,} caractères")
    
    sections = detect_article_sections(text, vol_info['titre'])
    log.info(f"  Sections détectées : {len(sections)}")
    
    all_chunks_text = []
    for titre_section, contenu in sections:
        sub_chunks = split_section_into_chunks(titre_section, contenu, vol_info['titre'])
        all_chunks_text.extend(sub_chunks)
    
    log.info(f"  Chunks à indexer : {len(all_chunks_text)}")
    
    # Vérifier si déjà indexé
    existing = check_already_indexed(vol_info['source'])
    if existing > 0:
        log.info(f"  Déjà indexé ({existing} chunks) — suppression et ré-indexation")
        delete_source(vol_info['source'])
    
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
                inserted = insert_via_ssh(batch)
                total_indexed += inserted
                log.info(f"  Progression : {total_indexed}/{len(all_chunks_text)} chunks")
                batch = []
                time.sleep(0.1)
                
        except Exception as e:
            log.error(f"  Erreur chunk {i}: {e}")
            time.sleep(2)
            continue
    
    # Insérer le dernier batch
    if batch:
        inserted = insert_via_ssh(batch)
        total_indexed += inserted
    
    log.info(f"  ✓ {total_indexed} chunks indexés pour {vol_info['titre']}")
    return total_indexed


def main():
    base_dir = '/home/ubuntu/batiment-knowledge-base'
    
    if not OPENROUTER_API_KEY:
        log.error("OPENROUTER_API_KEY non définie")
        sys.exit(1)
    
    log.info(f"Clé OpenRouter disponible ({len(OPENROUTER_API_KEY)} chars)")
    
    # Test de connexion SSH
    result = subprocess.run(
        ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', SSH_KEY, SSH_HOST,
         f"docker exec {PG_CONTAINER} psql -U {PG_USER} -d {PG_DB} -t -c 'SELECT COUNT(*) FROM batiment_chunks;'"],
        capture_output=True, text=True
    )
    count = result.stdout.strip()
    log.info(f"Connexion SSH OK — {count} chunks dans la base")
    
    total = 0
    for vol_info in PLANAT_VOLUMES:
        try:
            n = index_volume(vol_info, base_dir)
            total += n
        except Exception as e:
            log.error(f"Erreur sur {vol_info['titre']}: {e}")
            import traceback
            traceback.print_exc()
    
    log.info(f"\n=== TERMINÉ : {total} chunks Planat indexés au total ===")


if __name__ == '__main__':
    main()
