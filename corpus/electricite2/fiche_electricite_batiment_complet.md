# Installations Électriques du Bâtiment — Guide Technique Complet

## 1. Alimentation et raccordement au réseau

### 1.1 Branchement ENEDIS

Le branchement électrique relie le réseau de distribution public au tableau de comptage du client. Il comprend le câble de branchement (souterrain ou aérien), le coupe-circuit principal (CCP), le disjoncteur de branchement (calibre 30 à 90 A selon la puissance souscrite), et le compteur Linky. La puissance souscrite est choisie en fonction des besoins : 3 kVA (studio), 6 kVA (appartement), 9 à 12 kVA (maison individuelle), 18 à 36 kVA (maison avec chauffage électrique).

### 1.2 Tableau de répartition (TR)

Le tableau de répartition (tableau électrique) est le cœur de l'installation. Il comprend un disjoncteur général (interrupteur différentiel 30 mA), des disjoncteurs divisionnaires pour chaque circuit, et des interrupteurs différentiels 30 mA pour la protection des personnes. La norme NF C 15-100 définit les règles de conception et d'installation.

Le tableau doit être placé dans un endroit accessible, à une hauteur de 1 à 1,80 m, à l'abri de l'humidité. Il doit être équipé d'un repérage clair des circuits.

### 1.3 Mise à la terre (TT)

La mise à la terre protège les personnes contre les chocs électriques en cas de défaut d'isolement. Elle comprend une prise de terre (piquet, boucle en fond de fouille), un conducteur de protection (PE, vert-jaune), et un interrupteur différentiel 30 mA. La résistance de la prise de terre doit être inférieure à 100 Ω (schéma TT).

## 2. Circuits et câblage

### 2.1 Circuits spécialisés

La norme NF C 15-100 impose des circuits spécialisés pour certains usages : un circuit dédié pour le lave-linge (16 A), un pour le lave-vaisselle (16 A), un pour le four (32 A), un pour le chauffe-eau (20 A), un pour la plaque de cuisson (32 A). Ces circuits sont protégés par un disjoncteur adapté et un câble de section suffisante.

### 2.2 Circuits d'éclairage et de prises

Les circuits d'éclairage sont protégés par des disjoncteurs 10 A et câblés en 1,5 mm². Les circuits de prises de courant sont protégés par des disjoncteurs 16 A et câblés en 2,5 mm². La norme impose un minimum de prises par pièce : 5 prises dans le séjour, 3 dans les chambres, 6 dans la cuisine.

### 2.3 Sections des conducteurs

| Usage | Section | Disjoncteur |
|---|---|---|
| Éclairage | 1,5 mm² | 10 A |
| Prises de courant | 2,5 mm² | 16 A |
| Lave-linge, lave-vaisselle | 2,5 mm² | 16 A |
| Chauffe-eau | 2,5 mm² | 20 A |
| Cuisinière, four | 6 mm² | 32 A |
| Plaque de cuisson | 6 mm² | 32 A |
| Tableau secondaire | 10 mm² | 40-63 A |

### 2.4 Chemins de câbles et conduits

Les câbles sont posés dans des conduits (IRL, IRO, ICT) ou des goulottes. Les conduits encastrés dans les parois doivent être de type IRL (isolant rigide lisse). Les conduits apparents doivent être de type IRO (isolant rigide ordinaire). Les câbles ne doivent pas être posés dans les mêmes conduits que les canalisations d'eau ou de gaz.

## 3. Protection des personnes et des biens

### 3.1 Disjoncteurs différentiels

Les interrupteurs différentiels (ID) détectent les courants de fuite vers la terre et coupent l'alimentation en cas de défaut. La sensibilité de 30 mA est obligatoire pour la protection des personnes. La sensibilité de 300 mA est utilisée pour la protection des biens (incendie). Chaque tableau doit comporter au moins deux ID 30 mA pour répartir les circuits.

### 3.2 Parafoudres

Le parafoudre protège l'installation contre les surtensions dues à la foudre. Il est obligatoire dans les zones exposées (classées Isokeraunic Level ≥ 25) et recommandé partout. Il se place en tête du tableau, après le disjoncteur général.

### 3.3 Sécurité dans les salles de bain

Les salles de bain sont divisées en volumes (0, 1, 2, 3) selon leur distance aux points d'eau. Dans le volume 0 (dans la baignoire ou la douche), seuls les appareils très basse tension (TBTS 12V) sont autorisés. Dans le volume 1 (au-dessus de la baignoire), seuls les appareils spéciaux étanches sont autorisés. Les prises de courant ne sont autorisées qu'à partir du volume 3 (à plus de 60 cm des points d'eau).

## 4. Éclairage

### 4.1 Niveaux d'éclairement

Les niveaux d'éclairement recommandés (en lux) varient selon les usages : séjour 200-300 lux, cuisine 300-500 lux, bureau 500 lux, chambre 100-200 lux, salle de bain 300 lux, couloir 100 lux. L'éclairage de sécurité (BAES) est obligatoire dans les ERP et les parties communes des immeubles.

### 4.2 Technologies d'éclairage

Les lampes LED ont remplacé les lampes à incandescence (interdites depuis 2012) et les lampes fluorescentes compactes. Leur efficacité lumineuse est de 80 à 150 lm/W, contre 10 à 15 lm/W pour l'incandescence. Leur durée de vie est de 15 000 à 50 000 heures. La température de couleur (en Kelvin) détermine la teinte de la lumière : 2700-3000 K (blanc chaud), 4000 K (blanc neutre), 5000-6500 K (blanc froid).

### 4.3 Gestion de l'éclairage

Les détecteurs de présence permettent d'éteindre automatiquement l'éclairage dans les zones peu fréquentées (couloirs, parkings). Les variateurs d'intensité réduisent la consommation et permettent de créer des ambiances. Les systèmes domotiques (KNX, Zigbee) permettent une gestion centralisée et programmable de l'éclairage.

## 5. Courants faibles et domotique

### 5.1 Réseau informatique et téléphonie

Le câblage informatique (RJ45, catégorie 6 ou 6A) permet le raccordement des équipements informatiques et de téléphonie. La norme NF C 15-100 impose une prise RJ45 dans chaque pièce principale. Le tableau de communication (GTL) regroupe les équipements de distribution téléphonique et informatique.

### 5.2 Interphonie et contrôle d'accès

Les systèmes d'interphonie permettent la communication entre l'entrée et les logements. Les systèmes de contrôle d'accès (badges, codes, biométrie) sécurisent les accès aux bâtiments. Les systèmes de vidéosurveillance sont soumis à une réglementation spécifique (CNIL).

### 5.3 Domotique et gestion technique du bâtiment (GTB)

La domotique permet la gestion automatisée du chauffage, de l'éclairage, des volets et de la sécurité. Les protocoles courants sont : KNX (câblé, fiable, professionnel), Zigbee (sans fil, économique), Z-Wave (sans fil, longue portée), EnOcean (sans fil, sans batterie). La GTB (Gestion Technique du Bâtiment) est obligatoire dans les bâtiments tertiaires de plus de 290 kW depuis la RE2020.

## 6. Installations spéciales

### 6.1 Bornes de recharge pour véhicules électriques (IRVE)

Les bornes de recharge pour véhicules électriques (IRVE) sont obligatoires dans les parkings des bâtiments neufs depuis 2017. Elles nécessitent un circuit dédié (7,4 kW monophasé ou 22 kW triphasé), un disjoncteur différentiel 30 mA de type A, et un câble de section adaptée (6 à 10 mm²). L'installation doit être réalisée par un électricien certifié IRVE.

### 6.2 Panneaux photovoltaïques

Les panneaux photovoltaïques produisent de l'électricité à partir de l'énergie solaire. Ils sont raccordés au réseau via un onduleur. La puissance installée varie de 3 à 9 kWc pour une maison individuelle. L'autoconsommation (utilisation directe de l'électricité produite) est la solution la plus rentable. L'injection du surplus sur le réseau est rémunérée par ENEDIS.

### 6.3 Groupe électrogène et onduleur

Le groupe électrogène assure l'alimentation de secours en cas de coupure du réseau. Il est obligatoire dans les ERP de catégorie 1 à 4. L'onduleur (UPS) assure une alimentation sans coupure pour les équipements sensibles (informatique, médical). Il stocke l'énergie dans des batteries et prend le relais en cas de défaillance du réseau.

## 7. Vérification et contrôle

### 7.1 Vérification initiale

Toute installation électrique neuve ou rénovée doit faire l'objet d'une vérification initiale par un organisme agréé (Consuel) avant la mise en service. Le Consuel vérifie la conformité à la norme NF C 15-100 et délivre une attestation de conformité. Cette attestation est indispensable pour la mise en service par ENEDIS.

### 7.2 Vérifications périodiques

Les installations électriques des ERP et des locaux de travail doivent faire l'objet de vérifications périodiques par un organisme agréé. La périodicité est de 1 an pour les ERP de 1ère catégorie, 3 ans pour les autres ERP, et 5 ans pour les locaux de travail. Les vérifications comprennent un contrôle visuel, des mesures d'isolement et de continuité, et des essais de fonctionnement.

### 7.3 Diagnostic électrique

Le diagnostic électrique est obligatoire lors de la vente d'un logement dont l'installation a plus de 15 ans. Il est réalisé par un diagnostiqueur certifié. Il évalue l'état de l'installation et identifie les anomalies. Il n'est pas obligatoire de réaliser les travaux, mais les anomalies doivent être mentionnées dans le compromis de vente.
