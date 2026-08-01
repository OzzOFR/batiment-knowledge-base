"""
Indexation des figures vectorielles dans PostgreSQL et liaison aux chunks.
"""
import json
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host='localhost', port=5433,
    dbname='batiment_knowledge',
    user='createk', password='Forge2026Hozzo!'
)
cur = conn.cursor()

SERVER_BASE_URL = "https://knowledge.ozzo.fr"

# Charger le catalogue
with open("/home/ubuntu/batiment-knowledge-base/figures/catalogue_figures.json") as f:
    catalogue = json.load(f)

# Figures générées (les 7 SVG existants)
FIGURES_GENEREES = {
    "fondation-semelle-filante",
    "charpente-ferme-traditionnelle",
    "mur-brique-parpaing-coupe",
    "plancher-hourdis-poutrelles",
    "ventilation-vmc-simple-flux",
    "fissure-facade-diagnostic",
    "etancheite-toiture-terrasse",
}

# Mapping figure_id -> chunks à lier (mots-clés de recherche)
FIGURE_CHUNK_KEYWORDS = {
    "fondation-semelle-filante": ["semelle filante", "fondation", "béton armé", "hors-gel", "ferraillage fondation"],
    "charpente-ferme-traditionnelle": ["ferme charpente", "arbalétrier", "poinçon", "entrait", "charpente bois ferme"],
    "mur-brique-parpaing-coupe": ["mur porteur", "brique", "parpaing", "chaînage", "linteau"],
    "plancher-hourdis-poutrelles": ["poutrelles hourdis", "plancher préfabriqué", "table de compression", "plancher béton"],
    "ventilation-vmc-simple-flux": ["VMC", "ventilation mécanique", "simple flux", "bouche extraction", "entrée air"],
    "fissure-facade-diagnostic": ["fissure", "façade", "tassement différentiel", "retrait", "pathologie fissure"],
    "etancheite-toiture-terrasse": ["toiture-terrasse", "étanchéité", "membrane", "pare-vapeur", "acrotère"],
}

print("=== Indexation des figures dans batiment_figures ===\n")

# Insérer les figures dans la table
for fig in catalogue:
    fig_id = fig["id"]
    has_svg = fig_id in FIGURES_GENEREES
    url_svg = f"{SERVER_BASE_URL}/figures/{fig_id}.svg" if has_svg else None
    
    cur.execute("""
        INSERT INTO batiment_figures (id, titre, description, corps_etat, categorie, url_svg, url_png, mots_cles, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            titre = EXCLUDED.titre,
            description = EXCLUDED.description,
            url_svg = EXCLUDED.url_svg,
            mots_cles = EXCLUDED.mots_cles,
            source = EXCLUDED.source
    """, (
        fig_id,
        fig["titre"],
        fig["description"],
        fig["corps_etat"],
        fig["categorie"],
        url_svg,
        None,  # url_png (à générer plus tard)
        fig["mots_cles"],
        "generated" if has_svg else "planned"
    ))
    status = "✓ SVG disponible" if has_svg else "○ Planifiée"
    print(f"  {status} : {fig_id}")

conn.commit()
print(f"\n{len(catalogue)} figures indexées dans batiment_figures")

print("\n=== Liaison figures → chunks ===\n")

# Lier les figures aux chunks via les mots-clés
total_links = 0
for fig_id, keywords in FIGURE_CHUNK_KEYWORDS.items():
    # Construire la condition de recherche
    conditions = " OR ".join([f"content ILIKE %s" for _ in keywords])
    params = [f"%{kw}%" for kw in keywords]
    
    cur.execute(f"""
        SELECT id FROM batiment_chunks
        WHERE ({conditions})
        AND NOT (%s = ANY(figure_ids))
        LIMIT 50
    """, params + [fig_id])
    
    chunk_ids = [r[0] for r in cur.fetchall()]
    
    if chunk_ids:
        # Ajouter figure_id dans le tableau figure_ids des chunks
        cur.execute("""
            UPDATE batiment_chunks
            SET figure_ids = array_append(figure_ids, %s)
            WHERE id = ANY(%s)
            AND NOT (%s = ANY(figure_ids))
        """, (fig_id, chunk_ids, fig_id))
        
        total_links += len(chunk_ids)
        print(f"  {fig_id} → {len(chunk_ids)} chunks liés")
    else:
        print(f"  {fig_id} → aucun chunk trouvé")

conn.commit()
print(f"\nTotal : {total_links} liaisons figure-chunk créées")

# Vérification finale
cur.execute("SELECT COUNT(*) FROM batiment_figures WHERE url_svg IS NOT NULL")
n_svg = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE array_length(figure_ids, 1) > 0")
n_chunks_with_fig = cur.fetchone()[0]
print(f"\nBilan :")
print(f"  Figures avec SVG disponible : {n_svg}")
print(f"  Chunks avec figure(s) liée(s) : {n_chunks_with_fig}")

conn.close()
