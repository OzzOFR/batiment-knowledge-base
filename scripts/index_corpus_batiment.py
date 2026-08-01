#!/usr/bin/env python3
"""
Indexation générique des ouvrages du corpus bâtiment depuis Internet Archive.
Lit la liste des ouvrages depuis ouvrages_a_indexer.json et indexe ceux
qui ne sont pas encore dans la base PostgreSQL.

Utilise sentence-transformers (768 dims) pour les embeddings locaux.
"""
import os
import re
import json
import psycopg2
from sentence_transformers import SentenceTransformer

# Configuration PostgreSQL
DB_CONFIG = {
    "host": "172.20.0.6",
    "port": 5432,
    "dbname": "batiment_knowledge",
    "user": "createk",
    "password": "Forge2026Hozzo!"
}

EMBEDDING_MODEL = "paraphrase-multilingual-mpnet-base-v2"
CORPUS_DIR = "/home/ubuntu/corpus_batiment"
BATCH_SIZE = 32
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUVRAGES_JSON = os.path.join(SCRIPT_DIR, "ouvrages_a_indexer.json")


def clean_ocr_text(text):
    """Nettoie le texte OCR des artefacts courants."""
    # Supprimer les en-têtes Google Books / Internet Archive
    text = re.sub(
        r'This is a digital copy.*?usage guidelines\n',
        '', text, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(r'Digitized by (the )?Internet Archive.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'https?://archive\.org/\S+', '', text)
    text = re.sub(r'Digitized by Google\n?', '', text, flags=re.IGNORECASE)

    # Corriger les espaces entre majuscules consécutives (OCR séparé)
    text = re.sub(r'(?<=[A-ZÀÂÉÈÊËÎÏÔÙÛÜ])\s+(?=[A-ZÀÂÉÈÊËÎÏÔÙÛÜ])', '', text)

    # Supprimer les lignes purement numériques ou de ponctuation
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) > 3 and not re.match(r'^[\d\s\.\-\*\|_=]+$', stripped):
            cleaned.append(stripped)

    text = '\n'.join(cleaned)
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def chunk_text(text, chunk_size=800, overlap=100, min_words=50):
    """Découpe le texte en chunks avec overlap."""
    words = text.split()
    chunks = []

    if len(words) <= chunk_size:
        if len(words) >= min_words:
            chunks.append(' '.join(words))
        return chunks

    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        if len(chunk.split()) >= min_words:
            chunks.append(chunk)
        if end >= len(words):
            break
        start = end - overlap

    return chunks


def get_existing_sources(conn):
    """Récupère les sources déjà indexées."""
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT source FROM batiment_chunks")
        return {row[0] for row in cur.fetchall()}


def insert_chunks_batch(conn, chunks_data, embeddings):
    """Insère les chunks avec leurs embeddings en batch."""
    inserted = 0
    with conn.cursor() as cur:
        for (chunk_text, meta), embedding in zip(chunks_data, embeddings):
            try:
                cur.execute("""
                    INSERT INTO batiment_chunks
                    (content, embedding, auteur, titre_ouvrage, annee_publication,
                     source, corps_etat, fiabilite)
                    VALUES (%s, %s::vector, %s, %s, %s, %s, %s, %s)
                """, (
                    chunk_text,
                    '[' + ','.join(map(str, embedding.tolist())) + ']',
                    meta['auteur'],
                    meta['titre'],
                    meta['annee'],
                    meta['source'],
                    meta['corps_etat'],
                    meta['niveau_fiabilite']
                ))
                inserted += 1
            except Exception as e:
                print(f"  Erreur insertion: {e}")
                conn.rollback()
    conn.commit()
    return inserted


def main():
    print("=== Indexation corpus bâtiment (Archive.org) ===")
    print(f"Modèle: {EMBEDDING_MODEL}")

    # Charger la liste des ouvrages
    with open(OUVRAGES_JSON, 'r', encoding='utf-8') as f:
        ouvrages = json.load(f)
    print(f"Ouvrages à traiter: {len(ouvrages)}")

    # Charger le modèle
    print("\nChargement du modèle d'embedding...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("Modèle chargé.")

    # Connexion PostgreSQL
    print("\nConnexion à PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    existing_sources = get_existing_sources(conn)
    print(f"Sources déjà indexées: {len(existing_sources)}")

    total_inserted = 0
    skipped = 0

    for ouvrage in ouvrages:
        filepath = os.path.join(CORPUS_DIR, ouvrage['fichier'])

        # Vérifier si le fichier existe
        if not os.path.exists(filepath):
            print(f"\n[SKIP] Fichier non trouvé: {ouvrage['fichier']}")
            skipped += 1
            continue

        # Vérifier si déjà indexé
        if ouvrage['source'] in existing_sources:
            print(f"\n[SKIP] Déjà indexé: {ouvrage['titre'][:60]}")
            skipped += 1
            continue

        print(f"\n--- {ouvrage['titre'][:70]} ({ouvrage['annee']}) ---")
        print(f"    Corps d'état: {ouvrage['corps_etat']}")

        # Lire et nettoyer
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            raw = f.read()

        print(f"  Brut: {len(raw):,} chars")
        cleaned = clean_ocr_text(raw)
        print(f"  Nettoyé: {len(cleaned):,} chars")

        chunks = chunk_text(cleaned)
        print(f"  Chunks: {len(chunks)}")

        if not chunks:
            print("  [SKIP] Aucun chunk généré")
            continue

        # Générer les embeddings par batch
        chunks_with_meta = [(c, ouvrage) for c in chunks]
        all_embeddings = []

        for i in range(0, len(chunks), BATCH_SIZE):
            batch = chunks[i:i + BATCH_SIZE]
            embs = model.encode(batch, show_progress_bar=False)
            all_embeddings.extend(embs)
            done = min(i + BATCH_SIZE, len(chunks))
            if done % (BATCH_SIZE * 5) == 0 or done == len(chunks):
                print(f"    Embeddings: {done}/{len(chunks)}")

        # Insérer
        inserted = insert_chunks_batch(conn, chunks_with_meta, all_embeddings)
        total_inserted += inserted
        print(f"  Insérés: {inserted} chunks")

    # Stats finales
    with conn.cursor() as cur:
        cur.execute("SELECT corps_etat, COUNT(*) FROM batiment_chunks GROUP BY corps_etat ORDER BY COUNT(*) DESC")
        rows = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM batiment_chunks")
        total = cur.fetchone()[0]

    conn.close()

    print(f"\n=== Résumé ===")
    print(f"Chunks insérés cette session: {total_inserted}")
    print(f"Ouvrages ignorés (déjà indexés ou fichier manquant): {skipped}")
    print(f"\nÉtat par corps d'état:")
    for corps, count in rows:
        print(f"  {corps:<30} {count:>5} chunks")
    print(f"\nTotal base: {total} chunks")


if __name__ == "__main__":
    main()
