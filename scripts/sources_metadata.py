"""
Référentiel des sources de la base de connaissances bâtiment.
Chaque entrée associe un pattern de correspondance (sur le champ 'source')
aux métadonnées : auteur, titre_ouvrage, annee_publication, fiabilite.

Niveaux de fiabilité :
- 'patrimoine'        : Ouvrage du XIXe siècle, valide pour restauration du patrimoine
- 'technique-ancien'  : Manuel technique du début XXe siècle, pratiques révolues mais fondamentales
- 'technique-moderne' : Guide technique contemporain, pratiques actuelles
- 'norme-en-vigueur'  : Norme, DTU, réglementation en vigueur
"""

SOURCES_REGISTRY = [
    # ─── Champly (1900-1910) ───────────────────────────────────────────────────
    {
        "pattern": "champly_vol01",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment et de l'habitation — Vol.1 Arpentage, Fondations",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol02",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.2 Maçonnerie, Pierre, Brique",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol03",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.3 Béton armé, Ciment",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol04",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.4 Charpente en bois",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol05",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.5 Charpente métallique",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol06",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.6 Couvertures",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol07",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.7 Menuiserie",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol08",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.8 Serrurerie",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol09",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.9 Pavages, Carrelages, Peintures",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol10",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.10 Vitrerie, Chauffage",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol11",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.11 Éclairage, Chauffage au Gaz",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol12",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.12 Plomberie, Eau, Assainissement",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol13",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.13 Salubrité, Sonneries",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol14",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.14 Escaliers, Ascenseurs",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "champly_vol15",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment — Vol.15 Architecture, Plans",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    # ─── Viollet-le-Duc (1854-1868) ───────────────────────────────────────────
    {
        "pattern": "dictionnairerais01violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.1 (A)",
        "annee_publication": 1854,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais02violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.2 (B-C)",
        "annee_publication": 1856,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais03violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.3 (C-D)",
        "annee_publication": 1858,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais04violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.4 (D-F)",
        "annee_publication": 1859,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais05violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.5 (F-M)",
        "annee_publication": 1861,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais06violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.6 (M-P)",
        "annee_publication": 1862,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais07violuoft",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.7 (P-R)",
        "annee_publication": 1864,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnairerais08viol_0",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.8 (R-T)",
        "annee_publication": 1866,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "dictionnaireraison09viol",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française — Vol.9 (T-Z)",
        "annee_publication": 1868,
        "fiabilite": "patrimoine",
    },
    # ─── Rondelet (1834) ──────────────────────────────────────────────────────
    {
        "pattern": "traitedelartdeba01rond",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité de l'art de bâtir — Vol.1",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "traitedelartdeba02rond",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité de l'art de bâtir — Vol.2",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "traitedelartdeba03rond",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité de l'art de bâtir — Vol.3",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "traitedelartdeba04rond",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité de l'art de bâtir — Vol.4",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "traitedelartdeba05rond",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité de l'art de bâtir — Vol.5",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    # ─── Barberot (1900-1911) ─────────────────────────────────────────────────
    {
        "pattern": "barberot_menuiserie",
        "auteur": "Barberot, Étienne",
        "titre_ouvrage": "Traité pratique de menuiserie",
        "annee_publication": 1911,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "Traité de constructions civiles (Barberot",
        "auteur": "Barberot, Étienne",
        "titre_ouvrage": "Traité de constructions civiles",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    # ─── Oslet ────────────────────────────────────────────────────────────────
    {
        "pattern": "oslet",
        "auteur": "Oslet, Gustave",
        "titre_ouvrage": "Traité de charpente en bois",
        "annee_publication": 1903,
        "fiabilite": "technique-ancien",
    },
    # ─── Fiches techniques OzzO KB (2024) ─────────────────────────────────────
    {
        "pattern": "fiche_electricite_installations",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Installations électriques du bâtiment",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_electricite_batiment_complet",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Installations électriques complètes",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_plomberie_chauffage",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Plomberie et chauffage",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche plomberie et chauffage",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Plomberie, chauffage et installations sanitaires",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_plomberie_chauffage_complet",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Plomberie, chauffage et installations sanitaires",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_isolation_thermique",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Isolation thermique",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_maconnerie_precheur",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Maçonnerie (d'après Prêcheur/Eyrolles et Rondelet)",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_charpente_couverture",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Charpente et couverture",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_pathologies",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Pathologies du bâtiment",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_pathologies_batiment_complet",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Pathologies du bâtiment (complète)",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "fiche_normes_reglements",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Normes et réglements (RE2020, PMR, incendie)",
        "annee_publication": 2024,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "fiche normes et réglements",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Normes et réglements (RE2020, PMR, incendie)",
        "annee_publication": 2024,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "fiche normes et reglements",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Normes et réglements (RE2020, PMR, incendie)",
        "annee_publication": 2024,
        "fiabilite": "norme-en-vigueur",
    },
    # ─── ADEME (2020-2023) ────────────────────────────────────────────────────
    {
        "pattern": "guide_isolation",
        "auteur": "ADEME / Ministère de la Transition Écologique",
        "titre_ouvrage": "Guide — Isoler sa maison",
        "annee_publication": 2022,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "guide_materiaux_isolants",
        "auteur": "ADEME / AGEDEN",
        "titre_ouvrage": "Guide des matériaux isolants",
        "annee_publication": 2020,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "fiches_energies_renouvelables",
        "auteur": "ADEME",
        "titre_ouvrage": "Fiches pratiques — Énergies renouvelables",
        "annee_publication": 2023,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "fiche_reglementation_isolation",
        "auteur": "ADEME / Ministère",
        "titre_ouvrage": "Fiche réglementation — Isolation en rénovation",
        "annee_publication": 2023,
        "fiabilite": "norme-en-vigueur",
    },
    # ─── Sources avec noms complets (identifiés depuis Supabase) ─────────────
    {
        "pattern": "Traité pratique de menuiserie (Barberot",
        "auteur": "Barberot, Étienne",
        "titre_ouvrage": "Traité pratique de menuiserie",
        "annee_publication": 1911,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "Traité théorique et pratique de l'art de bâtir - Vol.1",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité théorique et pratique de l'art de bâtir — Vol.1",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Traité théorique et pratique de l'art de bâtir - Vol.2",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité théorique et pratique de l'art de bâtir — Vol.2",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Traité théorique et pratique de l'art de bâtir - Vol.3",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité théorique et pratique de l'art de bâtir — Vol.3",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Traité théorique et pratique de l'art de bâtir - Vol.4",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité théorique et pratique de l'art de bâtir — Vol.4",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Traité théorique et pratique de l'art de bâtir - Vol.5",
        "auteur": "Rondelet, Jean-Baptiste",
        "titre_ouvrage": "Traité théorique et pratique de l'art de bâtir — Vol.5",
        "annee_publication": 1834,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Fiches ADEME - Énergies renouvelables",
        "auteur": "ADEME",
        "titre_ouvrage": "Fiches pratiques — Énergies renouvelables",
        "annee_publication": 2023,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "Guide des matériaux isolants (ADEME",
        "auteur": "ADEME / AGEDEN",
        "titre_ouvrage": "Guide des matériaux isolants",
        "annee_publication": 2020,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "Guide ADEME - Isoler sa maison",
        "auteur": "ADEME / Ministère de la Transition Écologique",
        "titre_ouvrage": "Guide — Isoler sa maison",
        "annee_publication": 2022,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "Fiche réglementation isolation en rénovation",
        "auteur": "Ministère de la Transition Écologique",
        "titre_ouvrage": "Fiche réglementation — Isolation en rénovation",
        "annee_publication": 2023,
        "fiabilite": "norme-en-vigueur",
    },
    {
        "pattern": "Fiche technique plomberie-chauffage (OzzO",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Plomberie, chauffage et installations sanitaires",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Fiche technique électricité bâtiment (OzzO",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Installations électriques complètes",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Fiche technique pathologies bâtiment (OzzO",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Pathologies du bâtiment",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Fiche pathologies du bâtiment",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Pathologies du bâtiment",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Fiche charpente et couverture",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Fiche technique — Charpente et couverture",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Archive.org / Getty Research Institute",
        "auteur": "Collectif",
        "titre_ouvrage": "Encyclopédie de l'architecture (Getty Research Institute)",
        "annee_publication": 1880,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Archive.org / Éditions Mir",
        "auteur": "Collectif",
        "titre_ouvrage": "Manuel de construction (Éditions Mir)",
        "annee_publication": 1975,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "Archive.org / CSTB",
        "auteur": "CSTB",
        "titre_ouvrage": "Publications techniques CSTB",
        "annee_publication": 1990,
        "fiabilite": "technique-moderne",
    },
    {
        "pattern": "Archive.org",
        "auteur": "Collectif",
        "titre_ouvrage": "Ouvrage technique (Archive.org)",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "Synthèse technique",
        "auteur": "OzzO Knowledge Base",
        "titre_ouvrage": "Synthèse technique bâtiment",
        "annee_publication": 2024,
        "fiabilite": "technique-moderne",
    },
    # ─── Encyclopédie générale (domaine public) ───────────────────────────────
    {
        "pattern": "encyclopedie_architecture",
        "auteur": "Collectif",
        "titre_ouvrage": "Encyclopédie de l'architecture",
        "annee_publication": 1880,
        "fiabilite": "patrimoine",
    },
    {
        "pattern": "Gallica BnF",
        "auteur": "Champly, René",
        "titre_ouvrage": "Nouvelle encyclopédie pratique du bâtiment et de l'habitation",
        "annee_publication": 1900,
        "fiabilite": "technique-ancien",
    },
    {
        "pattern": "Viollet-le-Duc",
        "auteur": "Viollet-le-Duc, Eugène",
        "titre_ouvrage": "Dictionnaire raisonné de l'architecture française",
        "annee_publication": 1868,
        "fiabilite": "patrimoine",
    },
]


def get_metadata_for_source(source: str) -> dict:
    """Retourne les métadonnées pour une source donnée."""
    source_lower = source.lower()
    for entry in SOURCES_REGISTRY:
        if entry["pattern"].lower() in source_lower:
            return {
                "auteur": entry["auteur"],
                "titre_ouvrage": entry["titre_ouvrage"],
                "annee_publication": entry["annee_publication"],
                "fiabilite": entry["fiabilite"],
            }
    # Fallback générique
    return {
        "auteur": None,
        "titre_ouvrage": source,
        "annee_publication": None,
        "fiabilite": "technique-moderne",
    }


if __name__ == "__main__":
    # Test
    tests = [
        "Gallica BnF ark:/12148/bpt6k9774323q",
        "Traité de constructions civiles (Barberot, 1900)",
        "Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. 9)",
        "fiche_charpente_couverture.md",
        "guide_isolation_ademe.txt",
    ]
    for t in tests:
        m = get_metadata_for_source(t)
        print(f"\n{t}")
        print(f"  → {m['auteur']} ({m['annee_publication']}) — {m['fiabilite']}")
