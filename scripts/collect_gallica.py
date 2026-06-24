"""
Script de collecte des ouvrages libres de droits sur Gallica (BNF).
Cible : Nouvelle Encyclopédie Pratique du Bâtiment - René Champly
API Gallica : https://api.bnf.fr/api-gallica-de-recherche
"""

import requests
import json
import os
import time
from pathlib import Path

# Répertoire de sortie
OUTPUT_DIR = Path(__file__).parent.parent / "sources" / "gallica"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ARKs Gallica connus pour les volumes Champly (Nouvelle Encyclopédie Pratique)
# Identifiés manuellement depuis gallica.bnf.fr
CHAMPLY_VOLUMES = [
    {"ark": "bpt6k65806792", "volume": 7,  "titre": "Nouvelle encyclopédie pratique du bâtiment - Vol. 7"},
    {"ark": "bpt6k6580680d", "volume": 8,  "titre": "Nouvelle encyclopédie pratique du bâtiment - Vol. 8"},
    {"ark": "bpt6k6580681r", "volume": 9,  "titre": "Nouvelle encyclopédie pratique du bâtiment - Vol. 9"},
    {"ark": "bpt6k65806835", "volume": 10, "titre": "Nouvelle encyclopédie pratique du bâtiment - Vol. 10"},
]

# Autres ouvrages techniques libres de droits sur Gallica
AUTRES_OUVRAGES = [
    {
        "ark": "bpt6k6361498m",
        "titre": "Traité pratique de maçonnerie",
        "corps_etat": "maconnerie",
        "auteur": "Anonyme",
        "date": "1900"
    },
    {
        "ark": "bpt6k6236470j",
        "titre": "La charpente en bois",
        "corps_etat": "charpente-couverture",
        "auteur": "Anonyme",
        "date": "1910"
    },
]

GALLICA_TEXT_URL = "https://gallica.bnf.fr/ark:/12148/{ark}.texteBrut"
GALLICA_META_URL = "https://gallica.bnf.fr/services/OAIRecord?ark={ark}"


def fetch_text(ark: str) -> str | None:
    """Télécharge le texte brut d'un document Gallica via son ARK."""
    url = GALLICA_TEXT_URL.format(ark=ark)
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            return r.text
        else:
            print(f"  [ERREUR] HTTP {r.status_code} pour {ark}")
            return None
    except Exception as e:
        print(f"  [ERREUR] {e} pour {ark}")
        return None


def search_gallica(query: str, nb_results: int = 10) -> list:
    """Recherche des documents sur Gallica via l'API SRU."""
    url = "https://gallica.bnf.fr/SRU"
    params = {
        "operation": "searchRetrieve",
        "version": "1.2",
        "query": f'gallica all "{query}" and dc.type all "monographie"',
        "maximumRecords": nb_results,
        "startRecord": 1,
        "lang": "fr",
        "suggest": 0,
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        if r.status_code == 200:
            return r.text
        return ""
    except Exception as e:
        print(f"  [ERREUR SEARCH] {e}")
        return ""


def clean_text(text: str) -> str:
    """Nettoie le texte brut extrait de Gallica."""
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        # Supprimer les lignes vides répétées et les artefacts OCR courts
        if len(line) > 3:
            cleaned.append(line)
    return '\n\n'.join(cleaned)


def save_document(ark: str, titre: str, corps_etat: str, texte: str, metadata: dict):
    """Sauvegarde un document et ses métadonnées."""
    safe_name = ark.replace("/", "_")
    
    # Sauvegarde du texte
    text_path = OUTPUT_DIR / f"{safe_name}.txt"
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(texte)
    
    # Sauvegarde des métadonnées
    meta_path = OUTPUT_DIR / f"{safe_name}.json"
    meta = {
        "ark": ark,
        "titre": titre,
        "corps_etat": corps_etat,
        "source": "gallica_bnf",
        "url": f"https://gallica.bnf.fr/ark:/12148/{ark}",
        "libre_droits": True,
        "nb_caracteres": len(texte),
        **metadata
    }
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    
    print(f"  [OK] Sauvegardé : {text_path.name} ({len(texte):,} caractères)")
    return text_path


def main():
    print("=" * 60)
    print("Collecte Gallica - Ouvrages bâtiment libres de droits")
    print("=" * 60)
    
    results = []
    
    # 1. Volumes Champly
    print(f"\n[1/2] Téléchargement des volumes Champly ({len(CHAMPLY_VOLUMES)} volumes)...")
    for vol in CHAMPLY_VOLUMES:
        print(f"\n  → {vol['titre']}")
        texte = fetch_text(vol['ark'])
        if texte:
            texte_clean = clean_text(texte)
            path = save_document(
                ark=vol['ark'],
                titre=vol['titre'],
                corps_etat="encyclopedie-generale",
                texte=texte_clean,
                metadata={"auteur": "René Champly", "volume": vol['volume'], "date": "1920"}
            )
            results.append({"ark": vol['ark'], "titre": vol['titre'], "path": str(path)})
        else:
            print(f"  [SKIP] Texte non disponible pour {vol['ark']}")
        time.sleep(1)  # Respecter le rate limit Gallica
    
    # 2. Autres ouvrages techniques
    print(f"\n[2/2] Téléchargement des autres ouvrages ({len(AUTRES_OUVRAGES)} ouvrages)...")
    for ouvrage in AUTRES_OUVRAGES:
        print(f"\n  → {ouvrage['titre']}")
        texte = fetch_text(ouvrage['ark'])
        if texte:
            texte_clean = clean_text(texte)
            path = save_document(
                ark=ouvrage['ark'],
                titre=ouvrage['titre'],
                corps_etat=ouvrage['corps_etat'],
                texte=texte_clean,
                metadata={"auteur": ouvrage.get('auteur', 'Inconnu'), "date": ouvrage.get('date', 'N/A')}
            )
            results.append({"ark": ouvrage['ark'], "titre": ouvrage['titre'], "path": str(path)})
        else:
            print(f"  [SKIP] Texte non disponible pour {ouvrage['ark']}")
        time.sleep(1)
    
    # Rapport final
    print(f"\n{'=' * 60}")
    print(f"Collecte terminée : {len(results)} document(s) téléchargé(s)")
    
    index_path = OUTPUT_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Index sauvegardé : {index_path}")
    
    return results


if __name__ == "__main__":
    main()
