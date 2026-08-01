"""
Mise à jour des métadonnées des fiches OzzO Knowledge Base sur le VPS PostgreSQL.
Ces fiches sont des synthèses rédigées par IA (Manus/OzzO), pas des sources primaires.
On les marque explicitement avec :
  - type_contenu = 'synthese-ia'
  - fiabilite    = 'synthese-ia'
  - auteur       = 'OzzO Knowledge Base (synthèse IA)'
  - note dans le contenu si absent
"""

import psycopg2
import psycopg2.extras

PG_HOST     = "localhost"
PG_PORT     = 5433
PG_DB       = "batiment_knowledge"
PG_USER     = "createk"
PG_PASSWORD = "Forge2026Hozzo!"

def main():
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB,
        user=PG_USER, password=PG_PASSWORD, connect_timeout=10
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # 1. Compter les chunks concernés
    cur.execute("SELECT COUNT(*) FROM batiment_chunks WHERE auteur = 'OzzO Knowledge Base'")
    count = cur.fetchone()['count']
    print(f"Chunks OzzO à mettre à jour : {count}")

    # 2. Vérifier si la colonne type_contenu existe
    cur.execute("""
        SELECT column_name FROM information_schema.columns
        WHERE table_name = 'batiment_chunks' AND column_name = 'type_contenu'
    """)
    has_type_contenu = cur.fetchone() is not None
    print(f"Colonne type_contenu présente : {has_type_contenu}")

    # 3. Mettre à jour auteur et fiabilite
    cur.execute("""
        UPDATE batiment_chunks
        SET
            auteur   = 'OzzO Knowledge Base (synthèse IA)',
            fiabilite = 'synthese-ia'
        WHERE auteur = 'OzzO Knowledge Base'
    """)
    updated = cur.rowcount
    print(f"Chunks mis à jour (auteur + fiabilite) : {updated}")

    # 4. Si type_contenu existe, le mettre à jour aussi
    if has_type_contenu:
        cur.execute("""
            UPDATE batiment_chunks
            SET type_contenu = 'synthese-ia'
            WHERE auteur = 'OzzO Knowledge Base (synthèse IA)'
        """)
        print(f"Colonne type_contenu mise à jour : {cur.rowcount}")

    conn.commit()
    print("\n=== Vérification finale ===")
    cur.execute("""
        SELECT auteur, fiabilite, COUNT(*) as chunks
        FROM batiment_chunks
        WHERE auteur LIKE '%OzzO%'
        GROUP BY auteur, fiabilite
        ORDER BY chunks DESC
    """)
    for row in cur.fetchall():
        print(f"  {row['auteur']} | {row['fiabilite']} | {row['chunks']} chunks")

    conn.close()
    print("\nMise à jour terminée.")

if __name__ == "__main__":
    main()
