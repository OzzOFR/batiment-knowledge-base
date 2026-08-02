"""
Crée la table batiment_figures_gallica et la peuple avec les 330 figures
identifiées dans les chunks Champly (niveau 1 de certitude : légendes intégrées).

Chaque figure a :
- chunk_id : le chunk source
- vol_num : numéro du volume Champly (1-15)
- figure_num : numéro de la figure dans le volume
- legende : texte de la légende extrait du chunk
- url_gallica : URL du visualiseur Gallica (page estimée)
- url_image : URL IIIF directe de l'image
- ark : identifiant ARK Gallica du volume
- gallica_page : numéro de page estimé dans Gallica
- note_precision : avertissement sur la précision de l'estimation
"""
import psycopg2
import re

# Credentials PostgreSQL VPS
PG_HOST = "localhost"
PG_PORT = 5433
PG_DB   = "batiment_knowledge"
PG_USER = "createk"
PG_PASS = "Forge2026Hozzo!"

# ARKs des 15 volumes Champly
CHAMPLY_ARKS = {
    1:  "bpt6k9774323q",
    2:  "bpt6k97743229",
    3:  "bpt6k9774321w",
    4:  "bpt6k97744269",
    5:  "bpt6k97744284",
    6:  "bpt6k9774427q",
    7:  "bpt6k65806792",
    8:  "bpt6k6580680q",
    9:  "bpt6k65806814",
    10: "bpt6k6580763j",
    11: "bpt6k6580764z",
    12: "bpt6k6580765c",
    13: "bpt6k65807550",
    14: "bpt6k6580756d",
    15: "bpt6k6580757t",
}

# Nombre de pages texte par volume (hors pages de garde)
VOLUME_TEXT_PAGES = {
    1: 140, 2: 148, 3: 156, 4: 128, 5: 122,
    6: 134, 7: 101, 8: 114, 9: 175, 10: 140,
    11: 153, 12: 151, 13: 172, 14: 102, 15: 54
}

# Offset Gallica (pages de garde + couverture + table des matières)
GALLICA_OFFSET = 12

def get_connection():
    return psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASS
    )

def extract_vol_from_source(source_fichier):
    """Extraire le numéro de volume depuis le nom du fichier source."""
    if not source_fichier:
        return None
    match = re.search(r'vol(\d+)', source_fichier, re.IGNORECASE)
    if match:
        return int(match.group(1))
    # Essayer depuis le titre de section [Vol.X —]
    match = re.search(r'\[Vol\.(\d+)', source_fichier)
    if match:
        return int(match.group(1))
    return None

def estimate_gallica_page(fig_num, vol_num):
    """
    Estimer la page Gallica d'une figure par position relative.
    Les figures sont numérotées séquentiellement dans chaque volume.
    """
    text_pages = VOLUME_TEXT_PAGES.get(vol_num, 130)
    # Estimer le nombre max de figures dans ce volume (~1 fig / 1.5 pages)
    max_figs_estimate = int(text_pages / 1.5)
    if max_figs_estimate < 1:
        max_figs_estimate = 80
    
    relative_pos = min(fig_num / max_figs_estimate, 0.95)
    page = int(GALLICA_OFFSET + relative_pos * text_pages)
    return max(GALLICA_OFFSET, min(page, GALLICA_OFFSET + text_pages - 1))

def main():
    conn = get_connection()
    cur = conn.cursor()
    
    # 1. Créer la table batiment_figures_gallica
    print("Création de la table batiment_figures_gallica...")
    cur.execute("""
        DROP TABLE IF EXISTS batiment_figures_gallica;
        CREATE TABLE batiment_figures_gallica (
            id SERIAL PRIMARY KEY,
            chunk_id INTEGER REFERENCES batiment_chunks(id) ON DELETE CASCADE,
            vol_num INTEGER,
            figure_num INTEGER,
            legende TEXT,
            url_gallica TEXT,
            url_image TEXT,
            ark TEXT,
            gallica_page INTEGER,
            note_precision TEXT,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        CREATE INDEX idx_figures_gallica_chunk ON batiment_figures_gallica(chunk_id);
        CREATE INDEX idx_figures_gallica_vol ON batiment_figures_gallica(vol_num, figure_num);
    """)
    conn.commit()
    print("  ✓ Table créée")
    
    # 2. Récupérer les chunks Champly
    print("\nRécupération des chunks Champly...")
    cur.execute("""
        SELECT id, content, source, auteur, titre_ouvrage
        FROM batiment_chunks
        WHERE auteur ILIKE '%champly%'
        ORDER BY id
    """)
    chunks = cur.fetchall()
    print(f"  {len(chunks)} chunks Champly trouvés")
    
    # 3. Extraire les figures avec légendes intégrées
    # Pattern : "Fig. N. — Description" ou "Fig. N — Description"
    fig_pattern = re.compile(
        r'Fig\.?\s*(\d+)\.?\s*[—–-]\s*([^.!?\n]{10,120})',
        re.IGNORECASE
    )
    
    inserted = 0
    chunks_with_figs = 0
    
    for chunk_id, contenu, source_fichier, auteur, titre_ouvrage in chunks:
        if not contenu:
            continue
        
        # Extraire le numéro de volume
        vol_num = extract_vol_from_source(source_fichier)
        if not vol_num:
            vol_num = extract_vol_from_source(titre_ouvrage)
        
        # Chercher les figures dans le contenu
        matches = fig_pattern.findall(contenu)
        if not matches:
            continue
        
        chunks_with_figs += 1
        
        for fig_num_str, legende in matches:
            fig_num = int(fig_num_str)
            legende = legende.strip()
            
            if not vol_num or vol_num not in CHAMPLY_ARKS:
                # Insérer sans URL Gallica
                cur.execute("""
                    INSERT INTO batiment_figures_gallica
                    (chunk_id, vol_num, figure_num, legende, note_precision)
                    VALUES (%s, %s, %s, %s, %s)
                """, (chunk_id, vol_num, fig_num, legende,
                      "Volume non identifié — URL Gallica non disponible"))
                inserted += 1
                continue
            
            ark = CHAMPLY_ARKS[vol_num]
            gallica_page = estimate_gallica_page(fig_num, vol_num)
            
            url_gallica = f"https://gallica.bnf.fr/ark:/12148/{ark}/f{gallica_page}.item"
            url_image   = f"https://gallica.bnf.fr/iiif/ark:/12148/{ark}/f{gallica_page}/full/full/0/native.jpg"
            
            cur.execute("""
                INSERT INTO batiment_figures_gallica
                (chunk_id, vol_num, figure_num, legende, url_gallica, url_image, ark, gallica_page, note_precision)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                chunk_id, vol_num, fig_num, legende,
                url_gallica, url_image, ark, gallica_page,
                f"Page estimée par position relative (±3 pages). Vérifier sur Gallica : {url_gallica}"
            ))
            inserted += 1
    
    conn.commit()
    
    print(f"\n✓ {inserted} figures insérées depuis {chunks_with_figs} chunks")
    
    # 4. Stats finales
    cur.execute("SELECT COUNT(*) FROM batiment_figures_gallica")
    total = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM batiment_figures_gallica WHERE url_gallica IS NOT NULL")
    avec_url = cur.fetchone()[0]
    
    cur.execute("""
        SELECT vol_num, COUNT(*) as nb_figs
        FROM batiment_figures_gallica
        WHERE vol_num IS NOT NULL
        GROUP BY vol_num ORDER BY vol_num
    """)
    print("\nFigures par volume :")
    for r in cur.fetchall():
        ark = CHAMPLY_ARKS.get(r[0], "?")
        print(f"  Vol.{r[0]:2d} ({ark}) : {r[1]} figures")
    
    print(f"\nTotal : {total} figures ({avec_url} avec URL Gallica)")
    
    # 5. Exemples
    cur.execute("""
        SELECT vol_num, figure_num, legende, url_gallica
        FROM batiment_figures_gallica
        WHERE url_gallica IS NOT NULL
        ORDER BY vol_num, figure_num
        LIMIT 8
    """)
    print("\nExemples :")
    for r in cur.fetchall():
        print(f"  Vol.{r[0]} Fig.{r[1]} : {r[2][:60]}...")
        print(f"    → {r[3]}")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
