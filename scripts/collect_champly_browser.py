#!/usr/bin/env python3
"""
Collecte des 17 volumes Champly depuis Gallica via les ARK extraits.
Ce script est utilisé en combinaison avec le navigateur My Browser qui a les cookies ALTCHA.
Les textes sont récupérés via le navigateur et sauvegardés dans le corpus.
"""

import json
import os

# Les 17 ARK extraits depuis Gallica
VOLUMES = [
    {"ark": "bpt6k9774321w", "vol": 1, "sujet": "Arpentage, Nivellement, Terrassement, Fondations", "corps_etat": "gros-oeuvre"},
    {"ark": "bpt6k6580763j", "vol": 10, "sujet": "Vitrerie, Marbrerie, Chauffage et Ventilation", "corps_etat": "plomberie-chauffage"},
    {"ark": "bpt6k65807550", "vol": 11, "sujet": "Architecture, Plans de Maisons et Villas", "corps_etat": "encyclopedie-generale"},
    {"ark": "bpt6k65806814", "vol": 12, "sujet": "Plomberie, Eau, Gaz, Électricité", "corps_etat": "plomberie-chauffage"},
    {"ark": "bpt6k938837x",  "vol": 13, "sujet": "Galvanobie, Installations diverses", "corps_etat": "encyclopedie-generale"},
    {"ark": "bpt6k65806792", "vol": 14, "sujet": "Échelles, Escaliers, Ascenseurs", "corps_etat": "menuiserie"},
    {"ark": "bpt6k97744269", "vol": 15, "sujet": "Devis, Métrés, Marchés de Travaux", "corps_etat": "encyclopedie-generale"},
    {"ark": "bpt6k6580765c", "vol": 16, "sujet": "Législation du Bâtiment", "corps_etat": "encyclopedie-generale"},
    {"ark": "bpt6k938852q",  "vol": 4,  "sujet": "Charpentes en Bois et Échafaudages", "corps_etat": "charpente-couverture"},
    {"ark": "bpt6k9774323q", "vol": 3,  "sujet": "Travaux en Ciment et Béton Armés", "corps_etat": "gros-oeuvre"},
    {"ark": "bpt6k6580680q", "vol": 5,  "sujet": "Couverture, Zinguerie, Plomberie extérieure", "corps_etat": "charpente-couverture"},
    {"ark": "bpt6k6580756d", "vol": 6,  "sujet": "Menuiserie", "corps_etat": "menuiserie"},
    {"ark": "bpt6k9774427q", "vol": 7,  "sujet": "Serrurerie", "corps_etat": "menuiserie"},
    {"ark": "bpt6k97744284", "vol": 8,  "sujet": "Plâtrerie, Carrelage, Dallage", "corps_etat": "platrerie-peinture"},
    {"ark": "bpt6k6580757t", "vol": 9,  "sujet": "Peinture, Vitrerie, Tapisserie, Enduits", "corps_etat": "platrerie-peinture"},
    {"ark": "bpt6k6580764z", "vol": 2,  "sujet": "Maçonnerie, Pierre, Brique, Mortiers, Pisé", "corps_etat": "maconnerie"},
    {"ark": "bpt6k97743229", "vol": 17, "sujet": "Maçonnerie (édition complémentaire)", "corps_etat": "maconnerie"},
]

# Vérifier quels volumes sont déjà collectés
corpus_dir = "/home/ubuntu/batiment-knowledge-base/corpus/champly"
os.makedirs(corpus_dir, exist_ok=True)

already_collected = set()
for f in os.listdir(corpus_dir):
    if f.endswith('.md'):
        already_collected.add(f)

print(f"Volumes déjà collectés: {len(already_collected)}")
print(f"Volumes à collecter: {len(VOLUMES) - len(already_collected)}")
print()

for v in VOLUMES:
    filename = f"champly_vol{v['vol']:02d}_{v['corps_etat']}.md"
    if filename in already_collected:
        print(f"  ✓ Vol {v['vol']:02d} déjà collecté: {filename}")
    else:
        print(f"  → Vol {v['vol']:02d} à collecter: https://gallica.bnf.fr/ark:/12148/{v['ark']}/texteBrut")
        print(f"     Sujet: {v['sujet']}")
