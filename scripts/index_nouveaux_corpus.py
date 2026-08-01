#!/usr/bin/env python3
"""
Indexation des nouveaux corpus dans la base batiment_knowledge.
- pathologies_batiment_desordres.txt  → pathologies
- normes_reglements_batiment.txt      → normes-reglements
- materiaux_modernes_mise_en_oeuvre.txt → materiaux
- barberot_constructions_civiles_1900.txt → gros-oeuvre
- rondelet_vol3_art_batir.txt         → encyclopedie-generale
- rondelet_vol5_art_batir.txt         → encyclopedie-generale
- manuel_construction_terre_1985.txt  → maconnerie
"""

import re
import sys
import psycopg2
import psycopg2.extras
from sentence_transformers import SentenceTransformer

# Config
PG_HOST = "localhost"
PG_PORT = 5432
PG_DB   = "batiment_knowledge"
PG_USER = "createk"
PG_PASS = "Forge2026Hozzo!"

EMBEDDING_MODEL = "paraphrase-multilingual-mpnet-base-v2"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
BATCH_SIZE = 32

# Corpus à indexer
CORPUS = [
    {
        "file": "/home/ubuntu/corpus_batiment/pathologies_batiment_desordres.txt",
        "source": "pathologies_batiment_2024",
        "auteur": "OzzO Knowledge Base",
        "titre": "Pathologies du bâtiment — Désordres, causes et remèdes",
        "annee": 2024,
        "corps_etat": "pathologies",
        "fiabilite": "technique-moderne",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/normes_reglements_batiment.txt",
        "source": "normes_reglements_2024",
        "auteur": "OzzO Knowledge Base",
        "titre": "Normes et réglementations du bâtiment en France",
        "annee": 2024,
        "corps_etat": "normes-reglements",
        "fiabilite": "norme-en-vigueur",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/materiaux_modernes_mise_en_oeuvre.txt",
        "source": "materiaux_modernes_2024",
        "auteur": "OzzO Knowledge Base",
        "titre": "Matériaux de construction modernes — Propriétés et mise en œuvre",
        "annee": 2024,
        "corps_etat": "materiaux",
        "fiabilite": "technique-moderne",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/barberot_constructions_civiles_1900.txt",
        "source": "barberot_constructions_1900",
        "auteur": "Barberot, Étienne",
        "titre": "Traité de Constructions Civiles",
        "annee": 1900,
        "corps_etat": "gros-oeuvre",
        "fiabilite": "technique-ancien",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/rondelet_vol3_art_batir.txt",
        "source": "rondelet_art_batir_vol3",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre": "Traité théorique et pratique de l'art de bâtir — Vol. 3",
        "annee": 1834,
        "corps_etat": "encyclopedie-generale",
        "fiabilite": "patrimoine",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/rondelet_vol5_art_batir.txt",
        "source": "rondelet_art_batir_vol5",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre": "Traité théorique et pratique de l'art de bâtir — Vol. 5",
        "annee": 1834,
        "corps_etat": "encyclopedie-generale",
        "fiabilite": "patrimoine",
    },
    {
        "file": "/home/ubuntu/corpus_batiment/manuel_construction_terre_1985.txt",
        "source": "manuel_construction_terre_1985",
        "auteur": "CRATerre",
        "titre": "Manuel de construction en terre",
        "annee": 1985,
        "corps_etat": "maconnerie",
        "fiabilite": "technique-moderne",
    },
]


def clean_ocr(text: str) -> str:
    """Nettoie le texte OCR."""
    # Supprimer les lignes vides multiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Supprimer les artefacts OCR courants
    text = re.sub(r'[^\x00-\x7F\u00C0-\u024F\u2019\u2018\u201C\u201D\u2013\u2014\n ]', ' ', text)
    # Normaliser les espaces
    text = re.sub(r' {3,}', ' ', text)
    # Supprimer les lignes de moins de 20 caractères (numéros de page, etc.)
    lines = text.split('\n')
    lines = [l for l in lines if len(l.strip()) > 15 or l.strip() == '']
    return '\n'.join(lines).strip()


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Découpe le texte en chunks avec chevauchement."""
    # Découper d'abord par paragraphes
    paragraphs = re.split(r'\n\n+', text)
    
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Si le paragraphe seul dépasse chunk_size, le découper par phrases
        if len(para) > chunk_size * 1.5:
            sentences = re.split(r'(?<=[.!?])\s+', para)
            for sent in sentences:
                if len(current_chunk) + len(sent) < chunk_size:
                    current_chunk += " " + sent if current_chunk else sent
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = sent
        else:
            if len(current_chunk) + len(para) + 2 < chunk_size:
                current_chunk += "\n\n" + para if current_chunk else para
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                # Overlap : garder les derniers mots du chunk précédent
                if overlap > 0 and current_chunk:
                    words = current_chunk.split()[-overlap//10:]
                    current_chunk = " ".join(words) + "\n\n" + para
                else:
                    current_chunk = para
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    # Filtrer les chunks trop courts
    return [c for c in chunks if len(c) > 100]


def get_existing_sources(conn) -> set:
    """Récupère les sources déjà indexées."""
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT source FROM batiment_chunks")
        return {row[0] for row in cur.fetchall()}


def insert_chunks_batch(conn, chunks_data: list[dict]):
    """Insère un batch de chunks avec embeddings."""
    with conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, """
            INSERT INTO batiment_chunks
              (content, corps_etat, source, auteur, titre_ouvrage, annee_publication, fiabilite, embedding)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s::vector)
            ON CONFLICT DO NOTHING
        """, [
            (
                c["content"], c["corps_etat"], c["source"], c["auteur"],
                c["titre"], c["annee"], c["fiabilite"],
                "[" + ",".join(map(str, c["embedding"])) + "]"
            )
            for c in chunks_data
        ])
    conn.commit()


def main():
    print(f"[Index] Chargement modèle embedding : {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print(f"[Index] Modèle chargé — {model.get_sentence_embedding_dimension()} dims")
    
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASS
    )
    
    existing_sources = get_existing_sources(conn)
    print(f"[Index] Sources déjà indexées : {len(existing_sources)}")
    
    total_inserted = 0
    
    for corpus in CORPUS:
        source = corpus["source"]
        filepath = corpus["file"]
        
        if source in existing_sources:
            print(f"[SKIP] {source} — déjà indexé")
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                raw_text = f.read()
        except FileNotFoundError:
            print(f"[WARN] Fichier non trouvé : {filepath}")
            continue
        
        if len(raw_text) < 500:
            print(f"[WARN] Fichier trop court ({len(raw_text)} bytes) : {filepath}")
            continue
        
        print(f"\n[Index] Traitement : {source}")
        print(f"  Taille brute : {len(raw_text):,} chars")
        
        text = clean_ocr(raw_text)
        chunks = chunk_text(text)
        
        print(f"  Chunks générés : {len(chunks)}")
        
        # Générer les embeddings par batch
        all_chunks_data = []
        for i in range(0, len(chunks), BATCH_SIZE):
            batch = chunks[i:i+BATCH_SIZE]
            embeddings = model.encode(batch, show_progress_bar=False)
            
            for chunk_text_val, emb in zip(batch, embeddings):
                all_chunks_data.append({
                    "content": chunk_text_val,
                    "corps_etat": corpus["corps_etat"],
                    "source": source,
                    "auteur": corpus["auteur"],
                    "titre": corpus["titre"],
                    "annee": corpus["annee"],
                    "fiabilite": corpus["fiabilite"],
                    "embedding": emb.tolist(),
                })
            
            print(f"  Batch {i//BATCH_SIZE + 1}/{(len(chunks)-1)//BATCH_SIZE + 1} encodé")
        
        # Insérer en base
        insert_chunks_batch(conn, all_chunks_data)
        total_inserted += len(all_chunks_data)
        print(f"  ✓ {len(all_chunks_data)} chunks insérés pour {source}")
    
    # Stats finales
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE embedding IS NOT NULL")
        total = cur.fetchone()[0]
    
    conn.close()
    print(f"\n=== TERMINÉ ===")
    print(f"Chunks insérés dans cette session : {total_inserted}")
    print(f"Total en base : {total}")


if __name__ == "__main__":
    main()
