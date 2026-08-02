"""
Phase 1 : Analyser les chunks Champly avec légendes intégrées.
Détecte les patterns "Fig. XX. — description" dans les chunks
et cartographie les ARKs Gallica par volume.
"""
import psycopg2
import psycopg2.extras
import re
import json

# ARKs Gallica des 15 volumes Champly (identifiés précédemment)
CHAMPLY_ARKS = {
    "vol01": "bpt6k9774323q",   # Arpentage, Fondations
    "vol02": "bpt6k97743229",   # Maçonnerie, Pierre, Brique
    "vol03": "bpt6k9774321w",   # Béton armé
    "vol04": "bpt6k97744269",   # Charpentes bois
    "vol05": "bpt6k97744284",   # Charpentes métalliques
    "vol06": "bpt6k9774427q",   # Couverture
    "vol07": "bpt6k65806792",   # Menuiserie
    "vol08": "bpt6k6580680q",   # Serrurerie
    "vol09": "bpt6k65806814",   # Pavages, Peintures
    "vol10": "bpt6k6580763j",   # Vitrerie, Chauffage
    "vol11": "bpt6k6580764z",   # Éclairage
    "vol12": "bpt6k6580765c",   # Plomberie
    "vol13": "bpt6k65807550",   # Salubrité
    "vol14": "bpt6k6580756d",   # Escaliers, Ascenseurs
    "vol15": "bpt6k6580757t",   # Architecture
}

# Pattern de légende intégrée : "Fig. 43. — Pieu en bois ordinaire."
# ou "Fig. 43, 44. — ..." ou "Figs. 43-45. — ..."
LEGENDE_PATTERN = re.compile(
    r'[Ff]ig[s]?\.?\s*(\d+)(?:[,\s\-–]+\d+)*\s*[.—–-]+\s*([^.\n]{10,120})',
    re.UNICODE
)

conn = psycopg2.connect(
    host='localhost', port=5433, dbname='batiment_knowledge',
    user='createk', password='Forge2026Hozzo!'
)
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Récupérer tous les chunks Champly
cur.execute("""
    SELECT id, source, content
    FROM batiment_chunks
    WHERE auteur ILIKE '%champly%'
    ORDER BY source, id
""")
chunks = cur.fetchall()
print(f"Total chunks Champly : {len(chunks)}")

# Analyser les légendes intégrées
results = []
chunks_with_legends = 0

for chunk in chunks:
    source = chunk['source']
    content = chunk['content']
    
    # Extraire le volume depuis le source
    vol_match = re.search(r'vol(\d+)', source)
    if not vol_match:
        continue
    vol_num = f"vol{int(vol_match.group(1)):02d}"
    ark = CHAMPLY_ARKS.get(vol_num)
    if not ark:
        continue
    
    # Chercher les légendes intégrées
    legendes = LEGENDE_PATTERN.findall(content)
    if legendes:
        chunks_with_legends += 1
        for fig_num, legende_text in legendes:
            results.append({
                "chunk_id": chunk['id'],
                "source": source,
                "vol": vol_num,
                "ark": ark,
                "fig_num": int(fig_num),
                "legende": legende_text.strip(),
                "context": content[:200]
            })

print(f"Chunks avec légendes intégrées : {chunks_with_legends}")
print(f"Total légendes extraites : {len(results)}")

# Statistiques par volume
by_vol = {}
for r in results:
    by_vol.setdefault(r['vol'], []).append(r['fig_num'])

print("\n=== Légendes par volume ===")
for vol in sorted(by_vol.keys()):
    figs = sorted(by_vol[vol])
    print(f"  {vol} (ARK: {CHAMPLY_ARKS[vol]}): {len(figs)} légendes — fig. {min(figs)} à {max(figs)}")

# Afficher quelques exemples
print("\n=== Exemples de légendes extraites ===")
for r in results[:10]:
    print(f"  {r['vol']} fig.{r['fig_num']:3d}: {r['legende'][:80]}")

# Sauvegarder le résultat
with open('/tmp/champly_legendes.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nRésultats sauvegardés dans /tmp/champly_legendes.json")

conn.close()
