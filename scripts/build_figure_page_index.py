"""
Phase 2 : Construire l'index figure→page Gallica pour les 15 volumes Champly.

Stratégie :
- Le texte OCR contient les légendes "Fig. X. — description" à des numéros de ligne précis
- Le nombre de pages Gallica est connu (dans l'en-tête du fichier : "Nombre total de vues : N")
- On calcule : page_gallica = round(ligne_fig / total_lignes * total_pages) + offset_couverture
- L'URL IIIF de l'image sera : https://gallica.bnf.fr/iiif/ark:/12148/{ark}/f{page}/full/800,/0/native.jpg
"""
import re
import json
import os

CORPUS_DIR = "/home/ubuntu/batiment-knowledge-base/corpus/champly"

CHAMPLY_ARKS = {
    "vol01": ("bpt6k9774323q",  "Arpentage, Fondations"),
    "vol02": ("bpt6k97743229",  "Maçonnerie, Pierre, Brique"),
    "vol03": ("bpt6k9774321w",  "Béton armé"),
    "vol04": ("bpt6k97744269",  "Charpentes bois"),
    "vol05": ("bpt6k97744284",  "Charpentes métalliques"),
    "vol06": ("bpt6k9774427q",  "Couverture"),
    "vol07": ("bpt6k65806792",  "Menuiserie"),
    "vol08": ("bpt6k6580680q",  "Serrurerie"),
    "vol09": ("bpt6k65806814",  "Pavages, Peintures"),
    "vol10": ("bpt6k6580763j",  "Vitrerie, Chauffage"),
    "vol11": ("bpt6k6580764z",  "Éclairage"),
    "vol12": ("bpt6k6580765c",  "Plomberie"),
    "vol13": ("bpt6k65807550",  "Salubrité"),
    "vol14": ("bpt6k6580756d",  "Escaliers, Ascenseurs"),
    "vol15": ("bpt6k6580757t",  "Architecture"),
}

# Pattern légende intégrée
LEGENDE_RE = re.compile(
    r'^(Fig[s]?\.?\s*(\d+)(?:[,\s\-–]+\d+)*\s*[.—–-]+\s*.{10,120})',
    re.MULTILINE | re.UNICODE
)
# Pattern nombre de pages dans l'en-tête
PAGES_RE = re.compile(r'Nombre total de vues\s*:\s*(\d+)')

index = {}  # {vol: [{fig_num, legende, line_num, page_gallica, ark, url_iiif}]}

for vol_key, (ark, titre) in CHAMPLY_ARKS.items():
    # Trouver le fichier corpus
    candidates = [f for f in os.listdir(CORPUS_DIR) if vol_key in f and f.endswith('.md')]
    if not candidates:
        print(f"  {vol_key}: fichier non trouvé")
        continue
    filepath = os.path.join(CORPUS_DIR, candidates[0])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Extraire le nombre total de pages
    pages_match = PAGES_RE.search(content)
    total_pages = int(pages_match.group(1)) if pages_match else 150
    total_lines = len(lines)
    
    # Offset : les premières pages sont couverture/titre (~8-12 pages)
    # On estime l'offset en cherchant la première figure
    offset = 8  # pages de couverture/titre estimées
    
    # Trouver toutes les légendes avec leur numéro de ligne
    vol_figures = []
    for line_num, line in enumerate(lines):
        m = re.match(r'(Fig[s]?\.?\s*(\d+)(?:[,\s\-–]+\d+)*\s*[.—–\-]+\s*)(.{10,120})', line.strip())
        if m:
            fig_num = int(re.search(r'\d+', m.group(1)).group())
            legende = (m.group(1) + m.group(3)).strip()
            
            # Calculer la page Gallica
            # Formule : page = offset + round((line_num / total_lines) * (total_pages - offset))
            page_gallica = offset + round((line_num / total_lines) * (total_pages - offset))
            page_gallica = max(offset + 1, min(total_pages, page_gallica))
            
            url_iiif = f"https://gallica.bnf.fr/iiif/ark:/12148/{ark}/f{page_gallica}/full/800,/0/native.jpg"
            url_page = f"https://gallica.bnf.fr/ark:/12148/{ark}/f{page_gallica}.item"
            
            vol_figures.append({
                "fig_num": fig_num,
                "legende": legende[:150],
                "line_num": line_num,
                "page_gallica": page_gallica,
                "total_pages": total_pages,
                "ark": ark,
                "url_iiif": url_iiif,
                "url_page": url_page,
                "vol": vol_key,
                "titre_vol": titre
            })
    
    index[vol_key] = vol_figures
    print(f"  {vol_key} ({titre[:30]}): {len(vol_figures)} figures, {total_pages} pages")
    # Afficher quelques exemples
    for fig in vol_figures[:3]:
        print(f"    fig.{fig['fig_num']:3d} → page {fig['page_gallica']:3d} | {fig['legende'][:60]}")

# Sauvegarder l'index complet
total = sum(len(v) for v in index.values())
print(f"\nTotal : {total} figures indexées sur {len(index)} volumes")

with open('/tmp/champly_figure_page_index.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
print("Index sauvegardé dans /tmp/champly_figure_page_index.json")
