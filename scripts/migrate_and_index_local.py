#!/usr/bin/env python3
"""
Migration complète de la base batiment_knowledge vers le modèle d'embedding local.
- Migre la colonne embedding de vector(1536) vers vector(768)
- Réindexe les chunks existants avec paraphrase-multilingual-mpnet-base-v2
- Indexe les 6 volumes Planat (nouveaux)

Ce script tourne directement sur le VPS HOZZO.
"""
import os
import sys
import re
import time
import json
import psycopg2
import logging
from pathlib import Path

# Configuration logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('/tmp/migration_indexation.log'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# Configuration PostgreSQL (connexion directe au container)
PG_HOST = '172.20.0.6'  # IP interne du container forge-postgres
PG_PORT = 5432
PG_USER = 'createk'
PG_PASSWORD = 'Forge2026Hozzo!'
PG_DB = 'batiment_knowledge'

# Répertoire des corpus Planat
PLANAT_DIR = '/home/ubuntu/batiment-corpus/planat'

# Modèle d'embedding local
EMBEDDING_MODEL = 'paraphrase-multilingual-mpnet-base-v2'
EMBEDDING_DIMS = 768
BATCH_SIZE = 32  # Batch pour sentence-transformers

# Métadonnées des volumes Planat
PLANAT_VOLUMES = [
    {
        'file': 'planat_vol01_architecture-generale.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.1",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.1 (Archive.org encyclopediedela11unse)"
    },
    {
        'file': 'planat_vol02_materiaux-construction.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.2",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'materiaux',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.2 (Archive.org encyclopediedela21unse)"
    },
    {
        'file': 'planat_vol03_gros-oeuvre.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.3",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'gros-oeuvre',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.3 (Archive.org encyclopediedela31unse)"
    },
    {
        'file': 'planat_vol04_architecture-religieuse.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.4",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.4 (Archive.org encyclopediedela41unse)"
    },
    {
        'file': 'planat_vol05_architecture-civile.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.5",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.5 (Archive.org encyclopediedela51unse)"
    },
    {
        'file': 'planat_vol06_construction-moderne.txt',
        'titre': "Encyclopédie de l'architecture et de la construction — Vol.6",
        'auteur': 'Planat, Paul',
        'annee': 1888,
        'corps_etat': 'encyclopedie-generale',
        'fiabilite': 'patrimoine',
        'source': "Planat — Encyclopédie architecture Vol.6 (Archive.org encyclopediedela61unse)"
    },
]


def get_db_connection():
    """Connexion directe à PostgreSQL."""
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        dbname=PG_DB
    )


def migrate_embedding_column(conn):
    """Migre la colonne embedding de vector(1536) vers vector(768)."""
    log.info("=== Migration colonne embedding : 1536 → 768 dims ===")
    with conn.cursor() as cur:
        # Vérifier la dimension actuelle
        cur.execute("""
            SELECT atttypmod 
            FROM pg_attribute 
            WHERE attrelid = 'batiment_chunks'::regclass 
            AND attname = 'embedding'
        """)
        row = cur.fetchone()
        if row:
            # atttypmod pour pgvector = dims directement (pas de +1)
            current_dims = row[0] if row[0] > 0 else -1
            log.info(f"Dimension actuelle : {current_dims}")
            if current_dims == EMBEDDING_DIMS:
                log.info("Colonne déjà en 768 dims — pas de migration nécessaire")
                return False
        
        # Supprimer l'index vectoriel s'il existe
        cur.execute("""
            DROP INDEX IF EXISTS idx_batiment_embedding;
        """)
        
        # Modifier la colonne (nécessite de vider les embeddings d'abord)
        log.info("Mise à NULL des embeddings existants...")
        cur.execute("UPDATE batiment_chunks SET embedding = NULL")
        log.info(f"Modification de la colonne vers vector({EMBEDDING_DIMS})...")
        cur.execute(f"ALTER TABLE batiment_chunks ALTER COLUMN embedding TYPE vector({EMBEDDING_DIMS})")
        conn.commit()
        log.info(f"Migration réussie : colonne embedding → vector({EMBEDDING_DIMS})")
        return True


def clean_ocr_text(text: str) -> str:
    """Nettoie les artefacts OCR courants."""
    # Supprimer les lignes de numéros de page isolés
    text = re.sub(r'^\s*\d{1,4}\s*$', '', text, flags=re.MULTILINE)
    # Supprimer les tirets de coupure de mots en fin de ligne
    text = re.sub(r'-\n([a-zàâéèêëîïôùûüç])', r'\1', text)
    # Normaliser les espaces multiples
    text = re.sub(r'[ \t]+', ' ', text)
    # Supprimer les lignes vides multiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Supprimer les caractères parasites OCR courants
    text = re.sub(r'[|¦¡¿°©®™]', ' ', text)
    # Corriger les espaces avant ponctuation
    text = re.sub(r'\s+([,;:!?.])', r'\1', text)
    return text.strip()


def chunk_text(text: str, titre_ouvrage: str, chunk_size: int = 800, overlap: int = 100) -> list:
    """Découpe un texte en chunks avec overlap."""
    # Nettoyer d'abord
    text = clean_ocr_text(text)
    
    # Détecter les articles/sections (lignes en majuscules ou avec ==)
    sections = re.split(r'\n(?=[A-ZÀÂÉÈÊËÎÏÔÙÛÜÇ]{3,}[^a-z\n]*\n)', text)
    
    chunks = []
    for section in sections:
        section = section.strip()
        if len(section) < 50:
            continue
        
        # Extraire le titre de section si possible
        lines = section.split('\n')
        section_title = ''
        if lines and len(lines[0]) < 100 and lines[0].isupper():
            section_title = lines[0].strip()
            section = '\n'.join(lines[1:]).strip()
        
        # Découper en chunks de taille fixe avec overlap
        words = section.split()
        if not words:
            continue
        
        # Construire les chunks par mots
        i = 0
        while i < len(words):
            chunk_words = words[i:i + chunk_size]
            chunk_text_part = ' '.join(chunk_words)
            
            # Ajouter le contexte de section
            if section_title:
                prefix = f"[{titre_ouvrage}] {section_title}\n"
            else:
                prefix = f"[{titre_ouvrage}] "
            
            full_chunk = prefix + chunk_text_part
            
            if len(full_chunk.strip()) > 100:
                chunks.append(full_chunk)
            
            # Avancer avec overlap
            step = max(1, chunk_size - overlap)
            i += step
    
    return chunks


def load_sentence_transformer():
    """Charge le modèle sentence-transformers."""
    log.info(f"Chargement du modèle {EMBEDDING_MODEL}...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBEDDING_MODEL)
    log.info(f"Modèle chargé — dimensions : {model.get_sentence_embedding_dimension()}")
    return model


def get_embeddings_batch(model, texts: list) -> list:
    """Génère les embeddings pour une liste de textes."""
    embeddings = model.encode(texts, batch_size=BATCH_SIZE, show_progress_bar=False)
    return [emb.tolist() for emb in embeddings]


def reindex_existing_chunks(conn, model):
    """Réindexe tous les chunks existants qui n'ont pas d'embedding."""
    log.info("=== Réindexation des chunks existants ===")
    
    with conn.cursor() as cur:
        # Compter les chunks sans embedding
        cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE embedding IS NULL")
        total = cur.fetchone()[0]
        log.info(f"Chunks à réindexer : {total}")
        
        if total == 0:
            log.info("Tous les chunks ont déjà un embedding")
            return
        
        # Traiter par batches
        offset = 0
        batch_size = 100
        processed = 0
        
        while offset < total:
            cur.execute("""
                SELECT id, content 
                FROM batiment_chunks 
                WHERE embedding IS NULL 
                ORDER BY id
                LIMIT %s OFFSET %s
            """, (batch_size, offset))
            
            rows = cur.fetchall()
            if not rows:
                break
            
            ids = [r[0] for r in rows]
            texts = [r[1] for r in rows]
            
            # Générer les embeddings
            embeddings = get_embeddings_batch(model, texts)
            
            # Mettre à jour en base
            for chunk_id, embedding in zip(ids, embeddings):
                embedding_str = '[' + ','.join(map(str, embedding)) + ']'
                cur.execute(
                    "UPDATE batiment_chunks SET embedding = %s::vector WHERE id = %s",
                    (embedding_str, chunk_id)
                )
            
            conn.commit()
            processed += len(rows)
            offset += batch_size
            
            if processed % 500 == 0 or processed == total:
                log.info(f"  Réindexé : {processed}/{total} chunks")
    
    log.info(f"Réindexation terminée : {processed} chunks mis à jour")


def index_planat_volume(conn, model, vol_info: dict):
    """Indexe un volume Planat."""
    filepath = os.path.join(PLANAT_DIR, vol_info['file'])
    
    if not os.path.exists(filepath):
        log.warning(f"Fichier non trouvé : {filepath}")
        return 0
    
    log.info(f"\n=== Indexation : {vol_info['titre']} ===")
    
    # Vérifier si déjà indexé
    with conn.cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM batiment_chunks WHERE source = %s",
            (vol_info['source'],)
        )
        existing = cur.fetchone()[0]
        if existing > 0:
            log.info(f"  Déjà indexé ({existing} chunks) — ignoré")
            return existing
    
    # Lire et chunker le texte
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    
    log.info(f"  Texte : {len(text):,} caractères")
    chunks = chunk_text(text, vol_info['titre'])
    log.info(f"  Chunks générés : {len(chunks)}")
    
    if not chunks:
        log.warning("  Aucun chunk généré")
        return 0
    
    # Indexer par batches
    inserted = 0
    batch_size = 50
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        
        # Générer les embeddings
        embeddings = get_embeddings_batch(model, batch)
        
        # Insérer en base
        with conn.cursor() as cur:
            for chunk_text_val, embedding in zip(batch, embeddings):
                embedding_str = '[' + ','.join(map(str, embedding)) + ']'
                cur.execute("""
                    INSERT INTO batiment_chunks 
                    (content, embedding, corps_etat, source, auteur, titre_ouvrage, annee_publication, fiabilite)
                    VALUES (%s, %s::vector, %s, %s, %s, %s, %s, %s)
                """, (
                    chunk_text_val,
                    embedding_str,
                    vol_info['corps_etat'],
                    vol_info['source'],
                    vol_info['auteur'],
                    vol_info['titre'],
                    vol_info['annee'],
                    vol_info['fiabilite']
                ))
        
        conn.commit()
        inserted += len(batch)
        
        if inserted % 200 == 0 or inserted >= len(chunks):
            log.info(f"  Inséré : {inserted}/{len(chunks)} chunks")
    
    log.info(f"  Volume indexé : {inserted} chunks")
    return inserted


def create_vector_index(conn):
    """Crée l'index HNSW pour la recherche vectorielle."""
    log.info("=== Création de l'index vectoriel HNSW ===")
    with conn.cursor() as cur:
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_batiment_embedding 
            ON batiment_chunks 
            USING hnsw (embedding vector_cosine_ops)
            WITH (m = 16, ef_construction = 64)
        """)
        conn.commit()
    log.info("Index HNSW créé")


def print_stats(conn):
    """Affiche les statistiques finales."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                auteur,
                COUNT(*) as nb_chunks,
                MIN(annee_publication) as annee
            FROM batiment_chunks
            GROUP BY auteur
            ORDER BY nb_chunks DESC
        """)
        rows = cur.fetchall()
        
        log.info("\n=== STATISTIQUES FINALES ===")
        total = 0
        for auteur, nb, annee in rows:
            log.info(f"  {auteur or 'N/A'} ({annee or 'N/A'}) : {nb} chunks")
            total += nb
        log.info(f"  TOTAL : {total} chunks")
        
        # Vérifier les embeddings
        cur.execute("""
            SELECT 
                COUNT(*) FILTER (WHERE embedding IS NOT NULL) as avec_emb,
                COUNT(*) FILTER (WHERE embedding IS NULL) as sans_emb
            FROM batiment_chunks
        """)
        avec, sans = cur.fetchone()
        log.info(f"  Embeddings : {avec} avec, {sans} sans")


def main():
    log.info("=" * 60)
    log.info("MIGRATION ET INDEXATION BATIMENT KNOWLEDGE BASE")
    log.info(f"Modèle : {EMBEDDING_MODEL} ({EMBEDDING_DIMS} dims)")
    log.info("=" * 60)
    
    # Connexion PostgreSQL
    log.info("Connexion à PostgreSQL...")
    conn = get_db_connection()
    log.info("Connexion OK")
    
    # Charger le modèle d'embedding
    model = load_sentence_transformer()
    
    # Étape 1 : Migrer la colonne embedding
    migrated = migrate_embedding_column(conn)
    
    # Étape 2 : Réindexer les chunks existants (si migration effectuée)
    if migrated:
        reindex_existing_chunks(conn, model)
    else:
        log.info("Pas de migration — vérification des chunks sans embedding...")
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE embedding IS NULL")
            sans_emb = cur.fetchone()[0]
        if sans_emb > 0:
            log.info(f"{sans_emb} chunks sans embedding — réindexation...")
            reindex_existing_chunks(conn, model)
    
    # Étape 3 : Indexer les volumes Planat
    log.info("\n=== INDEXATION DES VOLUMES PLANAT ===")
    total_planat = 0
    for vol in PLANAT_VOLUMES:
        n = index_planat_volume(conn, model, vol)
        total_planat += n
    log.info(f"\nTotal Planat indexé : {total_planat} chunks")
    
    # Étape 4 : Créer l'index vectoriel
    create_vector_index(conn)
    
    # Étape 5 : Statistiques
    print_stats(conn)
    
    conn.close()
    log.info("\n=== MIGRATION ET INDEXATION TERMINÉES ===")


if __name__ == '__main__':
    main()
