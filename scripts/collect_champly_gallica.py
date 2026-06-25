#!/usr/bin/env python3
"""
Collecte des volumes de la Nouvelle Encyclopédie Pratique du Bâtiment de René Champly
depuis Gallica (BnF) via les identifiants ARK du catalogue BnF.
"""

import os
import time
import requests
from pathlib import Path

# Répertoire de sortie
CORPUS_DIR = Path(__file__).parent.parent / "corpus"
CORPUS_DIR.mkdir(exist_ok=True)

# Volumes Champly identifiés dans le catalogue BnF
# Format: (ark_id, volume_num, titre_court, corps_etat)
CHAMPLY_VOLUMES = [
    # Volumes numérisés (marqués NUMS dans le catalogue)
    ("bpt6k97743229", "02", "Maçonnerie - Pierre, Brique, Mortiers, Pisé", "maconnerie"),
    ("bpt6k938852q",  "04", "Charpentes en bois et échafaudages", "charpente-couverture"),
    ("bpt6k65398429", "03", "Travaux en ciment et béton armés", "gros-oeuvre"),
    ("bpt6k65398430", "14", "Échelles, escaliers, ascenseurs, monte-charges", "menuiserie"),
    # Volumes à tenter depuis les ARK catalogue
    ("cb31926615m",   "01", "Arpentage, nivellement, terrassement, fondations", "gros-oeuvre"),
    ("cb31926636k",   "03", "Travaux en ciment et béton armés", "gros-oeuvre"),
    ("cb31926624k",   "14", "Escaliers, ascenseurs, monte-charges", "menuiserie"),
    ("cb438226971",   "10", "Vitrerie, Marbrerie, Chauffage et ventilation", "plomberie-chauffage"),
    ("cb31926609p",   "11", "Architecture, plans de maisons et villas", "encyclopedie-generale"),
    ("cb319266237",   "12", "Plomberie, eau, water-closets, paratonnerres", "plomberie-chauffage"),
    ("cb31926627m",   "15", "Architecture, plans de maisons et villas (2)", "encyclopedie-generale"),
    ("cb319266268",   "09", "Pavages, carrelages, plafonds, enduits, peintures", "platrerie-peinture"),
]

# URLs à tester pour le téléchargement du texte OCR
GALLICA_TEXT_URLS = [
    "https://gallica.bnf.fr/ark:/12148/{ark}/texteBrut",
    "https://gallica.bnf.fr/ark:/12148/{ark}.texteBrut",
    "https://gallica.bnf.fr/services/ajax/action/download/ark:/12148/{ark}/f1.texteImage",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0; +https://github.com/OzzOFR/batiment-knowledge-base)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "fr-FR,fr;q=0.9",
}

def download_gallica_text(ark_id: str) -> str | None:
    """Tente de télécharger le texte OCR d'un document Gallica."""
    # Essayer les différentes URLs
    urls_to_try = [
        f"https://gallica.bnf.fr/ark:/12148/{ark_id}/texteBrut",
        f"https://gallica.bnf.fr/ark:/12148/{ark_id}.texteBrut",
        f"https://gallica.bnf.fr/ark:/12148/{ark_id}/f1.texteBrut",
    ]
    
    for url in urls_to_try:
        try:
            r = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
            if r.status_code == 200 and len(r.text) > 1000:
                # Vérifier que c'est bien du texte (pas du HTML de captcha)
                if "captcha" not in r.text.lower() and "robot" not in r.text.lower():
                    return r.text
            time.sleep(1)
        except Exception as e:
            print(f"  Erreur {url}: {e}")
            continue
    return None


def clean_text(text: str) -> str:
    """Nettoie le texte OCR."""
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        # Supprimer les lignes trop courtes ou vides
        if len(line) > 3:
            cleaned.append(line)
    return '\n'.join(cleaned)


def save_as_markdown(text: str, volume_num: str, titre: str, corps_etat: str, ark_id: str) -> Path:
    """Sauvegarde le texte comme fichier Markdown structuré."""
    filename = f"champly_vol{volume_num.zfill(2)}_{corps_etat}.md"
    filepath = CORPUS_DIR / corps_etat / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    content = f"""# Nouvelle Encyclopédie Pratique du Bâtiment — Volume {volume_num}
## {titre}

**Auteur** : René Champly  
**Source** : Gallica BnF (ark:/12148/{ark_id})  
**Corps d'état** : {corps_etat}  
**Domaine** : Bâtiment — Techniques de construction  
**Époque** : Début XXe siècle (1910-1940)  
**Licence** : Domaine public

---

{clean_text(text)}
"""
    filepath.write_text(content, encoding='utf-8')
    return filepath


def main():
    print("=" * 60)
    print("Collecte des volumes Champly depuis Gallica BnF")
    print("=" * 60)
    
    success = 0
    failed = []
    
    for ark_id, vol_num, titre, corps_etat in CHAMPLY_VOLUMES:
        print(f"\n[Vol. {vol_num}] {titre[:50]}...")
        print(f"  ARK: {ark_id}")
        
        # Vérifier si déjà téléchargé
        filename = f"champly_vol{vol_num.zfill(2)}_{corps_etat}.md"
        filepath = CORPUS_DIR / corps_etat / filename
        if filepath.exists() and filepath.stat().st_size > 5000:
            print(f"  ✓ Déjà présent ({filepath.stat().st_size:,} octets)")
            success += 1
            continue
        
        text = download_gallica_text(ark_id)
        if text:
            saved = save_as_markdown(text, vol_num, titre, corps_etat, ark_id)
            size = saved.stat().st_size
            print(f"  ✓ Téléchargé et sauvegardé ({size:,} octets)")
            success += 1
        else:
            print(f"  ✗ Échec du téléchargement")
            failed.append((vol_num, titre, ark_id))
        
        time.sleep(2)  # Respecter le serveur Gallica
    
    print("\n" + "=" * 60)
    print(f"Résultat: {success}/{len(CHAMPLY_VOLUMES)} volumes collectés")
    if failed:
        print(f"\nVolumes non récupérés ({len(failed)}):")
        for vol, titre, ark in failed:
            print(f"  - Vol. {vol}: {titre} ({ark})")
    print("=" * 60)


if __name__ == "__main__":
    main()
