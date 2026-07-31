#!/usr/bin/env python3
"""
Indexation des ouvrages plomberie/chauffage téléchargés depuis Internet Archive.
Utilise sentence-transformers (768 dims) pour les embeddings locaux.

Ouvrages indexés :
- Manuel du mécanicien fontainier, pompier, plombier (1828)
- Traité pratique du chauffage, de la ventilation et de la distribution des eaux (1873)
- Traité pratique du chauffage et de la ventilation - Pica (1897)
- Fumisterie, chauffage et ventilation - Aucamus (1898)
"""
import os
import re
import time
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
EMBEDDING_DIMS = 768
CORPUS_DIR = "/home/ubuntu/corpus_plomberie"
BATCH_SIZE = 32

# Métadonnées des ouvrages
OUVRAGES = [
    {
        "fichier": "manuel_mecanicien_fontainier_1828.txt",
        "auteur": "Anonyme",
        "titre": "Manuel du mécanicien fontainier, pompier, plombier",
        "annee": 1828,
        "source": "Internet Archive / Roret, Paris (1828)",
        "corps_etat": "plomberie-chauffage",
        "niveau_fiabilite": "patrimoine_xix",
        "langue": "fr"
    },
    {
        "fichier": "traite_chauffage_ventilation_1873.txt",
        "auteur": "Collectif",
        "titre": "Traité pratique du chauffage, de la ventilation et de la distribution des eaux dans les habitations",
        "annee": 1873,
        "source": "Internet Archive / Wellcome Library (1873)",
        "corps_etat": "plomberie-chauffage",
        "niveau_fiabilite": "patrimoine_xix",
        "langue": "fr"
    },
    {
        "fichier": "traite_chauffage_pica_1897.txt",
        "auteur": "Pica, A.",
        "titre": "Traité pratique du chauffage et de la ventilation : principes, appareils, installations",
        "annee": 1897,
        "source": "Internet Archive / Google Books (1897)",
        "corps_etat": "plomberie-chauffage",
        "niveau_fiabilite": "technique_xix_xx",
        "langue": "fr"
    },
    {
        "fichier": "fumisterie_chauffage_ventilation_1898.txt",
        "auteur": "Aucamus, E.",
        "titre": "Fumisterie, chauffage et ventilation",
        "annee": 1898,
        "source": "Internet Archive / Google Books (1898)",
        "corps_etat": "plomberie-chauffage",
        "niveau_fiabilite": "technique_xix_xx",
        "langue": "fr"
    }
]


def clean_ocr_text(text):
    """Nettoie le texte OCR des artefacts courants."""
    # Supprimer les en-têtes Google Books
    text = re.sub(r'This is a digital copy.*?usage guidelines\n', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'Digitized by (the )?Internet Archive.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'https?://archive\.org/\S+', '', text)
    
    # Corriger les espaces multiples dans les mots (OCR souvent sépare les lettres)
    # Ex: "M E C A N I C I E N" -> "MECANICIEN"
    text = re.sub(r'(?<=[A-ZÀÂÉÈÊËÎÏÔÙÛÜ])\s+(?=[A-ZÀÂÉÈÊËÎÏÔÙÛÜ])', '', text)
    
    # Supprimer les lignes avec uniquement des caractères spéciaux/numéros de page
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        # Garder les lignes avec du contenu substantiel
        if len(stripped) > 3 and not re.match(r'^[\d\s\.\-\*]+$', stripped):
            cleaned_lines.append(stripped)
    
    text = '\n'.join(cleaned_lines)
    
    # Normaliser les espaces multiples
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


def chunk_text(text, chunk_size=800, overlap=100):
    """Découpe le texte en chunks avec overlap."""
    words = text.split()
    chunks = []
    
    if len(words) <= chunk_size:
        if len(words) > 50:  # Ignorer les chunks trop courts
            chunks.append(' '.join(words))
        return chunks
    
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        
        if len(chunk.split()) > 50:  # Minimum 50 mots
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


def insert_chunks(conn, chunks_data, embeddings):
    """Insère les chunks avec leurs embeddings."""
    with conn.cursor() as cur:
        inserted = 0
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
                continue
        conn.commit()
        return inserted


def main():
    print(f"=== Indexation ouvrages plomberie/chauffage ===")
    print(f"Modèle: {EMBEDDING_MODEL} ({EMBEDDING_DIMS} dims)")
    
    # Charger le modèle
    print("\nChargement du modèle d'embedding...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("Modèle chargé.")
    
    # Connexion PostgreSQL
    print("\nConnexion à PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    existing_sources = get_existing_sources(conn)
    print(f"Sources existantes: {len(existing_sources)}")
    
    total_inserted = 0
    
    for ouvrage in OUVRAGES:
        filepath = os.path.join(CORPUS_DIR, ouvrage['fichier'])
        
        if not os.path.exists(filepath):
            print(f"\n[SKIP] Fichier non trouvé: {filepath}")
            continue
        
        # Vérifier si déjà indexé
        if ouvrage['source'] in existing_sources:
            print(f"\n[SKIP] Déjà indexé: {ouvrage['titre']}")
            continue
        
        print(f"\n--- Traitement: {ouvrage['titre']} ({ouvrage['annee']}) ---")
        
        # Lire et nettoyer le texte
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            raw_text = f.read()
        
        print(f"  Texte brut: {len(raw_text):,} caractères")
        cleaned = clean_ocr_text(raw_text)
        print(f"  Texte nettoyé: {len(cleaned):,} caractères")
        
        # Découper en chunks
        chunks = chunk_text(cleaned, chunk_size=800, overlap=100)
        print(f"  Chunks générés: {len(chunks)}")
        
        if not chunks:
            print(f"  [SKIP] Aucun chunk généré")
            continue
        
        # Préparer les métadonnées
        chunks_with_meta = [(chunk, ouvrage) for chunk in chunks]
        
        # Générer les embeddings par batch
        print(f"  Génération des embeddings ({len(chunks)} chunks)...")
        all_embeddings = []
        
        for i in range(0, len(chunks), BATCH_SIZE):
            batch = chunks[i:i+BATCH_SIZE]
            batch_embeddings = model.encode(batch, show_progress_bar=False)
            all_embeddings.extend(batch_embeddings)
            
            if (i // BATCH_SIZE + 1) % 5 == 0:
                print(f"    Batch {i//BATCH_SIZE + 1}/{(len(chunks)-1)//BATCH_SIZE + 1} traité")
        
        # Insérer dans PostgreSQL
        print(f"  Insertion dans PostgreSQL...")
        inserted = insert_chunks(conn, chunks_with_meta, all_embeddings)
        total_inserted += inserted
        print(f"  {inserted} chunks insérés")
    
    # Stats finales
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE corps_etat = 'plomberie-chauffage'")
        total_plomberie = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM batiment_chunks")
        total_all = cur.fetchone()[0]
    
    conn.close()
    
    print(f"\n=== Résumé ===")
    print(f"Chunks insérés cette session: {total_inserted}")
    print(f"Total plomberie-chauffage: {total_plomberie}")
    print(f"Total base: {total_all}")
    print("Indexation terminée.")


if __name__ == "__main__":
    main()
