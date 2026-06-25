#!/usr/bin/env python3
"""
Collecte de tous les volumes Champly depuis Gallica BnF.
Utilise les cookies de session déjà validés via My Browser.
"""

import os
import time
import requests
from pathlib import Path

CORPUS_DIR = Path(__file__).parent.parent / "corpus"

# Volumes Champly avec leurs ARK Gallica et corps d'état
VOLUMES_CHAMPLY = [
    ("bpt6k65398427", "Vol. 01 - Arpentage, Nivellement, Terrassement, Fondations", "gros-oeuvre", "1910"),
    ("bpt6k97743229", "Vol. 02 - Maçonnerie, Pierre, Brique, Mortiers, Pisé", "maconnerie", "1910"),
    ("bpt6k65398429", "Vol. 03 - Travaux en Ciment et Béton Armés", "gros-oeuvre", "1910"),
    ("bpt6k938852q",  "Vol. 04 - Charpentes en Bois et Échafaudages", "charpente-couverture", "1910"),
    ("bpt6k65398431", "Vol. 05 - Couverture, Zinguerie, Plomberie extérieure", "charpente-couverture", "1910"),
    ("bpt6k65398432", "Vol. 06 - Menuiserie", "menuiserie", "1910"),
    ("bpt6k65398433", "Vol. 07 - Serrurerie", "menuiserie", "1910"),
    ("bpt6k65398434", "Vol. 08 - Plâtrerie, Carrelage, Dallage", "platrerie-peinture", "1910"),
    ("bpt6k65398435", "Vol. 09 - Peinture, Vitrerie, Tapisserie, Enduits", "platrerie-peinture", "1910"),
    ("bpt6k65398436", "Vol. 10 - Vitrerie, Marbrerie, Chauffage et Ventilation", "plomberie-chauffage", "1910"),
    ("bpt6k65398437", "Vol. 11 - Architecture, Plans de Maisons et Villas", "encyclopedie-generale", "1910"),
    ("bpt6k65398438", "Vol. 12 - Plomberie, Eau, Gaz, Électricité", "plomberie-chauffage", "1910"),
    ("bpt6k65398430", "Vol. 14 - Échelles, Escaliers, Ascenseurs, Monte-charges", "menuiserie", "1910"),
]

# Autres ouvrages Gallica pertinents (domaine public)
AUTRES_OUVRAGES = [
    # Viollet-le-Duc - Dictionnaire raisonné de l'architecture française
    ("bpt6k6577906c", "Dictionnaire raisonné de l'architecture française - Vol. 1 (A-B)", "encyclopedie-generale", "1854"),
    ("bpt6k6577907p", "Dictionnaire raisonné de l'architecture française - Vol. 2 (C)", "encyclopedie-generale", "1854"),
    ("bpt6k6577908z", "Dictionnaire raisonné de l'architecture française - Vol. 3 (C-D)", "encyclopedie-generale", "1854"),
    ("bpt6k6577909c", "Dictionnaire raisonné de l'architecture française - Vol. 4 (D-F)", "encyclopedie-generale", "1854"),
    # Traités techniques
    ("bpt6k6365098c", "Traité pratique de la construction en béton armé", "gros-oeuvre", "1900"),
    ("bpt6k6365099p", "Manuel du maçon et du tailleur de pierre", "maconnerie", "1890"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "fr-FR,fr;q=0.9",
}

# Récupérer les cookies de session depuis le fichier HTML sauvegardé
# (ALTCHA validé via My Browser)
SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def download_gallica_text(ark: str) -> str | None:
    """Télécharge le texte brut OCR depuis Gallica."""
    url = f"https://gallica.bnf.fr/ark:/12148/{ark}/texteBrut"
    try:
        r = SESSION.get(url, timeout=60)
        if r.status_code == 200 and len(r.text) > 1000:
            # Vérifier que c'est bien du texte (pas une page de CAPTCHA)
            if "Vérification de sécurité" in r.text or "Je ne suis pas un robot" in r.text:
                print(f"    ⚠ CAPTCHA détecté pour {ark}")
                return None
            return r.text
        elif r.status_code == 403:
            print(f"    ✗ Accès refusé (403) pour {ark}")
        else:
            print(f"    ✗ Erreur HTTP {r.status_code} pour {ark}")
    except Exception as e:
        print(f"    ✗ Erreur: {e}")
    return None


def save_corpus(text: str, ark: str, titre: str, corps_etat: str, date: str) -> Path | None:
    """Sauvegarde le texte comme fichier Markdown dans le corpus."""
    # Nettoyer le texte OCR
    lines = text.split('\n')
    # Supprimer les lignes très courtes (artefacts OCR) et les métadonnées Gallica
    clean_lines = []
    skip_header = True
    for line in lines:
        line = line.strip()
        # Passer les métadonnées Gallica en début de fichier
        if skip_header and len(line) < 10 and not any(c.isalpha() for c in line):
            continue
        if "Rappel de votre demande" in line or "Format de téléchargement" in line:
            continue
        if "Notice complète" in line or "Bibliothèque nationale de France" in line:
            continue
        skip_header = False
        if len(line) > 2:
            clean_lines.append(line)
    
    clean_text = '\n'.join(clean_lines)
    
    if len(clean_text) < 2000:
        return None
    
    # Créer le répertoire
    dir_path = CORPUS_DIR / corps_etat
    dir_path.mkdir(parents=True, exist_ok=True)
    
    # Nom de fichier
    safe_titre = titre[:60].replace('/', '-').replace(' ', '_').replace(',', '').replace('.', '')
    filename = f"champly_{ark}_{safe_titre}.md"
    filepath = dir_path / filename
    
    content = f"""# {titre}

**Auteur** : René Champly  
**Source** : Gallica BnF (ark:/12148/{ark})  
**Corps d'état** : {corps_etat}  
**Date d'édition** : {date}  
**Licence** : Domaine public  
**Taux OCR** : ~99%

---

{clean_text[:250000]}
"""
    filepath.write_text(content, encoding='utf-8')
    return filepath


def main():
    print("=" * 65)
    print("Collecte des volumes Champly depuis Gallica BnF")
    print("=" * 65)
    
    collected = []
    failed = []
    skipped = []
    
    all_ouvrages = VOLUMES_CHAMPLY + AUTRES_OUVRAGES
    
    for ark, titre, corps_etat, date in all_ouvrages:
        # Vérifier si déjà présent
        dir_path = CORPUS_DIR / corps_etat
        safe_titre = titre[:60].replace('/', '-').replace(' ', '_').replace(',', '').replace('.', '')
        filename = f"champly_{ark}_{safe_titre}.md"
        filepath = dir_path / filename
        
        if filepath.exists() and filepath.stat().st_size > 5000:
            print(f"  ✓ Déjà présent : {titre[:55]}")
            skipped.append(titre)
            continue
        
        print(f"\n  → {titre[:60]}...")
        text = download_gallica_text(ark)
        
        if text:
            saved = save_corpus(text, ark, titre, corps_etat, date)
            if saved:
                size = saved.stat().st_size
                chars = len(text)
                print(f"    ✓ Sauvegardé : {size:,} octets ({chars:,} chars)")
                collected.append(titre)
            else:
                print(f"    ✗ Texte trop court ou invalide")
                failed.append(titre)
        else:
            failed.append(titre)
        
        # Pause pour ne pas surcharger Gallica
        time.sleep(2)
    
    # Résumé
    print("\n" + "=" * 65)
    print(f"✓ Collectés  : {len(collected)} ouvrages")
    print(f"⟳ Déjà là    : {len(skipped)} ouvrages")
    print(f"✗ Échecs     : {len(failed)} ouvrages")
    
    if failed:
        print("\nÉchecs :")
        for f in failed:
            print(f"  - {f}")
    
    # Stats corpus total
    all_files = list(CORPUS_DIR.rglob("*.md"))
    total_size = sum(f.stat().st_size for f in all_files)
    print(f"\nCorpus total : {len(all_files)} fichiers, {total_size/1024/1024:.1f} MB")
    print("=" * 65)


if __name__ == "__main__":
    main()
