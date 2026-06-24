"""
Collecte massive de tous les volumes de la Nouvelle Encyclopédie Pratique
du Bâtiment de René Champly depuis Gallica (BnF) et Archive.org,
ainsi que d'autres ouvrages techniques BTP libres de droits.
"""

import os
import json
import time
import re
import requests
from pathlib import Path

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
SOURCES_DIR = Path(__file__).parent.parent / "sources" / "gallica"

# ─── Catalogue complet des volumes Champly (ark BnF identifiés) ──────────────
CHAMPLY_VOLUMES = [
    {
        "ark": "bpt6k65806780",
        "volume": 1,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 1 (Arpentage, Nivellement, Terrassements, Fondations)",
        "corps_etat": "gros-oeuvre",
        "sujets": ["fondations", "terrassements", "arpentage", "nivellement"]
    },
    {
        "ark": "bpt6k9774322",
        "volume": 2,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 2 (Maçonnerie, Pierre, Brique, Mortiers)",
        "corps_etat": "maconnerie",
        "sujets": ["maçonnerie", "pierre", "brique", "mortier", "ciment"]
    },
    {
        "ark": "bpt6k65806791",
        "volume": 3,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 3 (Béton armé, Constructions métalliques)",
        "corps_etat": "gros-oeuvre",
        "sujets": ["béton armé", "constructions métalliques", "fer", "acier"]
    },
    {
        "ark": "bpt6k9388520",
        "volume": 4,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 4 (Charpentes en bois et échafaudages)",
        "corps_etat": "charpente-couverture",
        "sujets": ["charpente", "bois", "échafaudage", "assemblages"]
    },
    {
        "ark": "bpt6k65806803",
        "volume": 5,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 5 (Couverture, Zinguerie, Étanchéité)",
        "corps_etat": "charpente-couverture",
        "sujets": ["couverture", "tuiles", "ardoises", "zinc", "étanchéité"]
    },
    {
        "ark": "bpt6k9774427q",
        "volume": 6,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 6 (Menuiserie, Serrurerie)",
        "corps_etat": "menuiserie",
        "sujets": ["menuiserie", "portes", "fenêtres", "parquets", "serrurerie"]
    },
    {
        "ark": "bpt6k65806792",
        "volume": 7,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 7 (Plâtrerie, Peinture, Vitrerie)",
        "corps_etat": "platrerie-peinture",
        "sujets": ["plâtrerie", "peinture", "vitrerie", "enduits", "badigeons"]
    },
    {
        "ark": "bpt6k6580680q",
        "volume": 8,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 8 (Plomberie, Chauffage, Ventilation)",
        "corps_etat": "plomberie-chauffage",
        "sujets": ["plomberie", "chauffage", "ventilation", "canalisations", "sanitaires"]
    },
    {
        "ark": "bpt6k65806814",
        "volume": 9,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 9 (Électricité, Éclairage, Ascenseurs)",
        "corps_etat": "electricite",
        "sujets": ["électricité", "éclairage", "ascenseurs", "installations électriques"]
    },
    {
        "ark": "bpt6k6580763j",
        "volume": 10,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 10 (Carrelage, Dallage, Revêtements)",
        "corps_etat": "platrerie-peinture",
        "sujets": ["carrelage", "dallage", "revêtements", "mosaïque", "faïence"]
    },
    {
        "ark": "bpt6k65806826",
        "volume": 11,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 11 (Devis, Marchés, Législation)",
        "corps_etat": "encyclopedie-generale",
        "sujets": ["devis", "marchés", "législation", "contrats", "réglementation"]
    },
    {
        "ark": "bpt6k6580765c",
        "volume": 12,
        "titre": "Nouvelle Encyclopédie Pratique du Bâtiment - Vol. 12 (Jardins, Clôtures, Voirie)",
        "corps_etat": "gros-oeuvre",
        "sujets": ["jardins", "clôtures", "voirie", "pavage", "espaces extérieurs"]
    },
]

# ─── Autres ouvrages BTP libres de droits sur Archive.org ────────────────────
AUTRES_OUVRAGES = [
    # --- Déjà collectés ---
    {
        "identifier": "encyclopediedela62unse",
        "titre": "Encyclopédie de l'Architecture et de la Construction - Vol. 6",
        "corps_etat": "encyclopedie-generale",
        "auteur": "Collectif",
        "date": "1888",
        "source": "Archive.org / Getty Research Institute"
    },
    {
        "identifier": "encyclopediedarc34unse",
        "titre": "Encyclopédie d'Architecture - Vol. 3-4 (1853-1854)",
        "corps_etat": "encyclopedie-generale",
        "auteur": "Collectif",
        "date": "1853",
        "source": "Archive.org / Getty Research Institute"
    },
    # --- Nouveaux ouvrages ---
    {
        "identifier": "guide-chaux-hydro-bd",
        "titre": "Les Enduits Intérieur et Extérieur à la Chaux - Guide pratique",
        "corps_etat": "platrerie-peinture",
        "auteur": "Collectif",
        "date": "2010",
        "source": "Archive.org",
        "sujets": ["enduits", "chaux", "crépi", "façade", "murs"]
    },
    {
        "identifier": "GuideSurelevation",
        "titre": "Concevoir et Construire un étage en ossature bois (Surélévation)",
        "corps_etat": "charpente-couverture",
        "auteur": "Collectif",
        "date": "2015",
        "source": "Archive.org",
        "sujets": ["surélévation", "ossature bois", "charpente", "construction bois"]
    },
    {
        "identifier": "17507-atex-btc-mayotte",
        "titre": "Ouvrages en Maçonnerie de Blocs de Terre Comprimée - Dossier Technique",
        "corps_etat": "maconnerie",
        "auteur": "CSTB",
        "date": "2017",
        "source": "Archive.org / CSTB",
        "sujets": ["maçonnerie", "terre comprimée", "BTC", "blocs", "constructionécologique"]
    },
    {
        "identifier": "baikov-stronguine-calcul-des-structures-mir-1984",
        "titre": "Calcul des Structures - Manuel technique",
        "corps_etat": "gros-oeuvre",
        "auteur": "Baïkov, Stronguine",
        "date": "1984",
        "source": "Archive.org / Éditions Mir",
        "sujets": ["calcul de structures", "béton armé", "résistance des matériaux", "statique"]
    },
]


def clean_ocr_text(text: str) -> str:
    """Nettoie le texte OCR brut."""
    # Supprimer les lignes très courtes (artefacts OCR)
    lines = text.split('\n')
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) > 3 or stripped == '':
            clean_lines.append(line)
    text = '\n'.join(clean_lines)
    # Normaliser les espaces multiples
    text = re.sub(r' {3,}', '  ', text)
    # Supprimer les caractères parasites courants OCR
    text = re.sub(r'[|]{2,}', '', text)
    return text.strip()


def download_gallica_text(ark: str) -> str | None:
    """Télécharge le texte OCR d'un document Gallica via l'API."""
    # URL de l'API texte Gallica
    url = f"https://gallica.bnf.fr/ark:/12148/{ark}.texteBrut"
    headers = {"User-Agent": "Mozilla/5.0 (research bot, contact: research@example.com)"}
    
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.text) > 1000:
            return clean_ocr_text(r.text)
        else:
            print(f"    Gallica {ark}: HTTP {r.status_code}, taille: {len(r.text)}")
            return None
    except Exception as e:
        print(f"    Erreur Gallica {ark}: {e}")
        return None


def download_archive_org_text(identifier: str) -> str | None:
    """Télécharge le texte OCR d'un document Archive.org."""
    # Récupérer la liste des fichiers
    meta_url = f"https://archive.org/metadata/{identifier}"
    try:
        r = requests.get(meta_url, timeout=30)
        if r.status_code != 200:
            return None
        meta = r.json()
        files = meta.get("files", [])
        
        # Chercher le fichier texte (DjVuTXT ou _djvu.txt)
        txt_file = None
        for f in files:
            name = f.get("name", "")
            if name.endswith("_djvu.txt") or name.endswith(".txt"):
                txt_file = name
                break
        
        if not txt_file:
            print(f"    Pas de fichier texte pour {identifier}")
            return None
        
        txt_url = f"https://archive.org/download/{identifier}/{txt_file}"
        r2 = requests.get(txt_url, timeout=60)
        if r2.status_code == 200 and len(r2.text) > 1000:
            return clean_ocr_text(r2.text)
        return None
    except Exception as e:
        print(f"    Erreur Archive.org {identifier}: {e}")
        return None


def save_as_markdown(text: str, meta: dict, output_path: Path):
    """Sauvegarde le texte comme fichier Markdown avec front-matter."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    front_matter = f"""---
titre: {meta.get('titre', 'N/A')}
auteur: {meta.get('auteur', 'René Champly')}
date: {meta.get('date', '1910')}
corps_etat: {meta.get('corps_etat', 'encyclopedie-generale')}
source: {meta.get('source', 'Gallica BnF / Archive.org')}
libre_droits: true
volume: {meta.get('volume', '')}
sujets: {', '.join(meta.get('sujets', []))}
---

# {meta.get('titre', 'Document')}

**Auteur :** {meta.get('auteur', 'René Champly')}  
**Corps d'état :** {meta.get('corps_etat', 'N/A')}  
**Source :** {meta.get('source', 'Gallica BnF')}  
**Sujets :** {', '.join(meta.get('sujets', []))}

---

"""
    output_path.write_text(front_matter + text, encoding='utf-8')
    print(f"    Sauvegardé : {output_path} ({len(text):,} caractères)")


def collect_champly_volumes():
    """Collecte tous les volumes Champly disponibles."""
    print("\n" + "="*65)
    print("Collecte des volumes Champly (Gallica BnF)")
    print("="*65)
    
    collected = 0
    for vol in CHAMPLY_VOLUMES:
        ark = vol["ark"]
        vol_num = vol["volume"]
        print(f"\n  Vol. {vol_num:02d} — {vol['titre'][:55]}...")
        
        # Vérifier si déjà téléchargé
        output_path = CORPUS_DIR / vol["corps_etat"] / f"champly_vol{vol_num:02d}_{ark}.md"
        if output_path.exists():
            print(f"    Déjà présent, ignoré.")
            collected += 1
            continue
        
        # Essayer Gallica d'abord
        text = download_gallica_text(ark)
        
        if text and len(text) > 5000:
            meta = {**vol, "auteur": "René Champly", "date": "1910",
                    "source": f"Gallica BnF (ark:/12148/{ark})"}
            save_as_markdown(text, meta, output_path)
            collected += 1
        else:
            print(f"    Gallica indisponible, tentative Archive.org...")
            # Essayer Archive.org avec l'identifiant correspondant
            archive_id = f"NouvelleEncyclopdiePratiqueDuBtiment___ChamplyRenBpt6k{ark}"
            text2 = download_archive_org_text(archive_id)
            if text2 and len(text2) > 5000:
                meta = {**vol, "auteur": "René Champly", "date": "1910",
                        "source": f"Archive.org ({archive_id})"}
                save_as_markdown(text2, meta, output_path)
                collected += 1
            else:
                print(f"    Volume {vol_num} non disponible en ligne.")
        
        time.sleep(2)  # Respecter les serveurs
    
    print(f"\n  Total collecté : {collected}/{len(CHAMPLY_VOLUMES)} volumes")
    return collected


def collect_autres_ouvrages():
    """Collecte les autres ouvrages BTP depuis Archive.org."""
    print("\n" + "="*65)
    print("Collecte des autres ouvrages BTP (Archive.org)")
    print("="*65)
    
    collected = 0
    for ouvrage in AUTRES_OUVRAGES:
        identifier = ouvrage["identifier"]
        print(f"\n  {ouvrage['titre'][:60]}...")
        
        output_path = CORPUS_DIR / ouvrage["corps_etat"] / f"{identifier}.md"
        if output_path.exists():
            print(f"    Déjà présent, ignoré.")
            collected += 1
            continue
        
        text = download_archive_org_text(identifier)
        if text and len(text) > 5000:
            save_as_markdown(text, ouvrage, output_path)
            collected += 1
        else:
            print(f"    Non disponible.")
        
        time.sleep(2)
    
    print(f"\n  Total collecté : {collected}/{len(AUTRES_OUVRAGES)} ouvrages")
    return collected


if __name__ == "__main__":
    print("="*65)
    print("Collecte massive — Base de connaissances Bâtiment")
    print("="*65)
    
    c1 = collect_champly_volumes()
    c2 = collect_autres_ouvrages()
    
    # Résumé
    md_files = list(CORPUS_DIR.rglob("*.md"))
    total_chars = sum(f.stat().st_size for f in md_files)
    
    print(f"\n{'='*65}")
    print(f"Collecte terminée !")
    print(f"  Fichiers Markdown dans le corpus : {len(md_files)}")
    print(f"  Taille totale : {total_chars/1024/1024:.1f} MB")
    print(f"  Répertoire : {CORPUS_DIR}")
