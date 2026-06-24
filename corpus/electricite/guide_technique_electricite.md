---
titre: Guide Technique — Électricité du Bâtiment : Normes, Matériaux et Mise en Œuvre
auteur: Base de connaissances Bâtiment
corps_etat: electricite
source: Synthèse technique
libre_droits: true
sujets: électricité, NF C 15-100, tableau électrique, câblage, prises, éclairage, mise à la terre
---

# Guide Technique — Électricité du Bâtiment : Normes, Matériaux et Mise en Œuvre

**Corps d'état :** electricite  
**Sujets :** électricité, NF C 15-100, tableau électrique, câblage, prises, éclairage, mise à la terre

---

## Norme NF C 15-100

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

