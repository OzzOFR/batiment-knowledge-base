#!/usr/bin/env python3
"""
Collecte massive des ouvrages BTP français depuis Archive.org.
Inclut : Viollet-le-Duc, Encyclopédie de l'Architecture, traités techniques.
"""

import os
import time
import requests
from pathlib import Path

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
CORPUS_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0)",
    "Accept": "text/plain,text/html;q=0.9,*/*;q=0.8",
}

# Ouvrages à collecter : (identifier, titre, corps_etat, auteur, date)
OUVRAGES = [
    # Encyclopédie de l'Architecture - Constructions modernes (plusieurs tomes)
    ("frapn02-encyclopedie-de-l-architecture-constructions-modernes-tome-10-1937",
     "Encyclopédie de l'Architecture : Constructions modernes - Tome X",
     "encyclopedie-generale", "Collectif", "1938"),
    ("frapn02-encyclopedie-de-l-architecture-constructions-modernes-tome-7-1935",
     "Encyclopédie de l'Architecture : Constructions modernes - Tome VII",
     "encyclopedie-generale", "Collectif", "1935"),
    ("frapn02-encyclopedie-de-l-architecture-constructions-modernes-tome-4-1932",
     "Encyclopédie de l'Architecture : Constructions modernes - Tome IV",
     "encyclopedie-generale", "Collectif", "1932"),
    # Dictionnaire raisonné de l'architecture française - Viollet-le-Duc
    ("dictionairerais01sabigoog",
     "Dictionnaire raisonné de l'architecture française du XIe au XVIe siècle - Vol. 1",
     "encyclopedie-generale", "Viollet-le-Duc", "1854"),
    ("dictionairerais02sabigoog",
     "Dictionnaire raisonné de l'architecture française du XIe au XVIe siècle - Vol. 2",
     "encyclopedie-generale", "Viollet-le-Duc", "1854"),
    ("dictionairerais03sabigoog",
     "Dictionnaire raisonné de l'architecture française du XIe au XVIe siècle - Vol. 3",
     "encyclopedie-generale", "Viollet-le-Duc", "1854"),
    ("dictionairerais04sabigoog",
     "Dictionnaire raisonné de l'architecture française du XIe au XVIe siècle - Vol. 4",
     "encyclopedie-generale", "Viollet-le-Duc", "1854"),
    # Catalogue peinture bâtiment
    ("LeFrancCCA14668",
     "Catalogue pour la peinture en bâtiment et l'industrie : couleurs, vernis, siccatifs",
     "platrerie-peinture", "Le Franc", "1931"),
    # Installations hydro-électriques
    ("installations-hydroel-trabeka",
     "Installations Hydro-électriques construites de 1925 à 1940",
     "electricite", "Collectif", "1940"),
]

# Recherche dynamique d'autres ouvrages pertinents
SEARCH_QUERIES = [
    ("traite+maconnerie+pierre+brique", "maconnerie"),
    ("manuel+charpentier+couvreur+toiture", "charpente-couverture"),
    ("plomberie+sanitaire+chauffage+installation", "plomberie-chauffage"),
    ("menuiserie+bois+portes+fenetres+parquet", "menuiserie"),
    ("electricite+installation+eclairage+batiment", "electricite"),
    ("beton+arme+ciment+construction+fondation", "gros-oeuvre"),
    ("enduit+platre+peinture+decoration+interieur", "platrerie-peinture"),
    ("couverture+zinc+ardoise+tuile+toiture", "charpente-couverture"),
    ("serrurerie+ferronnerie+grilles+portes", "menuiserie"),
    ("carrelage+pavage+revetement+sol", "platrerie-peinture"),
]


def search_archive_org(query: str, rows: int = 10) -> list[dict]:
    """Recherche des ouvrages sur Archive.org."""
    url = (
        f"https://archive.org/advancedsearch.php?"
        f"q=language%3Afre+AND+mediatype%3Atexts+AND+date%3A%5B1850+TO+1950%5D+AND+({query})"
        f"&fl[]=identifier,title,date,creator&rows={rows}&output=json&sort[]=downloads+desc"
    )
    try:
        r = requests.get(url, timeout=20)
        return r.json().get('response', {}).get('docs', [])
    except Exception as e:
        print(f"  Erreur recherche: {e}")
        return []


def get_text_from_archive(identifier: str) -> str | None:
    """Télécharge le texte OCR depuis Archive.org."""
    # Lister les fichiers disponibles
    meta_url = f"https://archive.org/metadata/{identifier}"
    try:
        r = requests.get(meta_url, timeout=20)
        if r.status_code != 200:
            return None
        
        files = r.json().get('files', [])
        
        # Chercher un fichier texte (DjVuTXT, txt, _djvu.txt)
        text_files = []
        for f in files:
            name = f.get('name', '')
            if name.endswith('_djvu.txt') or name.endswith('.txt'):
                text_files.append(name)
        
        if not text_files:
            # Essayer l'URL directe
            direct_url = f"https://archive.org/stream/{identifier}/{identifier}_djvu.txt"
            r2 = requests.get(direct_url, headers=HEADERS, timeout=30)
            if r2.status_code == 200 and len(r2.text) > 500:
                return r2.text
            return None
        
        # Télécharger le premier fichier texte trouvé
        text_file = text_files[0]
        text_url = f"https://archive.org/download/{identifier}/{text_file}"
        r3 = requests.get(text_url, headers=HEADERS, timeout=60)
        if r3.status_code == 200 and len(r3.text) > 500:
            return r3.text
        
    except Exception as e:
        print(f"  Erreur téléchargement {identifier}: {e}")
    return None


def save_document(text: str, identifier: str, titre: str, corps_etat: str, 
                  auteur: str, date: str) -> Path | None:
    """Sauvegarde un document comme Markdown."""
    # Nettoyer le texte
    lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 3]
    clean = '\n'.join(lines)
    
    if len(clean) < 1000:
        return None
    
    # Nom de fichier sécurisé
    safe_id = identifier[:50].replace('/', '_').replace(' ', '_')
    filename = f"{safe_id}_{corps_etat}.md"
    filepath = CORPUS_DIR / corps_etat / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    content = f"""# {titre}

**Auteur** : {auteur}  
**Source** : Archive.org ({identifier})  
**Corps d'état** : {corps_etat}  
**Date** : {date}  
**Licence** : Domaine public

---

{clean[:200000]}
"""
    filepath.write_text(content, encoding='utf-8')
    return filepath


def main():
    print("=" * 60)
    print("Collecte massive des ouvrages BTP français — Archive.org")
    print("=" * 60)
    
    collected = []
    failed = []
    
    # Phase 1 : Ouvrages ciblés
    print("\n--- Phase 1 : Ouvrages ciblés ---")
    for identifier, titre, corps_etat, auteur, date in OUVRAGES:
        # Vérifier si déjà présent
        safe_id = identifier[:50].replace('/', '_').replace(' ', '_')
        filename = f"{safe_id}_{corps_etat}.md"
        filepath = CORPUS_DIR / corps_etat / filename
        if filepath.exists() and filepath.stat().st_size > 5000:
            print(f"  ✓ Déjà présent : {titre[:50]}")
            collected.append(titre)
            continue
        
        print(f"\n  → {titre[:60]}...")
        text = get_text_from_archive(identifier)
        if text:
            saved = save_document(text, identifier, titre, corps_etat, auteur, date)
            if saved:
                size = saved.stat().st_size
                print(f"    ✓ Sauvegardé ({size:,} octets, {len(text):,} chars)")
                collected.append(titre)
            else:
                print(f"    ✗ Texte trop court")
                failed.append(titre)
        else:
            print(f"    ✗ Téléchargement échoué")
            failed.append(titre)
        time.sleep(1.5)
    
    # Phase 2 : Recherche dynamique
    print("\n--- Phase 2 : Recherche dynamique ---")
    seen_ids = set(o[0] for o in OUVRAGES)
    
    for query, corps_etat in SEARCH_QUERIES:
        print(f"\n  Recherche: {query[:40]}...")
        docs = search_archive_org(query, rows=5)
        
        for doc in docs[:3]:
            identifier = doc.get('identifier', '')
            titre = doc.get('title', 'Sans titre')[:80]
            date = str(doc.get('date', ''))[:4]
            auteur = doc.get('creator', 'Collectif')
            if isinstance(auteur, list):
                auteur = ', '.join(auteur)
            
            if identifier in seen_ids:
                continue
            seen_ids.add(identifier)
            
            # Vérifier pertinence du titre
            keywords = ['maçon', 'charpent', 'plomberi', 'menuiser', 'électric', 
                       'bâtiment', 'construct', 'béton', 'enduit', 'couvertur',
                       'toiture', 'carrel', 'peintur', 'vitreri', 'serrurer',
                       'chauffage', 'fondation', 'terrassement', 'maison', 'villa',
                       'architecture', 'travaux', 'artisan', 'ouvrier']
            if not any(k in titre.lower() for k in keywords):
                continue
            
            print(f"    → {titre[:55]}... [{date}]")
            text = get_text_from_archive(identifier)
            if text and len(text) > 2000:
                saved = save_document(text, identifier, titre, corps_etat, auteur, date)
                if saved:
                    print(f"      ✓ Sauvegardé ({saved.stat().st_size:,} octets)")
                    collected.append(titre)
            time.sleep(1)
    
    # Résumé
    print("\n" + "=" * 60)
    print(f"✓ Collectés : {len(collected)} ouvrages")
    print(f"✗ Échecs    : {len(failed)} ouvrages")
    
    # Lister les fichiers du corpus
    all_files = list(CORPUS_DIR.rglob("*.md"))
    total_size = sum(f.stat().st_size for f in all_files)
    print(f"\nCorpus total : {len(all_files)} fichiers, {total_size/1024/1024:.1f} MB")
    print("=" * 60)


if __name__ == "__main__":
    main()
