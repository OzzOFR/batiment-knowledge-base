"""
Mise à jour des métadonnées de publication pour tous les chunks existants.
Lit les chunks par pages de 500, applique le référentiel sources_metadata.py,
et met à jour les colonnes annee_publication, auteur, titre_ouvrage, fiabilite.
"""
import requests
import sys
import os

# Ajouter le dossier scripts au path pour importer sources_metadata
sys.path.insert(0, os.path.dirname(__file__))
from sources_metadata import get_metadata_for_source

SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

PAGE_SIZE = 500
total_updated = 0
total_skipped = 0
page = 0

print("=== Mise à jour des métadonnées de tous les chunks ===")

while True:
    # Récupérer une page de chunks
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/batiment_chunks",
        headers={**HEADERS, "Range": f"{page*PAGE_SIZE}-{(page+1)*PAGE_SIZE-1}"},
        params={"select": "id,source,annee_publication", "order": "id.asc"},
        timeout=30
    )
    
    if r.status_code not in (200, 206):
        print(f"Erreur lecture page {page}: {r.status_code} — {r.text[:200]}")
        break
    
    chunks = r.json()
    if not chunks:
        break
    
    print(f"\nPage {page+1} : {len(chunks)} chunks")
    
    # Grouper les chunks par source pour optimiser les updates
    source_groups = {}
    for chunk in chunks:
        src = chunk.get("source", "")
        if src not in source_groups:
            source_groups[src] = []
        source_groups[src].append(chunk["id"])
    
    # Mettre à jour par groupe de source
    for source, ids in source_groups.items():
        meta = get_metadata_for_source(source)
        
        # Mettre à jour tous les chunks de cette source en une seule requête
        r_update = requests.patch(
            f"{SUPABASE_URL}/rest/v1/batiment_chunks",
            headers={**HEADERS, "Prefer": "return=minimal"},
            params={"id": f"in.({','.join(str(i) for i in ids)})"},
            json={
                "auteur": meta["auteur"],
                "titre_ouvrage": meta["titre_ouvrage"],
                "annee_publication": meta["annee_publication"],
                "fiabilite": meta["fiabilite"],
            },
            timeout=30
        )
        
        if r_update.status_code in (200, 204):
            total_updated += len(ids)
            print(f"  ✓ {len(ids)} chunks mis à jour — {meta['auteur']} ({meta['annee_publication']}) [{meta['fiabilite']}]")
        else:
            total_skipped += len(ids)
            print(f"  ✗ Erreur {r_update.status_code} pour source '{source[:60]}': {r_update.text[:100]}")
    
    page += 1
    
    # Si on a eu moins de PAGE_SIZE résultats, c'est la dernière page
    if len(chunks) < PAGE_SIZE:
        break

print(f"\n=== Terminé ! {total_updated} chunks mis à jour, {total_skipped} erreurs ===")

# Vérification finale
r_check = requests.get(
    f"{SUPABASE_URL}/rest/v1/batiment_chunks",
    headers=HEADERS,
    params={
        "select": "auteur,annee_publication,fiabilite",
        "auteur": "not.is.null",
        "limit": "1"
    },
    timeout=15
)
if r_check.status_code == 200 and r_check.json():
    sample = r_check.json()[0]
    print(f"\nVérification : {sample}")
