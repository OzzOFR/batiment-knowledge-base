"""
Script de collecte des ouvrages techniques bâtiment libres de droits
depuis Internet Archive (archive.org).
Utilise l'API metadata pour lister les fichiers et télécharge le texte OCR (djvu.txt).
"""

import requests
import json
import os
import time
import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "sources" / "gallica"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Catalogue des ouvrages identifiés sur Archive.org
CATALOGUE = [
    {
        "identifier": "NouvelleEncyclopdiePratiqueDuBtiment...ChamplyRenBpt6k97743229",
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 2 (Maçonnerie, Pierre, Brique, Mortiers)",
        "auteur": "René Champly",
        "corps_etat": "maconnerie",
        "date": "1910",
        "source": "Gallica/BnF via Archive.org",
        "libre_droits": True,
    },
    {
        "identifier": "NouvelleEncyclopdiePratiqueDuBtiment...ChamplyRenBpt6k938852q",
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 4 (Charpentes en bois et échafaudages)",
        "auteur": "René Champly",
        "corps_etat": "charpente-couverture",
        "date": "1910",
        "source": "Gallica/BnF via Archive.org",
        "libre_droits": True,
    },
    {
        "identifier": "LivreBtp",
        "titre": "Dictionnaire Technique du Bâtiment et des Travaux Publics",
        "auteur": "Collectif",
        "corps_etat": "encyclopedie-generale",
        "date": "1950",
        "source": "Archive.org",
        "libre_droits": True,
    },
]

ARCHIVE_METADATA_URL = "https://archive.org/metadata/{identifier}"
ARCHIVE_DOWNLOAD_URL = "https://archive.org/download/{identifier}/{filename}"


def get_djvu_filename(identifier: str) -> str | None:
    """Récupère le nom du fichier texte OCR (djvu.txt) depuis les métadonnées."""
    url = ARCHIVE_METADATA_URL.format(identifier=identifier)
    try:
        r = requests.get(url, timeout=20)
        if r.status_code != 200:
            print(f"  [ERREUR] Métadonnées HTTP {r.status_code} pour {identifier}")
            return None
        data = r.json()
        files = data.get("files", [])
        for f in files:
            if f.get("name", "").endswith("_djvu.txt"):
                return f["name"]
        # Fallback: chercher un fichier texte
        for f in files:
            if f.get("format") in ["DjVuTXT", "Plain Text"]:
                return f["name"]
        return None
    except Exception as e:
        print(f"  [ERREUR] {e}")
        return None


def download_text(identifier: str, filename: str) -> str | None:
    """Télécharge le texte OCR d'un document Archive.org."""
    url = ARCHIVE_DOWNLOAD_URL.format(identifier=identifier, filename=filename)
    try:
        r = requests.get(url, timeout=120, allow_redirects=True)
        if r.status_code == 200:
            return r.text
        else:
            print(f"  [ERREUR] Download HTTP {r.status_code}")
            return None
    except Exception as e:
        print(f"  [ERREUR] {e}")
        return None


def clean_text(text: str) -> str:
    """Nettoie le texte OCR : supprime les artefacts, normalise les espaces."""
    # Supprimer les lignes de header BnF/Gallica répétitives
    lines = text.split('\n')
    cleaned = []
    skip_header = True
    for line in lines:
        line = line.strip()
        # Fin du header légal BnF après "NOUVELLE ENCYCLOPÉDIE" ou équivalent
        if skip_header and (
            "ENCYCLOPÉDIE" in line.upper() or
            "DICTIONNAIRE" in line.upper() or
            "TRAITÉ" in line.upper() or
            "CHAPITRE" in line.upper()
        ):
            skip_header = False
        if not skip_header and len(line) > 2:
            cleaned.append(line)
    
    result = '\n'.join(cleaned)
    # Normaliser les espaces multiples
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result


def text_to_markdown(text: str, titre: str, auteur: str, corps_etat: str) -> str:
    """Convertit le texte brut en Markdown structuré avec métadonnées."""
    header = f"""---
titre: {titre}
auteur: {auteur}
corps_etat: {corps_etat}
source: Archive.org / Gallica BnF
libre_droits: true
---

# {titre}

**Auteur :** {auteur}  
**Corps d'état :** {corps_etat}

---

"""
    return header + text


def save_document(ouvrage: dict, texte_clean: str, texte_md: str):
    """Sauvegarde le texte brut, le Markdown et les métadonnées."""
    safe_id = re.sub(r'[^\w\-]', '_', ouvrage['identifier'])[:60]
    
    # Texte brut
    txt_path = OUTPUT_DIR / f"{safe_id}.txt"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(texte_clean)
    
    # Markdown structuré → dans le corpus
    corpus_dir = Path(__file__).parent.parent / "corpus" / ouvrage['corps_etat']
    corpus_dir.mkdir(parents=True, exist_ok=True)
    md_path = corpus_dir / f"{safe_id}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(texte_md)
    
    # Métadonnées JSON
    meta_path = OUTPUT_DIR / f"{safe_id}.json"
    meta = {**ouvrage, "nb_caracteres": len(texte_clean), "fichier_txt": str(txt_path), "fichier_md": str(md_path)}
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    
    print(f"  [OK] {txt_path.name} ({len(texte_clean):,} caractères)")
    return txt_path, md_path


def main():
    print("=" * 65)
    print("Collecte Archive.org — Ouvrages techniques bâtiment")
    print("=" * 65)
    
    results = []
    
    for i, ouvrage in enumerate(CATALOGUE, 1):
        print(f"\n[{i}/{len(CATALOGUE)}] {ouvrage['titre'][:60]}...")
        
        # 1. Récupérer le nom du fichier texte
        filename = get_djvu_filename(ouvrage['identifier'])
        if not filename:
            print(f"  [SKIP] Aucun fichier texte trouvé pour {ouvrage['identifier']}")
            continue
        print(f"  Fichier trouvé : {filename}")
        
        # 2. Télécharger le texte
        texte_brut = download_text(ouvrage['identifier'], filename)
        if not texte_brut:
            print(f"  [SKIP] Téléchargement échoué")
            continue
        
        # 3. Nettoyer et structurer
        texte_clean = clean_text(texte_brut)
        texte_md = text_to_markdown(
            texte_clean,
            ouvrage['titre'],
            ouvrage['auteur'],
            ouvrage['corps_etat']
        )
        
        # 4. Sauvegarder
        txt_path, md_path = save_document(ouvrage, texte_clean, texte_md)
        results.append({
            "identifier": ouvrage['identifier'],
            "titre": ouvrage['titre'],
            "corps_etat": ouvrage['corps_etat'],
            "fichier_txt": str(txt_path),
            "fichier_md": str(md_path),
            "nb_caracteres": len(texte_clean)
        })
        
        time.sleep(2)  # Respecter le rate limit Archive.org
    
    # Sauvegarder l'index
    index_path = OUTPUT_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 65}")
    print(f"Collecte terminée : {len(results)}/{len(CATALOGUE)} document(s) téléchargé(s)")
    total_chars = sum(r['nb_caracteres'] for r in results)
    print(f"Volume total : {total_chars:,} caractères")
    print(f"Index : {index_path}")
    
    return results


if __name__ == "__main__":
    main()
