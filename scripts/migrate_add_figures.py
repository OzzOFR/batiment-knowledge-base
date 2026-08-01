"""
Migration : ajout de la table batiment_figures et colonne figure_ids dans batiment_chunks
"""
import psycopg2

conn = psycopg2.connect(
    host='localhost', port=5433,
    dbname='batiment_knowledge',
    user='createk', password='Forge2026Hozzo!'
)
cur = conn.cursor()

# 1. Créer la table batiment_figures
cur.execute("""
CREATE TABLE IF NOT EXISTS batiment_figures (
    id          TEXT PRIMARY KEY,          -- ex: "fondation-semelle-filante"
    titre       TEXT NOT NULL,             -- ex: "Semelle filante en béton armé"
    description TEXT,                      -- description textuelle du schéma
    corps_etat  TEXT,                      -- ex: "gros-oeuvre"
    categorie   TEXT,                      -- ex: "fondation", "assemblage", "coupe", "detail"
    url_svg     TEXT,                      -- URL publique du fichier SVG
    url_png     TEXT,                      -- URL publique du fichier PNG (miniature)
    mots_cles   TEXT[],                    -- tags pour la recherche
    source      TEXT DEFAULT 'generated',  -- "generated" | "gallica" | "cstb"
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
""")
print("Table batiment_figures créée")

# 2. Ajouter la colonne figure_ids dans batiment_chunks (tableau de références)
cur.execute("""
ALTER TABLE batiment_chunks 
ADD COLUMN IF NOT EXISTS figure_ids TEXT[] DEFAULT '{}';
""")
print("Colonne figure_ids ajoutée dans batiment_chunks")

# 3. Index pour la recherche par mots-clés
cur.execute("""
CREATE INDEX IF NOT EXISTS idx_figures_corps_etat ON batiment_figures(corps_etat);
CREATE INDEX IF NOT EXISTS idx_figures_categorie ON batiment_figures(categorie);
CREATE INDEX IF NOT EXISTS idx_chunks_figure_ids ON batiment_chunks USING GIN(figure_ids);
""")
print("Index créés")

conn.commit()
conn.close()
print("\nMigration terminée avec succès")
