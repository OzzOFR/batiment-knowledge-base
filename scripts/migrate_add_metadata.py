"""
Migration DDL : ajout des colonnes de métadonnées de publication
- annee_publication : INTEGER (ex. 1834, 1900, 2023)
- auteur : TEXT (ex. "Rondelet", "Barberot", "ADEME")
- titre_ouvrage : TEXT (ex. "Traité de l'art de bâtir")
- fiabilite : TEXT (patrimoine | technique-ancien | technique-moderne | norme-en-vigueur)
"""
import requests

SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Utiliser l'endpoint SQL de Supabase via la fonction RPC
# On va utiliser l'API PostgREST pour vérifier d'abord la structure actuelle
r = requests.get(
    f"{SUPABASE_URL}/rest/v1/batiment_chunks?limit=1&select=id,source,corps_etat",
    headers=HEADERS, timeout=15
)
print(f"Test connexion: {r.status_code}")
if r.status_code == 200:
    print(f"Structure actuelle: {list(r.json()[0].keys()) if r.json() else 'vide'}")

# Vérifier si les colonnes existent déjà
r2 = requests.get(
    f"{SUPABASE_URL}/rest/v1/batiment_chunks?limit=1&select=annee_publication,auteur,titre_ouvrage,fiabilite",
    headers=HEADERS, timeout=15
)
print(f"Test colonnes métadonnées: {r2.status_code}")
if r2.status_code == 200:
    print("Les colonnes de métadonnées existent déjà !")
    print(r2.json())
elif r2.status_code == 400:
    print("Les colonnes n'existent pas encore — migration nécessaire")
    print(r2.text[:200])
