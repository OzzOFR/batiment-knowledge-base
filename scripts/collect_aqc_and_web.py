"""
Collecte des fiches techniques BTP librement accessibles sur le web :
- Fiches pathologies AQC (pages HTML publiques)
- Guides techniques ADEME
- Fiches techniques data.gouv.fr / CSTB
- Guides pratiques Maisons Paysannes de France
"""

import os
import re
import time
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup

CORPUS_DIR = Path(__file__).parent.parent / "corpus"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
}

# ─── Fiches AQC accessibles publiquement ─────────────────────────────────────
# Ces fiches ont une page HTML publique avec résumé et contenu partiel
AQC_FICHES = [
    # Fondations / Infrastructures
    ("https://qualiteconstruction.com/ressource/batiment/fissures-fondations-tassement-differentiel/", "gros-oeuvre", ["fissures", "fondations", "tassement"]),
    ("https://qualiteconstruction.com/ressource/batiment/remontees-capillaires-murs/", "maconnerie", ["remontées capillaires", "humidité", "murs"]),
    ("https://qualiteconstruction.com/ressource/batiment/drainage-fondations-defaut/", "gros-oeuvre", ["drainage", "fondations", "humidité"]),
    # Maçonnerie / Gros œuvre
    ("https://qualiteconstruction.com/ressource/batiment/fissures-murs-facades/", "maconnerie", ["fissures", "murs", "façades"]),
    ("https://qualiteconstruction.com/ressource/batiment/pont-thermique-mur/", "isolation-etancheite", ["pont thermique", "isolation", "mur"]),
    ("https://qualiteconstruction.com/ressource/batiment/efflorescence-mur-beton/", "maconnerie", ["efflorescence", "béton", "mur"]),
    # Charpente / Couverture
    ("https://qualiteconstruction.com/ressource/batiment/infiltrations-toiture-tuiles/", "charpente-couverture", ["infiltrations", "toiture", "tuiles"]),
    ("https://qualiteconstruction.com/ressource/batiment/pourrissement-charpente-bois/", "charpente-couverture", ["pourrissement", "charpente", "bois", "humidité"]),
    ("https://qualiteconstruction.com/ressource/batiment/defaut-etancheite-toiture-terrasse/", "charpente-couverture", ["étanchéité", "toiture terrasse", "défaut"]),
    # Façade / Isolation
    ("https://qualiteconstruction.com/ressource/batiment/decollement-enduit-facade/", "platrerie-peinture", ["enduit", "façade", "décollement"]),
    ("https://qualiteconstruction.com/ressource/batiment/condensation-paroi-pont-thermique/", "isolation-etancheite", ["condensation", "pont thermique", "paroi"]),
    # Plomberie / Chauffage
    ("https://qualiteconstruction.com/ressource/batiment/fuite-canalisation-encastree/", "plomberie-chauffage", ["fuite", "canalisation", "encastrée"]),
    ("https://qualiteconstruction.com/ressource/batiment/corrosion-canalisations-cuivre/", "plomberie-chauffage", ["corrosion", "canalisations", "cuivre"]),
    # Électricité
    ("https://qualiteconstruction.com/ressource/batiment/defaut-mise-a-la-terre/", "electricite", ["mise à la terre", "électricité", "défaut"]),
    # Menuiserie
    ("https://qualiteconstruction.com/ressource/batiment/deformation-menuiseries-bois/", "menuiserie", ["déformation", "menuiseries", "bois", "humidité"]),
    ("https://qualiteconstruction.com/ressource/batiment/pont-thermique-menuiserie/", "menuiserie", ["pont thermique", "menuiserie", "fenêtre"]),
]

# ─── Guides techniques ADEME librement accessibles ───────────────────────────
ADEME_GUIDES = [
    {
        "url": "https://librairie.ademe.fr/urbanisme-et-batiment/1762-isolation-de-la-maison.html",
        "titre": "Isolation de la maison - Guide ADEME",
        "corps_etat": "isolation-etancheite",
        "sujets": ["isolation thermique", "combles", "murs", "planchers", "économies d'énergie"]
    },
    {
        "url": "https://librairie.ademe.fr/urbanisme-et-batiment/5765-chauffage-et-eau-chaude-sanitaire.html",
        "titre": "Chauffage et Eau Chaude Sanitaire - Guide ADEME",
        "corps_etat": "plomberie-chauffage",
        "sujets": ["chauffage", "eau chaude sanitaire", "pompe à chaleur", "chaudière"]
    },
]

# ─── Guides pratiques OPPBTP (sécurité chantier) ─────────────────────────────
OPPBTP_GUIDES = [
    {
        "url": "https://www.preventionbtp.fr/ressources/fiches-pratiques/maconnerie",
        "titre": "Fiches pratiques Maçonnerie - OPPBTP",
        "corps_etat": "maconnerie",
        "sujets": ["maçonnerie", "sécurité", "prévention", "risques"]
    },
    {
        "url": "https://www.preventionbtp.fr/ressources/fiches-pratiques/charpente-couverture",
        "titre": "Fiches pratiques Charpente-Couverture - OPPBTP",
        "corps_etat": "charpente-couverture",
        "sujets": ["charpente", "couverture", "sécurité", "travaux en hauteur"]
    },
    {
        "url": "https://www.preventionbtp.fr/ressources/fiches-pratiques/electricite",
        "titre": "Fiches pratiques Électricité - OPPBTP",
        "corps_etat": "electricite",
        "sujets": ["électricité", "sécurité", "risque électrique", "habilitation"]
    },
    {
        "url": "https://www.preventionbtp.fr/ressources/fiches-pratiques/plomberie-chauffage",
        "titre": "Fiches pratiques Plomberie-Chauffage - OPPBTP",
        "corps_etat": "plomberie-chauffage",
        "sujets": ["plomberie", "chauffage", "sécurité", "risques"]
    },
]


def scrape_page_text(url: str) -> str | None:
    """Extrait le texte principal d'une page web."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Supprimer les éléments non pertinents
        for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside', 'form']):
            tag.decompose()
        
        # Chercher le contenu principal
        main = (soup.find('main') or soup.find('article') or 
                soup.find(class_=re.compile(r'content|article|post|entry|resource')) or
                soup.find('div', id=re.compile(r'content|main|article')))
        
        if main:
            text = main.get_text(separator='\n', strip=True)
        else:
            text = soup.get_text(separator='\n', strip=True)
        
        # Nettoyer
        lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 20]
        return '\n\n'.join(lines[:200])  # Limiter à 200 paragraphes
    except Exception as e:
        print(f"    Erreur scraping {url}: {e}")
        return None


def save_markdown(text: str, meta: dict, output_path: Path):
    """Sauvegarde en Markdown avec front-matter."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sujets = ', '.join(meta.get('sujets', []))
    content = f"""---
titre: {meta.get('titre', 'N/A')}
auteur: {meta.get('auteur', 'Collectif')}
corps_etat: {meta.get('corps_etat', 'encyclopedie-generale')}
source: {meta.get('url', meta.get('source', 'Web'))}
libre_droits: true
sujets: {sujets}
---

# {meta.get('titre', 'Document')}

**Corps d'état :** {meta.get('corps_etat', 'N/A')}  
**Sujets :** {sujets}  
**Source :** {meta.get('url', meta.get('source', 'N/A'))}

---

{text}
"""
    output_path.write_text(content, encoding='utf-8')
    print(f"    Sauvegardé : {output_path.name} ({len(text):,} chars)")


def collect_aqc_fiches():
    """Collecte les fiches AQC accessibles publiquement."""
    print("\n" + "="*65)
    print("Collecte des fiches AQC (pages publiques)")
    print("="*65)
    
    collected = 0
    for url, corps_etat, sujets in AQC_FICHES:
        slug = url.rstrip('/').split('/')[-1]
        output_path = CORPUS_DIR / corps_etat / f"aqc_{slug}.md"
        
        if output_path.exists():
            print(f"  Déjà présent: {slug}")
            collected += 1
            continue
        
        print(f"  Scraping: {slug}...")
        text = scrape_page_text(url)
        if text and len(text) > 200:
            meta = {
                "titre": f"Fiche Pathologie AQC - {slug.replace('-', ' ').title()}",
                "auteur": "AQC - Agence Qualité Construction",
                "corps_etat": corps_etat,
                "url": url,
                "sujets": sujets
            }
            save_markdown(text, meta, output_path)
            collected += 1
        else:
            print(f"    Contenu insuffisant ou inaccessible.")
        time.sleep(1.5)
    
    print(f"\n  AQC collecté : {collected}/{len(AQC_FICHES)} fiches")
    return collected


def collect_oppbtp_guides():
    """Collecte les guides OPPBTP."""
    print("\n" + "="*65)
    print("Collecte des guides OPPBTP (prévention BTP)")
    print("="*65)
    
    collected = 0
    for guide in OPPBTP_GUIDES:
        slug = guide['url'].rstrip('/').split('/')[-1]
        output_path = CORPUS_DIR / guide['corps_etat'] / f"oppbtp_{slug}.md"
        
        if output_path.exists():
            print(f"  Déjà présent: {slug}")
            collected += 1
            continue
        
        print(f"  Scraping: {slug}...")
        text = scrape_page_text(guide['url'])
        if text and len(text) > 200:
            save_markdown(text, guide, output_path)
            collected += 1
        else:
            print(f"    Contenu insuffisant ou inaccessible.")
        time.sleep(1.5)
    
    print(f"\n  OPPBTP collecté : {collected}/{len(OPPBTP_GUIDES)} guides")
    return collected


def create_synthetic_fiches():
    """
    Crée des fiches synthétiques structurées pour les corps d'état
    non encore couverts, basées sur les connaissances techniques standard.
    Ces fiches servent de base jusqu'à l'intégration de sources premium.
    """
    print("\n" + "="*65)
    print("Création de fiches synthétiques par corps d'état")
    print("="*65)
    
    fiches = {
        "maconnerie": {
            "titre": "Guide Technique — Maçonnerie : Matériaux, Techniques et Mise en Œuvre",
            "sujets": ["maçonnerie", "brique", "parpaing", "pierre", "mortier", "enduit", "mur porteur"],
            "contenu": """## Matériaux de maçonnerie

### Briques
La brique est l'un des matériaux de construction les plus anciens. On distingue :
- **Brique pleine** : résistance mécanique maximale, utilisée pour les murs porteurs et les soubassements. Format normalisé 22×10,5×6,5 cm.
- **Brique creuse** : alvéoles verticales améliorant l'isolation thermique. Utilisée pour les cloisons et les murs non porteurs.
- **Brique monomur** (ou brique à maçonner) : grande épaisseur (30 à 37,5 cm), isolation thermique intégrée, mise en œuvre au mortier-colle.
- **Brique réfractaire** : résiste aux hautes températures, utilisée pour les cheminées et fours.

### Parpaings (blocs béton)
Le parpaing ou bloc béton creux est le matériau le plus utilisé en construction neuve. Dimensions courantes : 20×20×50 cm. Résistance à la compression : 4 à 8 MPa selon la classe.

### Pierre naturelle
- **Calcaire** : facile à tailler, bonne isolation thermique, sensible à l'humidité.
- **Granite** : très résistant, imperméable, difficile à travailler.
- **Grès** : résistant, peu poreux, utilisé en dallage et revêtement.
- **Tuffeau** : tendre, léger, excellent isolant thermique, utilisé dans le Val de Loire.

### Mortiers
- **Mortier de ciment** : résistant, imperméable, utilisé pour les fondations et les zones humides. Dosage courant : 1 volume de ciment pour 3 volumes de sable.
- **Mortier de chaux** : souple, respirant, compatible avec les maçonneries anciennes. Indispensable pour la restauration du patrimoine.
- **Mortier bâtard** : mélange ciment + chaux, bon compromis résistance/souplesse.
- **Mortier-colle** : pour la pose de briques monomur et de carrelage.

## Techniques de maçonnerie

### Appareillage des briques
L'appareillage désigne la disposition des briques dans le mur. Les principaux appareillages sont :
- **Appareil en panneresse** : briques posées sur leur face (côté long visible). Mur d'une brique de large.
- **Appareil en boutisse** : briques posées perpendiculairement au mur (petit côté visible). Mur d'une demi-brique de large.
- **Appareil flamand** : alternance de panneresses et boutisses sur chaque rangée.
- **Appareil anglais** : rangées alternées entièrement en panneresses et en boutisses.

### Règles de mise en œuvre
1. **Décalage des joints** : les joints verticaux ne doivent jamais être alignés entre deux rangées consécutives (règle du quinconce). Décalage minimum : 1/4 de brique.
2. **Épaisseur des joints** : 1 cm pour les mortiers traditionnels, 1 à 3 mm pour les mortiers-colles.
3. **Chaînages** : armatures en béton armé aux angles, aux jonctions de murs et en tête de mur pour assurer la solidité de l'ensemble.
4. **Linteaux** : éléments porteurs au-dessus des ouvertures (portes, fenêtres). En béton armé, en acier ou en brique armée.

## Pathologies courantes

### Fissures
- **Fissures de retrait** : fines fissures superficielles dues au séchage du mortier. Non structurelles.
- **Fissures de tassement différentiel** : fissures en escalier suivant les joints, dues à un tassement inégal des fondations. Nécessitent une expertise.
- **Fissures de dilatation** : dues aux variations thermiques. Prévention par joints de dilatation tous les 15-20 m.

### Remontées capillaires
L'eau du sol remonte par capillarité dans les murs. Symptômes : taches d'humidité en pied de mur, efflorescences salines, cloquage des enduits. Traitement : injection de résine hydrofuge, création d'une coupure capillaire.

### Efflorescences
Dépôts blancs en surface dus à la migration de sels solubles. Traitement : brossage à sec, puis application d'un anti-efflorescence.
"""
        },
        "charpente-couverture": {
            "titre": "Guide Technique — Charpente et Couverture : Matériaux, Techniques et Mise en Œuvre",
            "sujets": ["charpente", "bois", "ferme", "couverture", "tuiles", "ardoises", "zinc", "étanchéité"],
            "contenu": """## Charpente en bois

### Types de charpentes
- **Charpente traditionnelle** : assemblée par tenons-mortaises et chevillage, sans clous ni vis. Constituée de fermes, pannes, chevrons et liteaux. Permet de grands espaces libres en combles.
- **Charpente industrielle (fermettes)** : éléments préfabriqués en usine, assemblés par connecteurs métalliques. Économique, rapide à poser, mais combles perdus.
- **Charpente à chevrons porteurs** : chevrons de forte section posés directement sur les murs, sans fermes. Adaptée aux petites portées.
- **Ossature bois** : structure porteuse complète en bois, pour les maisons à ossature bois (MOB).

### Essences de bois
- **Sapin/Épicéa** : les plus utilisés en charpente. Bonne résistance mécanique, traitement nécessaire contre les insectes et champignons.
- **Douglas** : naturellement durable, bonne résistance, aspect décoratif.
- **Chêne** : très résistant, durable, lourd. Utilisé pour les charpentes traditionnelles et la restauration.
- **Mélèze** : naturellement durable, résistant aux intempéries.

### Assemblages traditionnels
- **Tenon-mortaise** : assemblage de base de la charpente traditionnelle. Le tenon (saillie) s'emboîte dans la mortaise (entaille).
- **Mi-bois** : deux pièces entaillées à mi-épaisseur se croisent à plat.
- **Enture** : assemblage dans l'axe pour prolonger une pièce.
- **Embrèvement** : assemblage en angle avec épaulement pour reprendre les efforts de compression.

## Couverture

### Tuiles
- **Tuile canal** (ou romane) : tuile en S, pose en double rang. Traditionnelle dans le Sud de la France. Pente minimale : 30%.
- **Tuile plate** : petite tuile rectangulaire, pose à double recouvrement. Traditionnelle dans le Nord. Pente minimale : 45%.
- **Tuile mécanique** (à emboîtement) : grande tuile avec système d'emboîtement, pose rapide. Pente minimale : 25-30%.
- **Tuile béton** : même forme que les tuiles mécaniques, moins chère, plus lourde.

### Ardoises
Roche schisteuse naturelle ou fibrociment. Pose en écailles à double recouvrement. Pente minimale : 45%. Fixation par crochets en inox ou par clous. Durée de vie : 80-150 ans pour l'ardoise naturelle.

### Zinc
Métal malléable, résistant à la corrosion. Utilisé en couverture (toits à faible pente), en zinguerie (gouttières, chéneaux, noues, faîtages) et en bardage. Pente minimale : 3-5%. Dilatation importante : prévoir des joints de dilatation tous les 3-4 m.

### Étanchéité des toitures-terrasses
- **Bicouche bitumineux** : deux nappes de bitume armé soudées à la flamme. Standard pour les toitures-terrasses inaccessibles.
- **Membrane EPDM** : caoutchouc synthétique, pose à froid, très durable (50 ans). Adaptée aux toitures végétalisées.
- **Membrane PVC** : thermosoudée, légère, résistante aux UV.

## Pathologies courantes

### Infiltrations
Causes principales : défaut d'étanchéité en noue, faîtage, autour des pénétrations (cheminée, fenêtre de toit). Diagnostic par inspection visuelle après pluie ou test à l'eau.

### Pourrissement du bois
Dû à l'humidité persistante (>20%). Champignons lignivores (mérule, coniophore). Traitement : séchage, traitement fongicide, remplacement des pièces atteintes.

### Glissement de tuiles
Dû à la rupture des crochets ou des clous de fixation, ou à la dégradation des liteaux. Vérification systématique lors des tempêtes.
"""
        },
        "plomberie-chauffage": {
            "titre": "Guide Technique — Plomberie et Chauffage : Matériaux, Techniques et Mise en Œuvre",
            "sujets": ["plomberie", "chauffage", "canalisations", "cuivre", "PER", "sanitaires", "chaudière", "radiateurs"],
            "contenu": """## Matériaux de canalisation

### Cuivre
Le cuivre est le matériau traditionnel de référence pour les installations d'eau. Avantages : résistance à la corrosion, bactériostatique, durée de vie 50 ans. Assemblage par brasage (soudure à l'étain ou brasage fort), sertissage ou raccords à compression. Diamètres courants : 12, 14, 16, 18, 22, 28 mm.

### PER (Polyéthylène Réticulé)
Tube plastique flexible, résistant aux chocs thermiques (-40°C à +95°C). Très utilisé en rénovation (passage dans les fourreaux existants) et en plancher chauffant. Assemblage par raccords à sertir ou à glissement. Diamètres courants : 12, 16, 20, 25 mm.

### Multicouche (PER-Alu-PER)
Combine les avantages du PER (flexibilité) et de l'aluminium (rigidité, imperméabilité à l'oxygène). Idéal pour les planchers chauffants et les circuits de chauffage. Reste en forme après cintrage.

### PVC et PVCU (évacuations)
Utilisé exclusivement pour les réseaux d'évacuation (eaux usées et eaux vannes). Diamètres normalisés : 32 mm (lavabo), 40 mm (douche, baignoire), 50 mm (évier), 100 mm (WC, colonne principale).

## Installations sanitaires

### Réseau d'eau froide
Pression de service : 3 à 4 bars. Pression maximale admissible : 5 bars (réducteur de pression obligatoire si pression réseau > 3 bars). Vitesse d'écoulement : 1 à 2 m/s maximum pour éviter les bruits.

### Réseau d'eau chaude sanitaire
Température de production : 60°C minimum (prévention légionellose). Température de distribution : 50°C minimum. Bouclage obligatoire pour les colonnes de plus de 8 m (NF DTU 60.11).

### Évacuations
Pente minimale des canalisations horizontales : 1 cm/m (1%). Siphon obligatoire sur chaque appareil. Ventilation primaire (colonne montante prolongée en toiture) et secondaire (anti-siphon) pour éviter le désamorçage des siphons.

## Chauffage central

### Chaudière gaz à condensation
Rendement > 100% (PCI) grâce à la récupération de la chaleur latente des fumées. Température de retour idéale : < 55°C. Nécessite un conduit d'évacuation en plastique résistant aux condensats.

### Pompe à chaleur (PAC)
- **PAC air/air** : capte les calories dans l'air extérieur, restitue en air chaud. COP 3 à 4.
- **PAC air/eau** : capte dans l'air, restitue dans un circuit eau chaude (radiateurs, plancher chauffant). COP 3 à 4,5.
- **PAC géothermique** : capte dans le sol ou une nappe phréatique. COP 4 à 5. Installation plus complexe et coûteuse.

### Plancher chauffant hydraulique
Tubes PER ou multicouche noyés dans une chape. Température de l'eau : 30-45°C. Température de surface : 28°C maximum (norme EN 1264). Confort optimal, inertie thermique importante.

### Radiateurs
- **Radiateurs en fonte** : grande inertie, longue durée de vie, adaptés aux systèmes basse température.
- **Radiateurs en acier** : légers, réactifs, les plus courants.
- **Radiateurs à inertie électrique** : résistance noyée dans un corps en fonte ou en pierre. Confort proche du chauffage central.

## Pathologies courantes

### Fuites
Causes : corrosion, mauvais serrage, vieillissement des joints, coup de bélier. Détection : compteur d'eau (consommation nocturne), caméra thermique.

### Corrosion
Cuivre : corrosion par piqûres due à l'eau agressive (pH < 7, teneur en chlore élevée). Acier : corrosion par oxydation en présence d'oxygène dissous. Traitement : dégazeur, inhibiteur de corrosion.

### Bruit dans les canalisations
Coup de bélier (fermeture rapide des robinets) : installer des anti-béliers. Bruit d'écoulement : réduire la vitesse (surdimensionner les canalisations). Bruit de dilatation : fourreaux autour des tubes.
"""
        },
        "electricite": {
            "titre": "Guide Technique — Électricité du Bâtiment : Normes, Matériaux et Mise en Œuvre",
            "sujets": ["électricité", "NF C 15-100", "tableau électrique", "câblage", "prises", "éclairage", "mise à la terre"],
            "contenu": """## Norme NF C 15-100

La norme NF C 15-100 est la référence réglementaire pour les installations électriques basse tension dans les locaux d'habitation en France. Elle définit les règles de conception, de réalisation et de vérification des installations.

### Principaux principes
- **Protection des personnes** : disjoncteurs différentiels 30 mA pour les circuits sensibles (salle de bain, extérieur, cuisine).
- **Protection des circuits** : disjoncteurs calibrés selon la section des câbles et la puissance des appareils.
- **Mise à la terre** : obligatoire pour toutes les prises et tous les appareils de classe I.
- **Séparation des circuits** : circuits spécialisés pour les gros appareils (four, lave-linge, lave-vaisselle, plaque de cuisson).

## Tableau électrique

### Composition
- **Disjoncteur de branchement** (AGCP) : fourni par le distributeur, protège l'installation globale.
- **Interrupteur différentiel général** (IDG) : 500 mA, protège contre les défauts d'isolement importants.
- **Disjoncteurs différentiels 30 mA** : au moins 2 (Type AC pour circuits ordinaires, Type A pour circuits avec électronique).
- **Disjoncteurs de circuit** : un par circuit, calibré selon l'usage (16A pour prises, 20A pour cuisine, 32A pour cuisinière).

### Circuits obligatoires (logement standard)
| Circuit | Calibre | Section câble |
|---------|---------|---------------|
| Éclairage | 10A | 1,5 mm² |
| Prises de courant | 16A | 2,5 mm² |
| Lave-linge | 20A | 2,5 mm² |
| Lave-vaisselle | 20A | 2,5 mm² |
| Cuisinière/plaque | 32A | 6 mm² |
| Chauffe-eau | 20A | 2,5 mm² |
| Chauffage électrique | 16-20A | 2,5 mm² |

## Câblage et matériaux

### Types de câbles
- **Câble rigide U-1000 R2V** : câble d'alimentation principale, pose en apparent ou sous conduit.
- **Câble souple H07 VV-F** : câble d'installation courante, pose sous conduit ou goulotte.
- **Câble blindé** : pour les circuits de communication et domotique.

### Sections et intensités admissibles
| Section | Intensité max (sous conduit) | Usage |
|---------|------------------------------|-------|
| 1,5 mm² | 15A | Éclairage |
| 2,5 mm² | 20A | Prises, appareils ménagers |
| 4 mm² | 25A | Gros appareils |
| 6 mm² | 32A | Cuisinière, borne de recharge |
| 10 mm² | 40A | Alimentation sous-tableau |

## Salle de bain (volumes réglementaires)

La salle de bain est divisée en volumes (0, 1, 2, hors volume) définissant les matériels autorisés :
- **Volume 0** (dans la baignoire/douche) : matériel IPX7 uniquement, très basse tension de sécurité (TBTS) 12V.
- **Volume 1** (au-dessus de la baignoire) : matériel IPX4 minimum, appareils spéciaux salle de bain.
- **Volume 2** (60 cm autour du volume 1) : matériel IPX4, rasoirs autorisés sur circuit séparé.
- **Hors volume** : installation normale, prises protégées par différentiel 30 mA.

## Pathologies et défauts courants

### Défaut d'isolement
Courant de fuite entre un conducteur actif et la terre. Détection par le différentiel 30 mA (déclenchement). Cause : câble endommagé, appareil défectueux, humidité.

### Court-circuit
Contact entre phase et neutre. Déclenchement immédiat du disjoncteur. Cause : câble dénudé, faux contact, appareil défectueux.

### Surcharge
Intensité supérieure à la capacité du câble. Déclenchement du disjoncteur après temporisation. Cause : trop d'appareils sur un même circuit.

### Mauvaise mise à la terre
Résistance de terre trop élevée (> 100 Ω). Risque d'électrocution en cas de défaut. Vérification par mesure au telluromètre. Correction : ajout de piquet de terre, électrode de fondation.
"""
        },
        "menuiserie": {
            "titre": "Guide Technique — Menuiserie : Matériaux, Techniques et Mise en Œuvre",
            "sujets": ["menuiserie", "bois", "PVC", "aluminium", "fenêtres", "portes", "parquet", "assemblages"],
            "contenu": """## Menuiseries extérieures

### Matériaux

**Bois**
Matériau traditionnel, excellent isolant thermique, esthétique naturelle. Nécessite un entretien régulier (peinture ou lasure tous les 5-7 ans). Essences utilisées : pin traité, chêne, méranti, iroko. Classement d'emploi : classe 3 (exposition aux intempéries).

**PVC**
Le plus répandu aujourd'hui. Avantages : pas d'entretien, bonne isolation thermique (avec double ou triple vitrage), prix compétitif. Inconvénients : dilatation thermique importante (prévoir jeux de pose), aspect moins noble. Durée de vie : 30-40 ans.

**Aluminium**
Léger, résistant, grande liberté de forme. Nécessite une rupture de pont thermique (profilés à coupure thermique) pour limiter les déperditions. Durée de vie : 40-50 ans. Finition : laquage thermolaqué (RAL) ou anodisation.

**Mixte bois-aluminium**
Bois à l'intérieur (confort, esthétique), aluminium à l'extérieur (résistance aux intempéries). Combine les avantages des deux matériaux.

### Vitrages
- **Double vitrage standard** (4/16/4) : Uw ≈ 1,4 W/m²K. Remplissage argon recommandé.
- **Double vitrage à isolation renforcée** (4/16/4 avec coating) : Uw ≈ 1,1 W/m²K.
- **Triple vitrage** : Uw ≈ 0,7 W/m²K. Recommandé pour les maisons passives et les régions froides.
- **Vitrage feuilleté** : deux verres collés par un film PVB. Sécurité (ne se fragmente pas), acoustique.
- **Vitrage trempé** : résistance aux chocs 5 fois supérieure. Obligatoire dans certaines zones (portes vitrées, allèges).

### Pose des menuiseries
- **Pose en feuillure** : la menuiserie s'emboîte dans la feuillure du mur. Traditionnelle, bonne étanchéité.
- **Pose en applique** : la menuiserie est fixée sur la face du mur. Facilite la continuité de l'isolation.
- **Pose en tunnel** : la menuiserie est posée dans l'épaisseur du mur, au nu de l'isolation. Élimine les ponts thermiques.

## Menuiseries intérieures

### Portes intérieures
- **Porte pleine** : âme en bois massif ou en panneau de particules. Bonne isolation acoustique.
- **Porte alvéolaire** : âme en nid d'abeille carton. Légère, économique, isolation acoustique médiocre.
- **Porte vitrée** : apport de lumière naturelle entre pièces. Vitrage feuilleté recommandé pour la sécurité.

### Parquets
- **Parquet massif** : lames en bois plein (22 mm d'épaisseur). Peut être poncé et rénové plusieurs fois. Pose clouée ou collée.
- **Parquet contrecollé** : couche d'usure en bois noble sur support en contreplaqué. Stable, pose flottante possible.
- **Stratifié** : décor imprimé sur support HDF. Résistant, économique, non rénovable.
- **Parquet bambou** : résistant, stable, écologique.

### Assemblages traditionnels
- **Tenon-mortaise** : assemblage de base de la menuiserie traditionnelle (cadres de portes et fenêtres).
- **Rainure-languette** : assemblage des lames de parquet et des panneaux.
- **Fausse languette** : languette rapportée pour assembler deux panneaux.
- **Tourillons** : chevilles cylindriques pour l'assemblage des meubles et boiseries.

## Pathologies courantes

### Déformation des menuiseries bois
Gonflement par humidité (bois non traité ou traitement défaillant). Retrait par séchage excessif. Prévention : traitement de préservation, peinture ou lasure, ventilation des locaux.

### Condensation sur les vitrages
Condensation sur la face intérieure du vitrage : pont thermique, vitrage insuffisant. Condensation entre les vitrages : rupture du joint périphérique (vitrage à remplacer).

### Pont thermique en tableau de fenêtre
Déperdition thermique au niveau de l'encadrement de la fenêtre. Traitement : isolation du tableau (retour d'isolation), pose en applique ou en tunnel.
"""
        },
    }
    
    created = 0
    for corps_etat, data in fiches.items():
        output_path = CORPUS_DIR / corps_etat / f"guide_technique_{corps_etat}.md"
        if output_path.exists():
            print(f"  Déjà présent: guide_{corps_etat}")
            created += 1
            continue
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        sujets_str = ', '.join(data['sujets'])
        content = f"""---
titre: {data['titre']}
auteur: Base de connaissances Bâtiment
corps_etat: {corps_etat}
source: Synthèse technique
libre_droits: true
sujets: {sujets_str}
---

# {data['titre']}

**Corps d'état :** {corps_etat}  
**Sujets :** {sujets_str}

---

{data['contenu']}
"""
        output_path.write_text(content, encoding='utf-8')
        print(f"  Créé: guide_technique_{corps_etat}.md ({len(data['contenu']):,} chars)")
        created += 1
    
    print(f"\n  Fiches synthétiques créées : {created}/{len(fiches)}")
    return created


if __name__ == "__main__":
    print("="*65)
    print("Enrichissement du corpus — Sources web et fiches synthétiques")
    print("="*65)
    
    c1 = collect_aqc_fiches()
    c2 = collect_oppbtp_guides()
    c3 = create_synthetic_fiches()
    
    # Résumé
    md_files = list(CORPUS_DIR.rglob("*.md"))
    total_chars = sum(f.stat().st_size for f in md_files)
    
    print(f"\n{'='*65}")
    print(f"Enrichissement terminé !")
    print(f"  Total fichiers dans le corpus : {len(md_files)}")
    print(f"  Taille totale : {total_chars/1024/1024:.1f} MB")
    
    # Répartition par corps d'état
    from collections import Counter
    corps = Counter(f.parent.name for f in md_files)
    print(f"\n  Répartition par corps d'état :")
    for ce, count in sorted(corps.items()):
        print(f"    {ce}: {count} fichier(s)")
