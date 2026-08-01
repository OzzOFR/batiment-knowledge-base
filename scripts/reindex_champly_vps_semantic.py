"""
Ré-indexation sémantique des 15 volumes Champly sur le VPS PostgreSQL.

Utilise le SemanticChunker existant (découpe par sections Markdown H1-H4)
ET un chunker OCR pour les textes bruts Gallica (découpe par marqueurs N°, titres).

Connexion : PostgreSQL VPS via tunnel SSH (localhost:5433)
Embedding  : sentence-transformers paraphrase-multilingual-mpnet-base-v2 (768 dims)
"""

import re
import os
import sys
import psycopg2
import psycopg2.extras
from pathlib import Path
from sentence_transformers import SentenceTransformer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semantic_chunker import SemanticChunker

# ─── PostgreSQL (via tunnel SSH sur port 5433) ────────────────────────────────
PG_HOST     = os.environ.get("PG_HOST", "localhost")
PG_PORT     = int(os.environ.get("PG_PORT", "5433"))
PG_DB       = os.environ.get("PG_DB", "batiment_knowledge")
PG_USER     = os.environ.get("PG_USER", "createk")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "Forge2026Hozzo!")

# ─── Chunker OCR pour les textes bruts Gallica ───────────────────────────────
# Les fichiers Champly sont des textes OCR, pas du Markdown structuré.
# On utilise un chunker basé sur les marqueurs de sections du texte.

SECTION_PATTERNS = [
    re.compile(r'^\d{1,2}°\s'),
    re.compile(r'^(CHAPITRE|Chapitre|SECTION|Section)\s'),
    re.compile(r'^§\s*\d'),
    re.compile(r'^[A-ZÉÀÈÙÂÊÎÔÛÄËÏÖÜ][A-ZÉÀÈÙÂÊÎÔÛÄËÏÖÜ\s\-,\']{7,}[A-ZÉÀÈÙÂÊÎÔÛÄËÏÖÜ]$'),
]
MIN_WORDS = 80; TARGET_WORDS = 300; MAX_WORDS = 500

def is_section_start(line: str) -> bool:
    line = line.strip()
    if not line or len(line) < 4: return False
    return any(p.match(line) for p in SECTION_PATTERNS)

def count_words(text: str) -> int:
    return len(text.split())

def split_at_sentence(text: str, target: int) -> tuple:
    ends = [m.end() for m in re.finditer(r'[.!?]\s+', text)]
    if not ends:
        words = text.split(); mid = min(target, len(words))
        return ' '.join(words[:mid]), ' '.join(words[mid:])
    best = min(ends, key=lambda p: abs(len(text[:p].split()) - target))
    return text[:best].strip(), text[best:].strip()

def ocr_chunk(text: str) -> list[str]:
    """Découpe un texte OCR en chunks sémantiques."""
    # Nettoyage OCR
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\n\d{1,4}\n', '\n', text)
    # Supprimer l'en-tête Gallica
    for marker in ['NOUVELLE ENCYCLOPÉDIE', 'ENCYCLOPÉDIE PRATIQUE', 'CHAPITRE PREMIER']:
        idx = text.find(marker)
        if idx > 200: text = text[idx:]; break
    # Découper par sections
    lines = text.split('\n'); sections = []; current = []
    for line in lines:
        if is_section_start(line) and current:
            j = '\n'.join(current).strip()
            if j and count_words(j) > 5: sections.append(j)
            current = [line]
        else:
            current.append(line)
    if current:
        j = '\n'.join(current).strip()
        if j and count_words(j) > 5: sections.append(j)
    # Fusionner micro-sections + couper macro-sections
    merged = []; buf = ""
    for sec in sections:
        if buf and count_words(buf) < MIN_WORDS:
            buf = buf + "\n\n" + sec
        else:
            if buf: merged.append(buf)
            buf = sec
    if buf: merged.append(buf)
    final = []
    for sec in merged:
        rem = sec
        while count_words(rem) > MAX_WORDS:
            part, rem = split_at_sentence(rem, TARGET_WORDS)
            if part and count_words(part) >= 20: final.append(part)
            if not rem: break
        if rem and count_words(rem) >= 20: final.append(rem)
    return [c for c in final if count_words(c) >= 20]

def extract_section_title(chunk: str) -> str:
    lines = chunk.strip().split('\n')
    first = lines[0].strip()
    if len(first) < 150 and is_section_start(first): return first[:120]
    m = re.match(r'^(\d{1,2}°\s+[^.—]{3,60})', first)
    if m: return m.group(1).strip()
    return ""

# ─── Métadonnées par fichier ───────────────────────────────────────────────────
CHAMPLY_META = {
    "champly_vol01_arpentage-fondations.md":         {"corps_etat": "gros-oeuvre",           "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.1 Arpentage, Fondations"},
    "champly_vol02_maconnerie-brique.md":             {"corps_etat": "maconnerie",             "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.2 Maçonnerie, Pierre, Brique"},
    "champly_vol03_beton-arme.md":                    {"corps_etat": "gros-oeuvre",           "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.3 Béton armé, Ciment"},
    "champly_vol04_charpente-bois.md":                {"corps_etat": "charpente-couverture",  "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.4 Charpentes en bois"},
    "champly_vol05_charpentes-metalliques.md":        {"corps_etat": "charpente-couverture",  "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.5 Charpentes métalliques"},
    "champly_vol06_couvertures-toitures.md":          {"corps_etat": "charpente-couverture",  "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.6 Couverture, Zinguerie"},
    "champly_vol07_menuiserie-parquets.md":           {"corps_etat": "menuiserie",            "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.7 Menuiserie, Parquets"},
    "champly_vol08_serrurerie-fermetures.md":         {"corps_etat": "menuiserie",            "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.8 Serrurerie, Stores"},
    "champly_vol09_pavages-carrelages-peintures.md":  {"corps_etat": "platrerie-peinture",    "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.9 Pavages, Carrelages, Peintures"},
    "champly_vol10_vitrerie-chauffage-ventilation.md":{"corps_etat": "plomberie-chauffage",   "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.10 Vitrerie, Chauffage, Ventilation"},
    "champly_vol11_plomberie-chauffage.md":           {"corps_etat": "plomberie-chauffage",   "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.11 Plomberie, Chauffage"},
    "champly_vol12_plomberie-eau-assainissement.md":  {"corps_etat": "plomberie-chauffage",   "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.12 Plomberie, Eau, Assainissement"},
    "champly_vol13_salubrite-sonneries.md":           {"corps_etat": "gros-oeuvre",           "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.13 Salubrité, Sonneries"},
    "champly_vol14_escaliers-ascenseurs.md":          {"corps_etat": "gros-oeuvre",           "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.14 Escaliers, Ascenseurs"},
    "champly_vol15_architecture-plans.md":            {"corps_etat": "encyclopedie-generale", "titre": "Nouvelle Encyclopédie Pratique du Bâtiment — Vol.15 Architecture, Plans"},
}

def main():
    corpus_dir = Path("/home/ubuntu/batiment-knowledge-base/corpus/champly")
    
    print("[CHUNKER] Chargement du modèle d'embedding...")
    model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
    print(f"[CHUNKER] Modèle chargé — {model.get_sentence_embedding_dimension()} dims")
    
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASSWORD
    )
    cur = conn.cursor()
    
    # Supprimer les anciens chunks Champly
    cur.execute("DELETE FROM batiment_chunks WHERE auteur = 'René Champly'")
    deleted = cur.rowcount
    conn.commit()
    print(f"[CHUNKER] {deleted} anciens chunks Champly supprimés\n")
    
    total_inserted = 0
    
    for filename, meta in CHAMPLY_META.items():
        filepath = corpus_dir / filename
        if not filepath.exists():
            print(f"⚠️  Fichier manquant : {filename}")
            continue
        
        text = filepath.read_text(encoding='utf-8')
        
        # Extraire l'année depuis l'en-tête Gallica
        annee = None
        for line in text[:2000].split('\n'):
            if "Date d'édition :" in line:
                m = re.search(r'\d{4}', line)
                if m: annee = int(m.group()); break
        
        # Découper en chunks sémantiques (OCR)
        raw_chunks = ocr_chunk(text)
        
        # Préfixer chaque chunk avec son titre de section
        chunks_with_titles = []
        for chunk in raw_chunks:
            title = extract_section_title(chunk)
            content = f"[{meta['titre']} — {title}]\n{chunk}" if title else f"[{meta['titre']}]\n{chunk}"
            chunks_with_titles.append(content)
        
        sizes = [count_words(c) for c in chunks_with_titles]
        print(f"[{filename}]")
        print(f"  → {len(chunks_with_titles)} chunks | min={min(sizes) if sizes else 0}, max={max(sizes) if sizes else 0}, moy={sum(sizes)//len(sizes) if sizes else 0} mots")
        
        for i, content in enumerate(chunks_with_titles):
            embedding = model.encode(content, show_progress_bar=False).tolist()
            emb_str = "[" + ",".join(str(x) for x in embedding) + "]"
            source_id = f"champly_{filename.replace('.md','')}_s{i:04d}"
            
            cur.execute("""
                INSERT INTO batiment_chunks 
                    (source, content, corps_etat, auteur, titre_ouvrage, annee_publication,
                     fiabilite, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s::vector)
            """, (
                source_id, content, meta["corps_etat"],
                "René Champly", meta["titre"],
                annee or 1912, "technique-ancien", emb_str
            ))
            total_inserted += 1
        
        conn.commit()
        print(f"  ✓ {len(chunks_with_titles)} chunks insérés")
    
    cur.close()
    conn.close()
    print(f"\n✅ TERMINÉ — {total_inserted} chunks sémantiques Champly indexés sur le VPS")

if __name__ == "__main__":
    main()
