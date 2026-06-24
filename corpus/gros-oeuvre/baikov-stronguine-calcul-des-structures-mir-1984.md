---
titre: Calcul des Structures - Manuel technique
auteur: Baïkov, Stronguine
date: 1984
corps_etat: gros-oeuvre
source: Archive.org / Éditions Mir
libre_droits: true
volume: 
sujets: calcul de structures, béton armé, résistance des matériaux, statique
---

# Calcul des Structures - Manuel technique

**Auteur :** Baïkov, Stronguine  
**Corps d'état :** gros-oeuvre  
**Source :** Archive.org / Éditions Mir  
**Sujets :** calcul de structures, béton armé, résistance des matériaux, statique

---

V. Baïkov, S. Stronguine 


CALCUL DES 
STRUCTURES 


Éditions Mir Moscou 


B. H. Bañxos, 
C. F. Crpoarux 


CTPOUTEJIBHBIE 
KOHCTPYKIUN 


CTPOAUSIAT 
MOCKBA 


V. Baikov 


S. Stronguine 


CALCUL 
DES STRUCTURES 


ÉDITIONS MIR°-MOSCOU 


Traduit du russe 
par VLADIMIR KOTLIAR 


Ha fpanyysckou asuxke 


‘(© Crpoïñïnsnar 1980 
© Traduction française Editions Mir, 1984 


PRÉFACE 


Le présent livre est consacré aux structures en béton armé, en métal 
et en maçonnerie utilisées pour la construction des bâtiments et des 
ouvrages spécialisés incorporés dans les réseaux de distribution 
et d'évacuation des eaux et dans les réseaux de transport de la 
chaleur. L'accent est mis sur les structures en béton armé, les plus 
répandues dans les domaines indiqués du Génie civil. 

La présentation des matières dans ce livre, qui est choisi en 
Union Soviétique comme ouvrage de référence pour la spécialité 
« Réseaux d’eau et de chauffage » (« Techniques sanitaires ») de 
l'Enseignement supérieur, permet à l'étudiant d’assimiler le pro- 
gramme dans un ordre logique. I] sera aussi utile pour l'établissement 
des projets, tant à l'étudiant pour ses travaux pratiques qu'à l’ingé- 
nieur confirmé. 

Les structures sont calculées suivant la méthode des états-limites 
préconisée dans les textes normatifs soviétiques. Cette méthode de 
calcul garantit une haute fiabilité de la structure au prix d’une dépen- 
se minimale des matériaux. Les solutions techniques proposées 
s’intègrent dans le cadre de l’industrie moderne du bâtiment et 
tiennent compte des impératifs de la production de masse. 

La conception et le calcul des pièces sont basés sur l’analyse de 
l’état de contrainte et de déformation de l'élément qui subit l’action 
des charges et des efforts de calcul. 

En préparant le livre à la traduction en langue française, les 
auteurs ont omis toute référence aux textes normatifs soviétiques, 
complétant en conséquence, dans la mesure du possible, les annexes 
et les chapitres correspondants. Quelques exemples concrets ont 
été ajoutés aux chapitres traitant du calcul des éléments des structu- 
res en béton armé. 


Les auteurs 


CHAPITRE PREMIER 
PRINCIPES DE CALCUL DES STRUCTURES 


$ I.1. ÉTATS-LIMITES DES STRUCTURES 


Les structures sont calculées afin de: 

— déterminer les efforts engendrés dans les structures par les 
charges appliquées ; 

— dimensionner correctement les éléments et les pièces de raccor- 
dement : 

— connaître la proportion d'armatures (pour le béton armé); 

— garantir la conservation des qualités nécessaires de la struc- 
ture pendant toute la durée prévue de son service sans consommation 
exagéréce des matériaux. 

Üne structure peut devenir apte à l'utilisation normale pour 
l'une des deux causes suivantes : 

1° épuisement de la capacité portante, c'est-à-dire ruine du maté- 
riau dans les sections les plus sollicitées, flambement ou déverse- 
ment de certains éléments de la construction ou perte de stabilité 
de la construction dans son ensemble: 

29 déformations exagérées (flexion, vibration, affaissement), 
formation ou ouverture excessive des fissures. 

Les valeurs des charges, des résistances et des déformations à 
prendre en compte dans le: calcul sont réglementées dans des textes 
officiels 1). Sensiblement variables, elles peuvent se trouver tant 
supérieures qu'inférieures aux valeurs caractéristiques. 

En Bâtiment, les structures sont calculées suivant la méthode des 
états-limites. Les structures calculées par cette méthode conservent 
leurs qualités d'utilisation même quand les écarts des charges par 
rapport aux valeurs caractéristiques atteignent les plus grandes 
valeurs observées dans la pratique et quand la qualité du matériau 
se trouve au niveau le plus bas de la gamme des qualités existantes. 

Conformément aux deùx causes indiquées plus haut, on distingue 
deux groupes d'états-limites : 

1° états-limites ultimes (perte de la capacité portante); 

2° états-limites d'utilisation (inaptitude à l'exploitation nor- 
male). 


1) En Union Soviétique dans les SNiP, ou Normes et Règles du Bâtiment 
(CHnIT — Crponrersane Hopun 1 IIpasuxra). 




Le premier groupe d'états-limites peut servir au calcul de toute 
structure. Le second groupe ne s'applique que pour les structures qui 
risquent de devenir inaptes à l’utilisation à cause des déformations 
excessives avant que leur capacité portante soit épuisée. Tel est par 
exemple le cas des dalles et poutres à grande portée dont la section 
n’est pas choisie en fonction de la résistance à assurer mais en fonction 
de la flèche admissible dans les conditions d'exploitation normales. 

Le calcul aux états-limites d'utilisation permet de limiter non 
seulement la flexion des éléments en béton armé mais aussi leur fis- 
suration (prévenir la formation des fissures dans le béton ou mainte- 
uir leur ouverture à une valeur requise). 


$ I.2. COEFFICIENTS FORFAITAIRES 


Afin de tenir compte des variations possibles de la charge et de la 
résistance du matériau, on introduit pendant le calcul certains coeffi- 
cients de prise en compte for- 
faitaires : 

19 coefficient de surcharge n 
affectant les charges appliquées; 

29 coefficient de sécurité k qui 
dépend du matériau et tient 
compte des caractéristiques de 
résistance ; 

3° coefficient de comportement 
m qui permet d'évaluer de façon 
indirecte certaines particularités 
du comportement des matériaux 
et des structures. 

Les Normesindiquent un coef- 
ficient de surcharge n > 11) 
pour chaque type de charge en 
fonction de sa variabilité, et un ee 
coefficient de sécurité À => 4 pour FIG. I.1. Courbes de distribution 
chaque matériau en fonction de 
la variabilité de sa résistance. Plus la charge (la résistance du maté- 
riau) est sujette à des variations, plus le coefficient » (4) est élevé, 
et inversement. 

Le degré de variabilité des charges et des résistances est établi 
sur la base d’une étude statistique d’un grand nombre d'essais, qui 
se traduit par des courbes de distribution (fig. [.1). Par exemple, en 
étudiant la distribution des valeurs de résistance d'un matériau 
on porte en ordonnée la fréquence des cas où l’on a observé la valeur 


Fréquence des cas 


Ecarts au-del& 


Ecarts en deçà 
de la moyenne 


de la moyenne 


1) Dans le cas où une charge trop faible présente un danger plus grave 
qu’une charge excessive, on pose x << 1. Par exemple, en calculant la résistance 
au basculement d’un château d’eau ou d’un mur de soutènement, on affecte le 


POLE HEOpEE de la construction (qui s’oppose au basculement) d’un coefficient 
n — , Li] 


de résistance portée en abscisse. Dans la plupart des cas la résistance 
se situe autour d’une valeur moyenne. Les variations par rapport à 
la moyenne (valeurs supérieures et inférieures à la valeur moyenne) 
sont d'autant moins fréquentes qu'elles sont plus prononcées. L'’al- 
lure de la courbe permet d'évaluer la variabilité de la grandeur en 
question : si la courbe est raide (a), la grandeur est peu variable, et si 
la courbe est aplatie (b), la grandeur est très variable. 


$ I.3. VALEURS CARACTÉRISTIQUES ET DE CALCUL 
DES CHARGES ET DES RÉSISTANCES 


Les charges indiquées dans les Normes pour les conditions d’exploita- 
tion normales de la structure s'appellent charges caractéristiques (ou 
normatives) q°. 

Multipliant les charges normatives par des coefficients de sur- 
charge appropriés x, on obtient les charges de calcul q: 


q —= q°n. 


On trouve quelques valeurs de q°t et de nr dans l’Annexe II. 

Les charges qui s’exercent sur la construction pendant toute la 
durée de son utilisation sont appelées permanentes. Ce sont le poids 
propre de la structure, le poids des éléments portés par la structure, 
le poids du sol (pour les ouvrages souterrains). Les charges dont la 
valeur et le point d'application peuvent changer pendant le service 
de la structure s'appellent surcharges. Ce sont les charges dues au 
poids des personnes, des meubles, de l’équipement (sur les planchers), 
la pression des matières liquides et pulvérulentes (dans les capacités), 
les effets de la neige et du vent, les efforts transmis par les ponts rou- 
lants, etc. 

Il y a aussi des surcharges accidentelles : actions sismiques, affais- 
sement irrégulier de la fondation, etc. 

En fonction de la durée possible de leur application, les surcharges 
peuvent être: 

— de longue durée: ,pression des matières liquides ou pulvéru- 
lentes dans les capacités, poids de l’équipement à poste fixe dans les 
bâtiments industriels, charge exercée sur les planchers des magasins 
et entrepôts, poids de la neige diminué de 70 kgf/m° (700 N/m°), 
une fraction de l'effort transmis_par le pont roulant, etc. ; 

— de courte durée : une fraction de la charge sur les planchers due 
au poids des personnes et au poids des matériaux entreposés autour 
des équipements en vue de leur réparation, la partie de l'effet de la 
neige et de l'effort du pont roulant non comprise dans les surcharges 
de longue durée, les effets du vent, etc. 

Les structures sont calculées en vue de résister à différentes com- 
binaisons de charges. Le cas où les charges permanentes, les surchar- 
ges de longue durée et les surcharges de courte durée interviennent en 
même temps s'appelle combinaison fondamentale. Le cas où la com- 




binaison fondamentale est augmentée d’une surcharge accidentelle 
s'appelle combinaison accidentelle des charges. 

Si la combinaison fondamentale choisie pour le calcul ne contient 
qu'une seule surcharge de courte durée (la plus caractéristique du cas 
considéré), cette surcharge est prise en compte sans minoration. S'il 
y a deux ou plusieurs surcharges de courte durée, elles sont minorées 
en multipliant leurs valeurs (ou les efforts correspondants) par le 
coefficient de concomitance nr, — 0,9. Si le calcul se fait pour une 
combinaison accidentelle des charges, toutes les surcharges de courte 
durée sont minorées en multipliant leurs valeurs de calcul (ou les 
cfforts engendrés par ces surcharges) par r — 0,8; quant à la sur- 
charge accidentelle, elle est prise en compte sans minoration. 

A titre de paramètre fondamental caractérisant la résistance du 
matériau aux efforts appliqués, les Normes indiquent la résistance 
caractéristique (ou normative) du matériau À° exprimée en kgf/cm° 
(MPa). C'est la résistance minimale que le matériau doit posséder 
en vertu des Normes d'Etat. La valeur de R°, retenue après le dépouil- 
lement mathématique d’un grand nombre d'expériences, est garan- 
tie à 95 % ; autrement dit, le matériau a 95 chances sur 100 d’avoir 
une résistance égale ou supérieure à ARC. 

La résistance de calcul R, exprimée en kgf/cm*° (MPa), est obtenue 
en divisant la résistance caractéristique ÀC par un coefficient de sécu- 
rité correspondant # > 1; dans certains cas ÀC est multiplié par un 
coefficient de comportement mn = 1 défini par le taux d'utilisation 
de la résistance du matériau en fonction du type de calcul, les par- 
ticularités du comportement de la structure dans son ensemble, les 
conditions d'exploitation, etc. : 

R= Te m. 

Les valeurs des résistances caractéristiques, des coefficients de 
sécurité et de comportement, des résistances de calcul des matériaux 
utilisés dans les structures en béton armé, les maçonneries, la char- 
pente métallique sont citées dans les Normes correspondantes !). 

Dans les calculs courants on se base généralement sur les valeurs 
de calcul des résistances. 


$ I.4. CALCUL DES STRUCTURES AUX ÉTATS-LIMITES 


Calcul aux états-limites ultimes. Il s’agit de garantir la conservation 
de la capacité portante de la structure en admettant que les charges 
peuvent être plus élevées et la résistance du matériau plus faible que 
prévu. On écrit donc à gauche l'effort engendré dans l'élément 
par les charges de calcul (en faisant intervenir les coefficients de sur- 
charge) et à droite l’effort exercé sur l’élément quand la contrainte 


1) On en trouve quelques-unes dans les chapitres III, VIII, IX du présent 
ouvrage. 




dans le matériau est égale à la résistance de calcul (c'est-à-dire en 
faisant intervenir les coefficients de sécurité et de comportement). 
Si la valeur obtenue à gauche n'est pas supérieure à celle obtenue à 
droite, la capacité portante de la structure est garantie. 

Par exemple, la formule utilisée pour le calcul d’une pièce en 
matériau homogène soumise à une traction simple se présente comme 
suit : 



> Non< Fit RE, 


Soit V la charge totale de calcul. Comme a m — R, on obtient 
la formule abrégée très usitée dans les calculs courants : 


N£ Fur. 


Pour définir la section nécessaire #,+ en fonction de W connu, 
on met le signe d'égalité dans la formule précédente. 

Calcul aux états-limites d'utilisation. Il s’agit de garantir les 
qualités d'utilisation de la structure en admettant que la résistance 
et la capacité de déformation du matériau peuvent varier. S'il est 
nécessaire de limiter les déformations (par exemple en flexion), on 
écrit à gauche la déformation f de la structure calculée en fonction 
de son schéma de calcul, et à droite la valeur limite fc de la défor- 
mation citée dans les Normes pour la structure considérée et déduite 
de façon empirique. 

La condition à garantir s'écrit ainsi: 


f< F. 


S'il est nécessaire d'éviter absolument la fissuration dans une 
structure en béton armé compte tenu des variations possibles de la 
résistance du matériau (et aussi des variations possibles de la charge 
pour certains types de structures !)), on écrit à gauche l'effort AVC 
exercé sur l’élément sous l’action des charges caractéristiques (ou W, 
sous l’action des charges de calcul), et à droite l'effort W, repris 
par l'élément immédiatement avant la fissuration du béton, compte 
tenu des coefficients de sécurité et de comportement correspondants. 

La condition à garantir s'écrit comme suit: 




N£EN, où NE. 


Si les fissures sont tolérables, on doit limiter leur ouverture. 
Dans ce cas on écrit à gauche l’ouverture des fissures a, calculée 
selon le schéma de calcul de la structure compte tenu des variations 
possibles de la résistance et de la déformabilité du matériau, et à 


1) Ce sont les structures en béton précontraint qui doivent satisfaire aux 
conditions de résistance à la fissuration de première catégorie (voir chapitre III). 




droite l'ouverture maximale des fissures af définie dans les Normes 
et établie de façon empirique pour les structures du type donné. 
La condition à garantir est la suivante: 


at — af. 


$ I.5. SYSTÈMES D'UNITÉS 


Pour le calcul des structures, les Normes et Règles du Bâtiment 
prescrivent le système d'unités suivant : 

— masse, kilogramme (kg) ou tonne (t); 

— force, kilogramme-force (kgf) ou tonne-force (tf); 

— moment de la force, kilogramme-force-mètre (kgf-m) ou tonne- 
force-mètre (tf-m); 

— charge linéique, kilogramme-force par mètre (kgf/m) ou kilo- 
gramme-force par centimètre (kgf/cm), tonne-force par mètre (tf/m); 

— charge surfacique, pression, contrainte, module de déforma- 
tion, kilogramme-force par centimètre carré (kgf/cm°), kilogramme- 
ne par millimètre carré (kgf/mm°) ou tonne-force par mètre carré 
tf/m°). 

Un tel système ne tient pas compte de la variation de l’accélé- 
ration de la pesanteur g en fonction de Îa latitude; en outre, la con- 
trainte et la charge surfacique y ont même dimension. Pour pallier 
ces inconvénients, on utilise dans denombreuses branches de la science 
et de la technique le système d'unités international SI: 

— masse, kilogramme (kg) ou tonne (t): 

— force, charge, poids, newton (N) ou kilonewton (kN); 

— moment de la force, newton-mètre (Nm): 

— charge surfacique, newton par mètre carré (N/m°); 

— pression, contrainte, module de déformation, pascal (Pa) ou 
mégapascal (MPa = 10% Pa). 

Le présent ouvrage est rédigé dans le système préconisé par les 
Normes. On trouve en Annexe I un tableau de correspondance qui 
permet de passer facilement aux unités SI (en arrondissant la valeur 
de g = 9,8 m/s? à 10 m/s°). 


CHAPITRE II 


NOTIONS SUR LE BÉTON ARMÉ 


$ IL. PRINCIPES DU BÉTON ARMÉE 


Le béton armé se compose du béton et des armatures d'acier qui tra- 
vaillent conjointement dans l’œuvre, malgré leurs caractéristiques 
physiques et mécaniques différentes. 

Le béton résiste bien à la compression et mal à la traction. L’acier 
résiste tout aussi bien à la traction qu'à la compression. Ces particu- 
larités des matériaux sont mises à profit dans le béton armé. 

Dans une pièce fléchie, la bonne résistance à la compression du 
béton est utilisée dans la zone comprimée et la haute résistance de 

l'acier à la traction dans la zone tendue; 

a) 0 le béton résiste mal à la traction et pré- 
sente des fissures en zone tendue 
(fig. II.1, a). Les poutres ne contiennent 
que très peu d’armatures (par rapport à 
la section de la pièce), qui suffisent 
cependant à améliorer très sensiblement 
le comportement en flexion: la résistance 
est plusieurs fois supérieure à celle 
ÿ | d'une pièce non armée. Les armatures 

b) | s'avèrent aussi utiles dans les pièces 
travaillant en compression (fig. [I.1, b) 

1 1 dont elles augmentent la résistance jus- 


qu'à 90 % et plus. 
2 Le béton durci adhère fortement aux 


aciers d'armature, si bien que les deux 

constituants se déforment ensemble sous 

les efforts exercés sur la pièce. L’adhé- 

] rence persiste dans le temps malgré les 

h | modifications qui surviennent dans la 

FIG. Lu en béton masse dû béton; elle n’est pas détruite 

A les variations de température (le 

aciers d’armature; 2, béton ten béton et l'acier présentant des coefficients 

n d’allongement assez voisins) et d'humidité. 

Le béton est un milieu favorable pour 

l'acier. Dans les conditions normales les armatures restent conservées 
dans le béton pendant une durée pratiquement illimitée. 

Le béton armé est durable, il résiste bien au feu, aux agents atmo- 

sphériques, aux charges statiques et dynamiques, il est suffisamment 




dense et offre un obstacle efficace à la pénétration de l’eau, des gaz, 
des rayonnements radioactifs. 

Au contraire, il se fissure facilement sous un effort de traction 
relativement faible, ce qui est généralement indésirable. En effet, 
dès que les fissures se sont produites dans la pièce, celle-ci devient 
beaucoup moins rigide et plus perméable; si les fissures s'ouvrent 
largement, les armatures sont menacées de la corrosion. 

Il existe un moyen très efficace d'améliorer la résistance à la fis- 
suration du béton armé: c’est la précontrainte. Elle consiste à faire 
naître des contraintes de compression très élevées dans le béton au 
stade de la fabrication de la pièce, avant l'application de la charge 
d'exploitation ; les contraintes sont créées dans les zones qui, dans 
l'ouvrage, seront exposées à la traction. 

On distingue deux procédés de précontrainte, appelés pré-tension 
et post-tension. 

Contrainte par pré-tension (fig. 11.2, a). Ce procédé est appelé 
également précontrainte par adhérence. I] consiste à mettre en tension 


a) 1 3 


FIG. 11.2. Pièces en béton précontraint (dans le sens axial): 


a, pré-tension ; b, post-tension ; 1, avant la mise en tension, IT, après la mise en tension ; 
J, armatures de précontrainte; 2, culées; 3, organe de mise en tension; 4, appareil d’an- 
crage; 5, rondelle de retenue 


les armatures sur des culées spéciales fixées sur le banc de bétonnage, 
le moule ou le plateau, et à les maintenir provisoirement à l'état 
tendu. Après la coulée, on attend que le béton devienne suffisamment 
dur et on libère les armatures : tout en se contractant, les armatures 
entraînent le béton avec elles par adhérence et engendrent ainsi un 
état de contrainte. Plus tard, au moment d'application de la charge, 
l'effort de traction exercé sur la pièce précontrainte se trouve diminué 
dès le début par les contraintes de compression qui existent dans le 
béton, ce qui explique justement sa tenue améliorée à la fissurætion. 

Contrainte par post-tension (fig. II.2, b). Ce procédé est appelé 
aussi précontrainte par ancrage. On fabrique d’abord la pièce en béton 
non armé ou faiblement armé présentant des canaux dans la masse 
ou des rainures en surface. Le béton étant durci, on tend les armatures 
de précontrainte dans ces canaux (rainures) et on les fixe directement 
sur le béton à l’aide de dispositifs particuliers appelés appareils d’an- 




crage. Les armatures communiquent l'effort de précontrainte au béton 
qui devient donc comprimé. Puis les canaux sont injectés avec du 
lait de ciment (coulis). Après que le ciment est devenu suffisamment 
dur, la pièce en béton précontraint est prête à la mise en œuvre. 

La précontrainte améliore très considérablement la résistance 
du béton armé à la fissuration, limite sensiblement l'ouverture des 
fissures, diminue beaucoup la déformabilité de la pièce. 

On distingue plusieurs modes de fabrication des structures en bé- 
ton armé. 

Elles peuvent être fabr iquées en usine, sur des machines perfor- 
mantes, en observant des régimes technologiques qui garantissent 
une qualité de fabrication très élevée et une économie de matériaux. 
Amenées à pied d'œuvre, les structures sont assemblées à l’aide d’en- 
gins puissants. C’est la construction en éléments fabriqués en usine, 
dits éléments préfabriqués, qui répond au mieux aux impératifs 
d'industrialisation. De plus, elle permet de réduire beaucoup les 
délais de construction. 

Les structures en béton armé peuvent aussi être coulées en place, 
c'est-à-dire sur chantier. Le procédé consiste à mettre en place des 
échafaudages, à fabriquer les coffrages, à mettre en place et fixer les 
armatures, puis à couler le béton. À la différence du premier procédé, 
la fabrication sur chantier se prête difficilement à la mécanisation. 
En effet, le béton doit rester dans le coffrage pendant toute la durée 
de son durcissement ; par temps froid, on est obligé de chauffer et de 
calorifuger le béton frais. Les structures réalisées sur place sont donc 
plus difficiles à fabriquer, moins duïables et en somme moins bonnes. 
Pour ces raisons les structures ne sont coulées sur chantier que si 
l'ouvrage est très massif, ou bien si cela est exigé par des conditions 
techniques et économiques particulières. 

On associe quelquefois les deux procédés, ce qui permet de profi- 
ter au mieux des avantages de chacun. Il y a intérêt à combiner les 
éléments préfabriqués et les éléments coulés in situ quand on réalise 
des massifs destinés à supporter des charges exceptionnelles, ainsi 
que des planchers qui seront exposés aux sollicitations dynamiques. 


$ II.2. BÉTON 


Le béton est un matériau hétérogène. La plus grande partie de son 
volume est occupée par un granulat (ou agrégat) inerte, constitué par 
des particules de dimensions différentes (pierres cassées, pierres 
roulées, sable) réunies par le ciment durci. Ce dernier est obtenu à par- 
tir de deux constituants chimiquement actifs : le ciment sec et l’eau 
(chimiquement liée et libre). 

Les processus chimiques se produisent au sein du ciment durci 
pendant une période prolongée. La résistance du béton augmente 
donc avec le temps. Son volume change légèrement en fonction de sa 
composition propre et de la composition chimique du ciment: il se 
produit un retrait ou (avec des ciments spéciaux) un gonflement. 




Quelque soigné que soit le serrage, le béton n'est jamais parfaite- 
ment dense. Afin de faciliter la mise en place du béton, on est toujours 
obligé d'augmenter la quantité d’eau au-dessus de la quantité néces- 
saire pour le gâchage (réaction chimique avec le ciment). L'eau en 
excédent s’évapore et fait naître des canaux capillaires dans le ciment 
durci et des vides sous les gros granulats et les barres d’armature. 
L'eau et le gaz peuvent se propager dans la masse du béton en emprun- 
tant ces vides et aussi, en partie, les canaux capillaires. Le béton de- 
vient donc partiellement perméable à l’eau et aux gaz; cette parti- 
cularité doit être prise en considération en construisant des réseaux 
de distribution d’eau et de chauffage. 

On peut diminuer la porosité en réduisant la teneur en eau initiale 
du béton frais, en serrant soigneusement ce dernier et en introduisant 
des adjuvants chimiquement actifs qui gonflent au contact de l’eau. 

La caractéristique mécanique fondamentale du béton est sa résis- 
tance à la compression. Elle dépend de la résistance du ciment durci, 
de la qualité du granulat et de la densité du béton. Le ciment durci 
est d'autant plus résistant que la classe du ciment est élevée et le 
rapport eau/ciment est bas. Pour le béton lourd (le plus utilisé dans 
les réseaux de distribution d’eau et de chauffage), on utilise des gra- 
nulats denses, plus résistants que le ciment durci. La résistance du 
béton est alors plus élevée si les granulats présentent une surface 
rugueuse (meilleure adhérence avec le ciment durci). Les pierres cas- 
sées sont donc à préférer aux pierres roulées (gravier). Le béton est 
d'autant plus élevé que sa densité est forte. 

La résistance du béton à la compression est exprimée dans sa 
classe (ou marque), qui n’est autre que la charge de rupture en com- 
pression (en kgf/cm? ou MPa) d’un cube en béton de 150 mm de côté. 
L'âge réglementaire des échantillons de contrôle (c'est-à-dire le délai 
de durcissement du béton) est égal à 28 jours pour les structures cou- 
lées in situ et un peu plus court pour les éléments préfabriqués, en 
fonction du mode de fabrication et de durcissement. 

Les Normes et Règles du Bâtiment mentionnent les classes de 
résistance en compression suivantes : 

— pour le béton lourd: M 100, M 150, M 200, M 250, M 300, 
M 350, M 400, M 450, M 500, M 600, M 700, M 800: 

— pour les bétons légers de granulats poreux : M 35, M 50, M 75, 
M 100, M 150, M 200, M 250, M 300. 


La résistance sur cube R est définie par l'essai de compression 
des échantillons normalisés maintenus dans des conditions contrôlées, 


en utilisant la formule 




où M est la charge de rupture en N (kgf) et F la section du cube en 

Pendant la compression, les dimensions du cube diminuent dans 
le sens de l'effort appliqué et augmentent en sens ‘ss (fig. II.3). 




C2 ærnnta DE - 15 


Les essais de traction ont montré que le béton présente en traction 
une déformation relative limite de 10 à 20 fois inférieure à celle en 
compression. La ruine de l'échantillon se produit par extension 
transversale du matériau entraînant la fissuration. Dans le cas où 
rien ne s'oppose aux déformations transversales (les faces de l’échan- 
tillon étant graissées, fig. IL.3, a), les fissures s’orientent parallèle- 
ment à l'effort de compression ; si la dilatation transversale est gênée 


FIG. II.3. Essai de compression du béton sur cube: 


a, faces lubrifiées; b, faces non lubrifiées; 1, fissures; 2, 
couche de lubrifiant; #, contraction parallèle aux efforts de 
compression ; v, dilatation dans le sens transversal 


par le frottement sur les faces (absence de lubrifiant, fig. I[.3, b), 
les fissures sont dirigées sous un certain angle par rapport aux efforts 
appliqués. Dans le second cas le béton présente une résistance à la 
compression beaucoup plus élevée (de 2 à 2,5 fois). Les Normes pres- 
crivent de faire l'essai sur cube sans lubrifiant. 

Dans le cas où l'échantillon a la forme d’un prisme, l'effet du 
frottement sur les faces est inversement proportionnel au rapport 
de la hauteur du prisme au côté de sa base, au point de devenir in- 
signifiant dès que la hauteur devient égale ou supérieure à 4 fois le 
côté de la base. Les essais ont montré que la résistance à la compres- 
sion sur prisme est de 20.à 30 %r- inférieure à la résistance sur cube. 

En traction axiale, le béton présente une résistance de 10 à 15 fois 
plus petite que la résistance en compression sur cube. Un essai de 
flexion sur une poutre en béton permet de voir que la résistance à la 
traction du béton est d'environ 70% plus grande que sa résistance à 
la traction axiale. 

Les Normes précisent en outre, pour le béton lourd, d’autres clas- 
ses : 

— classes de résistance à la traction, kgf/cm°: P 10, P 15, P 20, 
P 25, P 30, P 35, P 40; 




— classes de résistance au froid, en fonction du nombre de cycles 
gel-dégel imposés à l'échantillon : Mps 50, Mps 75, Mps 100, Mps 150, 
Mp3 200, Mps 300, Mps 400, Mps 500; 

— classes d'étanchéité à l’eau, en fonction de la pression d’eau 
en kgf/cm? qui ne provoque aucune fuite à travers l'échantillon: 
B2,B4,B 6, B 8,B 10,B 12. 

Ces classes sont prévues pour les ouvrages conçus pour des con- 
ditions d'exploitation particulières. 

Le béton est un matériau anélastique. I] présente une dépendance 
non linéaire entre les contraintes o et les déformations relatives e 


FIG.II.4.Courbecontrain- FIG. 11.5. Courbes contrainte-déformation du bé- 


te-déformation du béton ton (charges durables et constantes) : 
(charge simple; de courte à, pour différentes durées des essais: b, sous une charge 
durée) : constante prolongée 


1, déformations totales élas- 
toplastiques: 2, déformations 
élastiques 


(fig. II.4). La déformation totale e; se compose d’une déformation 
élastique (instantanée, réversible) es, et d’une déformation plastique 
(prolongée, irréversible) e,,. En cas d'application d’un effort unique 
de courte durée, la part des déformations plastiques est d'autant plus 
grande que la contrainte est plus forte. 

L'’effort étant appliqué pendant une durée t plus longue, la défor- 
mation du béton devient de plus en plus différente de la déformation 
élastique (fig. II.5, a); la contrainte o, restant la même, la défor- 
mation croît en fonction de t. 

Une autre particularité du béton est son fluage, c'est-à-dire Ya 
croissance spontanée des déformations consécutive à un état de con- 
trainte constant et prolongé du matériau (fig. II.5, b). Dans l'ouvrage 


les déformations de fluage s'’amortissent à la longue, tendant asymp- 


totiquement vers une limite el. 


Le fluage est une propriété du ciment durci. Il est d’autant plus 
grand que le dosage en ciment est plus élevé, que le béton frais con- 
tient plus d’eau au moment initial et que le béton est moins âgé au 


2—0948 17 


moment d'application de la charge. Le fluage dépend de l'intensité 
des contraintes: plus les contraintes dans le béton sont fortes, plus 
le fluage est important. Le fluage dépend également du type de ci- 
ment, décroissant dans l’ordre suivant : ciment portland avec laitier — 
ciment portland ordinaire — ciment portland à résistance élevée — 
ciment alumineux. 

C’est dans les premiers mois de service de l’ouvrage que le fluage 
du béton se manifeste le plus, atteignant sa valeur limite el" au 
bout de quelques années; cette valeur peut être 2 ou 3 fois supérieure 
aux déformations élastiques. Le fluage du béton exerce une influence 
considérable sur l’état de contrainte et de déformation de la structure 
en béton armé. 

Les propriétés élastiques du béton sont évaluées par son module 
d'élasticité initial E;,, défini par essai de compression sur prisme 
suivant la partie initiale de la courbe représentative du rapport o/e 
(voir Annexe III). 

Le module de déformation totale du béton, ou module d'élasticité- 
plasticité Ey, est une quantité variable. La relation entre Æ, et Eÿ 
est déduite, conformément à la figure II.4, des relations 


Op — E Lea ; Op = Eÿ (£a SE Ep1) ; 


EE  p, =vE, où ue (th 
Eg] + Epl u Eg + Epl° 


Le coefficient v traduit le rapport de la partie élastique de la 
déformation du béton à sa valeur totale. Les valeurs empiriques dev 
pour le béton comprimé varient entre 1 et 0,2 ou 0,15. Les Normes 
indiquent les valeurs de v en tenant compte de l'humidité de l'air. 

Le béton résiste remarquablement au feu, s’avérant très supérieur 
à beaucoup d’autres matériaux au point de vue de la conservation de 
la capacité portante et des qualités d'utilisation des structures. 

Le béton lourd ordinaire peut être mis en œuvre dans les structures 
qui sont souvent exposées à des températures de 50 à 200 °C. Comme 
liant on utilise le ciment portland sans ou avec laitier, et comme 
granulats, les granits, les dolomies, les svénites, les roches calcaires 
dures, elc. 

Si la température d'utilisation normale de la structure dépasse 
200 °C, on utilise le béton réfractaire. Comme liant, on utilise, en 
fonction de la température d'échauffement, le ciment alumineux, le 
ciment portland, le verre soluble additionné d'agents durcissants 
(fluosilicate de sodium. résidu d'extraction de l’alumine à partir de 
la néphéline) et de produits finement moulus (chamotte, magnésite, 
laitier, cendres, etc.). Les granulats du béton réfractaire sont consti- 
tués de chromite, diorite, basalte, diabase, andésite, débris de cha- 
motte et de briques, laitier de haut fourneau, scorie d'incinération. 

Le béton est un matériau très durable. Dans les conditions nor- 
males il conserve sa structure et sa résistance pendant une durée 
pratiquement illimitée. Au contraire, il se dégrade prématurément 




dans un milieu agressif gazeux (gaz acides et haute humidité), liquide 
(solutions d'acides et d’alcalis, sels liquides, solvants, huiles, solution 
de sucre) ou solide (poussières agressives dans l’air humide, charbon, 
nombreux minerais, sels, scories, etc.). 

Pour améliorer la tenue du béton aux agents agressifs, on peut: 

— augmenter sa densité en modifiant sa composition, en utilisant 
un ciment approprié et en appliquant une méthode de serrage efficace ; 

— réduire sa perméabilité en réduisant le rapport eau/ciment 
et en introduisant des adjuvants spéciaux ; 

— employer des liants et granulats qui résistent bien aux acides. 

Pour protéger les structures en béton, on utilise différents moyens 
choisis en fonction de l'agressivité du milieu. On peut par exemple: 

— améliorer la tenue aux agents agressifs du béton lourd ordi- 
naire ; 

— protéger la surface du béton par des procédés spéciaux, tels 
que la fluatisation, l’imprégnation avec des produits à haut poids 
moléculaire, l'application des vernis, peintures, résines époxydes; 

— mettre en place une couche protectrice en dalles céramiques 
ou en béton de plastique contenant des liants ou adjuvants polymères. 

En plus du béton lourd ordinaire, on utilise aussi en génie indus- 
triel et civil: 

— les bétons sans ciment de granulats compacts (béton silico- 
calcaire, bétons à liants à base de laitier, béton de plâtre); 

— les bétons de granulats poreux (argile expansée, agloporite, 
laitier expansé, perlite, tuf, etc.); 

— les bétons cellulaires. 

Aucun de ces bétons n’est utilisé pour les structures portantes des 
ouvrages courants des réseaux de distribution d’eau et de chauffage, 
à l'exception de certains bétons de granulats poreux que l’on utilise 
dans l'isolation des canalisations de gaz. 

En fonction de la masse volumique, on distingue les bétons lourds 
(masse volumique p, >> 1800 kg/m*) et les bétons légers (pp < 
< 1800 kg/m*). Les Normes mentionnent également les bétons par- 
ticulièrement lourds (p, > 2500 kg/mÿ), allégés (1800 kg/m° < 
<< pr L 2200 kg/m°) ct particulièrement légers (p, 500 kg/m*). 


$ IL.3. ARMATURES 


Les armatures incorporées dans le béton servent essentiellement à 
encaisser les efforts de traction dans les pièces fléchies et tendues et 
à renforcer les sections des pièces comprimées. La quantité d’arma- 
tures est calculée de façon à assurer la résistance aux charges détermi- 
nées. Ces armatures sont appelées armatures principales. 

D'autres armatures, dites armatures de montage, sont mises en 
place afin de reprendre les efforts provenant du retrait et des défor- 
mations thermiques du béton, des charges de montage, de maintenir 
les armatures principales à leur position prévue dans le plan de fer- 
raillage, ainsi que pour réaliser certaines autres fonctions. 


2* 19 


a, treillis de fils; b, carc: 


de barres: c, carcasse tridimensio e de barres 


FIG. 11.6. Constitution des pièces en béton arm 
ca C 


LA l [A — 


AN TE 


DITITF".) 


FN IN 


FIG. 11.7. Barres à haute adhé 


a, classe A-J1; b, classe A-IIT; c, classes 


asses planes de barr 
(cage); 1, dalle, 2, poutre, 3, poteau 


rence. 
A-I1V et AV 


Les armatures principales et de montage sont réunies par soudure 
et par ligatures en treillis (grilles) et cages (carcasses) planes ou tri- 
dimensionnelles que l’on dispose d’une façon déterminée dans les 
pièces en béton armé (fig. II.6). 

Les armatures d'acier utilisées dans le béton armé sont fabriquées 
en barres laminées à chaud et en fils étirés à froid. 

On entend par barre une armature de diamètre quelconque 
qu’elle soit livrée dressée ou enroulée. Après le laminage à chaud, 
les aciers peuvent être durcis thermiquement ou par étirage à froid. 

Les aciers mis en tension avant leur mise enÿplace dans le béton 
s'appellent armatures de précontrainte. 

Selon la nature de la surface, on distingue les aciers lisses et les 
aciers à haute adhérence. Ces derniers sont obtenus en façonnant des 
crénelures et des nervures à la surface des barres (fig. II.7) et des em- 
preintes à la surface des fils. 

Les barres d'armature sont divisées en six classes en fonction de 
leurs caractéristiques mécaniques principales: A-I (Tableau II.1), 
A-IT, A-III, etc. Les aciers durcis sont identifiés à l’aide d’un symbole 
supplémentaire Tr (durcissement thermique), par exemple: ArT-V. 
Chaque classe peut comprendre plusieurs nuances d'acier. 

La désignation de la nuance indique sommairement la composition 
chimique de l’acier. C’est ainsi que la désignation 251 2C donne les 
renseignements suivants sur l'acier: 

— Île chiffre 25: la teneur en carbone en centièmes de % (soit 
0,25 %) : 

— la lettre l: l'acier est allié au manganèse; 

— Je chiffre 2: la teneur en Mn peut atteindre 2 % ; 

— Ja lettre C: l'acier contient du silicium. 

La lettre X figurant dans la désignaticn de la nuance 20XT2I 
signifie que l'acier est allié au chrome. 

Les barres d'acier des classes A-IV, A-V et de toutes les classes Ar 
sont destinées à la précontrainte. 

Les fils d'armature sont divisés en deux classes: 

— classe B-T (lisse), Bp-I (à haute adhérence): fils ordinaires non 
destinés à la précontrainte, à bas carbone, fabriqués par étirage à 
froid (écrouis) ; 

— classe B-IT (lisse), Bp-II (à haute adhérence): fils à haute ré- 
sistance, à carbone moyen, fabriqués par étirage à froid et tréfilés, 
destinés à la précontrainte. 

Les fils peuvent aussi être mis en œuvre sous forme de câbles 
fabriqués en usine. On utilise comme armatures de précontrainte 
des câbles torsadés des classes X-7, K-19 à sept et à dix-neutfils 
respectivement (fig. [II.8, a), ainsi que des câbles à torons multiples 
de classe À X N, où est le nombre de torons. Dans le même but, 
on utilise également des câbles non torsadés (fig. II.8, b) formés de 
fils ou torons droits disposés généralement suivant une circonférence, 
fixés par des spirales ou étoiles particulières et retenus aux extrémités 
dans des appareils d'ancrage appropriés ; les fils (torons) sont agencés 




TABLEAU II.1 
Classes des aciers d’armature 


: | Ch: d - Lim 
Nature et classe Nuances PRES: ire actions d’ élastieité MPa 
MPa (kgf/cm?) (kgf/c cm2) 

Barres lisses | Cr3cn3; 6-40 380(3800) 240(2400) 
laminées à Cranc3; » 
chaud, AI CT3Kn3; » 

BCr3cn2; » 

BCT3nc2; 

BCT3Kn2; 

BCr3Tuc2 6-18 
Idem, A-IT BCr5cu2; 10-40 500(5000) 300(3000) 

BCrouc2; 18-40 

18r2C 40-80 

40TT 10-32 
Idem, A-III |35rC: 2572C | 6-40 | 609(6000) | 400(4000) 
Idem, A-IV 80C | 10-18 900(9000) 600(6000) 

20XT2L 10-22 
Idem, A-V |28X272T | 10-22 | 1050(10 500) | 800(8000) 
Barres durcies — 10-25 900(9000) 600(6000) 
thermique- 
ment, AT-IV 
Idem, Ar-V | es | 10-25 | 1050(10 500) | 800(8000) 
Idem, Ar-VI | — | 40-25 | 1200(12 000) | 1000(10 000) 
Fils ordinaires — 500(5000) — 
lisses, B-I 
Idem, à haute — 525-550 — 
adhérence, Bp-I (5250-5500) 
Fils à haute . «3-8 1900-1400 — 
résistance, lis- (19 000- 14 000) 
ses, B-II 
Idem, à haute 1800-1300 — 
adhérence, (18 000-13 000) 
Bp-Il 




en groupes, de façon à laisser des espaces vides par lesquels le coulis 
de ciment pénètre à l’intérieur de l’armature. Les fils (torons) peuvent 
être disposés en une seule rangée ou en rangées multiples. 

Les caractéristiques mécaniques des aciers d’armature sont déga- 
gées de façon empirique à partir des essais de traction, en déterminant 


la relation entre la contrainte © et la 
déformation relative € (fig. II.9). Si 
l'acier présente un palier d'écoulement 
(fig. II.9, a), on détermine limite d'élas- 
ticité (ou d'écoulement) apparente 64: 
c'est la contrainte (mesurée en MPa ou 
en kgf/cm*) au-delà de laquelle l’éprou- 
vette se déforme sans que la charge aug- 
mente sensiblement. Si l’acier n'a pas 
de palier d'écoulement (fig. II.9, b), on 
détermine la limite d'élasticité (d'écou- 
lement) conventionnelle 652: c'est la 
contrainte (mesurée toujours en MPa ou 
kgf/cm*) qui produit une déformation 
relative résiduelle égale à 0,2 %. 

La limite d'élasticité og peut être 
augmentée par écrouissage de l’acier: ce 
procédé consiste à soumettre l’armature à 
une précontrainte jusqu'à une valeur 
Ogg >> Ga et à l’abandonner ensuite. 
L'acier écroui se déforme suivant:un 


FIG. II.8. Câbles d’arma- 
ture : 


«, toisadé; b, droit; 1, vue de 

profil d’un câble torsadé à sept 

fils; 2, 3, vues en section des 

câbles torsadés à sept et à dix- 

neuf fils; 4, fils droits; 5, gaine; 
6, spirale; 7, fil court 


diagramme dit court (courbe O'A'B" sur la figure II.9, a), présen- 


tant une limite d’élasticité élevée. 




0,2% 


FIG. 11.9. Diagrammes de traction des aciers d’armature: 
a, avec palier d'écoulement; b, sans palier d'écoulement 


Une autre caractéristique fort importante des propriétés méca- 
niques de l'acier est sa charge (ou limite) de rupture o,: c'est la plus 
grande contrainte que l’éprouvette subit sans se détruire. 




Les nuances d’acier utilisées dans l’armature présentent une haute 
limite de proportionnalité; il s'agit de la contrainte au-delà de laquelle 
la déformation cesse d'être directement proportionnelle à la contrain- 


FIG. II.10. Treillis soudés: 


a, en rouleau; b, en nappe 


te. Cette qualité précieuse de l’acier permet d'appliquer des forces 
très élevées pour la précontrainte. Comme limite de proportionnalité 
Go,02, On adopte conventionnellement la contrainte (mesurée en MPa 


FIG. 11.11. Carcasses soudées : 
a, planes; b, tridimensionnelle (cage) 


ou kgf/cm*) qui provoque une déformation relative résiduelle de 
0,02 %. 

L’acier d'armature possède une bonne plasticité, qui prévient la 
rupture brusque (fragile) de la structure en béton armé par déficience 




de l’armature. La plasticité est caractérisée par la valeur de l'allonge- 
ment relatif total de rupture 6, % (variation de la longueur initiale de: 


l’éprouvette, la longueur de stric- 
tion y comprise) et la valeur de 
l'allongement relatif uniforme ô,n, % 
(variation de la longueur initiale 
de l’éprouvette, la longueur de 
striction non comprise). Pour les 
classes ÂÀ-I, A-IT, A-III l’allonge- 
ment relatif de rupture est égal à 
25, 19 et 14 % respectivement ; 
pour les autres classes il varie entre 
8 et 4 %. 

Les diamètres figurant dans les 
catalogues des aciers d’armature 
(voir Tableau II.1 et Annexe VIII) 
sont des diamètres conventionnels. 
Autrement dit: 

— pour les barres à haute 
adhérence ce sont les diamètres des 
barres rondes lisses de même sec- 
tion ; 

— pour les fils ordinaires et à 
haute résistance, à haute adhérence, 
les diamètres avant le façonnage 
à empreintes ; 

— pour les câbles, les diamè- 
tres des cercles circonscrits. 

Les treillis soudés sont fabri- 
qués (fig. I[.10) en assemblant les 
barres longitudinales et transver- 
sales par des points de soudure par 
résistance à leurs croisements. Les 
treillis peuvent être livrés en nap- 
pes planes ou en rouleaux. Les treil- 
lis en nappes ont la largeur totale 
maximale B = 2,9 m, la longueur 
L=9 m; la largeur maximale 
des treillis en rouleaux est B — 
— 3,959 m, et leur longueur est 
choisie de façon que le poids 
du rouleau soit d’environ 100 à 
000 kg (Bet L sont les distances 
séparant les barres extrêmes). 
Les treillis soudés sont confec- 


Sa _ | 
(4d) ‘ 


FIG. 11.12. Types de jonctions sou- 
dées des barres: 


1, soudure bout a bout par résistance: 
2, soudure par bain de fusion sur sup- 
port en U; 3, soudure par bain de 
fusion à la molette sur support en U: 
4, soudure à l’arc électrique avec cou- 
vre-joints (quatre soudures latéral: 
5, idem, à recouvrement (deux soudures 
latérales); 6, soudure à l’arc sur plat, 
cornitre, profilé (deux soudures latérales) 


tionnés à partir des fils à bas carbone étirés à froid de clas- 
se B-I, de 3 à 5 mm de diamètre, et de barres à haute adhérence 
laminées à chaud, en acier faiblement allié, de classe A-III, de 6 à 




‘0 mm de diamètre. Pour les treillis en rouleaux, le diamètre des barres 
longitudinales ne doit pas dépasser 7 mm. Les treillis sont désignés 
par une fraction dont le numérateur indique leur constitution 
(t/t./d/d,) et le dénominateur, les dimensions hors tout (Z X L). 
POP: il est constitué de barres 
longitudinales de diamètre d — 4 mm espacées de t — 150 mm 
et de barres transversales de diamètre d, — 3 mm espacées de {, — 
— 250 mm; sa largeur est B — 1100 mm et sa longueur Z = 
— 5900 mm. 

Pour un treillis en rouleau, on n'indique dans le dénominateur 
que sa largeur. 

Les carcasses soudées sont faites de barres longitudinales et trans- 
versales. Elles peuvent être planes ou tridimensionnelles (cages) 
(fig. II.11). En dessinant une carcasse, on doit prendre en considé- 
ration les particularités du soudage résumées dans le Tableau sui- 
vant : 


Soit par exemple un treillis 


Rapport des diamètres des barres assemblées 
par points de soudure par résistance 


Diamètres des barres 
allant dans un sens, 


3-12 14 , 16 18 ; 20 22 25-32 36 ; 40 


Diamètres minimum 
-admissibles des 
barres allant dans 
l'autre sens, mm 3 4 si] 6 8 10 


Il est déconseillé d'utiliser pour les carcasses soudées les aciers à 
mauvaise soudabilité (classe A-IV). Les espacements des axes des 
barres uw doivent être multiples de 50 mm. 

Les jonctions des barres dans le sens de la longueur sont générale- 
ment réalisées par soudure bout à bout par résistance ou par soudure 
sous laitier dans un moule de cuivre. Sur chantier, les jonctions 
sont faites par bain de fusion ou à l’arc électrique avec des couvre- 
joints en Ü ou bien à l’arc électrique avec des couvre-joints à deux 
faces ; dans certains cas les barres sont soudées à recouvrement. La 
figure II.12 présente les principaux types de jonctions soudées des 
barres. = TT: 

Les armatures durcies des classes Bp et Ar perdent leur dureté 
pendant le soudage; au lieu de les souder, on les utilise donc coupées 
à longueur conformément aux bordereaux de commande passées 
aux aciéries. Dans certains cas les barres en acier durci sont réunies 
-dans le sens de la longueur à l’aide des frettes. 

Dans les sections de la structure où la résistance de l’armature 
n'est pas utilisée complètement, il est permis de joindre les barres 
de classe non supérieure à A-IIT, dans le sens de la longueur, sans 




soudure mais en laissant une longueur de recouvrement L,, non 
inférieure aux valeurs indiquées dans le Chapitre suivant. Une telle 
jonction est toutefois à déconseiller, car elle entraîne une dépense 
excessive de l’acier sans garantir une réunion parfaite. 

On utilise également comme armatures des profilés d'acier: 
cornières, aciers en T, etc. Les armatures de ce type sont appelées 
rigides. 


$ II.4. PRINCIPALES PROPRIÉTES DU BÉTON ARMÉE 


Associés dans le béton armé, l’acier et le béton exercent une influence 
positive l’un sur l’autre, tant sous les charges appliquées que pendant 
les variations de la température, le retrait et le fluage du béton. Les 
armatures enrobées dans le béton se trouvent à l’abri du feu et de la 
corrosion. 

Dans les pièces en béton armé exposées aux sollicitations énu- 
mérées, l’acier et le béton travaillent conjointement, grâce à la 
bonne adhérence suivant la sur- 
face de contact. 

La force d’adhérence est évaluée 
à l'aide des tests d’arrachement 
(ou d’enfoncement) des armatures 
enrobées. Les études ont mis en 
évidence la distribution irrégu- 
lière des contraintes tangentielles 
suivant la longueur de l’armature 
enrobée dans le béton; les contrain- 
tes reportent graduellement les 
efforts normaux de la barre et les 
transmettent sur le béton (fig. 11.13). 
La contrainte d'adhérence moyen- 
ne entre l'acier et le béton se 
définit par l'expression 

Hdlenr * 


Tmoy — 
Tadh, max 
Pour les aciers lisses elle atteint 

environ 2,9 à 9,9 MPa (25 à FIG. II.13. Adhérence acier-bé- 
35 kgf/cm?). L'adhérence est d'au- ton : 

tant plus forte que le rapport  s,épruretiss b dlagramme des etorts 
eau/ciment est moins élevé, que le des forces d'adhérence À la ‘surface 
béton est mieux serré et qu'il est PR æ 
plus âgé. 

Les forces d’adhérence sont plus élevées à l’enfoncement de la 
barre qu'à son arrachement du béton, car le béton s'oppose à la dila- 
tation transversale de la barre comprimée. Les aciers crénelés pré- 
sentent une adhérence deux ou trois fois plus haute que les arma- 


tures lisses. 


Avant la fissuration de la pièce exposée aux sollicitations exté- 
rieures, l'acier et le béton se déforment ensemble; la distribution 
des efforts dans ces matériaux est fonction des sections respectives 
et des modules d’élasticité. Après la fissuration du béton tendu 
l’état de contrainte devient plus compliqué (voir $ V.2 et VI.6). 

Au cours du retrait du béton, les armatures s'opposent aux défor- 
mations libres du béton; il en résulte des compressions dans l'acier 
et des tractions dans le béton. Dans certaines conditions le béton 
tendu se couvre de fissures. Les déformations générales du béton 
armé sont beaucoup moins grandes que dans le béton non armé et 
dépendent de la proportion des armatures. 

Les aciers d’armature s'opposent tout aussi bien au fluage du 
béton. La charge étant appliquée pendant une période prolongée, 
il se produit une redistribution des efforts entre le béton et l’acier. 
Par exemple, une pièce soumise à un effort de compression constant 
et prolongé présente à la longue des contraintes moins grandes dans 
le béton et des contraintes plus fortes dans les armatures. À cause 
de la déformation gênée du béton, le fluage dans les pièces en béton 
armé est 1,5 à 2 fois moins grand que dans les pièces en béton non 
armé. 

Le retrait du béton et les variations de la température, provoquant 
la variation de la longueur initiale des pièces en béton armé, peuvent 
faire naître des contraintes internes dans les constructions et même 
occasionner la ruine de certaines pièces. Pour y remédier, on laisse 
des espaces libres, dits joints de dilatation et de contraction, dans les 
ouvrages de grandes dimensions. 

Soumises périodiquement à des températures élevées (50 à 200 °C) 
les structures en béton armé deviennent moins solides et moins rigi- 
dés. C’est la raison pour laquelle, au cours du calcul, on procède à 
la minoration des caractéristiques des matériaux constitutifs du bé- 
ton armé. Si la structure est étudiée en vue du fonctionnement à une 
température très élevée (au-delà de 200 °C), tous les éléments por- 
tants seront fabriqués en béton réfractaire (voir $ II.2). 

Le béton armé, tout comme le béton non armé, est assez durable 
dans les conditions normales mais risque de se dégrader prématuré- 
ment en milieu agressif, principalement à cause de la corrosion du 
béton. Le lecteur a vu quelques recommandations sur la protection 
du béton contre la corrosion dans le $ 11.2. 


CHAPITRE III 


PARTICULARITÉS DE CALCUL ET DE CONCEPTION 
DES PIÈCES EN BÉTON ARMÉ 


$ III.1. GÉNÉRALITÉS SUR LE CALCUL 


Les structures en béton armé sont calculées pour résister aux 
charges de calcul. On choisit une combinaison déterminée de charges 
et l’on retient les valeurs de calcul de résistance du béton (Annexes 
III, IV) et de l’acier (Annexes VI, VIT) indiquées dans les Normes 
pour les états-limites ultimes et les états-limites d'utilisation. 

La résistance à la fissuration des structures en béton armé doit 
répondre aux exigences classées en trois catégories, en fonction des 
conditions de service et du type des armatures. 

La première catégorie couvre les constructions qui doivent être 
parfaitement imperméables : les réservoirs, les conduites de refoule- 
ment, les structures à armatures à haute résistance. Dans ces cons- 
tructions. la fissuration est inadmissible en raison des conditions 
d'utilisation particulières. En calculant leur résistance à la fissura- 
tion, on fait la majoration des charges en les affectant d'un coeffi- 
cient desurcharge #7 > 1, introduit dans le calcul de résistance méca- 
nique. 

Les exigences de la deuxième catégorie admettent une ouverture de 
fissures de courte durée, à condition qu'elles soient refermées ensuite 
complètement. Il s’agit des constructions à l'air libre et des structu- 
res armées avec des fils à haute résistance. Le calcul à la fissuration 
(dont le but est de voir s’il est nécessaire de vérifier l'ouverture des 
fissures de courte durée et leur fermeture) se fait en affectant les 
charges d’un coefficient » > 1. Le calcul à l'ouverture et à la fer- 
meture des fissures se fait en prenant nr — 1. 

Dans la troisième catégorie, on admet une ouverture limitée des 
fissures de courte et de longue durée (structures armées avec des 
barres d'acier). Le calcul à la fissuration (afin de voir s’il est néces- 
saire de vérifier l’ouverture des fissures) et le calcul à l'ouverture des 
fissures se font en affectant les charges d’un coefficient n = 4, 

Comme paramètres normalisés de résistance du béton, on adopte 
les résistances caractéristiques à la compression (axiale) sur cube A, 


les résistances caractéristiques à la compression sur prisme ÆR;,, les 


résistances caractéristiques à la traction R*, ainsi que les résistances 
de calcul pour les états-limites ultimes À, R,,, R+ et pour les états- 
limites d'utilisation Ry:rr, Rtrr- 




— | Gr'o G FO | Sr'0 € €‘O | 7'0 £ £'o | 7'0 & 8907 UN SUP s,9n71S S91N19n1)S 


— |S0'0! & — |SrO! 2 £'O | 7'0 £ g'o | ‘0 (4 onbrieauyd neoaru np snssop 
-Nt SJ119JU9 NO OIQIJ IIB,[ € SoBvIANO 


— | G0'‘0 c —_ l'O 4 c'O | £‘0 Ç z‘0o | £‘0 ç sojuopnigaqnd soouejsqns s9p uolssaiq 


—- —  — | ol z |z'o leo! e |z'oleol e oœout1duos juow: 


-2[[0111ed Pope 
A onbresiqd 
À NEJAIU np  snossop 
= se } Fu — } ES ES l F0 c'0 S onpuoy JUowU |-ne SHII9JU0 SOBPIANO 


-0191U9  U01199S |['SOPIN[J S0P UOISSII 


PL D bo 5 | 2108 lp eg, [po 3, | 208 |pi 3, [po :j, | 1108 | pi -5, | po y, | o1108 


9109 -9109 


uu g & p anod WU YZp inod L-Y L-déf ‘I-£ ‘A-2v 7 : SUOIJON1)SU09 Sup JIIAIYS OP SUOIJIPUOI 
L-M ‘II-dg ‘II-4 1I-d€ ‘II-Œ ‘IA-LV |'A-V ‘AI-LV ‘AI-V III-V [IV I-V 
EE  * 
S9IN]PWIIE Sp Sosse[N 
TT …—…—"—"——"————"— —— 
un ‘JD 591nSSI} SP 2JeWIXPU 21n)19ANQ "UOTJUANSSIT U[ E 92UU)SISHDI U[ 9P SIA-E-SIA SOOU9SIX9 SOp So1103978) 


» » e 


Dans le texte qui suit, toutes les valeurs citées se rapportent auw 
béton lourd qui est le plus employé dans les réseaux de distribution 
d’eau et de chauffage. 

La résistance caractéristique sur cube se définit en fonction de la 
classe de résistance M du béton, c’est-à-dire de la résistance à la 


compression axiale du cube À (mesurée en MPa ou en kgf/cm°), à 
l’aide de la formule 


Re = R (4 — 1,64), 


où test le coefficient de variation de Îla résistance, égal à 0,135 pour. 
le béton lourd ; 1,64 est le facteur qui garantit que les valeurs caracté- 
ristiques de la résistance sont égales ou supérieures à la valeur indi- 
quée dans 95 cas sur 100. 

La résistance caractéristique sur prisme est calculée à l’aide de la. 
formule empirique 


 — RC(0,77 — 0,0001R), mais > 0,72Rc. 


Lesrésistances caractéristiques du béton sont données en AnnexelIlIl. 
Pour obtenir les résistances de calcul du béton R,,, R+ (voir. 


Annexe IV), on divise les résistances caractéristiques Rj;, Rt par 
des coefficients de sécurité dépendant du matériau (béton) k. 
Pour le béton lourd, au calcul suivant les états-limites ultimes, on 
prend en compression k,,. — 1,8 et en traction (la résistance caracté- 
ristique du béton à la traction axiale n'étant pas contrôlée) k,,4 = 
— 1,5; au calcul suivant les états-limites d'utilisation, on prend 
kpe = kp.t = 1. 

Dans certains cas les résistances de calcul du béton sont majorées 
ou minorées en les multipliant par des coefficients de comportement 
du béton »7,, indiqués dans les Normes. Ces coefficients tiennent 
compte des facteurs suivants: 

— la durée d’action de la charge (m,,,). Pour tenir compte 
des charges permanentes et des surcharges de courte et de longue durée 
(à l'exception des efforts provenant des ponts roulants, des actions 
du vent, etc.) on prend m3, — 0,85. Si les conditions d'exploitation 
sont favorables à l'accroissement de Ia résistance du béton, on met 
Mp.1 = 1 Pour tenir compte de toutes les charges, y compris les 
surcharges de courte durée et les surcharges accidentelles, on prend 
Mp1 — 11: 

— l’action des charges répétées (m3,,:). On choisit les coefficients 
mp. < 1 en fonction de la nature du béton, de sa teneur en eau gt 


Ob.m 
de la caractéristique du cycle p =.b)mm,. 
è Oh 


— l'influence des gels et dégels alternée (m3.,3). On choisit 
Mp.3 & 1 en fonction des conditions de service, du type du béton 
et de la température de calcul de l'air; 

— Ja possibilité d'adopter un coefficient de sécurité plus petit 
en cas de précontrainte (m,,,). On prend m3, = 1,1 pour les struc- 


conlA DE 


2 -sinct rest 05. Lui 31 


tures avec fils de précontrainte et mp4 = 1,2 pour les structures avec 
barres de précontrainte; 

— la nécessité d'améliorer la fiabilité des structures en béton 
non armé mp5 — 0,9: 

— la chute de résistance des bétons cellulaires qui est proportion- 
nelle à leur humidité, mi.ç 1; 

— l'influence des conditions du bétonnage, mp7 < 1; 

— l'effet des dimensions de la section de la pièce coulée en place, 
Mp.s < 1; 

— la résistance accrue du béton à grain fin dans les joints des 
éléments préfabriqués, mp9 > 1; 

— la baisse de résistance du béton autoclavé, mp10 — 0,85; 

— l'effet de la radiation solaire (pour certaines zones géographi- 
ques), Mp.11 — 0,85. 

Au calcul suivant les états-limites d'utilisation, les résistances 
de calcul du béton Rsrr, Rerx sont multipliées par un coefficient 
de comportement du béton my = 1. 

Comme résistances caractéristiques de l’armature à la traction (voir 
Annexes VI, VII), on adopte les plus petites valeurs contrôlées 
{c'est-à-dire présentant une probabilité garantie égale à 0,95); pour 
les fils, de la limite d'’élasticité (apparente ou conventionnelle, 
c'est-à-dire correspondant à un allongement relatif résiduel de 0,2 %), 
pour les barres, de la charge de rupture. 

Les résistances de calcul à la traction de l'armature R;, sont obtenues 
en divisant les résistances caractéristiques correspondantes R$ par 
un coefficient de sécurité dépendant de l’acier k,. Au calcul suivant 
les états-limites ultimes, on prend k, = 1,1 à 1,25 pour les barres 
et À, = 1,55 à 1,75 pour les fils. Au calcul suivant les états-limites 
d'utilisation, on prend k, — 1 pour toutes les armatures. 

Les résistances de calcul à la compression de l'armature R,,, sont 
prises égales aux résistances de calcul correspondantes à la traction 
R;:, sans qu’elles dépassent cependant 400 MPa (4000 kgf/cm°). 

La résistance de calcul à la traction des armatures transversales 
cadres, étriers, barres inclinées), prise en compte au calcul des 
sections obliques à l’action des forces transversales (voir chapitre VI), 
est désignée R,+, et calculée à l’aide de la formule 


Rate = Ma.trRa. 
7 FER ! 
Le coefficient m:a.+- est introduit afin de tenir compte des facteurs 
suivants : 
— distribution irrégulière des contraintes dans les armatures 
transversales suivant la longueur de la section oblique (ma.tr — 0,8); 
— éventualité de la rupture fragile des assemblages des barres 
dans les carcasses soudées (Mma.tr —= 0,9); 
— adhérence imparfaite des cadres en fils lisses de classe B-1 
faisant partie d'une carcasse ligaturée (ma.tr — 0,75). 




Parfois les résistances de calcul R;,, R;,.c, Ra.tr (Voir Annexes IV, 
V) sont multipliées par un coefficient de comportement de l’arma- 
ture m7, indiqué dans les Normes et destiné à tenir compte de: 

— l'influence de la charge répétée, m1 < 1; 

— la présence des assemblages soudés des armatures exposés 
à une charge répétée, mao 1; 

— ]a diminution de la résistance de calcul, dans la zone de trans- 
fert au béton des efforts des armatures longitudinales non ancrées 
l;. et dans la zone d'ancrage des armatures ordinaires (non pré- 
contraintes) l,n (indépendamment de la classe), ma.3 << 1: 


men = tie (ms =: 


où Z, est la distance entre le bord de la zone de transfert des efforts 
des armatures et la section considérée; pour les notations lan et Lt: 
voir les formules (II1.26) et (III.27); 

— la possibilité d'employer des armatures de précontrainte 
à haute résistance pour des contraintes supérieures à la limite d’élasti- 
cité conventionnelle, m,., > 1. Les valeurs de ce coefficient seron 
indiquées plus tard, dans les chapitres V et VI; 

— la diminution de la résistance de calcul des armatures utilisées 
dans des bétons légers des classes M-100 et au-dessous, m,., < 1, 
Mas 1: 


$ III.2. PARTICULARITEÉS DE CALCUL DES PIÈCES 
EN BEÉTON PRÉCONTRAINT 


Les structures en béton précontraint sont calculées suivant les 
états-limites ultimes ou les états-limites d'utilisation pour résister 
aux charges de calcul auxquelles viennent s’ajouter les effets de la 
précontrainte. 

L’intensité de la précontrainte créée pendant la fabrication des 
pièces exerce une influence considérable sur l’état de contrainte 
et de déformation pendant l'exploitation des structures, c’est-à-dire 
en charge. Plus les compressions initiales dans le béton ont été 
fortes, mieux le béton chargé en traction résiste à la fissuration. 
Il est à noter que la précontrainte diminue à la longue, au point de 
disparaître totalement si elle était peu élevée à l'origine, à cause 
du retrait du béton, de son fluage et de certains autres facteurs®” 

Avant la fissuration, la pièce en béton armé soumise aux charges 
se déforme comme une structure élastique en matériau homogène. 
En cet état les valeurs des contraintes dans le béton et l’acier sont 
définies par leur déformation commune. 

Pendant le travail en traction de la pièce en béton armé (avant 
la fissuration), compte tenu de l'égalité des déformations du béton 


3—0948 33 


et de l’acier £1 — €a, la relation entre les contraintes dans le béton 
op et dans les armatures 0, est égale à 


Op/E +} —= Oa/E a, (III.1) 


où Æ1, E, sont les modules d’élasticité du béton et de l'acier. 
La somme des efforts développés dans le béton et l’acier de la 
pièce est égale à l’effort extérieur W : 


N = Obplh + Cats, (III.2) 


où F;, F1 sont les sections de l'acier et du béton dans la pièce. 
La solution commune des deux équations fournit les expressions 
qui définissent les contraintes dans le béton et l'acier: 


Op = N/Fégs Où Fega = Fr +nFa; n = EE»; (111.3) 
Oa = NO}, (III.4) 


où Féeg est la section homogène équivalente, c'est-à-dire la section 
de la pièce en béton armé dans laquelle la section des armatures est 
remplacée par une section équivalente du béton. 

On définit de la même façon les moments d'inertie équivalents 
et les modules de résistance équivalents pour les sections homogènes 
des pièces fléchies en béton armé, à condition que la zone tendue 
du béton soit exempte de fissures. 

La précontrainte est réalisée par la mise en tension des arma- 
tures, par les procédés mécaniques ou électrothermiques. 

En cas de précontrainte par pré-tension, la résultante de toutes 
les tractions dans les armatures se voit équilibrée par la réaction 
encaissée par les culées. Au moment où les armatures sont libérées, 
la résultante exerce sur le béton un effort de compression V, qu'on 
assimile à une sollicitation extérieure. Sa valeur est déterminée 
en fonction de la section de l’armature de précontrainte F4 et 
l'intensité de la précontrainte des armatures avant leur libération 
Oo : 

No = FpcOo-: (III .5) 


Si la force de précontrainte V, est exercée sur la pièce dans le 
sens axial (compression centrée), la contrainte dans le béton est 
égale à 

Gp = Wo/Féq (III.6) 


et si elle est appliquée avec une excentricité e, par rapport au centre 
de gravité de la section homogène (compression excentrée), la con- 
trainte est égale à 


_ No Ne 
GE TE y (III.7) 


Dans ces expressions J4 est le moment d'inertie de la section homo- 
gène équivalente et y la distance entre le centre de gravité de la 




section homogène et la section dont on cherche à déterminer la 
contrainte. 

La contrainte de compression maximale G} max Créée dans le 
béton au cours de la fabrication de la pièce est choisie en fonction 
des facteurs suivants: 

— ]a résistance de précontrainte du béton R,; 

— le mode de précontrainte employé (pré-tension, post-tension); 

— la nature du travail de la pièce en charge (augmentation ou 
diminution de ©}. max dans l'ouvrage). 

Lorsque la charge a pour effet de diminuer Oj, max: On adopte 
Op.max L 0,65R, en cas de pré-tension et O}j.max < 0,99R, en cas 
de post-tension. Dans une pièce soumise à une compression excentrée 
pendant la précontrainte, on prend Oh.max <0,70RQ en cas de 
pré-tension et Ob.max < 0,69À, en cas de post-tension. Si la charge 
a pour effet d'augmenter 6} max, on choisit, dans une pièce pré- 
contrainte en compression centrée, Op.max <0,9R, pour la pré- 
tension et Op.max < 0,45R, pour la post-tension, et dans une pièce 
soumise à une compression excentrée pendant la précontrainte, 
respectivement Op.max < 0,99R) et Op.max SL 0,9R,5. La valeur 
de la résistance de précontrainte À, sera prise non inférieure à 80 % 
de la résistance théorique quand celle-ci est minimale pour le type 
d'armature donné (voir tableau III.4) et non inférieure à 50 % de 
la résistance théorique du béton quand celle-ci est supérieure à la 
minimale. 

L'intensité de la précontrainte ©, est choisie dans les limites 
suivantes : 

pour les barres, 


0,8Rarr + P < 00 < Rart — P; (TIT.8) 
pour les fils, 
0,2Rarr EN P < Oo < 0,8Rarr — P; (IIT.9) 


où RArx est la résistance de calcul à la traction retenue dans le calcul 
aux états-limites d'utilisation; p est l’écart admissible de l’inten- 
sité de la précontrainte par rapport à sa valeur de référence. En cas 
de précontrainte par les procédés mécaniques, on a p — 0,050,, et 
en cas de précontrainte par les procédés électrothermiques 


p (kgf/em?) = 300 + ©, (IIT.40) 


où Z est la longueur de la barre mise en tension. ” 


Les armatures des pièces en béton précontraint présentent un 
phénomène appelé pertes de précontrainte, déterminé par une série 
de facteurs. 

On distingue: 

— les pertes premières, ou pertes instantanées: elles se produisent 
pendant la fabrication et la mise en tension de la pièce : 


s* 35 


— les pertes secondes, ou pertes différées: elles se manifestent 
postérieurement à la mise en tension. 
En cas de précontrainte par pré-tension (par adhérence), les pertes 


instantanées (premières) oRn) sont exprimées par la somme 


TE = O0 + O2 + opt 1) DE O5 + Os (IT.11) 


et les pertes différées (secondes) TS par la somme 


gti) — RE (II1.12) 


Les facteurs intervenant dans ces expressions sont les suivants: 

— 6, pertes par relaxation des armatures ; 

— 0, pertes dues aux variations de la température; 

— ofadh), pertes dues à la déformation des pièces de retenue 
sur les culées : 

— ondh), pertes dues au frottement de l'acier; 

— 6;:, pertes dues à la déformation des moules d'acier; 

— 0%, pertes par fluage rapide du béton; 

— ofadh), pertes par retrait du béton; 

— ofadh), pertes par fluage différé du béton. 

En cas de précontrainte par post-tension (par ancrage), les pertes 
instantanées (premières) of) ont pour expression la somme 


g{anc) = LUE gfanc) (IIT.13) 


et les pertes différées (secondes) {ao la somme 


gtanc) — 0, + gen) gene Cp+ on. (III.14) 


Les facteurs intervenant dans les expressions (III.13), (III.14) 
sont les suivants: 

— ofanc), pertes par déformation des ancrages; 

— ofanc), pertes par frottement de l'acier sur le béton; 

— O7, pertes par relaxation des tensions dans les armatures; 

— ofanc), pertes par retrait du béton; 

— ofanc), pertes par fluage du béton; 

— O39, pertes par écrasement du béton fretté; 

— On, pertes par déformation des joints des blocs juxtaposés 
soumis à la précontrainte. | 


Pertes instantanées 


Pertes par relaxation des tensions dans les armatures. Une barre 
de longueur donnée soumise à une traction d'intensité élevée pré- 
sente à la longue une chute de tension, ou relaxation. La valeur de 
la précontrainte 0, étant exprimée en kgf/cm°, ces pertes se définis- 
sent par les expressions suivantes: 




pour les fils mis en tension par les procédés mécaniques, 


oO, — (0,27 Re —0,1) 0,>0; (111.45) 


pour les barres mises en tension par les procédés mécaniques, 
O1 — 0,10, — 200 > 0. (111.16) 


En cas de mise en tension par les procédés électrothermiques, on a 
6, = 0,050, pour les fils et o, — 0,030, pour les barres. 

Pertes dues aux variations de la température. Au cours de la 
cure par la chaleur du béton frais de la pièce mise en précontrainte 
par pré-tension, une partie de l'allongement élastique de l'acier 
est perdue à cause de la chaleur. Les pertes de précontrainte sont 
évaluées à 


Oo — 12,5At, 


où At est la différence entre les températures des armatures chauffées 
et des culées fixes. Faute de données sur les températures, on pose 
At = 65 °C. 

Pertes par déformation des pièces de retenue sur les culées. En 
cas de précontrainte par pré-tension (par adhérence), on a 


on LE, (III.47) 


où l'est la longueur de la barre mise en tension; À, la déformation 
des pièces de retenue (rondelles, têtes), prise égale à 2 mm, ou le 
déplacement des barres dans les organes de mise en tension calculé 
par la formule À = 1,25 + 0,154, où d est le diamètre de la barre 
en mm. 

En cas de précontrainte de post-tension (par ancrage), on à 


og nthp,, (II1.18) 


où À, — 1 mm (déformation des rondelles et ües garnitures) et 
ko = 1 mm (déformation des appareils d'ancrage). 

Pertes par frottement de l’acier dans les canaux pendant la pré- 
contrainte. La contrainte dans l’armature devient d'autant plus 
faible qu'on s’éloigne du point de mise en tension en lequel la con- 
trainte est égale à o,: 


6) = 09 (her 0:220)e gens) 69 (1—e-x+n0)),  (IIL.49) 


où e est la base des logarithmes naturels ; 8, l'angle au centre capable 
de l’arc en radians de la portion en courbe du canal (fig. III.1); 
x, la longueur en mêtres mesurée entre le dispositif de mise en tension 
et la section à calculer; À et a, deux coefficients de frottement qu’on 
trouve dans le tableau III.1. 




TABLEAU 111.1 
Valeurs des coefficients k et pu 


Type du canal k à barres à haute 
câbles adhérence 
A surface métallique | 0,003 | 0,35 | 0,4 
À surface en béton, formée par une 
gaine rigide 0 
0,55 0,65 
Idem, formée par une gaine souple 0,0015 


Pertes par déformation des moules. Elles sont calculées par la 
formule 

t—1 AI 

5— 57 7 Eas (III.20) 

où t est le nombre des groupes de barres mis en tension non simulta- 

nément; A/, le rapprochement des culées compté suivant la ligne 


FIG. II1.1. Détermination des pertes'de précontrainte de l’armature par frotte- 
ment dans les canaux: 
1, armature ; 2, organe de mise en tension; 3, pièce d’ancrage 


d'action de la résultante des efforts de précontrainte et pris en 
compte lors du calcul des moules. 

Faute de données plus précises, on poseo, — 30 MPa (300 kgf/cm°). 

Pertes par fluage rapide du béton. Elles sont dues à la diminu- 
tion complémentaire de la longueur de la pièce qui se produit au 
cours de deux ou trois heures_qui. suivent la mise en tension. Ces 
pertes ne jouent que si la pièce est précontrainte par le procédé de 
pré-tension. Plus la précontrainte a été forte, plus le fluage est pro- 
noncé et plus les pertes correspondantes sont graves. Pour le béton 
durci à l'air 


MD RE — 
6e = 500a + 1000b (mer 5) si mer > 0, | 
Ro 0 




où Opemax est la précontrainte dans le béton calculée avec la dé- 
duction de toutes les pertes étudiées ci-dessus, au niveau de l'effort 
de précontrainte initial; a = 0,6, b = 1,5 pour le béton de classe 
M 300 et des classes supérieures ; a = 0,5, b — 3 pour le béton de 
classe M 200; R, est la résistance de précontrainte du béton. 

Pour le béton durci à l’autoclave on calcule les pertes suivant 
la formule (III.21) en introduisant un coefficient 0,85. 


Pertes différées 


Pertes par relaxation des tensions dans l'armature. En cas de pré- 
contrainte par post-tension, ces pertes sont comptées parmi les pertes 
différées et calculées suivant les formules (III.15) et (III.16), soit 
O7 = Oj. 

Pertes par retrait du béton. Elles font diminuer la longueur ini- 
tiale de la pièce et, partant, la contrainte dans l'acier initialement 
tendu. Les pertes par retrait du béton 6, sont déterminées à l’aide 
du tableau III.2. 


TABLEAU III.Z2 


Pertes de précontrainte dans les armatures par retrait 
du béton (lourd), kgf/cm? (MPa) 


Mode de mise en tension des armatures 


pré-tension (par adhérence), *) Ju 
Classe de résistance du béton ALU Hier (par 
béton durci à l’au- ancrage), gt2nc 
ei SUrel toclave. He SRE ton ë 
atmosphérique 
M400 et au-dessous 400 (40) 350 (35) 300 (30) 
M500 900 (50) 400 (40) 300 (35) 
M600 et au-dessus 600 (60) 500 (50) 400 (40) 


_ Pertes par fluage différé du béton. Quel que soit le procédé de 
mise en tension des armatures, ces pertes sont calculées pour le béton 
durci à l’air à l’aide des formules 


Of = 0ÿ 0) = 2000 “bmx si bemax 0,6 ; 
° à (III .22) 
ota 5 = of" = 4000 (ME 0,3) si MEL > 0.6; 
Ro | Ro de : 
pour la quantité Oh.max, Voir plus haut. 
Pour le béton durci à l’autoclave sous pression atmosphérique, 
les pertes en question sont affectées d’un coefficient 0,85. 
Pertes par frettage. Il s’agit des pertes de précontrainte à cause 
de l’écrasement du béton des pièces de section ronde jusqu'à 3 m 




de diamètre (par exemple des tubes en béton armé) munies de frettes 
sous forme de cercles ou d’hélices. Ces pertes sont prises égales à 
O10 — 300 kgf/cm°? (30 MPa). 

Pertes par déformation des joints des blocs juxtaposés soumis à 
la précontrainte. Prises en compte en cas de précontrainte par post- 
tension, elles sont calculées d’après la formule 


u=—} En (111.23) 


où #, est le nombre de joints exposés à la précontrainte ; À, la défor- 
mation de chaque joint égale à 0,3 mm si le joint est garni et à 
0,5 mm s’il est creux. 

La précontrainte considérée dans les calculs est affectée d’un 
coefficient m?- qui tient compte de la précision de la mise en tension 
de l’armature: 


= 1 + Amy (111.24) 


(le signe positif correspondant à l’effet défavorable de la précontrainte 
et le signe négatif à l'effet favorable). 

Pour la mise en tension par les procédés mécaniques on prend 
Ampr = 0,1, et pour la mise en tension par les procédés électro- 
thermiques 


Ampr = 0,5 + (1+ =) mais >0,1, (IIT.25) 




où 7, est le nombre des armatures de précontrainte dans la section 
de la pièce; pour les quantités p et 04, voir les formules (III.8) 
et (III.9). 

En calculant les pertes de précontrainte de l’armature, l'ouverture 
des fissures et les flèches, on _ poser Ampr = 0. 

Les pertes totales 6, = 0, 2 peuvent atteindre des valeurs 
aussi élevées que 2000 à 2500 Pts (200 à 250 MPa), voire davanta- 
ge. En aucun cas la valeur des pertes totales ne doit être prise infé- 
rieure à 1000 kgf/cm°? (100 MPa). 

La force de précontrainte V, définie par la formule (III.5) ne 
tient compte que des armatures de précontrainte de section Fe 
situées dans la zone tendue (sous charge). Dans certains cas on dis- 
pose des armatures de précon&#ainte de section F,. aussi dans la 
zone comprimée (sous charge). Dans les pièces fléchies à grande 
hauteur de section, cela est nécessaire pour éviter la formation (ou 
l'ouverture excessive) des fissures dans la zone comprimée future 
de la pièce à cause de la flexion qui se produit pendant la précon- 
trainte, vu que la force V, = F,0, présente uneïorte excentricité 
par rapport au centre de gravité de la section. 

Dans une pièce travaillant en compression ou traction excentrées, 
les aciers sont toujours disposés de part et d’autre de la section. 




Désignant par 6, la valeur de la précontrainte dans les aciers 
de section F;c, on à 


No = Fpe00 + Fhe08. (TII.5a) 


Les déformations de retrait du béton et les déformations de 
fluage sous précontrainte font diminuer les contraintes de traction 
dans les armatures de précontrainte (pertes de précontrainte par 
retrait et par fluage). Si la pièce contient aussi des armatures ordi- 
naires (non précontraintes) de section }’, dans la zone tendue et F; 
dans la zone comprimée, ces armatures éprouvent les mêmes défor- 
mations à cause de leur adhérence avec le béton; de ce fait, le retrait 
et le fluage du béton font naître dans les armatures ordinaires des 
contraintes de compression 6,, 6, égales en valeur aux pertes de 
précontrainte correspondantes dans les armatures de précontrainte. 
On a donc en somme 


No= Fp000 + Fhc0!— Fa0a — Fi04. (III.5b} 


La position du point d'application de W, suivant la hauteur de 
section est facile à déterminer: c’est le point d'application de la 
résultante du système de forces parallèles. 

La section des armatures ordinaires dans la pièce précontrainte 
étant généralement assez faible, on détermine souvent V, en utili- 
sant les formules (III.5) ou (III.5a). 


$ IILS. GÉNÉRALITES SUR LA CONCEPTION 


Les classes de résistance (marques) du béton armé utilisées pour la 
fabrication des structures sont choisies en général sur la base des. 
calculs technico-économiques. L'expérience montre qu'il est pré- 
férable d'employer pour les pièces comprimées les classes M 200 à 
M 400, pour les pièces fléchies M 150 à M 300 et pour les pièces pré- 
contraintes M 300 à M 500. 

La section des armatures longitudinales principales est très faible 
(0,3 à 3 %) devant la section utile du béton de la pièce. Or, les pièces. 
ainsi armées présentent un avantage décisif vis-à-vis des pièces en 
béton non armé: elles ne se détruisent jamais en mode fragile. 

Si la quantité d’'armatures est insuffisante, la pièce se détruit 
en mode fragile comme une pièce en béton non armé. Afin d'éviter 
ce danger, les Normes prescrivent une proportion minimale des. 
armatures longitudinales à employer dans les pièces. Nous exposerons 
cette question en détail dans les chapitres suivants. 

La disposition des armatures dans la section de la pièce dot? 
être étudiée de façon à prévoir une couche de béton suffisante autour 
d'elles (épaisseur d’enrobage). Cette couche de béton permet à l'acier 
et au béton de travailler ensemble sous charge et protège l'acier 
contre la corrosion et un échauffement excessif. 

Comme armatures ordinaires (sans précontrainte), on utilisera 
de préférence des barres laminées à chaud de classe A-IIT ainsi que 




des fils ordinaires de 3 à 5 mm de diamètre des classes Bp-I et B-I 
sous forme de carcasses et treillis soudés. On peut aussi employer 
des barres laminées à chaud des classes A-ITI et A-I, surtout comme 
armatures transversales. Si la structure à armatures non précontrain- 
tes doit être étanche à l’eau, on utilise des barres des classes A-II 
et A-I. Peuvent aussi être utilisés des barres laminées à chaud de 
classe A-ITI et des fils ordinaires des classes Bp-I et B-I. 

Comme armatures de précontrainte, on utilise des barres laminées 
à chaud de classe A-IV et des classes supérieures, des câbles torsadés 
et des fils à haute résistance des classes B-II et Bp-Il. 

Certaines nuances d'acier et les assemblages soudés des aciers 
de ces nuances présentent une fragilité excessive à froid. On interdit 
donc l'emploi des barres laminées à chaud de classe A-IV de nuance 
80C et de certaines nuances couvertes par les classes A-II (nuance 
BCronc2) et A-I (nuances Cr3kn2, BCr3l'nc2) dans les structures 
conçues pour un service prolongé à basse température (entre —30 
@t —40 °C). 

Les barres ordinaires (sans précontrainte) doivent être prolongées 
au-delà de la section où leur résistance de calcul est utilisée complé- 
tement, d’une longueur /,, nécessaire à leur ancrage, égale à 


L — (mange + Aan) d, (III.26) 


mais non inférieure à lan — Mand, ainsi qu'à la longueur d'ancrage 
minimale lin. min- Toutes ces quantités sont indiquées dans le tableau 
II1.3 pour les aciers à haute adhérence et (entre parenthèses) pour 
Jes aciers lisses. 


TABLEAU III.S 
Valeurs des grandeurs intervenant dans la formule (111.26) 


Cas de charge æ Man Alan kan lan. min 
Armatures tendues dans le bé- 
ton tendu 0,7 (1,2) 11 20 250 
Armatures comprimées ou ten- 
dues dans le béton tendu 0,5 (0,8) 8 12 (15) 200 


- ‘2 '. 

Sur les appuis extrêmes libres des pièces fléchies, les barres longi- 
tudinales arrivées aux appuis sont ancrées en les prolongeant au-delà 
du nu de l’appui d’une longueur ln > 104 (fig. III.2). Si la pièce 
est calculée sans armatures transversales, on peut diminuer la lon- 
gueur d'ancrage jusqu’à lan > 94. Si l’on est obligé de prendre la 
longueur /,, inférieure aux valeurs indiquées, il y a lieu de renforcer 
l’ancrage des barres en les munissant de barreaux ou de rondelles 
de retenue ou en les soudant sur des pièces de retenue en acier. 




Pour assembler les carcasses et les treillis soudés entre eux dans 
la structure, on emploie généralement la soudure, tout comme pour 
les barres isolées. Les différents types de jonctions soudées ont été 
montrés sur la figure II.12. 

Il est permis d'abouter sans soudure, par simple recouvrement, 
les barres chargées en traction de l’armature ordinaire jusqu'à 
36 mm de diamètre, dans les treillis et carcasses soudés ou ligaturés. 


FIG. III.2. Ancrage des carcasses et treillis soudés des pièces  échies reposant 
sur appuis libres: 
a, dalle; b, poutre 


La longueur de recouvrement l,.. doit être alors non inférieure à la 
valeur de /,, calculée à l’aide de la formule (II1.26). Les aboutements 
réalisés en un point donné ne doivent concerner qu'une partie des 
barres travaillant en traction, non supérieure à 25 % en cas de 
barres lisses et à 50 % en cas de barres à haute adhérence. Les jonc- 
tions des barres seront disposées en dehors des zones où la résistance 
mécanique des armatures est utilisée complètement. Les barres solli- 
citées en traction centrée ou faiblement excentrée ne peuvent pas 
être jointes par recouvrement sans soudure. 

Dans les treillis et carcasses soudés où toutes les barres principales 
sont situées d'un même côté, les jonctions sont réalisées comme & 
est montré sur la figure III.3. La longueur de recouvrement doit 
couvrir au moins deux barres transversales appartenant à chacun 
des deux treillis (carcasses) à assembler. 

La position correcte des armatures dans les moules avant la 
coulée du béton est assurée à l’aide de goujons, tiges de suspension, 
carcasses ou treillis auxiliaires. 




L'écartement entre les barres est choisi de façon à faciliter la 
mise en place du béton et le serrage. Si, au moment de bétonnage, les 
aciers sont en position horizontale, l’espace libre entre eux doit 


FIG. 111.3. Jonctions sans soudure des carcasses et treillis soudés: 


a, par recouvrement dans le sens des barres principales lisses, toutes les barres transversales 

étant situées dans un même plan; bet c, idem, les barres transversales étant disposées dans 

des plans différents; d, dans le sens des barres principales à haute adhérence, la longueur 

de recouvrement necontenant que des barres transversales d’un treillis ; e, idem, la longueur 

de recouvrement ne contenant aucune barre transversale; f, par recouvrement dans le sens 

des barres de répartition (de montäge); g, idem, jonction hout à bout avec treillis couvre- 
joints; 1, barres principales, 2, barres de montage 


être non inférieur au diamètre de la barre, mais aussi non inférieur 
à 25 mm pour le ferraillage inférieur et à 30 mm pour le ferraillage 
supérieur ; si les aciers sont verticaux, ils seront espacés de 50 mm 
au moins. 


$ III.4. PARTICULARITÉS DE CONCEPTION 
DES PIÈCES EN BÉTON PRECONTRAINT 


Précontrainte par post-tension (par ancrage). Les extrémités des 
armatures de précontrainte (câbles torsadés, câbles de fils et de 
torons droits, barres) tendues sur le béton durci doivent toujours 
être retenues dans des appareils d'ancrage (fig. III.4) après leur 
mise en tension à l’aide des vérins. L'appareil d'ancrage peut avoir 
la forme d’une tige filetée engagée dans une douille taraudée et serrée 
avec un écrou, ou bien d’un cône mâle serré dans un cône femelle. En 




cas de mise en tension des barres à haute adhérence par les procédés 
électrothermiques, l’ancrage peut être réalisé à l’aide de têtes refou- 
lées en bout de la barre et de plaques de retenue fendues. 


3 4 Ÿ 




a) 1 2 


FIG. 111.4 Appareils d'ancrage des câbles de précontrainte à fils droits (pré- 
contrainte par post-tension) : 


a, ancrage pas tige filetée et douille ; b, ancrage par cône; 1, fils du câble; 2 partie annelée 
de la tige; 3, douille; 4, partie tiletée de la vers 5, écrou de serrage; 6, cône femelle: 
7, cône mâle; , tubulure 


Afin d'assurer une bonne adhérence entre l'acier et le béton, 
les canaux dans le béton sont remplis de coulis de ciment avec ou 
sans sable par injection après la mise en tension et l'ancrage des 
armatures de précontrainte. 



a) K 
2 CD >> ES KE D ARE IT 
> 29 De: -20® = 4 


Tube 435 à 50 mm 
d-J-4mm  & 
€) & 


15024, 3mm 


FIG. II1.5. Dispositifs d'ancrage des fils lisses: 


a, barreaux de répartition; b, tubes; ce, clavettes « 


Précontrainte par pré-tension (par adhérence). Avec ce procédé 
basé sur l’adhérence naturelle, aucun ancrage des extrémités n’est 
nécessaire pour les barres et fils à haute adhérence, ainsi que pour 
les câbles torsadés, à condition que le béton employé soit conforme 
aux prescriptions du tableau III.4. 




TABLEAU III.4 
Classes de résistance minimales du béton précontraint 


Armature de précontrainte | crc Case où 

Barres sans ancrages, diamètres 10 

à 48 mm A-IV, AT-IV M200 
A-V, AT-V M250 
AT-VI M350 

Idem, diamètre 20 mm et plus A-IV, AT-IV M250 
A-V, AT-V M350 
AT-VI M400 

Fils avec ancrages B-II M250 

Idem, sans ancrages, diamètre 

5 mm et plus Bp-Il M250 

Idem, diamètre 6 mm et plus Bp-Il M400 

Câbles torsadés K-7 M350 


Dans les autres cas l’adhérence naturelle est insuffisante, si bien 
qu’on est obligé de prévoir des appareils d'ancrage aux extrémités 
des armatures. 

Les fils lisses de précontrainte doivent toujours être munis d'’an- 
crages (fig. III.5). 

Les appareils d'ancrage concentrent des contraintes dans le béton. 
Pour cette raison les zones d’about des structures contenant des 


FIG. 111.6. Renforcement de la pièce précontrainte dans la zone d’ancrage des 
armatures : 


1, treillis soudés; 2, armatures longitudinales de renforcement; 3, barres transversales 
complémentaires 


ancrages doivent être renforcées en utilisant des treillis soudés et 
des cadres auxiliaires ou en augmentant l'épaisseur d’enrobage 
(fig. III.6). 




En cas de précontrainte par adhérence, les armatures reportent. 
l'effort de précontrainte sur le béton à leurs extrémités, dans les. 
limites de la « zone d’auto-ancrage » dont la longueur atteint 10 à 
45 fois le diamètre de la barre, 30 à 70 fois le diamètre du câble 
torsadé à sept fils et 45 à 100 fois le diamètre du fil à haute adhé- 
rence. Dans cette zone, le béton doit également être renforcé (treillis. 
auxiliaires, frettes en hélice, etc.). 

La longueur de la zone de transfert des contraintes /;,. des arma- 
tures de précontrainte sans ancrages est égale à 

he (mMte-pe+ AM) d, (III.27) 
où les valeurs de m+,., A1. Sont tirées du Tableau III.5 et 04. est. 
pris égal à la plus grande des valeurs À, et o,. 


TABLEAU 111.5 
Valeurs des grandeurs intervenant dans la formule (111.27) 


Coefficients 


Armatures es 


Barres à haute adhérence, toutes 

classes, tous diamètres 0,3 10 
Fils à haute résistance, classe 

Bp-Il, diamètre : 


5 mm 40 
4 mm | 1,8 50 
3 mm 60 
Câbles torsadés, classe K-7, dia- 
mètre : 
45 mm 1,25 25 
12 mm 1,4 25 
9 mm 1,6 30 
1,5, 6, 4,5 mm 1,8 40 


Pour toutes les barres à haute adhérence, la valeur de /:, est. 
choisie non inférieure à 154. 


CHAPITRE IV 


PIÈCES EN BÉTON ARMÉ CHARGÉES 
EN COMPRESSION SIMPLE 


$ IV.1. DISPOSITIONS CONSTRUCTIVES 


Dans le calcul des structures, on range parmi les pièces travaillant 
en compression simple (compression axiale longitudinale) les poteaux 
intermédiaires des bâtiments, les membrures supérieures des fermes 
sollicitées en leurs nœuds, les diagonales ascendantes et les mon- 
tants du treillis des fermes (fig. IV.1) et certains autres éléments. 

La force de compression longitudinale est en réalité toujours 
excentrée par rapport à l’axe théorique de la pièce. Cette excentricité 
s'appelle excentricité accidentelle. Sa 
valeur est indiquée dans les Normes: 
elle doit être prise inférieure à 1/600 
de la longueur de la pièce (entre ses 
points d'attache), à 1/30 de sa hau- 
teur de section, ou à 1 cm. 

Les poteaux ont généralement une 
section carrée ou rectangulaire. Les 
dimensions de la section sont déter- 
minées par le calcul. Afin de norma- 
liser les dimensions des coïffrages et 
des cages d’armatures, les longueurs 
des côtés des sections des poteaux 
sont choisies multiples de 50 mm. 
Au risque de nuire à la bonne qualité 
FIG. IV.1. Exemples de pièces du béton, il est déconseillé, pour les 
chargées en compression simple: Poteaux coulés sur chantier, d'avoir 


1, poteau intermédiaire ‘(charges .une longueur de côté de la section 


égales de part et d’autre); 2, mem- oops : 
brure supérieure d’une ferme  (char- inférieure à 25 cm. 


gée en ses nœuds); 3, diagonales Les bétons employés pour la réa- 
ascendantes; 4, montants li à 
isation des poteaux sont des classes 
M 200, M 300, M 400. 

Les poteaux sont armés de barres longitudinales (armatures prin- 
cipales) de 12 à 40 mm de diamètre, généralement en acier laminé à 
chaud, des classes A-TT, A-ITI, et de barres transversales en acier la- 
miné à chaud, de classe A-I ; on emploie aussi comme armatures trans- 
versales des fils à base carbone étirés à froid (fig. IV.2). Les armatures 




Jongitudinales et transversales sont réunies en carcasses planes (nap- 
es) ou tridimensionnelles (cages) soudées ou ligaturées (fig. IV.3). 
La quantité des armatures longitudinales dans la section d’une 
pièce est évaluée à l’aide de la proportion p ou du pourcentage d'arma- 
tures : 


u % = nu 100 = (F,/F) 100, 


où F, est la section totale des armatures longitudinales: FÆ est la 
section du béton, c’est-à-dire la section de la 
pièce avant la déduction de la section des 
armatures. 

On prend généralement dans les calculs 
04<u % <3. 

Les armatures principales sont à disposer 
le plus près possible de la peau de la pièce, 
tout en respectant cependant la valeur mini- 
male de l'épaisseur d'enrobage &@onr qui, selon 
les Normes, doit rester non inférieure au dia- 
mètre de la barre d'armature ni à 20 mm. 

Un poteau de section non supérieure à 40 x 
x 40 cm peut recevoir comme armature princi- 
pale quatre barres longitudinales, ce qui 
correspond à l’espacement maximal; quant à 
l'espacement minimal, il est défini par les pjg. 1v.2. Disposition 
conditions du bétonnage (voir $ III.3). des armatures dans 

L'espacement des armatures transversales une pièce chargée en 
ne fait pas l’objet d’un calcul particulier  — simple : 
mais il est précisé dans les Normes. Afin 2. es nel 
d'éviter la poussée au vide des barres lon- ‘enr épaisseur d’enrobage 
gitudinales sous l'effort de compression, l'es- 9% ArMAÎNTeS pee 
pacement des armatures transversales u4, doit  d'enrobage des armatures 
rester non supérieur à 204 (fig. IV.2) dans transversales 
les carcasses soudées, à 15d dans les carcasses 
Jigaturées et en tout cas non supérieur à 900 mm (ici d est le diamètre 
minimal des barres longitudinales sollicitées en compression). La 
valeur de u. est arrondie à une valeur multiple de 50 mm. 

Le diamètre des barres transversales d+. faisant partie d’une car- 
casse soudée est choisi de façon à garantir une soudure efficace (voir 
$ II.3). Les cadres des carcasses ligaturées doivent avoir un dia- 
mètre non inférieur à o mm ni à 0,254, où d est le plus grand dia 
mètre des barres longitudinales. 

L’épaisseur d’enrobage des barres transversales aénr ne doit jamais 
être inférieure à 15 mm. 

Les jonctions des barres longitudinales dans le sens de la lon- 
gueur sont à éviter. 

Aux endroits d'aboutement des carcasses, les barres transversa- 
les situées sur la longueur de recouvrement des barres longitudina- 


4—0948 49 


les doivent avoir un espacement non supérieur à 104, où d est le 
diamètre des barres longitudinales jointes. 


101 46: 


0, © & 


FIG. IV.3. Disposition des Re dans une pièce chargée en compression 
simple : 


a, carcasses soudées; b, carcasses ligaturées; 1, carcasses soudées; 2, barres de liaison; 
3, cadres; 4, cadres ‘auxiliaires : 5, épingles 


$ IV.2. CALCUL DES PIÈCES PRÉSENTANT 
UNE EXCENTRICITÉ ACCIDENTELLE 


Les expériences (fig. IV.4) ont montré que la résistance offerte par 
une pièce de faible longueur à l'effort de compression centré se com- 
pose de la résistance du béton et de celle des armatures longitudina- 
les. La résistance du béton atteint généralement 
sa limite de rupture, et la résistance de l’acier, 
sa limite d'’élasticité, en raison des défor- 
mations plastiques importantes du béton 
soumis à des contraintes élevées. 

Au calcul de résistance d’après les états- 
limites, l'effort longitudinal provenant des 
charges de calcul ne doit pas, de toute éviden- 
ce, se trouver supérieur à la somme des 
efforts internes de calcul développés dans le 
béton et dans l'acier: 


OT UNE Rprl + RacPas (IV.1) 


où N est l'effort de calcul (provenant des 

AE be un bd charges de calcul, c’est-à-dire des charges 
un essai de compres- Caractéristiques multipliées par le coefficient 
sion simple de surcharge) ; Rpr, la résistance de calcul 

du béton à la compression axiale (résistance 


sur prisme); Ra.., la résistance de calcul de l'acier à la compres- 
sion. 




Les Normes de calcul prescrivent d'introduire l’excentricité 
accidentelle dans le calcul des pièces élancées (de forte longueur) 
sollicitées en compression (voir $ IV.1) en assimilant celles-ci à 
des pièces chargées en compression excentrée (voir Chapitre VIT). 
Conformément aux Normes, la capacité portante d’une pièce de sec- 
tion rectangulaire armée de façon symétrique par des barres d'acier 
des classes A-I, A-II, A-IIT et telles que 1, < 20h (où /, est la lon- 
gueur de flambement de la pièce, dépendant des conditions de fixa- 
tion de ses extrémités, et À sa hauteur de section) peut être calculée 
d'après la formule 


N < mQ (RprE + Ra.cFa); (IV.2) 


où À = hb (b, largeur de section) ; F,, la section totale des armatu- 
res longitudinales ; m»m, un coeïficient de comportement égal à 0,9 
pour k < 200 mm et à 1 pour k => 200 mm, y, un coefficient empi- 
rique dépendant de la durée d'action de la charge, de l’élancement de 
la pièce et de la disposition des armatures: 


Ra.cF 
PP +2(p D) (IV.3) 


mais toujours inférieur ou égal à œ. Les coefficients œ, et @, sont 
tirés du Tableau IV.1 dans lequel W,4 est la force longitudinale pro- 
venant des charges permanentes et des surcharges de longue durée 
et int est la section des barres intermédiaires (voir le schéma de 
disposition des armatures en tête du Tableau). 

Rassemblant toutes les données disponibles sur la section, les 
armatures et les charges, on calcule la capacité portante de la pièce 
chargée en compression simple à l’aide des formules (IV.2) et (IV.3), 
après avoir déterminé le coefficient @ d’après la formule (IV.3) et 
les données du Tableau IV.1. 

Lorsque les dimensions de la section sont connues et qu'il ne 
reste qu'à déterminer la section des armatures, on fait intervenir 
l'expression (1V.2) qui donre 


Ro" = pp = Pr. 
' MmPRa.c Ra.c ? 


(IV.4) 


la valeur de étant déduite j ar itérations. 

Les dimensions de la section à donner à la pièce chargée en com- 
pression simple et la section à donner à son armature sont calculées 
en fonction de la charge imposée, de la longueur de flambement et 
des caractéristiques des matériaux, en se donnant à priori q = m =, 1 
et F, = 0,01 F. On tire de (1V.2) 
MP (Rpr+hRa.c) 
et l’on choisit les dimensions à donner à la pièce en tenant compte 
des impératifs de normalisation. On calcule ensuite le rapport L,/h 
et l’on choisit F, comme il vient d'être dit. S'il se trouve que le 


(IV.5) 


4 51 


8c‘0 99‘0 ÿL'0 80 98‘0 68‘0 76‘0 cb‘ 0 } 
G9‘0 &L‘0 6L‘0 €8‘0 L8‘0 6‘0 16‘0 &6'0 G'0 
GL'O 8‘0 78‘ 0 180 68‘0 6 0 &6‘0 &6°0 0 


UJt/1 R OAnoOTOJUI UOU 459 91pnJ9 ue[d ne sopappuied 59987 S0p 
said sognqis }UT'A}y SOliBIPautIORUI SOIIEY S9pP U01199$ PT ‘4 


L'O LL‘0 £8‘0 98‘0 88‘0 6°0 6‘0 6° 0 } 
GL'O 8‘0 #8‘ 0 L8‘0 6‘0 16‘0 &6‘0 60 G‘0 
78‘0 78° 0 L8‘0 68‘0 60 16°0 &6 0 €6‘0 0 

8JS/r 8 9AnolI9JUI 369 91pn39 ued ne sorarpeied s99e] S9p 
said saanjis FT} SaIIBIPAUIIOQUI S9118Y SIP U01199$ ET ‘V 
5d qu919177809 
GG‘0 €9‘0 yL'0 780 98‘0 68‘ 0 60 A b 
c9°0 €L'‘0 8‘0 Gg‘0 88‘0 6‘0 6‘0 G6°0 G°0 
8'0 c8‘0 980 680 6‘0 6‘0 &6 0 €6‘0 0 


Th Jua1917}809 - 


N/PUN 


SOJUIPNJISUOT soie Sp [e)0} uot390s ‘C7 Ju1'4) 
SOIIBIPAWII9IUI SOIIEE ‘2 
o1pno ueld ‘7-7 


‘b 32e lb Sjua191/J009 s9p simo[uA 
T'AI AVATIGVI 




pourcentage des armatures dans la section calculée ne vérifie pas la 
condition Hmin © ZH © L Himax ©, on change les dimensions 
transversales de la pièce et l’on calcule à nouveau les quantités 
et #,. On considère que la section est correctement choisiesiu % = 1 
Exemple IV.1. Déterminer les dimensions de la section d’un po- 
teau chargé en compression simple et la section à donner à ses arma- 
tures. La longueur de flambement du poteau est !, — 6,4 m, la 
force longitudinale de calcul est N = 150 tf = 1500 LN, l'effort 
provenant des charges permanentes et des surcharges de longue 
durée est NV ;4 — 100 tf — 1000 KN. On emploie un béton lourd de 
classe M 200 (m1 = 0,85) armé de barres à haute adhérence en acier 
laminé à chaud de classe A-IT. 

Solution. On trouve dans les Annexes II et IV les valeurs de 
Rpr = 90 kgf/cm? (9 MPa) et de R,.. — 2700 kgf/cm* (270 MPa). 
En se donnant @ = m = 1 et p = 0,01, on trouve à l’aide de la for- 
mule (I1V.5) 


: N : 150 000 : | 
FE Rortufac 085 X 00-001 X 2700 — 1450 cm?. 


Prenons une section de 40 x 40 cm avec # — 1600 cm°. Cal- 
culons les rapports 


lLy/b — 640/40 = 16; N,a/N — 100/150 — 0,667. 
Le coefficient »2 est pris égal à 1, parce que À — 40 cm >> 20 cm. 


Interpolant dans le Tableau IV.1, on trouve q, = 0,78 et p, = 
— 0,837 (en posant que Fi int < #/3FA). D'après la formule (I1V.3} 


P= Pt 2 (pr) RE M 0,78 + 2 (0,887 — 


2700 
— 0,78) 55x50 0:01 = 0,78+ 0,04 = 0,82. 


Afin d’avoir @ < %,, on pose  — 0,82. Conformément à (IV.4) 
on a 


D =. Mbiipe OO EG 0 po 7 ie 


re mPRa.c Ra.c 14 X 0,82 x 2700 2700 


Avec ces dimensions le pourcentage des armatures dans la sec- 
tion sera égal à 


22,4 
U% = 7070 100 = 1,4. ee 


La valeur précisée de , obtenue par le calcul d’après la formu- 
le (III.3) pour u = 0,014 (nous omettons ce calcul), est égale à @ — 
— 0,83. Un nouveau calcul donne F, — 21,6 cm°. Le pourcentage 
des armatures obtenu nu % — 1,4 est conforme aux valeurs recom- 




mandées. Nous choisissons donc pour notre poteau une section de 
40 x 40 cm et une armature longitudinale 420 + 418 A-II 
(avec F, — 22,74 cm°). 

Disposant ces barres dans la section, on s’assure que la condition 
initiale F.int < 1/3, est vérifiée. Aucune modification n'est donc 
plus à faire. 

Désirant poser des carcasses soudées, on utilisera des barres trans- 
versales de diamètre dt, — 8 mm (voir Tableau II.2), espacées de 
he 39 cm conformément à la condition ut, < 20d = 20 x 1,8 — 
= cm. 


CHAPITRE V 


PIÈCES EN BÉTON ARMÉE CHARGÉES 
EN TRACTION SIMPLE 


& V.1. DISPOSITIONS CONSTRUCTIVES 


En calculant les structures, on considère comme soumises à la trac- 
tion simple (traction centrée) des pièces telles que les tirants des arcs, 
les membrures inférieures et les diagonales descendantes des fermes, 


FIG. V.1. Pièces chargées en traction 
simple : 

1, tirant d'arc; 2, membrure inférieure de 

la ferme: 3, diagonales descendantes de la 

ferme; 4, paroi du réservoir de forme 
circulaire 


FIG. V.2. Disposition des armatures 


dans la section d'une pièce élancée en 
béton précontraint : 

a, en pré-tension; b, en post-tension ; 1, arma- 

tures de précontrainte (barres, câbles de fils 

droits, câbles torsadés); 2, armatures ordi- 


naires; 3, canal pour armature de précon- 
trainte: 4, barres transversales 


les parois des réservoirs à liquides de forme circulaire (fig. V.{), 
ainsi que certains autres éléments. 

Les principes fondamentaux de la conception des pièces en béton 
armé exposés dans le chapitre III restent applicables aussi aux pièces 
travaillant en traction simple. Les armatures principales ordinaires 
{non précontraintes) constituées par des barres d'acier sont aboutées 
généralement par soudure; les jonctions de barres par recouvrement 
simple, sans soudure, ne sont admises que dans les dalles et les murs. 




Quant aux armatures de précontrainte travaillant en traction 
(barres, câbles de fils droits, câbles torsadés) utilisées dans des pièces 
élancées, telles que le tirant d’un arc ou la membrure inférieure d’une 
ferme, elles ne doivent présenter aucune jonction. Les aciers de pré- 
contrainte sont disposés de façon symétrique dans la section de la 
pièce (fig. V.2), afin d'éviter autant que possible toute excentricité 
de la contrainte créée dans la pièce lors du déblocage des barres (qui 
peuvent être débloquées toutes ensemble ou par groupes). 

En cas de précontrainte par post-tension, les armatures de pré- 
contrainte sont placées dans des canaux appropriés et ne travaillent 
pas encore, au moment de la mise en tension, dans la section de la 
pièce. Il y a donc intérêt à prévoir dans la pièce un certain nombre 
d’'armatures ordinaires, c’est-à-dire autres que les armatures de pré- 
contrainte (voir fig. V.2, b). Les armatures ordinaires sont situées 
sensiblement près de la peau de la pièce, afin de mieux parer à toute 
excentricité lors de la mise en tension. 


$ V.2. ÉTAT DE CONTRAINTE ET CALCUL D’UNE PIÈCE TENDUE 


Au fur et à mesure que la traction exercée sur la pièce devient plus 
grande, la pièce subit trois stades consécutifs caractérisant son état 
de contrainte. Le stade Î prend fin avant l’apparition des fissures 
dans le béton. Le stade II commence avec la fissuration. Le stade III 
correspond à la ruine. 

Stade I. Sous l’action de la force de traction À, l’armature et le 
béton se déforment ensemble, présentant le même allongement rela- 
tif e, — et. Cette égalité permet de chercher la relation entre 
les contraintes dans l'acier 0, et dans le béton 6}. tr: 

Ja __ Ob.tr 
E a Eb. tr d 


Les expériences montrent qu’au moment où le béton est prêt à 
se fissurer, son module dt déformation en traction E}+- est à peu 
près égal à la moitié du module d'’élasticité initial du béton en com- 
pression Æ,, de sorte que £ 4, Æ 0,5 E}. La contrainte subie par le 
béton en cet état est égale à sa charge de rupture en traction axiale 


(simple) R:,. On a donc 
Ca = 2 58 Fr = 20 Rte où n— _ (V.2) 


OÙ Oa = Oh, tr (V.1) 


Eb.tr ° 


Immédiatement avant la fissuration, la contrainte dans le béton 
étant égale à opte = Rtr, la valeur de la force de traction extérieure 
N;, se compose des efforts engendrés dans le béton et dans l'acier: 


Nir = Opete Fo + Gala = Rir (FD + 2nFa), (V.3) 
où F, et F, sont les sections du béton et des armatures longitudina- 
les respectivement. Comme le béton résiste mal à la traction, la 


pièce en béton non précontraint présente des fissures sous un effort 
très faible qu’on n’a aucun intérêt à calculer. 




Dans une pièce tendue en béton armé, dès que la contrainte dans 
le béton a atteint une valeur égale à la charge de rupture en traction, 
on voit se former des fissures dans le béton. Dans une section fissurée 


tout l'effort de traction est 
repris par les armatures, si 
bien que la contrainte dans 
l'acier devient plus grande 
(voir le diagramme de oô;,ft, 
sur la figure V.3, a). La 
contrainte dans le béton 6:.+r 
de la section fissurée est égale 
à zéro: à mesure que l'on 
s'éloigne de la fissure, cette 
contrainte croît jusqu'à at- 
teindre R4. Aux endroits où 
elle devient égale à la charge 
de rupture en traction, d’au- 
tres fissures peuvent se pro- 
duire (voir fig. V.3, a). C'est 
cette condition qui détermine 
la distance entre fissures /{. 
Dans la zone de longueur À, 
l'adhérence entre l’acier et 
le béton fait naître des con- 
traintes tangentielles Tan. 
Les diagrammes des con- 
traintes tangentielles et des 
efforts sur lf dans le béton 
et l'acier sont montrés sur 
la figure V.3. 

Dans la zone de longueur 
ls, les résultantes des contrain- 
tes tangentielles t,4n et des 


contraintes normales À+, se 
font équilibre dans le béton. 
On a donc 


RtrFp = TaanS@Ë,  (V.4) 
OÙ Tadn Est la contrainte tan- 
gentielle maximale sur 4; S 
est le périmètre de la section 
de l'acier; «,le coefficient 


Première Fissure 
à fissure Suivante 
ee 2e 


ttes 
ED. NS 






FIG. V.3. Etat de contrainte d’une pièce. 
chargée en traction simple: 


a, pendant la fissuration; b, après la fissura- 
tion; 1, diagramme des contraintes nonnales 
dans le béton; 2, diagramme des contraintes 
dans l'acier; 3, diagramme des contraintes 
tangentielles dans le béton; 4, distribution des 
efforts dans la zone de longueur l{; 5, distri- 


bution des efforts dans l’acier de cette zone d 
idem, dans le béton 


de remplissage du diagramme réel des contraintes tangentielles par 
rapport à sa forme rectangulaire. 


Introduisant les notations 


(V.5) 




on déduit de (V.4) l'expression de la distance entre fissures: 


Nes Le ; 
l n S n ie” (V 6) 

Stade II. Les fissures se sont formées, l'effort extérieur NV est 
plus grand que W:, la pièce se trouve divisée en blocs séparés de lon- 
gueur /4 reliés entre eux par les armatures (voir fig. V.3, b). L’effort N 
dans les sections fissurées est reporté tout entier par les aciers. La 
contrainte développée dans l’acier est égale à 


Ca = NF. (V.7) 


L’armature de chaque bloc, tout en s’allongeant, fait travailler 
en traction le béton aussi par adhérence. À mi-distance entre deux 
fissures voisines, la contrainte dans l’acier 0,, est moins grande que 
dans la section fissurée 0,. Quant à la contrainte dans le béton, elle 
croît à partir du zéro au droit de la fissure jusqu’à une valeur maxi- 
male 61.+- à mi-distance entre deux fissures. Il va de soi que cette 


valeur maximale ne peut guère dépasser R+, (voir fig. V.3, b). 

La contrainte moyenne de l'acier 6: moy; définie en tenant comp- 
te de la contribution du béton entre fissures à la déformation de la 
pièce, est inférieure à o,, et son allongement relatif moyen €, moy €St 
plus petit que l’allongement €, calculé sans tenir compte de la contri- 
bution du béton. Le taux de travail du béton entre fissures dans la 
pièce sollicitée en traction est égal à 


Oa. Ba, 
Va = 2: moy — a. moy (V.8) 
a Ea 


En regardant la figure V.3, b, on remarque que le taux de tra- 
vail 1, est aussi égal au rapport des aires du diagramme réel des 
contraintes dans l’acier sur // et du diagramme rectangulaire pour la 
contrainte O,: 




__ Calt—GQtrOa2it _4 Ca2 
re = 1 — ot On ? (V.9) 


où &+- est le coefficient de remplissage du diagramme des contrain- 
tes de traction dans le béton entre fissures. 

L'ouverture des fissures a peut être assimilée, avec une précision 
satisfaisante, à l'allongement des armatures sur +, abstraction 
faite de l’allongement du béton. On tire de (V.8) l'expression 




a1= En. moylt = Vatalt = Va Ge lt. ‘(V.10) 


Les relations caractéristiques du stade II restent en vigueur 
tant que les contraintes dans l’acier restent en dessous de la limite 
de proportionnalité. 

Stade III. La ruine de la pièce commence dès que les contraintes 
dans l'acier sont devenues supérieures à la limite de proportionna- 
lité et que des déformations anélastiques se sont manifestées. La 




ruine est considérée comme définitive quand les contraintes dans 
l'acier ont atteint la limite d'élasticité 64, apparente (si l’acier pré- 
sente un palier d'écoulement) ou conventionnelle (dans le cas con- 
traire). L’effort occasionnant la rupture de la pièce est égal à la charge 
de rupture de l'acier seul, sans l'intervention du béton dans le tra- 
vail à la traction de la pièce. 

La résistance de la pièce est vérifiée suivant les états-limites 
ultimes à l’aide de la formule 


N<R,F, (V.11) 


où À est l'effort de calcul dans la pièce engendré par les charges de 
calcul; R, est la résistance de calcul à la traction de l'acier. 

Les pièces en béton non précontraint offrent si peu de résistance 
à la fissuration qu'on n’a aucun intérêt à la calculer. D'une façon 
approximative, on évalue l'effort correspondant au début de la fis- 
suration à l’aide de la formule 


Net =0,8RiF, (V.12) 


où le coefficient 0,8 tient compte de la diminution de la résistance 
caractéristique du béton à cause du retrait. 

L'ouverture des fissures est calculée pour le stade II de l'état 
de contrainte de la pièce. Nous avons signalé que la formule (V.10) 
ne fournit que des valeurs approchées de at. Les Normes préconisent 
une relation empirique 


a (mm)= can Fe 20 (3,5 — 100u) 7 Z(mm), (V.13) 


où À — 1,2; ca est un coefficient égal à 1 si l’on tient compte des 
surcharges de courte durée et des actions peu prolongées des charges 
permanentes et des surcharges de longue durée, et à 1,5 si l’on prend 
en considération les surcharges répétées et les actions prolongées des 
charges permanentes et des surcharges de longue durée pour des struc- 
tures en béton lourd durci à l'air; n est un coefficient égal à 1 si le 
béton est armé de barres à haute adhérence, à 1,2 s’il s'agit des fils 
à haute adhérence et des câbles torsadés et à 1,4 si les armatures re- 
présentent des fils lisses; 0, est la contrainte dans l'acier calculée 
par la formule (V.7); u est la proportion des armatures de la section 
assimilée à un profil rectangulaire (sans parties comprimées dé- 
bordantes) ayant une hauteur utile L,, mais non supérieure à 0,02; d 
est le diamètre des armatures. 

L'ouverture des fissures de courte durée provenant de la charge 
totale est calculée à l’aide de la formule « 


atcd — Ety — Ate + At (V.14) 


où af, est l'ouverture des fissures causée par une action peu prolon- 
gée de la charge totale ; as,, l'ouverture initiale des fissures provoquée 
par l’action peu prolongée des charges permanentes et des surchar- 




ges de longue durée; 473, l'ouverture des fissures de longue durée 
provenant des charges permanentes et des surcharges de longue durée. 
Les quantités ar:, ar, et ay, sont calculées à l’aide de la formule 
(V.13) où les différentes grandeurs prennent les valeurs suivantes: 
Ca — 1, Ga = (Nia + Noa)/Fa pour ar; 
Ca = 1,9, 0 = Njd/FAa pour as. 


L'ouverture des fissures consécutive à une action prolongée des 
charges permanentes et des surcharges de longue durée est af. ja = 
Exemple V.1. Calculer la section à donner aux armatures et véri- 
fier l'ouverture des fissures dans une pièce soumise à une traction 
simple. Section 25 x 295 cm; aciers de classe A-IIT; béton lourd de 
classe M 200; mp1 = 1; Na = 10 tf; Na = 6 tf; effort de calcul 
N = 20 tf. La résistance à la fissuration de la pièce doit satisfaire 
aux conditions de la 3° catégorie : at. ja < 0,8 mm, a1..q & 0,4 mm. 
Solution. On trouve dans l’Annexe VI 
E, = 2-10% kgf/cm° (2-105 MPa), 
Ra = 3600 kgf/cm° (360 MPa). 


La formule (V.11) fournit la section à donner aux armatures: 


__ MN 20000 ; 
Fa = 5660 — °:58 cm”. 


On adopte comme armatures 4 @ 14 A-III de section F, — 6,16 cm°. 
Calculons l'ouverture des fissures d’après la formule (V.13) 
après avoir déterminé p = F;/F, = 6,16/25 x 25 = 0,01: 


On. 10 = Wèa/Fa = 40 000/6,16—1620 kgf/cm!: 
Oastot = (Na + N£)/Fa = (10 000 + 6000)/6,16 — 2594 kgf/em? ; 
at.s= ar, ja = 1,2 X 1,5 X 1-20 (8,5 — 100 x 0,01) 14 
—0,175 mm<0,3 mm; 


an=1,2 x 1x 1-2 (85— 100 x 0,01) Ÿ 140,187 mn ; 


aa = 1,2 x 1 x 1-28 (8,5— 100 x 0,01) Ÿ/14=0,117 mm; 


d’après la formule (V.14) 
dt.cda — Ati — to + Atg — 0,187 — 0,117 + 0,175 — 
— 0,245 mm < 0,4 mm. 




$ V.3. PARTICULARITES DU COMPORTEMENT ET CALCUL 
D'UNE PIECE EN BÉTON PRECONTRAINT 


Soit une pièce en béton mise en précontrainte par compression simple, 
conçue pour travailler en traction simple. Désignons par F;, F, les 
sections du béton et des armatures de précontrainte respectivement, 
et par Co, la contrainte qui se manifeste dans l'acier soit avant la 
mise en précontrainte du béton, soit en cas d'annulation de la pré- 
contrainte du béton à cause de l’action des forces extérieures. 


Comportement de la pièce en pré-tension 


Les armatures sont posées dans le moule et tendues sur les culées 
avec une contrainte 64. Pendant toute la durée du bétonnage et tant 
que le béton durci n’a pas atteint sa résistance de précontrainte R,, 
les aciers restent fixés sur les culées. Au cours de cette période ils 
présentent des pertes de précontrainte instantanées (pertes premiè- 
res) Op1, qui sont antérieures à la mise en précontrainte du béton, 
si bien que les contraintes dans les aciers deviennent égales à 6, — 6,1. 

Débloquer les aciers revient à appliquer à la pièce un effort de 
compression extérieur égal à 


(Oo — Op1) Fpe- (V.15) 


Sollicités par cet effort, le béton et l'acier présentent le même rac- 
courcissement relatif €, — €,. On a donc 


AO, — Fe Oh — 20h) 


où 6L est la contrainte du béton; Ao,, la diminution de la contrainte 
de l'acier qui se produit au moment où l’on relâche les armatures 
tendues et la pièce se raccourcit. 

Après qu'on a relâche les armatures, la contrainte dans l'acier 
devient égale à 


Og — Op1 — Op: (V.16) 


Avant la mise en action de la force extérieure, les tractions dans 
l'acier et les compressions dans le béton de la pièce se font équilibre : 


Fe (O0 — Op1 — 26p) = FpOp: (V.17) 
D'où 
o, = mire, (V.18) 
b.éq 
Fréq = Fr + nFpc: (V.19) 


Après avoir encaissé l'effort de la précontrainte, le béton pré- 
sente des pertes de précontrainte différées (pertes secondes) 62. 




A partir de ce moment, on observe dans les sections de la pièce des 
contraintes dites permanentes, dans l'acier 


Og — (Opa Ale Op2) — AO (V.20} 
et dans le béton 
oi, —=-Le— Ci 0pe)l Pre, (V.21) 
b. éq 


Pendant la phase initiale de l’action de la traction simple exté- 
rieure V, la précontrainte du béton diminue graduellement pour 
s’annuler finalement. En ce moment la contrainte du béton est nulle, 
6 = 0, et celle de l’acier est 


Oo — (Op1 + Opo): (V.22) 


Si l'effort extérieur continue à croître, l’état de contrainte de la 
pièce passe par les trois stades consécutifs décrits dans le $ V.3, à 
SAVOIrT : : 

— stade I, avant la fissuration; 

— stade IT, après la fissuration; 

— stade III, ruine de la pièce. 

En fin du stade I la contrainte du béton atteint une valeur égale 
à la charge de rupture en traction simple. Pendant que la contrainte 
du béton passe de zéro à la charge de rupture, la contrainte dans les 
armatures de précontrainte augmente d'une valeur définie par (V.2), 
soit en moyenne de 30 MPa (300 kgf/cm°). Immédiatement avant la 
fissuration, la contrainte dans l'acier (compte tenu de la formu- 
le (V.22)) est donc 


Oo — (Op1 + Ope) + 2nRtr. (V.23) 


C'est d’après cet état que l’on calcule la valeur de l'effort extérieur 
conduisant à la fissuration. 

Au stade II, les fissures étant formées, ce sont les aciers qui re- 
portent la totalité de l'effort extérieur dans chaque section fissurée. 
Le béton compris entre deux fissures voisines contribue aussi à la 
résistance à la traction de la pièce. 

La contrainte dans l'acier traversant une section fissurée s’éva- 
lue à l’aide de la formule 


0x ={N — NoFas (V.24) 
où l'effort de précontrainte est 


No = Fpe [08 — (Op1 + Opa)l. (V.25) 


Au stade III il se produit la ruine de la pièce. C’est d’après cet 
état que l'on calcule la capacité portante. 

Dans bien des cas, la précontrainte de la pièce n’exerce aucune 
influence sur la capacité portante de cette dernière. 




Comportement de la pièce en post-tension 


Cette méthode de précontrainte consiste à fabriquer la pièce en 
béton non armé ou faiblement armé présentant des canaux dans la 
masse ou des rainures en surface, à attendre que le béton soit durci, 
à engager les armatures longitudinales dans les canaux (rainures) 
et à tendre les armatures de telle façon que les efforts de compression 
soient repris par les faces en bout de la pièce. L'’acier présente alors 
des pertes de précontrainte instantanées (pertes premières) 6,1, qui 
se manifestent avant la mise en tension du béton; quant au béton, 
il se trouve uniformément comprimé jusqu'à une valeur 6}. La 
contrainte dans l'acier est calculée suivant la formule (V.18). 
Ensuite, ce sont les pertes différées (pertes secondes) 6,, qui se 
produisent dans l'acier, tandis que la contrainte du béton diminue. 
jusqu’à 01. La contrainte dans l'acier se calcule à l’aide de la for- 


mule (V.20). 
En ce moment la précontrainte de la pièce atteint une valeur 


permanente. 

Avec l'augmentation progressive de la charge extérieure, la pré- 
contrainte du béton tombe à zéro, après quoi l’état de contrainte 
de la pièce passe par tous les trois stades décrits plus haut. 


Calcul de la pièce aux états-limites 




La pièce est calculée aux états-limites ultimes, de façon à vérifier 
la condition 
N < Ra.pel'pe + RaFa (V.26) 


OÙ Ra.pe et Fhe Sont respectivement la résistance de calcul et la sec- 
tion des armatures de précontrainte; À, et F, sont la résistance de 
calcul et la section des armatures ordinaires. 

Si l’armature est fabriquée en acier à haute résistance, les valeurs. 
de À; (Ra.pe) données en Annexes VI et VII sont à multiplier par un 
coefficient de comportement mn, égal à 1,2 pour les armatures des 
classes A-IV, Ar-IV, à 1,15 pour les armatures des classes A-V, Ar-V, 
B-II, Bp-II, K-7 et à 1,1 pour les armatures des classes AT-VI. 

La condition de fissuration prise en compte dans le calcul d'une 
pièce précontrainte chargée en traction simple s'écrit 


S E : 
NN où NMr=Ren(Fi+2 Fa) + Nos  (V.27) 


ici V est l’effort de calcul déterminé en considérant les charges caräc- 
téristiques et en introduisant un coefficient nr > À ou x = 1, en fonc- 
tion de la catégorie des conditions de résistance à la fissuration de la 
structure (voir $ III.1); V; est l’effort repris par la section normale 
de la pièce au moment de la fissuration; WV, est l'effort de précon- 
trainte calculé en faissant intervenir les pertes et le coefficient de 




précision de la mise en tension des armatures en fonction du stade 
de travail considéré de la pièce. 

L'ouverture des fissures est calculée suivant la formule (V.13) 
en prenant 


Ta = 7 | (V.28) 


L'exigence de la non-réouverture des fissures (voir $ III.{) 
est considérée comme satisfaite si les deux conditions ci-après sont 
réunies : 

a) aucune déformation irréversible ne se produit dans les arma- 
tures de précontrainte sous l’action des charges permanentes et des 
surcharges de longue et de courte durée, c'est-à-dire 


Oo + Ca < ÂRarr; (V.29) 


où 6, est l’accroissement de la contrainte dans les armatures de pré- 
contrainte déterminé par l’action des charges extérieures: 4 = 0,65 
pour les fils d'acier et 4 — 0,8 pour les barres d'acier : 

b) une contrainte d'au moins 1 MPa (10 kgf/cm?) est conservée 
dans chaque section du béton pendant l’action des charges perma- 
nentes ct des surcharges de longue durée. 

Exemple V.2. Calculer une pièce en béton précontraint conçue 
pour travailler en traction simple à l'air libre (membrure de ferme 
d'une rampe ouverte). Longueur 24 m. Section 24 x 16 cm. Béton 
lourd M 500 traité par la chaleur. Armatures de classe K-7, diamètre 
15 mm. tendues en pré-tension. Efforts dans la pièce: Mermanente= 
— 20 1f, Na = 40 tf, Néa — 25 tf. Coefficients de surcharge #7, — 
— 1,1 pour la charge permanente et 7, — 1,4 pour les surcharges de 
longue et de courte durée. 

Solution. La charge de calcul est N = 20 x 1,1 + (40 + 25) x 
X 1,4 — 113 tf. Dans l'Annexe VII on trouve R, — 10 600 kgf/cm?, 
Rarr = 16 500 kgf/cm°?, E, — 1,8:105 kgf/cm°’. Le coefficient de 
comportement de l'acier est ma, = 1,15. Les barres longitudinales 
des treillis placés autour des armatures de précontrainte n’entrent 
pas dans le calcul, si bien qu'on a F, = 0 

Calculons la section à donner aux armatures de précontrainte 
Fe à l’aide de la formule (V,26) en y mettant }; = 0 et Rape = 
= Mayla = 1,15 X 10 G00 — 12 200 kgf/cm°: 


Fe= =" —=—113000/12 200 = 9,3 cm2. 
a FRE 


Nous adoptons comme armature 8 @ 15 K-7 avec Fe = 8 X 1,41 = 
— 11,3 cm°. 

Calcul de la résistance à la fissuration. Les structures destinées 
à être exploitées à l'air libre et munies d’armatures de classe K-7 




doivent satisfaire aux conditions de résistance à la fissuration de 
9e catégorie, avec af ca & 0,15 mm. On a donc 


F,=24 x 16—384 cm2; u— F- — 11,3/384 —0,0294, ou 2,94%° 


Pour voir si le calcul à l’ouverture et à la non-réouverture des 
fissures est nécessaire ou non, calculons la pièce à la fissuration sous 
l'action de la charge totale de calcul N = 113 tf. Supposons que la 
précontrainte de l'acier soit égale à o, — 11 000 kgf/cm?et voyons 
si la condition (III.9) est vérifiée avec p = 0,050, = 0,05 x 11 000— 
= 550 kgf/cm° et 0,8R,rr = 0,8 X 16 500 = 13 200 kgf/cm°?: 

Oo < Rarr — p; 11 000 < 13 200 — 550, 


La condition est vérifiée. 
Trouvons dans l'Annexe V la valeur de Æ£,, = 0,9 x 3,6-105 — 
— 3,25.105 kgf/cm°: 


__ Ea 1,840 
Ep  3,25.410 


La section homogène équivalente de la pièce est égale, en vertu de 
(III.3), à 


Feqa = Fp + nFpe = 394 + 5,6 X 11,3 = 447 cm°. 


Calculons à présent les pertes de précontrainte: 
par relaxation des tensions, selon la formule (III.15): 


(s) 11 000 

G,= (0,27 FR — 0,1) = (0,27 5255 — 0,1) x 11 000 = 
— 880 kgf/cm? ; 

par variation de température, avec At — 65°: 


O2 = 12,9 At = 12,5 x 65 = 810 kgf/cm?; 


n 5,6. 


par déformation des ancrages, suivant la formule (III.17) avec 
l — 24 met À = 2 mm: 


03= + Eu —0,2/2400 x 1,8. 10° — 140 kgf/em? ; 


par déformation du moule. Faute de données sur la construction 
du moule, on pose 6, — 300 kgf/cm°. 
En somme 


Opi-s = O1 + Op + O3 + 03 = 880 + 810 + 140 + 300 = 

— 2130 kgf/cm°. 

Compte tenu de ces pertes 6, — 11 000 — 2130 — 8870 kgf/cm°. 
La force de précontrainte est égale, d’après (III.5), à 
No = Fpe0o = 11,3 X 8870 = 100 000 kgf. 


5—0948 65 


La précontrainte dans le béton se calcule selon la formule (ITI.6) : 
29- — 100 000/447 — 224 kgf/cm?. 
Admettons que la résistance de précontrainte du béton soit égale à. 
R, = 0,8R = 0,8 x 500 — 400 kgf/cm:. 


Voyons si le béton peut supporter la contrainte 6.» = 
— 224 kgf/cm°: 
DE — 224/400 = 0,56 < 0,65 
(la valeur de o61.pe/RQ peut aller jusqu'à 0,65, car la charge fait di- 


minuer Ob.pe): 

Ceci fait, calculons les autres pertes de précontrainte: 

par fluage rapide du béton avec 6}.pe/Ro = 0,56 << a = 0,6 
(voir formule (III.21)): 


Ob.po — 


0e = 500 2 0,85 — 500 x 0,56 x 0,85— 280 kgf/em?. 
Les pertes instantanées s'évaluent donc à 6,1 = G1-5 + O8 = 
— 2130 + 280 — 2410 kgf/cm°: 
par retrait du béton (Tableau III.2) 


O7 — 400 kgf/cm°; 


par fluage différé du béton, en prenant 64.pe/Ro = 0,56, en ap- 
pliquant la formule (111.22) et en introduisant le coefficient 0,85 
(béton traité par la chaleur): 

Le 0,85 — 2000 x 0,56 x 0,85— 950 kgf/em. 

Les pertes différées s’évaluent à 0, = 07 + 69 = 400 + 950 = 
— 1350 kgf/cm*. 

Les pertes totales sont égales à 


Op = 2000 


Op = Op + Opo = 2410 + 1350 = 3760 kgf/cm°. 


Calculons la précontrainta de, l’acier après déduction des pertes 
totales : 
Op = 11 000 — 3760 — 7240 kgf/cm°. 


Le coefficient de précision de la mise en tension des armatures 
de précontrainte se calcule d’après la formule (111.24) en prenant 
AMmt = 0,1 (mise en tension mécanique): 


Mmt = 1 — Ammi = 1 — 0,1 — 0,9. 


Calculons la force de précontrainte en tenant compte des pertes 
totales et du coefficient de précision: 


NA= Fpemt0o = 11,3 X 0,9 X 7240 = 73 500 kgf. 
Pour 1e béton M 500 on trouve dans l’Annexe III 
R{r11 = 20 kgf/cm°. 


L'effort subi par la section avant la formation des fissures est égal, 
en vertu de la formule (V.27), à 


Nr = Run (Fr + 2nFie) + No = 20 (884 +2 X 5,6 x 11,3) + 
+ 73 500 — 83 700 kgf — 83,7 ti. 


On a donc WV; << N, car 83,7 << 113; cela veut dire que le calcul à 
l'ouverture et à la non-réouverture des fissures doit obligatoirement 
être fait. 

Cherchons l'ouverture des fissures de courte durée provenant de 
la charge caractéristique totale 


Ne = 20 + 40 + 25 = 85 tf. 


D'après la formule (V.28) 
___ NC—N, __ 85 000— 73 500 


Fe 113 — 1020 kgf/cm°. 




D'après la formule (V.13) 


ar= k-ca-n 5e 20 (3,5— 100p) ÿ/ d— 


—1,2x 1 x 1,20 20:(3,5 — 100 x 0,0294) 15 — 


— 0,023 mm<0,15 mm. 


Faisons maintenant le calcul à la non-réouverture des fissures. 
Dans le cas étudié le plus grand danger est le dépassement de 6,, 
aussi mettrons-nous 


Mmt = 1 + Ammt = 1 + 0,1 = 1,1 
Op — 1240 X 1,1 — 7960 kgf/cm°. 


Vérifions la condition (V.29) en posant À = 0,65 (les armatur®s 
étant constituées par des fils d'acier): 
O9 + Oa — RER arr; 7960 + 1020 < 
Z 0,65 x 16 500; 8980 << 10 720; 


la condition est vérifiée. 


5% 67 


Vérifions maintenant les contraintes de compression dans le 
béton engendrées par les charges permanentes et les surcharges en 
longue durée: 


o, — Whermanente + Nia)— No __ (40 0004 20 000) —73 500 _ 
Pis Féa = _ 44 _ 


— — 30,2 kgf/cm?. 


Autrement dit, le béton conserve des contraintes de compression 
supérieures à 10 kgf/cm°? qui préviennent toute réouverture des fis- 
sures. 


CHAPITRE VI 


PIÈCES EN BÉTON ARMÉ CHARGÉES 
EN FLEXION SIMPLE 


$ VI.1. DISPOSITIONS CONSTRUCTIVES 


Dans les structures en béton armé, les pièces simplement fléchies 
les plus courantes sont les dalles et les poutres. On appelle dalle 
(ou hourdis) une pièce plane continue dont l'épaisseur ka est très 
inférieure à la longueur !, et à la largeur ba. La poutre est une pièce 
élancée dont la longueur ! est très supérieure aux dimensions trans- 
versales k, b. Les dalles et les poutres servent à composer des struc- 
tures variées, le plus souvent des planchers et des toitures planes, 


FIG. VI.{. Planchers en béton armé constitués par des éléments préfabri- 
qués (a) ou coulés in situ (b): 
1, dalles; 2, poutres 


constitués d'éléments préfabriqués, coulés in situ ou fabriqués par 
une combinaison de ces deux procédés (fig. VI.1). 

Les dalles et les poutres peuvent être à simple travée ou à travées 
multiples. 

Coulées in situ, les dalles ont une épaisseur de 60 à 100 mm. 
Quant aux dalles préfabriquées, elles possèdent la plus petite épais- 
seur compatible avec les conditions d'utilisation. 

On voit sur la figure VI.2, a une dalle à simple travée reposant 
sur ses deux côtés opposés, et sur la figure VI.2, b une dalle à travées 
multiples coulée in situ et reposant sur une rangée d’appuis parallè,, 
les. De telles dalles se déforment en charge à la façon d’une structure 
composée de poutres, à condition que la valeur de la charge reste in- 
changée dans la direction perpendiculaire à la travée. 

Les dalles sont ferraillées avec des treillis soudés (voir $ I[.3) 
dont les armatures principales sont orientées parallèlement à la 
travée et reportent les tractions qui se manifestent en charge, con- 
formément au diagramme des moments fléchissants (fig. VI.2). 




On_prévoit donc un ferraillage inférieur en travée et un ferraillage 

supérieur de renforcement au droit des appuis intermédiaires. Les 

treillis des dalles à travées multiples peuvent être continus 
(fig. VI.2, b) ou composés (fig. VI, 2, c). 

Les barres principales, de 3 à 10 mm de diamètre, sont espacées 

de 100 à 200 mm et protégées par un enrobage d'au moins 10 mm. 

Dans des dalles très épaisses 


- nr. (plus de 100 mm), l'épaisseur 
M0, 0/1 ? s Q A 
(charge uniformément d'enrobage ne doit pas être 

répartie) inférieure à 15 mm. 


RL Er Les armatures transversa- 


les (de répartition) servent à 

maintenir l’espacement prévu 

24 des barres principales, à di- 

= minuer les déformations pro- 

voquées par les variations de 

L la température et le retrait et 

Diagramme des moments (charge à répartir les charges locales 

b) RAUPNMEMENE EPAREE) sur une surface plus étendue. 

Elles ont un diamètre moins 

grand que les armatures prin- 

cipales. Leur section totale 

doit être non inférieure à 

1/10 de la section des arma- 

tures principales au droit du 

moment fléchissant maximal. 

Les armatures transversales 

sont  espacées de 250 à 

300mm, exceptionnellement de 
350 mm. 

FIG. VI.2.NFerraillage des dalles: Les barres longitudinales 


bee ee contre een der sont ancrées sur les appuis 
raillage :composé ; 1, barres principales; 2, extrêmes libres (non encastrés) 
warres de répartition . Luz z 
comme il a été montré sur la 
figure [II.2, a. 

Il y a des cas où les dalles reçoivent un ferraillage de barres isolées 
assemblées en grilles par ligatures manuelles: ce sont les cas où un 
treillis soudé standard ne peut être utilisé (contour sinueux de la 
dalle, nombreux trous et ouwertures, etc.). 

Les poutres en béton armé peuvent avoir une section rectangulai- 
re, en T, en double T, une section trapézoïdale (fig. VI.3). 

La hauteur À d’une poutre est comprise entre 1/10 et 1/20 de la 
portée, en fonction du type d la structure et du cas de charge. Dans 
le but d’unification, on choisit une hauteur multiple de 50 mm si 
elle ne dépasse pas 600 mm et multiple de 100 mm si elle est plus 
grande que 600 mm. 

La largeur de la section rectangulaire b d’une poutre (largeur de 
profil) est choisie entre 1/4 et 1/2 de sa hauteur À, à savoir: 100 — 




__ 420 — 150 — 200 — 220 — 250 mm, ensuite de 50 mm en 50 mm. 
11 y a intérêt à prendre b aussi petit que possible, afin de réduire la 
dépense de béton. 

Les armatures longitudinales sont disposées dans la section de 
la poutre en simple ou en double file, de façon à laisser des espaces 


b) D d) 
; T Î 


FIG. VI.3. Formes de section et variantes de ferraillage des poutres: 


a,’section rectangulaire; b, section en T; c, section en double T'; d, section trapézoïdale; 
1, armatures longitudinales; 2, armatures transversales 


libres suffisants pour un bétonnage correct (sans vides ni cavités). 
Les valeurs des espaces libres et des épaisseurs d’enrobage à prévoir 
sont indiquées sur la figure VI.4. 

Les armatures longitudinales des poutres et des dalles sont dis- 
posées conformément aux diagrammes des moments fléchissants dans 


a}? 4 pour k>250mm 
%|2 /Omm pour k<250mm 


2 20mm pour k 2 250mm 
Cenr > 15mm pour h<250mm 






FIG. VI.4. Disposition des armatures idans'la section d’une poutre: 


enr épaisseur d’enrobage des armatures principales; dors épaisseur d’enrobage des armatures 

de montage; d, diamètre de la barre longitudinale la plus épaisse; Ein» €Spacement deg 

armatures longitudinales inférieures (au moment du bétonnage) ; esup, espacement des arma- 
tures supérieures (au moment du bétonnage) 


les zones tendues, afin de reporter les tractions longitudinales qui 
se manifestent en charge dans la structure fléchie. Ce sont des barres 
à haute adhérence (moins souvent des ronds lisses) de 12 à 32 mm 
de diamètre. 

En plus des moments fléchissants, la poutre en béton armé est 
exposée à des efforts tranchants qui doivent être repris par des arma- 




Diagramme des moments (charge 
uniformément répar tie) 


Aciers en allente soudes 
sur chantier 
a) 4 | Béton | 
4}, 4 C-1 nca rcus ET C7 
DRE 77 LUE 
ÉRROR “eme 
uiventil V2 ( Suantss Li 
Fa EE # 
b) 12 8 J ] 
7A 12 3 L 
Suivant 2-2 1 
Et Variante Suivant 5-5 7— Suivant 66 T-f 
6 ICE tif TI, Jo) HE 
d : 6 EFc -1 C-2 


FIG. VI.5. Variantes du ferraillage des poutres: 


a, poutre à simple travée armée de carcasses soudées; b, idem, avec carcasses ligaturées : 
ce, poutre préfabriquée à travées multiples de section rectangulaire ; d, poutre coulée en place 
à travées multiples de section en T ; 1, barres longitudinales principales: 2, barres transver- 
sales des carcasses; 3, harres longitudinales de montage ; 4, barres transversales de raccorde- 
ment; 5, barres principales relevées; 6, cadres des carcasses ligaturées ; 7, barres principales 
des treillis sur appui; &, barres de répartition des treillis sur appui; 9, barres de raccorde- 
ment (deux barres de diamètre non”’inférieur À 10 mm ni au demi-diamètre des barres de rac- 
cordement inférieures) 


tures transversales. La proportion des armatures transversales est 
déterminée par le calcul et par les dispositions constructives. 

Les armatures longitudinales et transversales sont réunies en 
carcasses, soudées (voir $ II.3) ou ligaturées (à défaut de soudeuses). 
Moins résistantes, exigeant beaucoup de travail manuel, les carcas- 
ses ligaturées ne sont admises Q@'à titre d'exception, dans les cas où 
les conditions locales s'opposent à l'emploi des carcasses soudées. 

Les carcasses soudées planes (nappes) sont assemblées entre elles: 
par des barres transversales horizontales espacées de 1 à 1,5 m, de 
façon à former des carcasses tridimensionnelles (cages). 

Quelques schémas de ferraillage des poutres à simple travée 
avec des carcasses soudées sont montrés sur la figure VI.5, a. Si 
l’on est obligé d'employer des carcasses ligaturées (fig. VI.5, b), on 
met des cadres fermés dans les poutres de section rectangulaire et. 




des cadres ouverts sur le haut dans les poutres en T où l’arête de la 
section est liée des deux côtés à un hourdis continu. Une poutre large 
de plus de 35 cm reçoit des cadres à branches multiples. Les cadres: 
des carcasses ligaturées doivent avoir un diamètre non inférieur à 
6 mm si la hauteur de la poutre est de 800 mm au plus, et un dia- 
mètre non inférieur à 8 mm si la poutre est plus haute. 

Les calculs et les dispositions constructives définissent l’écarte- 
ment longitudinal des aciers ou cadres transversaux : non supérieur à. 
h/2 ni à 150 mm pour À < 450 mm et non supérieur à 2/3 ni à 500 mm 
pour k > 450 mm. Cette exigence est applicable à la portion de la 
poutre voisine de l'appui, longue de 1/4 de la portée de la pièce si la 
charge est répartie uniformément, et à la partie de la poutre entre 
l'appui et la masse pesante la plus proche si les charges sont loca- 
lisées. Dans les autres parties de la pièce de À > 300 mm l’écarte- 
ment des armatures transversales (cadres) peut être plus grand, sans 
dépasser toutefois 3/4 de À ni 500 mm. 

Si la hauteur de la poutre dépasse 150 mm, les armatures trans- 
versales (cadres) doivent être prévues même si cela n’est pas exigé 
par le calcul. 

Une poutre dont la hauteur dépasse 700 mm reçoit des barres lon- 
gitudinales supplémentaires disposées près des faces latérales de la 
section et espacées de 400 mm au maximum dans le sens de la hau- 
teur. Concurrement avec les armatures transversales, ces barres s’op- 
posent à l'ouverture des fissures obliques sur les faces latérales de: 
la poutre. 

Pour maintenir en place toutes les armatures de la poutre au 
cours de la coulée, on prévoit des barres longitudinales de montage: 
de 10 ou 12 mm de diamètre placées dans la partie supérieure de la 
poutre. Dans une poutre préfabriquée, ces barres peuvent être cal- 
culées de façon à reporter une partie des charges pendant la manu- 
tention et le montage. 

Quelquefois on prévoit des barres inclinées, au lieu ou en plus. 
des barres transversales. Elles sont plus efficaces que les barres trans- 
versales, car elles correspondent mieux aux directions des contrain- 
tes de traction principales dans la poutre. Or, les barres transversa- 
les sont plus faciles à poser, donc préférables. Les barres inclinées 
sont généralement orientées sous 45° par rapport aux armatures lon- 
gitudinales. Dans une poutre très haute (plus de 800 mm) cette in- 
clinaison peut atteindre 60°; si la poutre est basse ou si les charges. 
sont concentrées, l’inclinaison peut être diminuée jusqu'à 30°. 

Lorsque le ferraillage de la poutre est constitué par une carcasse: 
ligaturée (en acier des classes A-I ou A-II), il est rationnel de releëèr 
certaines barres principales longitudinales (fig. VI.5, b) afin de 
réduire la dépense d'acier et d'améliorer les qualités mécaniques. 
de la carcasse. Les parties relevées des barres lisses sont terminées. 
par des crochets. 

Une poutre préfabriquée à travées multiples est constituée de 
plusieurs pièces à simple travée armées de carcasses soudées. 




fig. VI.5, c). Les places et les dimensions des armatures principales 
des carcasses sont déterminées d'après le diagramme des moments 
fléchissants, comme pour un système continu (non composé). Dans 
les joints disposés à l’aplomb des appuis intermédiaires, les aciers 
supérieurs en attente sont aboutés à la soudure par bain de fusion au 
cours du montage à l’aide des cales de montage tandis que les aciers 
inférieurs sont fixés par soudure sur des pièces d'appui scellées pré- 
vues à cet effet dans les éléments préfabriqués. Les travaux de sou- 
.dage étant terminés, le joint est scellé (rempli de béton). 

Une poutre de section en T à travées multiples coulée in situ et 
armée en travée par une carcasse soudée est renforcée à l’aide de 
treillis soudés posés au droit des appuis intermédiaires (fig. VI.5, d). 

Les barres principales des treil- 
a) lis sont orientées le long de 
la travée, afin de reprendre les 
tractions dans la zone tendue 
au-dessus de l'appui qui se 
manifestent en ces points dans 
, les systèmes à travées mul- 
b) lpe tiples. 
Dans une pièce simple- 
ment fléchie en béton pré- 
TA F F7 contraint, les armatures sont 
disposées conformément aux 
FIG. VI. 6. Schémas de ferraillage des diagrammes des moments 
poutres en béton précontraint : fléchissants et des efforts tran- 
a, avec des armatures de précontrainte cour- Chants développés sous la 
bes: b, avec des ie de précontrainte charge. Ce sont les armatures 
de précontrainte courbes (fig. 
VI. 6, a) qui correspondent 
le mieux aux trajectoires des contraintes de traction principales 
et sont donc plus rationnelles que les armatures droites (fig. VI.6, b): 
or, elles sont moins faciles à poser. Avec les armatures droites, 
le ferraillage Ff, encaissant en charge les efforts dans la 
zone tendue est complété par un deuxième ferraillage F,. posé contre 
la face opposée de la poutre à raison de 0,15 à 0,25 F,.. Une telle 
solution s'avère rationnelle pour les pièces de forte hauteur où l’ef- 
fort de précontrainte se situe en dehors du noyau central et risque 
de provoquer des fissures dans cette zone au cours de la fabrication 
de la pièce. Quant aux-dallëé$ elles sont généralement dotées d’un 
simple ferraillage Fe. 

La forme de section la plus avantageuse d’une pièce simplement 
fléchie en béton précontraint est à double T (fig. VI.3, c) ou (si 
l'âme est épaisse) à simple T (fig. VI.3, b). La partie comprimée 
de la section (appelée respectivement membrure ou hourdis) est 
Calculée pour résister à la résultante du couple de forces interne en- 
gendré par le moment fléchissant en charge, et la membrure infé- 
rieure tendue de la section à double T, pour contenir les armatures 




travaillant en traction et assurer la résistance suffisante de cette 
partie de la section au cours de la précontrainte réalisée par la mise 
en tension des aciers. 

Les armatures de précontrainte sont disposées dans les zones ten- 
dues des sections comme il est montré sur la figure VI.7. L’épaisseur 








FIG. VI.7. Disposition des armatures dans la zone tendue de la section d’une 
poutre précontrainte: 


a, ferraillage avec des barres à haute adhérence ; b, ferraillage avec des câbles posés dans les 
canaux; c, ferraillage avec des fils de haute résistance; 1, armatures de précontrainte;: 
2, armatures longitudinales ordinaires: 2, armatures transversales 


d'enrobage et la distance entre barres et câbles tendus sur culées 
sont à choisir conformément à la figure VI.4. Si les armatures sont 
tendues sur le béton durci, la distance entre la surface de la pièce 


FIG. VI.8. Renforcement de lazone d’about d’une poutre en béton précontraint : 


a, avec treillis soudés transversaux ; b, avec cadres ou treillis soudés entourant les armafhres 
longitudinales 


et celle du canal sera non inférieure à 40 mm ni à la largeur ou à la 
mi-hauteur du canal. 

Dans une poutre précontrainte, ce sont les zones d’about (ad- 
jacentes aux appuis) qui revêtent une importance capitale. S'il n’y 
a pas d'armatures de précontrainte relevées aux appuis, on est obligé 




ou bien de poser des armatures transversales de précontrainte, ou 
bien d'élargir la section de la poutre près de l’appui tout en la ren- 
forçant avec des armatures transversales ordinaires supplémentaires 
dont le nombre sera choisi de façon à résister à un effort non inférieur 
à 0,2 fois l’effort dans les armatures de précontrainte longitudinales 
de la zone inférieure de la section sur appui, ce dernier effort étant 
déterminé par le calcul de résistance (de sorte que R,F;:, > 0,2R,F,c)- 
Les barres transversales doivent être solidement ancrées à leurs ex- 
trémités en les soudant sur des pièces scellées. 

Des treillis supplémentaires de renforcement ou des cadres espacés 
de 5 à 10 cm sont à prévoir aux bouts de la pièce précontrainte à arma- 
tures non ancrées, ou dans les zones d'ancrage, c’est-à-dire là où le 
béton subit des efforts concentrés très significatifs qui risquent de 
faire naître des contraintes locales excessives et d’occasionner la 
rupture du béton (fig. VI.8). La longueur / de la partie renforcée 
est égale au double de la longueur de l’appareil d'ancrage; à défaut. 
des appareils d'ancrage, on prend ! & 0,614;, ou ! & 20 cm. 


$ VI.2. ÉTAT DE CONTRAINTE ET DE DÉFORMATION 
D'UNE PIÈCE CHARGÉE EN FLEXION SIMPLE 


Soit une poutre en béton armé à simple travée reposant librement 
sur deux appuis et chargée par deux efforts concentrés symétriques. 
La partie de la poutre comprise entre les points d'application des 
efforts travaille en flexion simple n'étant exposée qu’à un moment 


Diagramme 
de M 


Diagramme 
de Q 


FIG. VI.9. Travail en flexion d’une pièce en béton armé: 
1, zone d’action de M 6€"@; II, zone d’action de M seul 


fléchissant A7 à l'exception de tout effort tranchant (fig. VI.9). 
À un certain stade de travail de la poutre, le béton tendu de cette 
partie présente des jissures normales, c'est-à-dire perpendiculaires 
à l’axe longitudinal de la poutre. Les parties de la poutre comprises 
entre l'appui et le point d'application de l'effort sont exposées à 
la fois à un moment fléchissant À7 et à un effort tranchant Q. On voit 
se former, dans ces parties, des fissures obliques. 




En fonction de la quantité d’armatures dans la zone tendue, on 
distingue deux cas de ruine de la pièce: 

Premier cas. Ruine en mode non fragile: la limite d'élasticité 
{apparente ou conventionnelle) est atteinte dans l’acier tendu, et la 
limite de rupture en compression est atteinte dans le béton. 

Deuxième cas. Ruine en mode fragile (pièce « surferraillée ») : 
la limite de rupture est atteinte dans le béton, tandis que la contrain- 
te dans l'acier n’a pas atteint la limite d'élasticité. 

Conformément au principe de Loleit !), les Normes en vigueur 
en U.R.S.S. mettent en garde le projeteur contre le surferraillage, 
car une pièce présentant une proportion d'armatures excessive rompt 


stade I Stade I __ Stade 


ns N 
Gitr<Rtr Fissures 
b) Mise en c) Pièce précontrainte, 
précontrainte stade I 

Tractions 

PRES 



Compressi ons 


FIG. VI.10. Stades de l’état de contrainte suivant les sections normales de la 
poutre dans la zone de flexion simple: 


a, pièce non précontrainte; b, stade de mise en précontrainte; c, stade I de la pièce pré- 
contrainte 


brusquement sans utiliser complètement la résistance de l'acier tra- 
vaillant en traction. 

De nombreuses expériences ont montré qu’une poutre en béton 
armé non précontraint conforme au principe de Loleit présente dans 
ses parties exposées à la flexion simple, au cours de la croissance pro- 
gressive de la charge appliquée, trois stades consécutifs d'état de 
contrainte suivant les sections normales (fig. VI.10, a). 

Stade I. Phase initiale de mise en charge, avant l'apparition des 
fissures dans la zone tendue du béton. L'acier et le béton s’allongent 
ensemble grâce à l’adhérence. En fin du stade I le diagramme ds 
contraintes dans le béton tendu 6,+, devient incurvé, car la rela- 
tion entre la contrainte et l’allongement relatif cesse d'être linéaire. 
La plus grande ordonnée devient égale à la charge de rupture du béton 


1) Arthur Loleit (1868-1933), ingénieur et chercheur russe soviétique, un 
des fondateurs de la théorie moderne du béton armé. 




en traction (À+, sur la figure VI.10, a). Dans la zone tendue Île dia- 
gramme des contraintes ©, présente un aspect sensiblement triangu- 
laire. Vers la fin de ce stade la pièce est prête à se fissurer. La ré- 
sistance à la fissuration d'une pièce non précontrainte étant faible, 
la fin du stade I correspond à des valeurs assez basses des charges. 


Stade II. La pièce présente des fissures dans le béton tendu. Dans 
les sections fissurées de la pièce les efforts de traction sont reportés 
désormais par les armatures. Dans les zones comprises entre deux 
fissures voisines, le béton continue à résister à la traction grâce à 
son adhérence avec l’acier, ce qui fait que les contraintes dans les 
armatures y sont un peu moins grandes (voir fig. V.3). L’axe neutre 
de la section occupe donc une position variable suivant la longueur 
de la poutre (voir fig. II.4). Les contraintes dans le béton comprimé 
0 deviennent très élevées en ce stade; leur diagramme devient in- 
curvé en raison des propriétés anélastiques du béton. Or, la contrainte 
dans la zone comprimée n'’atteint pas encore la valeur de la charge 


de rupture en compression du béton R,, (voir fig. VI.10, a). 

Entre deux fissures, le béton subit l’action locale des compres- 
sions qui se manifestent dans les sections au-dessus des fissures. 
C'est la raison pour laquelle les contraintes sont variables dans le 
béton compris entre deux fissures voisines, étant légèrement moins 
grandes à mi-distance entre les fissures. 

La fin du stade II est marquée par les premières déformations 
non élastiques visibles de l’acier qui correspondent à la limite d’é- 
lasticité. 

Stade III. C’est la phase ultime de résistance de la pièce aux 
charges appliquées. La contrainte dans l'acier 0, devient égale à la 
limite * d’élasticité apparente © ou conventionnelle og. (voir 
fig. VI. 10, a). La charge devenant encore plus grande, les contraintes 
dans les armatures cessent de croître si l’acier présente un palier d'’é- 
coulement (l'acier s’allonge sensiblement sans augmentation de la 
contrainte) ou croissent lentement si l’acier n’a pas de palier. Les 
ordonnées du diagramme en zone comprimée augmentent légèrement 
et la hauteur de la zone comprimée devient plus petite, ce qui allonge 
le bras de levier du couple de forces interne. La rupture de la pièce 
survient par déficience du béton de la zone comprimée au moment 
où la contrainte du béton 6, devient égale à sa charge de rupture en 


compression À, (rupture en mode non fragile, cas 1). Si la pièce 
est surferraillée, elle rompt pasdéficience du béton comprimé sans 
que les contraintes de traction dans l’acier atteignent la limite d'’é- 
lasticité (rupture en mode iragile, cas 2). 

Considérons à présent une pièce précontrainte. Avant l’applica- 
tion de la charge de service, les zones du béton destinées à supporter 
des tractions se trouvent fortement comprimées par l'effort de pré- 
contrainte excentré V,. Quant aux zones qui seront comprimées en 
service, elles présentent généralement un petit domaine où règnent 
des tractions (fig. VI.10, b). 




Au stade de mise en précontrainte le diagramme des contraintes 
dans le béton n’est pas rectiligne, car les contraintes créées dans la 
pièce sont assez fortes. 

En service, il se produit d’abord l'annulation de la précontrainte: 
(fig. VI.10, b), puis la pièce travaille dans les conditions du stade I 
décrit ci-dessus (fig. VI.10, c). 

La résistance à la fissuration de la pièce précontrainte est nette-- 
ment améliorée, grâce aux fortes compressions que l’on arrive à 
créer dans le béton par la précontrainte. De ce fait, le stade I de son 
état de contrainte (séjour en charge sans fissuration) est sensible- 
ment prolongé. En fin du stade I la:pièce en béton précontraint pré- 
sente un diagramme (fig. VI.10, c) analogue à celui d’une pièce non. 
précontrainte (voir fig. VI.10, a), à ceci près que la zone tendue y est 
moins prononcée. 

Comparé au diagramme de la mise en précontrainte (fig. VI.10, b), 
le diagramme des contraintes dans la pièce en stade I (fig. VI.10, c) 
se trouve inversé tant en signe qu'en valeur des tractions et des com- 
pressions. 

Jusqu'à la fin du stade I (limite de fissuration), la pièce précon-- 
trainte se déforme à peu près comme une pièce élastique. 

Aux stades IT et ITT, les pièces précontraintes et non précontrain- 
tes se comportent de façon similaire. Il est à noter que la précontrain-- 
te se trouve peu utile, dans bien des cas attestés par voie expéri- 
mentale, pour améliorer la résistance mécanique de la pièce suivant 
les sections normales dans la zone de flexion simple. 

Les états de contrainte décrits plus haut sont pris en considé- 
ration lors du calcul des pièces en béton armé. Tant qu'il n’y a pas. 
de fissures, on considère que la pièce se déforme en mode élastique. 
Le moment de fissuration d’une pièce précontrainte est calculé d’a- 
près la phase finale du stade I. Les flèches et l’ouverture des fissures 
sont calculées suivant les stades I et IT pour des phases intermédiai- 
res de mise en charge, en fonction de la catégorie exigée de résistance 
à la fissuration. La capacité portante de la pièce et sa résistance mé- 
canique suivant les sections normales sont déterminées d’après la 
phase terminale du stade III. 

Dans les zones exposées à un moment fléchissant et à un effort 
tranchant à la fois (fig. VI.9), la ruine de la poutre peut survenir sui- 
vant les sections obliques., selon l’un des deux modes suivants. 

Mode I. La charge accrue surmonte la résistance des armatures 
et entraîne une rotation relative des deux parties de la poutre autour 
d'un axe situé en zone comprimée sur le prolongement d’une fissure 
oblique. L'ouverture progressive et la propagation de la fissure ob- 
lique provoquent le rétrécissement, puis la rupture de la zone compri- 
mée (fig. VI.11, a). Ce mode de rupture est analogue à la rupture sui- 
vant les sections normales. 

Mode IT. La ruine de la zone comprimée est provoquée par les 
effets cumulés des contraintes de compression et de l'effort tranchant 
(fig. VI.11, b). Ce cas est observé quand la pièce possède ure arma- 




ture longitudinale robuste et solidement ancrée qui se déforme mais 
reste élastique. 

On prend en considération le mode de rupture suivant une section 
oblique en calculant la capacité portante des pièces fléchies suivant 
les sections obliques. 

Les particularités décrites de l’état de contrainte et de déforma- 
tion des pièces fléchies en béton armé sont mises à la base de la théo- 


FIG. VI.i11. Modes de ruine d’une poutre suivant les sections obliques: 
a, mode 1; b, mode 11 


rie moderne du calcul des structures en béton armé. Elles ont été 
mises en évidence par une longue série d'expériences et de travaux 
théoriques. Dans notre pays ces travaux ont été commencés par 


A. Loleit et poursuivis sous la direction générale du professeur 
A. Gvozdev. 


$ VIS. CALCUL DE RÉSISTANCE SUIVANT 
LES SECTIONS NORMALES 


Pièce de profil symétrique quelconque 


Considérons une pièce sur la fig VI. 12 sollicitée en flexion simple. 
On admet, dans le schéma des efforts, que la pièce subit un moment 


Wa" Kila 
FIG. VI.12, Schéma des efforts adopté au calcul de résistance de la pièce fléchie 
suivant une section normale 


fléchissant À7 défini par les valeurs de calcul des charges, tandis que 
les efforts développés dans l’acier et le béton sont déterminés 
en prenant des contraintes égales aux résistances de calcul 




Dans la zone comprimée du béton, le diagramme des contraintes 
curviligne est remplacé pour plus de simplicité par un diagramme 
rectangulaire, ce qui n’affecte pas trop les résultats des calculs. Quant 
à la contrainte dans le béton, on admet qu'elle est la même dans 
toute la zone comprimée et égale à la résistance de calcul à la com- 
pression sur prisme Az. 

La pièce peut avoir une section de forme quelconque, à condition 
qu'elle soit symétrique par rapport à un axe situé dans le plan des 
forces de flexion. Dans la zone tendue de la section de la pièce est 
située une armature de section }, présentant une résistance égale à 
la résistance de calcul en traction RÀ,. La zone comprimée peut aussi 
comporter une armature de section F, présentant une résistance égale 
à la résistance de calcul en compression R,... 

Les notations employées sur la figure VI.12 sont les suivantes: 
a, distance entre la résultante des efforts dans l’armature F, et le 
bord tendu de la section; a”, distance entre la résultante des efforts 
dans l’armature F, et le bord comprimé de la section; k,, la hauteur 
de section théorique; #',, section de la zone comprimée du béton; 
Zn, distance entre le centre de gravité de la zone comprimée du béton 
et la résultante des efforts dans toute l'’armature tendue. 

Les résultantes des efforts dans l'acier et le béton sont égales à 


Na = Ralai No = Rp; Na = Ra.cFa: (VI.1) 


On sait que la somme des projections de tous les efforts normaux 
sur l’axe de la pièce est égale à zéro 


RaFa — RprFh _ Rica = 0; (VI.2) 


cette condition permet de déterminer la section du béton en zone 
comprimée #;, d'où l’on déduit la hauteur de cette zone x (fig. VI.12). 

On considère que la pièce est suffisamment résistante si le moment 
fléchissant extérieur de calcul ne dépasse pas la capacité portante 
calculée de la pièce égale au moment des forces internes pris avec le 
signe opposé. Les moments étant calculés par rapport à un axe nor- 
mal au plan d'action du moment fléchissant et passant par le point 
d'application de la résultante des efforts dans l’armature tendue F;, 
la condition de résistance suffisante est exprimée par l'inégalité 


M < Rprl bn + Ra.cFa (Ro — à). (VL.3) 


Si l'armature est fabriquée en acier de haute résistance, la valeur 
de À, intervenant dans les formules (VI.1), (VI.2) et trouvée dans 
les Annexes VI, VII doit être majorée en la multipliant par un casf- 
ficient de comportement 


May = Mai — (Mai —1) À (VI.4) 


OÙ Mau — 1,2 pour les armatures A-IV et Ar-IV, 1,15 pour les arma- 
tures A-V, Ar-V, B-II, Bp-II et K-7 et 1,1 pour les armatures AT-VI]; 


6—0948 81 


E est la hauteur relative de la zone comprimée égale à x/h,, où x 
est calculé sans faire intervenir m,,. 
Pour les pièces fléchies, il est recommandé de prendre zx < 
< Ehho, afin d'éviter la rupture en mode fragile (voir $ VI.2). 
La valeur limite de la hauteur relative de la zone comprimée des 
sections rectangulaires, en T et en double T est cherchée à l’aide de 
la formule 


ER ———, (VI.9) 
E A ë 
1+ 7500 (1—-#) 


où £, est la caractéristique de la zone comprimée du béton calculée 
par la formule 


Es = 0,85 — 0,0008R,, : (VI.6) 


GA est la contrainte conventionnelle dans l'acier. Pour les armatures 
en acier à limite d'élasticité conventionnelle (classe A-IV et au- 
dessus), fils de classe B-II, Bp-IT, câbles droits on a 


O1 = Ra + 4000 — 0,, (VI.7) 


où 0, est la contrainte dans l’acier créée par la mise en précontrainte ; 
R, est la résistance de calcul à la traction de l'acier, déterminée 
sans tenir compte de m,, mais en faisant intervenir les autres coef- 
ficients Mn: ; 

pour les armatures ordinaires (sans précontrainte) des classes 
À-I, A-II, A-IIT, B-I, Bp-I on a 


Où = hi (VI.7a) 


En utilisant un béton présentant le coefficient de comportement 
mp1 = 0,85 (voir $ III.1), on prend 5000 au lieu de 4000 dans la 
formule (VI.5). 

Si l’on a x > E Lh, conformément à (VI.2), il est permis de cal- 
culer le moment fléchissant maximal admissible à l’aide de l’iné- 
galité (VI.3) en prenant x = Ë rh. 

Si la pièce contient des armatures de précontrainte de section 
Fe dans la zone tendue et de section F,. dans la zone comprimée, 
il est nécessaire de prendre en considération l’effort dans l’armature 
Fpe égal à may Rpe Fpe €t l'effort dans l’armatureF},,. égal à 6cF;e, où 
Oe —= 4000 — mmt0;. La formule citée pour o4 est établie en sup- 
posant que l’armature F,. subit des contraintes de compression ; 
or, au début de la mise en charge de la pièce, cette armature pré- 
sente des contraintes de traction Mm+0, (avec un coefficient de pré- 
cision de la mise en tension Mmt > 1). Après que les contraintes de 
traction ont été annulées, l’armature F,£ commence à travailler en 
compression. Puisque l’acier et le béton se déforment ensemble grâce 
à l’adhérence, les contraintes de compression maximales s’évaluent à 




4000 kgf/cem°?. Si m,10, > 4000, la valeur de © est négative, ce 
qui signifie que l’armature F,, travaille en traction. 
On a donc 
RaFa + Mask pel pe — RprF5 — RacFa — GeFpe = 0, (VI.2a) 
M< RorFn2r + RacFa(ho—4')+ocFpe (ho — ape).  (VI.3a) 


Pièce de profil rectangulaire à simple ferraillage 


Une pièce de section rectangulaire munie d’une simple nappe 
d'’armatures non précontraintes présente la géométrie suivante 
(fig. VI.13): 

Fh = bt; 21 = ho — 0,5%. 
(VI.8) 


La hauteur de la zone 
comprimée x est déduite à 


DATE de l'égalité (V1:2) FIG. VI.18. Pièce de section rectangulaire 
en utilisant l'expression à simple ferraillage. Schéma des efforts 


bxRpr = Rala. (VI 9) adopté au calcul de résistance 
r » . 


La condition de résistance suffisante, compte tenu de (VI.3), 
s'écrit ainsi: 

M < Rrbt (ko — 0,52). (VI.10) 

On peut utiliser également l'inégalité suivante dans laquelle 


les moments sont pris par rapport à un axe passant par le centre de 
gravité de la zone comprimée: 


M < RaFa (Ro — 0,52). (VI.11) 
Les formules (VI.9) et (VI.10) ou (VI.11) sont appliquées en- 
semble pour 
T < E ro 


où la valeur de Ë , est calculée par (VI.5). 


La proportion d'armatures p = et le pourcentage d’arma- 


tures 1+100, compte tenu des relations (VI.9) et £ = x/h,. se pré: 
sentent sous la forme 


(VI) 


On en déduit la quantité maximale PE d’armatures dans la 
section rectangulaire en prenant des valeurs limites de £x et en 
faisant intervenir la condition (VI.5). 

Sixz > ERho, on calcule le moment fléchissant à l’aide de la for- 
mule (VI A0) ou de la formule (VI.11) en mettant x = Ë bho. 


n=E-; p(% 


“ .83 


En regardant les expressions (VI.10) et (VI.11), on se rend compte 
que la résistance suffisante de la pièce se trouve garantie pour diffé- 
rentes combinaisons des dimensions de la section de la pièce et des 
quantités d’armatures dans cette section. 

En pratique, la condition de prix optimal des pièces en béton 
armé impose les valeurs suivantes: 

pour les poutres u = 1 à 2 % et & — 0,3 à 0,4; 

pour les dalles u = 0,3 à 0,6 % et & = 0,10 à 0,15. 

Les paramètres géométriques b, x, F, étant donnés et les caracté- 
ristiques des matériaux et le moment M étant supposés connus, on 
procède à la vérification de la résistance de la section: à cet effet 
on détermine la hauteur de la zone comprimée x à partir de l’expres- 
sion (VI.9), on s’assure qu'elle satisfait à la condition x < 6 ho: 
puis on applique les expressions (VI.10) ou (VI.11). 

On considère que la section est bien dimensionnée si sa capacité 
portante, calculée en fonction du moment, est égale ou de 3 à 5 % 
supérieure au moment extérieur de calcul. 

Exemple VI.1. La valeur de calcul du moment fléchissant engendré 
par les charges permanentes et les surcharges de longue et de courte 
durée est M — 7,6 tfm (76 kN:m). La poutre présente une section 
de dimensions b — 20, h — 40 cm. Armatures longitudinales cons- 
tituées par des barres à haute adhérence 4 @ 16 mm de classeA -ITI. 
Béton lourd de classe M 200 (coefficient de comportement du béton 
Mp1 — 0,85). On demande de vérifier la résistance de la pièce sui- 
vant la section normale. 

Solution. On trouve dans les Annexes IV, VI et VIII les valeurs 
de R,r = 90 kgf/cm? (9 MPa), R; = 3600 kgf/cm° (360 MPa), F, = 
— 8,04 cm°. 

La hauteur utile de la pièce, avec a = 3,5 cm, est égale à 


ho = hk — a = 40 — 3,5 — 36,5 cm. 
La hauteur de la zone comprimée (voir (VI.9)) est 


__RaFa ___ 3600X 8,04 499 cm. 
— GE ? 


D'après les formules (VI.6) et (VI.5) 
Eo = 0,85 — 0,0008 A7. — 0,85 — 0,0008 x 0,85 x 90 = 0,79; 
0,79 
ÊR = —}# : REV 3007, 0,79 — 0002 
so (1-47) 1H (1-17) 
La condition x < Eh, est vérifiée, car 


t— THE 0,518 < E4 — 0,653. 


La capacité portante de la section, conformément à la formule 
(VI.11), est égale à 


RAF a (ho — 0,5x) = 3600 X 8,04 (36,5 — 0,5 x 18,9) — 
— 783 000 kgf:cm — 7,83 tf-m = 78,3 kN:m, 


ou de 3 % supérieure à la résistance qui doit être opposée au mo- 
ment de calcul M = 7,6 tf:m (76 kN:m). Autrement dit, la pièce 
présente une bonne résistance suivant la section normale. 

Le moment étant donné, on choisit les sections d’après les ex- 
pressions (VI.9) et (VI.10) ou (VI.11) en y mettant le signe d’éga- 
lité. 

Dans la pratique, les sections rectangulaires à simple ferraillage 
sont choisies en se servant d’un tableau de calcul simplifié (voir 
Tableau VI.1). À cet effet, on met les expressions (VI.9) et (VI.11) 
sous la forme 


M = AbhèRon (VI.13) 
F=-pp (VI.14) 
49=—(1—0,5-)=E(1— 0,58), (VI.15) 
2 _4_052E—4— 
n=g=1—0,5- —1—0,58. (VI.16) 


De l'égalité (VI.13) on déduit l'expression de la hauteur de sec- 
tion utile: 


Het (V1.17) 


Les coefficients À, et n calculés d’après les expressions (VI.15) 
et (VI.16) sont présentés sous forme d’un tableau (voir Tableau VI.1) 
qui simplifie grandement les calculs. 

La section est dimensionnée dans l’ordre suivant. On se donne 
d'abord une largeur de profil b et une valeur recommandée de £ pour 
laquelle on trouve À, dans le Tableau VI.1. Ensuite on calcule par 
la formule (VI.16) la hauteur de section utile k,, on trouve la hauteur 
totale k = h, + a et l’on choisit une section standard qui a cette 
hauteur. Si les dimensions b et » ainsi trouvées se trouvent mal adap- 
tées aux dispositions constructives ou aux conditions de fabrication, 
on procède à leur ajustement par un nouveau calcul. 

La section à donner aux armatures F, est déterminée comme sut. 
On détermine À, à l’aide de la formule (VI.13) après avoir trouvé 
et £ dans le Tableau VI.1, puis on calcule F, et l’on vérifie que la 
condition (VI.4) est satisfaite. 

Le Tableau VI.1 convient également à la vérification de la ré- 
sistance de la pièce. La section étant connue, on calcule u = F,/bh,, 
on trouve Ë d'après (VI.12) et l’on s'assure que la condition zx < Eh 




TABLEAU VI.1 


Coefficients n et À, intervenant dans le calcul des pièces 
de section rectangulaire à simple ferraillage 


6 = x/ho n = zp/ho Ao E — +/ho | n = 2p/ho Ao 
0,01 0,995 0,01 0,37 0,815 0,301 
0,02 0,99 0,02 0,38 0,81 0,309 
0,03 0,985 0,03 0,39 0,805 0,314 
0,04 0,98 0,039 0,4 0,8 0,32 
0,05 0,975 0,048 0,41 0,795 0,326 
0,06 … 0,97 0,058 0,42 0,79 0,332 
0,07 0,965 0,067 0,43 0,785 0,337 
0,08 0,96 0,077 0,44 0,78 0,343 
0,09 0,955 0,085 0,45 0,775 0,349 
0,1 0,95 0,095 0,46 0,77 0,354 
0,11 0,945 0,104 0,47 0,765 0,359 
0,12 0,94 0,113 0,48 0,76 0,365 
0,13 0,935 0,121 0,49 0,755 0,37 
0,14 0,93 0,13 0,5 0,75 0,375 
0,15 0,925 0,139 0,51 0,745 0,38 
0,16 0,92 0,147 0,52 0,74 0,385 
0,17 0,915 0,155 0,53 0,735 0,39 
0,18 0,91 0,164 0,54 0,73 0,394 
0,19 0,905 0,172 0,55 0,725 0,399 

* 0,2 0,9 0,18 0,56 0,72 0,403 
0,21 0,895 0,188 0,57 0,715 0,408 
0,22 0,89 0,196 0,58 0,71 0,412 
0,23 0,885 0,203 0,59 0,705 0,416 
0,24 0,88 0,211 0,6 0,7 0,42 
0,25 0,875 0,219 0,61 0,695 0,424 
0,26 0,87 0,226 0,62 0,69 0,428 
0,27 0,865 0,236 0,63 0,685 0,432 
0,28 0,86 0,241 0,64 0,68 0,435 
0,29 0,855 0,248. .| 0,65 0,675 0,439 
0,3 0,85 "0,255 0,66 0,672 0,442 
0,31 0,845 0,262 0,67 0,665 0,446 
0,32 0,84 0,269 0,68 0,66 0,449 
0,33 0,835 0,275 0,69 0,655 0,452 
0,34 0,83 0,282 0,7 0,65 0,455 
0,35 0,825 0,289 
0,36 0,82 0,295 


est satisfaite. Ceci fait, on trouve dans le Tableau VI.1 la valeur de 
À, pour Ë£ donné et l’on calcule le moment fléchissant maximal ad- 
missible pour la section étudiée. 

Exemple VI.2. Poutre de section rectangulaire. Moment de cal- 
cul provenant des charges permanentes et des surcharges de longue 
et de courte durée M = 8,5 tf-m (85 kN :m). Béton lourd de classe 
M 200 (coefficient de comportement mp1 = 0,85). Barres à haute 
adhérence en acier de classe A-IT. On demande de déterminer b, 
h et Fa. 

Solution. On trouve dans les Annexes IV et VI les résistances 
Ror = 90 kgf/cm° (9 MPa) et R, — 2700 kgf/cm* (270 MPa). On se 
donne une largeur de profil b — 20 cm et ë — 0,35. Dans le Ta- 
bleau VI.i, pour £ — 0,35, on trouve À, — 0,289. D'après la for- 
mule (VI.17) 


M V4 850 000 : 
ko — Vas = 0,289 X20X90X0,85 — 43,8 cm. 


La hauteur de section totale est k = h, + a = 43,8 + 3,5 — 
— 47,3 cm. On choisit À — 45 cm (multiple de 5 cm), où la hauteur 
de section utile est k, — 45 — 3,5 — 41,5 cm. A l’aide de la for- 
mule (VI.13) on calcule 


M 850 000 
Ào = ThéRpris — 20X APE X 00% 085 — VrH2d. 
En fonction de cette valeur, on trouve dans le Tableau VI. les 
valeurs de n = 0,797 et de £ — 0,405. D'après (VI.14) 
M 850 000 


Pare nhoka 0,79 X 41,5 X 2700 9,55 cm”. 


Il vient en vertu des formules (VI.6), (VI.5) 
Es — 0,85 — 0,0008R,, = 0,85 — 0,0008 x 0,85 x 90 — 0,79; 


: E : 0,79 : 
Er RD nn go — 0,687. 


(ii) 1480 (1-7) 


de condition z & ËRho est satisfaite, car £ — 0,405 << E, — 
— 0,687. 

On peut adopter (voir Annexe VIIT) un ferraillage de 4 g 18 A-IT 
(F, = 10,18 cm°). 

Exemple VI.3. Une dalle prévue pour résister à un moment de 
calcul M = 380 kgf-m (3800 N -m) par 1 m de longueur de la sec- 
tion (sous l’action des charges permanentes et des surcharges de æal- 
cul de longue et de courte durée), épaisse de k — 8 cm, est renforcée 
par un treillis soudé 150/250/6/4 confectionné en fils lisses de résis- 
tance normale de classe B-I. Béton lourd de classe M 150 (coeffi- 
cient de comportement m1, = 1). Vérifier la résistance de la dalle. 

Solution. On trouve dans les Annexes IV, VII, IX les résistan- 
ces Rr = 70 kgf/cm°? (7 MPa) et R, — 3150 kgf/cm°? (315 MPa) et 




la section à donner aux armatures principales (longitudinales) par 
4 m de longueur du treillis F, — 2,07 cm°. 
La hauteur utile de la dalle est À = h, — a — 8 — 1,5 — 6,5 cm. 
Le pourcentage d’armatures est 


F 2,07 
u = 100 h =100-%55 5 = 0.32%. 


On a d’après (VI.12) 


valeur nettement inférieure à celle de Ex. 
En fonction de ë — 0,144, on trouve dans le Tableau VI.1 la 
valeur de À, = 0,134. Conformément à (VI.13), 


M = AobhiRpr = 0,134 X 100 X 6,57 x 70 = 
— 39 600 kgf:cm (3960 N :m). 


Autrement dit, la capacité portante de la section étudiée est plus 
que suffisante pour résister au moment de calcul imposé À — 
— 380 kgf:m (3800 N:m). 


Pièce de profil rectangulaire à double ferraillage 


C’est une pièce qui possède des armatures longitudinales de résis- 
tance déterminée non seulement dans la zone tendue (F,) mais 
aussi dans la zone comprimée (7,;). 

Le calcul de résistance des armatures comprimées est effectué 
dans les cas où x > Ë ho. 

Malgré la forte dépense d'acier, les pièces à double ferraillage 
s'avèrent quelquefois rationnelles, car elles ont une section plus 
réduite. L'état de contrainte en service d’une telle pièce est repré- 
senté sur la figure VI.12. Afin d'éviter la rupture de la section en 
mode fragile, on limite la hauteur de la zone comprimée x par la 
condition x < É rh; en vue de permettre à l’armature comprimée 
d'atteindre la contrainte R,., on impose à x la condition x > 2a’. 

Pour F;, — bzx, on a d’après la formule (VI.2) 


Rpr0t = RaFa — Ra.cFa. (VI.18) 
La formule (VI.3) nous-donfté pour z, = hk4 — x/2 
M Robt (ho) + RacFa(ho— a) (VIA9) 


Le premier terme de la condition de résistance suffisante (VI.19) 
représente le moment supporté par la section dotée d’une seule nappe 
d’armatures. Ce moment peut être exprimé par la formule (VI.13) 
en utilisant le Tableau VI.1. La condition (VI.19) devient alors 


M < Aobh3Rpr + Ra.cFa (Ro — a’). (VI.20) 


Dans le calcul des sections, on distingue deux types de problèmes. 
Problème 1. Connaissant A, b,k, Rpr; Ra et Ra, déterminer F, 


et (éventuellement) F;. 
Le calcul commence dans le même ordre que pour un ferraillage 


simple. En se servant de la formule (VI.13), on trouve 
0 — Mb Rprohè . (VI .21) 
Si À, est plus grand que 4, trouvé en fonction de Ë», on fait 
la conclusion que le ferraillage simple est insuffisant (ë > E) et. 
qu'il est nécessaire de calculer une deuxième armature F;. Posant 
Ao = ÀAor, On trouve alors d’après la formule (VI.20) 
1 M — AspthämpiRpr 
PR a) (VI.22) 
La section à donner à l’armature F, sera déterminée d’après la for- 
mule (VI.18) en y mettant x = xp = Ëhho: 
Fa Fi + PHRREÈRe (VI.23) 
Problème 2. Connaissant M, b,h, Rrr, Ra, Ra.c et Fa, chercher F,. 
On calcule À, à l’aide de la formule (VI.20) : 


_ M—R : Fa (h — a") 
A nee (VI.24) 


En fonction de cette valeur de 4,!), on cherche Ë dans le Tableau 
VI.1, puis, en posant x — Eh,, on Culcule Fa à l’aide de la formu- 


le (VI.18): 


Fa= ee Fa + MR (VI.25) 


Exemple VI.4. Une pièce de section b — 25 cm, À — 50 cm en 
béton lourd de classe M 200 (m1, — 0,85) à armatures de classe 
A-IT est conçue pour résister à un moment M — 22 tf:m (220 kKN:m). 


Chercher F, et F:. 
Solition. On trouve dans les Annexes IV, VI les résistances Ryr = 


— 90 kgf/cm? (9 MPa) et R, = R,. — 2700 kgf/cm°? (270 M Pa). 
On calcule 
Mbp1Rpr = 0,85 X 90 = 77 kgf/cm? (7,7 MPa). 
D'après la formule (VI.6) 
Es = 0,85 — 0,0008 x 77 — 0,788. 
D'après la formule (VI.5), en posant 61 — R, et en prenant 5008 
au lieu de 4000, on a 
= Éo _ 0,788 : 
Er ETES (ES) TA 
5000 | 1,1 9000 1,1 ] 
À) Si Ao > Aonp: la section donnée F4 est trop faible et doit être augmentée. 


À cette valeur de E, correspond 
Aor = Er (A —0,5ËR) —= 0,686 (1 — 0,343) — 0,45 1). 


Prenons a — 4 cm, a — 3 cm. Il vient alors k, — 50 — 4 — 
— 46 cm. 
D'après la formule (VI.21) 
__ M 2200000 - 
0 mprRprohg  T11X25X 467 — 0,54 Ar. 


Autrement dit, une section à simple ferraillage ne peut reporter 
complètement le moment agissant; elle doit donc être renforcée 
par une armature comprimée dont nous calculerons la section à 
l’aide de la formule (VI.22): 


4’ — M — Aorbhômp1R pr — 2 200 000 — 0,45 X 25 pe 46? X 77 


PAT RU) 12700 (46 — 3) nn US 


D'après la formule (VI.23), en posant R, — R,., on obtient 


pe MbiRprtËrho 71X25X0,686X46 
Fa = Eat = À, 24 + ——— 5 = 25,6 cm2. 
On adopte comme armatures comprimées 2 @ 16 A-II (F7; — 
— 4,02 cm°), et comme armatures tendues 4 @ 28 A-II (F, — 
— 24,63 cm°). 
Exemple VI.5. Mêmes conditions que ci-dessus. Sachant que 
F; = 6,28 cm? (2 @ 20 A-II), calculer F,. 
Solution. D'après la formule (VI.24) 
_ M—Ra.cFa(ho—a')  2200000—2700 x 6,28 (46—3) 
Ao — Mb1 Rprôhè : 77 X 25 X 462 = 0,368. 


n trouve dans le Tableau VI.1 la valeur de £ — 0,485 < £ ,. 
UY'après la formule (VI.25), en prenant R;, — RAae, on obtient 


“mis RS DER 77 K 25 X 0,485 X 46 
É PE — 6,28 + 2700 ue 


— 6,28 + 15,92 — 22,2 cm2. 
On adopte comme armatures 2 G 32 A-II + 2 G 20 A-II: 
F, = 16,09 + 6,28 = 22,37 cm°. 


Pièce de profilenT - 

Le profil en T est très répandu en construction, tant sous forme de 
poutres isolées en béton armé (fig. VI.14, a, b) que de structures 
entières, par exemple de planchers en panneaux nervurés préfabri- 
qués ou coulés en place (fig. VI.14, c, d). La section en T se compose 
d'un hourdis et d’une nervure. 


1) Au lieu de calculer cette quantité, on pourrait la trouver dans le 
Tableau VI. en regard de Ë = 0,686. 




La section en T est beaucoup plus économique que la section rec- 
tangulaire (en pointillé sur la figure VI.14, a), car, la capacité por- 
tante étant la même (la capacité portante d'une pièce en béton armé 
ne dépend pas de la section de la zone tendue du béton), une pièce 
en T demande moins de béton qu'une pièce rectangulaire à cause 
de la diminution de la zone tendue. 
Pour cette même raison le hourdis de 
la section doit être situé en zone 
comprimée (fig. VI.14, a): en effet, 
le hourdis travaillant en traction 
(fig. VI.14, b) n'améliore pas la capa- 
cité portante de la pièce. Une pièce 
de profil en T est généralement dotée 
d'un simple ferraillage. c) be 

Si le hourdis est très large, ses 
parties extrêmes éloignées de la ner- 
vure subissent des contraintes moins 
grandes. On prend donc en compte les 
largeurs équivalentes en porte-à-faux 
du hourdis b,r (voir fig. VI.14, c, d). 
La largeur équivalente en porte-à- 


faux sera prise, de part et d'autre 
de la nervure, non supérieure à la 
mi-distance nu au nu entre nervures c 
ni à 1/6 de la portée de la pièce; si 
la pièce possède un hourdis d'épais- 
seur hi < 0,12 sans nervures trans- 


FIG. VI.14. Sections en T: : 


a, le hourdis de la noutre est situé 
dans la zone:comprimée ; b, le hourdis 
de:la poutre est situé dans la zone 


tendue; c, plancher nervuré coulé 
en place; d, plancher nervuré en 
éléments préfabriqués; 1, hourdis; 


2, nervure, 3, zone comprimée 


versales ou avec des nervures trans- 

versales plus espacées que les nervures longitudinales, b,, sera 
prise non supérieure à 6h. Pour les poutres en T isolées à hourdis 
en porte-à-faux, la largeur en porte-à-faux prise en compte b,r (voir 
fig. VI.14, a) devra rester: 

— non supérieure à GA pour h} > 0,1 k; 

— non supérieure à 3h pour 0,05h < hi << 0,1}. 

Si hkh << 0,05h, les porte-à-faux du hourdis ne sont pas pris en 
considération. Deux cas différents sont à distinguer au calcul d'une 
section en T, suivant que le bord inférieur de la zone comprimée 
(axe neutre) passe dans le hourdis (fig. VI.15, a) ou plus bas que 
le hourdis (fig. VI.15, b). 

Le premier cas (x < hi) se présente généralement quand le hour- 
dis est très large. Dans ce cas le calcul se fait comme pour une section 
rectangulaire, en prenant les dimensions b; et h, (voir fig. VI.15, #, 
vu que la section du béton tendu n'’affecte pas la capacité portante. 

Les formules à employer dans les calculs (en l’absence de la pré- 


contrainte) sont les suivantes: 
Rproht = RaFa; (VI.26) 
M < Rprôht (ko — 0,57) (VI.27) 




M < AoRyrbih, (VI.28) 


où À, est un coefficient qu’on trouve dans le Tableau VI.1. 

Le deuxième cas (x > hi) est caractéristique d’un hourdis étroit. 
La zone comprimée de la section couvre alors la partie comprimée 
de la nervure et le hourdis tout entier (fig. VI.15, b). 


FIG. VI.15. Deux profils en T différents: 


a, l’axe neutre est dans le hourdis; b, l’axe neutre passe plus bas que le hourdis 


La position de l’axe neutre est définie par l’équation 
RaFa = Rpr0 + Ror (bh — b) hx. (VI.29) 


Si l’on prend les moments par rapport à un axe normal au plan 
de flexion et passant par le point d'application de la résultante des 
efforts dans l’armature tendue, la condition de résistance suffisante 
s'écrit 

M< Rprdt (ho — 0,57) + Ror (bh — db) hn (ho — 0,5h5). (VI.30) 

La section en T doit vérifier la condition x < E rho. 

Il existe une formule empirique approchée pour déterminer la 
hauteur d’une poutre de section en T: 


h=(15 à 20)Ÿ/M, (VI.31) 


où À est exprimé en cm et M en tf-m. 
Quant à l’épaisseur de la nervure, elle est généralement égale à 


b — (0,4 à 0,5). (VI.32) 


Les dimensions du hourdis bj, hkn sont le plus souvent choisies 
d’après les dispositions constructives. La section à donner à l’arma- 
ture F, pour résister au moment-.de. calcul est déterminée en fonction 
de la position de l’axe neutre. Si l’axe neutre tombe dans le hourdis, 
on trouve F, en assimilant la section de la pièce à un profil rectan- 
gulaire de dimensions b et h,, à l’aide du Tableau VI.i. 

En déterminant la position de l’axe neutre, deux éventualités 
doivent être considérées : 

19 On connaît les dimensions de la section et la section des arma- 
tures F,. Si l'on a 


RaFa € Rorbbh, (VI.33) 


l'axe neutre tombe dans le hourdis. Si l’on a l'inégalité inverse, 
l'axe neutre passe dans la nervure. 

20 On connaît les dimensions de la section b}, kh, b, k et le mo- 
ment fléchissant de calcul. La section des armatures F, est inconnue. 
Si l’on a 

M< Rprôhhh (ko —0,5hh), (VI.34) 


l'axe neutre tombe dans le hourdis; si l’on a l'inégalité inverse, 
l'axe est dans la nervure. 

Quand l’axe neutre passe plus bas que le hourdis, on peut trans- 
former les formules (VI.29) et (VI.30) en faisant intervenir les rela- 
tions x = Eh, et (VI.15): 

RaFa = ERpr bhs + Ror (bh — b) hi, (VI.35) 
M < AR prbh4 + Rpr (bé — d) hi (Ro—0,5ki), (1.36) 


les coefficients £, À, étant tirés du Tableau VI.f. 
Ces formules peuvent être utilisées lors du choix de la section. 
Si l’on veut connaître F,, on doit calculer À, au départ de la for- 
mule (VI.36): 
 M—Rpr (bi —b) hÿ (ko —0,5h;) 
Ao= Rprbhé ? 
puis trouver Ë dans le Tableau VI.i en fonction de la valeur de À, 
calculée ci-dessus et enfin appliquer la formule (VI.35) qui donne 


(VI.37) 


Fa = 1Ebho+ (Dh — 6) RE] EE. (VL.38) 

S'il est nécessaire de vérifier la résistance d’une section connue, 
le meilleur moyen consiste à déterminer la position de l’axe neutre 
à l’aide de la formule (VI.34), puis calculer la hauteur de la zone 
comprimée x d'après (VI.29) (si l’axe neutre passe plus bas que le 
hourdis) et enfin appliquer la formule (VI.30). 

Si le hourdis de la pièce est relativement mince mais large (l’iné- 
galité x < hà étant garantie), on peut déterminer la section à donner 
aux armatures F, de façon approchée, sans recourir au Tableau. Pre- 
nant dans la formule (VI.27) R,F, au lieu de R,,bnx (voir (VI.26)) 
et posant approximativement x = hj, on obtient 


Fa= Ra (ko—hj,/2) * (VI.39) 
La même formule se laisse déduire de (VI.11) en prenant pen 
2h = ho —+ Æ ho——.. (VI.40) 


Exemple VI.6. Soit une poutre en T conçue pour résister à un 
moment fléchissant de calcul provenant des charges permanentes et 
des surcharges de longue et de courte durée M — 45 tf:m (450 kN :m), 




de section À — 70 cm (k, = 66 cm), b = 25 cm. Largeur de calcul 
du hourdis b} — 60 cm; kny — 8 cm. Béton lourd de classe M 200 
(coefficient de comportement my, = 0,85). Armature en barres à 
haute adhérence de classe A-IITI. On démande de savoir F,. 

Solution. On trouve dans les Annexes IV et VI les valeurs de 
Rpr = 90 kgf/cm° (9 MPa) et de R; — 3600 kgf/cm* (360 MPa) pour 
les diamètres supérieurs à 10 mm. 

Cherchons la position de l’axe neutre. Conformément à la for- 
mule (VI.34) 


MpiR prôhhh (k5 — 0,0hn) = 0,85 X 90 X 60 x 8 (66 — 0,5 x 8) — 
— 2 280 000 kgf:cm = 22,8 tf-m, 
donc moins que le moment imposé A = 45 tf.m (450 kN-m). Par 


conséquent, l’axe neutre passe dans la nervure. On a selon Ia for- 
mule (VI.37) 


M—mhRpr (b}, — b) ki, (ko —0,5h;) — 


0 Mb1R prbhé 
__ 4 500 000— 0,85 x 90 (60— 25) 8(66—0,5*X8) _ p 3g4 
E 0,85 X 90 X 25 X 66? re : 


On trouve dans le Tableau VI.1, pour ce coefficient, la valeur de 
E — 0,512. D'après la formule (VI.38), la section à donner à l'arma- 
ture est égale à 


Fa = 1Ebh6+ (Gi — 6) hi] er 
== [0,512 x 25 x 66 + (60 — 25) 8] LEXN 23,0 cs, 


On peut adopter comme armature (voir Annexe VIII) 218 A-III + 
+ 425 A-TIT avec F', = 24,72 cm°. 

La valeur de £ — 0,512 est plus petite que la valeur limite 
Er = 0,653 (voir l'exemple VI.1); la condition de validité des 
formules de calcul est donc respectée. 

Exemple VI.7. Calculer la section à donner à l’armature du 
plancher nervuré montré sur la figure VI.14, c. Distance nu au nu 
entre nervures © — 150 cm. Portée ! — 6,0 m. Hauteur de section 
h = 50 cm (h, = 46,5 cm). Epaisseur de la nervure b = 20 cm. 
Epaisseur du hourdis kj — 6 cm. Moment fléchissant M — 
ne tf.m (260 KkN :m). Béton_M 200 (m3, = 1), armature de classe 

-ITI. a 

Solution. On trouve dans les Annexes IV et VI les résistances 
Rpr = 9Ù kgf/cm° (9 MPa) et R, — 3600 kgf/cm? (360 MPa). 

Puisque ge 




> 0,1, on prend en compte comme largeur du hour- 


bh Lc + b — 160 + 20 — 180 cm, 
bi 21/6 + b — 2 x 100 + 20 — 220 cm. 


Soit b, — 180 cm. 
Le hourdis est large, si bien que la condition + << h;j est garantie. 
D'après la formule (VI.28) 


___ M: 260000 
a Robe = DO x 180 x 46,8e — V7. 


On trouve dans le Tableau VI.i 
E = 0,08 < E£,; n — 0,963. 


D'après la formule (VT.14) 


F,= M 2 600 000 — 46,1 em? 


D'après la formule approchée (VI.39) 


: M ___ 260000 ; 
Fa Ra io—hnl2) — 3600(46,5—6/2) — 16,6 cm?. 


Nous adoptons comme armature 2@ 29 A-III + 2 20 A-IIB 
avec F, = 9,82 + 6,28 — 16,1 cm:. 

Vérifions la hauteur de la zone comprimée. D'après la formu- 
le (VI.26) 


7 FaFa _ 3600 x 16,1 
— Rprô — 90 X 180 


= 3,6 cm< = 6 cm. 


$ VI.4 CALCUL DE RÉSISTANCE 
SUIVANT LES SECTIONS OBLIQUES 


Formules usuelles 


Une pièce fléchie peut se rompre suivant une section oblique sous 
l'effet des moments fléchissants et des efforts tranchants appliqués 
simultanément dans la zone considérée. Ces sollicitations font naître 
des efforts internes dans les aciers traversés par la fissure oblique, 
ainsi que dans le béton comprimé. La figure VI.16 montre la zone 
d’about d’une pièce en béton armé avec ses armatures longitudinales, 
transversales et relevées. Cette zone de la pièce est séparée par une 
section qui se confond avec la fissure oblique. 

Les conditions de résistance suffisante de la pièce suivant ugg 
section oblique se traduisent par deux exigences imposées au moment 
fléchissant À7 et à l'effort tranchant Q qui agissent dans la zone 
considérée de la poutre (voir fig. VI.9, zone 1). Dans le schéma des 
efforts de la figure VI.16, il est supposé que les valeurs du moment 
et de l'effort tranchant sont déterminées par les charges de calcul 
et que les contraintes engendrées dans l'acier et dans le béton sont 


2°, 195: 


égales aux résistances de calcul. Les conditions de résistance suffi- 
sante s’écrivent donc sous la forme 


Mo RaFaz + RaPrr + D RaFtritrs (VI.41) 
QE } RatrFr Sin & >) RatrFtir + On: (VI.42) 


OÙ Fa, Fr F, sont les sections des armatures longitudinales, trans- 
versales et relevées respectivement ; ©}, l'effort encaissé par le béton 
de la zone comprimée dans la section oblique; «, l’inclinaison des 
armatures relevées sur l’axe lon- 
gitudinal de la pièce; Z, Zr, Ztr les 
Q bras de levier des efforts dans les 
| W, armatures longitudinales, relevées 

ze et transversales; M, et Qnp, le 


+ D moment fléchissant de calcul et 

2 Ne ss l'effort tranchant de calcul déter- 
Rire minés par rapport au point D. 

(Ra br) La formule (VI.41) exprime la 


condition du moment: on considère 
que la pièce a une résistance suf- 
FIG. VI.16. Schéma des efforts fisante suivant la section oblique si 
adopté pour le calcul suivant une Je moment fléchissant M, de tou- 


section oblique (entre parenthèses: + RE 
es les f rieures exercées 

efforts dans les armatures longitu- d | JECES exte éd la Di 

dinales et relevées retenus dans le ans la zone considérée de la pièce, 


calcul des sections obliques vis-à- pris par rapport au centre de la 
vis du moment fléchissant) zone comprimée, reste non supé- 
rieur à la somme des moments des 

efforts de calcul internes dans les armatures longitudinales, trans- 
versales et relevées pris par rapport au même point de référence. 

La formule (VI.42) exprime la condition de l'effort: on considère 
que la pièce a une résistance suffisante suivant la section oblique 
si l'effort tranchant Q, provenant de toutes les forces extérieures 
exercées dans la zone considérée de la pièce reste non supérieur à la 
somme des projections sur la normale à l'axe de la pièce des efforts 
de calcul internes dans les armatures transversales et relevées, tra- 
versées par la fissure oblique, et de l'effort tranchant encaissé par le 
béton comprimé. 

Üne fraction de la résistance des armatures transversales et rele- 
vées situées dans la fissure oblique.au voisinage de la zone comprimée 
reste inutilisée à cause de la faible ouverture des fissures à cet en- 
droit. Pour cette raison les efforts dans les armatures transversales et 
relevées sont pris égaux, dans la formule (VI.42), à la résistance de 
calcul R,:. qui est légèrement inférieure à R, (voir Annexe VII). 
Cette minoration est omise cependant dans la formule (VI.41), car 
les moments des efforts dans les armatures transversales et relevées 
voisines du point de référence sont faibles et n'affectent pratique- 
ment pas les résultats des calculs. 




L'effort tranchant de calcul subi par le béton comprimé est défini 
à l’aide de la formule empirique 


un kaR trbhi 
Q= 2% 


Z., (VI.43) 
où B = k:Rtr0h;; k, est un coefficient empirique, égal à 2 pour le 
béton lourd ; k,, la hauteur de section utile de la pièce; b, la largeur 
de la section rectangulaire ou l’épaisseur de la nervure (de l’âme) de 
la section en T (en double T); c, la projection de la section oblique 
sur l'axe de la pièce. 

La condition du moment (VI.41) est généralement satisfaite sans 
calculs, en adoptant certaines dispositions constructives dont nous 
parlerons plus tard. Quant à la condition de l'effort (VI.42), elle 
demande généralement une série de calculs. 

Dans les recommandations pratiques relatives aux pièces de sec- 
tion rectangulaire, en T et d’autres profils analogues, on trouve la 
condition à laquelle doit satisfaire l'effort tranchant maximal: 


Q < 0,35Ryrbhoe (VI.44) 


Si cette condition est vérifiée, le béton de la nervure (de l’âme) entre 
deux fissures obliques résistera bien à l’action des efforts de com- 
pression obliques qui se manifestent dans cette zone. 

La résistance de la pièce à l’effort tranchant n'est pas à calculer, 
sauf si la pièce risque de présenter des fissures obliques d’après les 
calculs. Ce risque est établi en utilisant la relation empirique 


Q < kiRtrbho (VI.45) 


où k, est un coefficient égal à 0,6 pour le béton lourd. 


Calcul des armatures transversales 


Considérons une pièce fléchie munie d’armatures transversales 
sans barres relevées; c’est le cas le plus fréquent en pratique. 

De toutes les sections obliques qui prennent naissance dans le 
point B (fig. VI.17), nous retenons celle qui présente la plus petite 
capacité portante. Notons que 


Qb = Q — PC; > RatrFtr = tre. (VI.46) 


où Q est l'effort tranchant à l’origine de la section oblique (fig. VI.17): 
qtr est l'effort reporté par les armatures transversales par unité de 
longueur de la pièce. a 

Portons les expressions (VI.43) et (VI.46) dans (VI.42). J)vient 


Q< (gr + p)c + Ble (VI. 47) 


La plus petite capacité portante de la section oblique se définira 
bien évidemment par la condition 


| dQlde = (que + p) — Blé = 0. 


7—0948 97 


Nous en tirons la longueur de la projection de la section oblique 
retenue : 
= BB k:Rtrbh$ | 
NE V QtrTP Qtr+P (VE2) 
Portant cette quantité dans l'expression (VI.47), nous obtenons 
la condition de l’effort pour la plus petite capacité portante de la 
section oblique: 


Q<2V B (Qtr + P). 


Prenant la valeur de B dans (VI.43), 
nous obtenons l'effort tranchant Qi.» 
reporté par les armatures transversales. 
et le béton dans la section oblique con- 
sidérée : 


Qir.b = 2V koRtrbhE(Qir + p). (VI.49) 


FIG. VI.17. Efforts dans les Dans bien des a pratiques la charge 
armatures transversales inter- P: répartie uniformément par hypothèse, 
venant dans le calcul sui- est en réalité concentrée en quelques. 
vant les sections obliques points. Elle peut se trouver inexistante 

dans les limites de la section oblique. 
On ne tient compte de la charge, pour cette raison, que dans les cas 
où elle est vraiment répartie de façon uniforme (cas de pression de 
l’eau ou du sol par exemple). 

Posant p = 0 dans (VI.48) et (VI.49), nous voyons que la capa- 
cité portante de la section vis-à-vis de l’effort tranchant, assurée 
par la résistance du béton comprimé et des armatures transversales, 
est égale à 


Otrb = 2 V' kb Rirdtr. (VI. 50) 
La longueur de la projettion de la section oblique retenue se dé- 
finit alors par l'égalité 
keRtrbhè | 
= Re, (VI.51) 


Conformément au schéma de la figure VI.18, on a 
Qtrl = Ratrftrf OÙ Qt = Rate Fir tr = Jtr (VIL.92) 


où uw est l’écartement des armatures transversales CU tr, la 
section d’une barre transversale (une branche du cadre) ; n, nombre 
d'armatures transversales dans la section de la pièce. 

Dans les calculs, on se donne le plus souvent le diamètre des 
armatures transversales et leur nombre dans la section de la pièce, 
considérant dans la suite que f{-2 = F;, est une quantité donnée. 
La proportion des armatures transversales se déduit de l'égalité 
VI.50): 


_ Q? é Rtrb 
tr — AbhERy mals > D (VI.53) 




Cette valeur de g4 doit ètre égale à l'effort développé dans les 
armatures transversales par unité de longueur de la pièce: 


Qu= atrite, (VI.54) 




Il est à noter que l’écartement des armatures transversales ne 
doit jamais être excessif, sinon la section oblique risque de tomber 
entre deux barres transversales voisines, auquel cas sa capacité 
portante dépendra uniquement de Ia résistance du béton comprimé: 
on a alors Q < Q,. Pour définir l’écartement maximal des barres 
transversales, reprenons l'expression (VI.43) et affectons-la d’un 




FIG. VI.18. Sections obliques choisies pour le calcul: 


a, dans une zone à écartement inégal des armatures transversales; b, entre l'appui et une 
charge concentrée, avec a < © 


coefficient 0,75 qui tiendra compte des déviations possibles des fis- 
sures réelles par rapport à leur tracé théorique à cause de la non-ho- 
mogénéité du béton, ainsi que de l’inexactitude possible de la mise 
en place des cadres. Il vient 


= RM, (VL55) 


Le calcul de x doit être complété par des dispositions constructives 
(voir $ VI.). 

La proportion des armatures transversales (écartement, diamètre 
des aciers) peut varier suivant la longueur de la poutre. L'origine 
des sections obliques à retenir dans les calculs sera choisie à l’aplomb 
du nu de l'appui et dans le point où Q = Q4. prr (voir fig. VI.18, à. 
Les valeurs de calcul de l'effort tranchant seront choisies en consé- 
quence. La longueur de la pièce caractérisée par gq+,r est comptée 
entre l’appui et le point où Q = Q:,. prrvoir fig. VI.18, a). 

Si la pièce subit un effort concentré 2 appliqué à une distance 
a << c, de l’appui, la pièce risque de se détruire suivant la section 
oblique entre l'appui et le point d'application de P (fig. VI.18, b, 


q* 99 


section /-7). La condition de résistance suffisante dans cette section 
se déduit de (VI.47) en y posant c = a: 


Qr <trû +, 
ou compte tenu de (VI.43) 
QE gere + RU, (VI.56) 


De cette inégalité nous déduisons l'effort par unité de longueur 
de la poutre exercé sur les armatures transversales dans la section 


gui= Si tre (VL.57) 


Pour une section 77-II située au-delà du point d'application de 
P, l'effort dans les armatures transversales se laisse calculer, con- 
formément à (VI.53), à l’aide de la formule 


1 _ (@—P} 
FLOUE = Re (VI.58) 


Les armatures transversales sont dimensionnées pour résister au 


plus grand des efforts qe ou que” -11 


Exemple VI.8. Soit à calculer les armatures transversales d’une 
poutre de b — 20 cm, k — 40 cm (hk, — 36,5 cm) pour Q = 8 tf 
(80 kN). Béton lourd de classe M 200 (m1, = 1). Barres transversa- 


les en acier de classe A-II. 
Solution. On trouve dans les Annexes IV et VI les valeurs des 


résistances R,. — 90 kgf/cm? (9 MPa), R+, = 7,5 kgf/cm° (0,75 MPa), 
Ra.tr = 2150 kgf/cm? (215 MPa). 
La vérification suivant les conditions (VI.44), (VI.45) 


kiRibho & Q < 0,35Rprbho : 
0,6 x 7,5 x 20 x 36,5 = 3300 kgf (33 kN) < Q — 
— 8000 kgf (80 kN) < 0,35 x 90 x 20 x 36,5—23 000 kgf (23 kN) 


montre que les armatures transversales sont nécessaires et que les 
dimensions de la section de la poutre sont convenables. 

On adopte pour les armatuxes transversales d:, = 6 mm (f;, — 
= 0,283 cm°); n = 2; Fi, = 0,283 X 2 = 0,566 cm°. 

D'après la formule (VI.53), l'effort de calcul par unité de lon- 
gueur de la poutre encaissé par les armatures transversales est éva- 
lué à 


— 40 kgf/em (400 eh < ie. » TER 75 (750 N/em). 




L'écartement des armatures transversales calculé suivant la 
formule (VI.54) est égal à 
Ra.trFtr 2150 X 0,566 
Atr 40 
l'écartement maximal défini par la condition (VI.55) est 


0,75k:Rtrbhè 0,75 X 2 X 7,5 X 20 x 36,52 
Las gg = 81 Cm ; 
enfin, l’écartement dicté par les dispositions constructives (voir 
$ VI.1) doit être u < h/2 — 40/2 — 20 cm; u < 15 cm. 
On retient comme écartement des armatures transversales la 


plus petite des valeurs obtenues, soit u = 15 cm. 


— 30 cm ; 


Calcul des armatures relevées 


Les armatures relevées sont utilisées assez rarement, dans le but de 
renforcer des parties isolées de la poutre où les efforts tranchants 
sont particulièrement grands. L'emplacement des armatures relevées, 
c'est-à-dire des barres longitudinales isolées déviées de façon à pas- 
ser de la zone tendue vers la zone comprimée, est défini par le calcul 
suivant les sections normales et obliques (fig. VI.16). Les armatures 
seront relevées dans les zones où Q >> Q4..n (voir formule (VI.50)). 

La condition de résistance suffisante d’une pièce à armatures 
relevées, définie pour une section oblique d’après la formule (VI.42), 
peut être mise sous la forme 


Q < Ra.trFr sin & + Qtr.b (VI.59) 
La section à donner aux armatures relevées sera donc 
F,.= -2—Ctrb_ (VI.60) 


ÈS Ra.tr sin œ g 


Dispositions constructives garantissant 
la condition du moment 


La capacité portante de la section oblique vis-à-vis du moment flé- 
chissant (voir le second membre de l'inégalité (VI.41)) ne doit pas 
être inférieure à celle de la section normale passant par D (voir 
fig. VI.16). Les dispositions constructives exposées ci-après garan- 
tissent cette condition, rendant superflu le calcul des sections obli- 
ques en fonction du moment fléchissant. 

Si l’ancrage des armatures longitudinales sur l’appui libre est 
exécuté conformément aux prescriptions du $ IIIL.3, c’est-à-dire si la 
résistance de ces armatures est complètement utilisée en travée, la 
résistance suffisante en flexion de la pièce est garantie dans toutes 
les sections obliques qui prennent naissance près du nu de l'appui. 

En pratique, les poutres sont fabriquées le plus souvent sans 
armatures relevées. En effet, si toutes les armatures longitudinales 




tendues sont prolongées jusqu'aux appuis et convenablement ancrées, 
la condition du moment se trouve satisfaite en toute section oblique 
même sans l'intervention des armatures transversales, grâce aux 
seules armatures longitudinales dont la proportion a été calculée 
pour la section normale en 
prenant une valeur non infé- 
rieure du moment fléchissant. 
Il devient inutile, dans ces 
conditions, de calculer les 
sections obliques vis-à-vis du 
moment fléchissant. 

Afin de diminuer la dé- 
pense d'acier, il est permis 
d'interrompre une fraction des 
armatures longitudinales (jus- 
qu'à 50 % de la section cal- 
culée) en travée, là où elles 
deviennent inutiles conformé- 
ment au calcul de la pièce 
suivant les sections normales. 

Les barres interrompues 
doivent être cependant pro- 


FIG. VI.19. Recherche du point d’inter- 


ruption des armatures en travée: 


a, plan de ferraillage de la pièce; b, dia- 
gramme des moments; c, diagramme des efforts 
tranchants: 1-I, point d’ interruption théorique 
des barres 2 S16 : II-II, point d'interruption 
pratique de ces barres : 1. iagramme des 1no- 
ments provenant de la charge; 2, diagramme 
des moments reportés par les sections normales 


longées au-delà du point d'in- 
terruption théorique, confor- 
mément au diagramme des 
moments fléchissants (section 
I-T sur la figure VI.19), d'une 
longueur w sur laquelle l’ab- 


d 1 iè & | aurc d té iat Q 
e la pièce iarraniené es matériaux) sence des armatures longi- 


tudinales sera compensée par 
des armatures transversale:, de façon à garantir la condition 
des moments dans les sections obliques (section Z7ZI-ITI sur la 
figure VI.19, a). Compte tenu de ces considérations et des con- 
ditions d'ancrage des barres interrompues dans le béton, la longueur 
w sera choisie égale à la plus grande des deux valeurs suivantes: 


_ ©0— Q-—Qr + 5d : 


ÉTAT we 204, 


(VI.61) 


où Q est l'effort tranchant déCaltul dans le point d'interruption 
théorique de la barre (section Z-7 sur la figure VI.19) correspondant 
à la charge pour laquelle ce point a été calculé; @, est l'effort tran- 
chant reporté par les armatures relevées dans le point d'interruption 
théorique, au cas où la pièce en comporte; gt. est l’effort par unité 
de la longueur repris par les armatures transversales, calculé pour 
résister au moment fléchissant exercé sur les armatures transversa- 
les dans la section oblique (section Z11-IIT sur la figure VI.19, a); d 
est le diamètre de la barre interrompue. 




Les quantités Q,, qtr.» sont calculées en utilisant les équations 
Q, = R,F,sin a, (VI. 62) 
Qtrw = RaFtr/u. (VI.63) 


S'il n’y a aucune armature relevée dans la zone d'interruption 
des barres, on pose Q, = 0 dans la première formule (VI.61). 

Proposons-nous de chercher le point d’interruption des armatures 
en travée en prenant à titre d'exemple le cas montré sur la figu- 
re VI.19. Portons sur le diagramme des moments provenant des 
charges de calcul extérieures l’ordonnée du moment subi par la 
section normale de la pièce en béton armé, à condition que cette 
section contienne uniquement des armatures non interrompues en 
travée (F5 pour 2@20, avec Map = Mo@o0 Sur la figure). La valeur 
de cette ordonnée sera calculée par la formule 


Map = RaFPz. (VI.64) 


Ce sont les points de rencontre de 7,, avec le diagramme des 
moments de calcul qui définissent le point d'interruption théorique 
des barres 7-7. Le point d'interruption pratique 77-IT doit se trouver 
à une distance w de Z-I. Sur le diagramme des efforts tranchants on 
distingue l’ordonnée Q qui a été introduite dans la formule (VI.61) 
de w. 


$ VI.5. CALCUL À LA FISSURATION DES PIÈCES 
PRÉCONTRAINTES 


Lors du calcul à la formation des fissures normales dans une pièce 
précontrainte fléchie, l’état-limite de cette dernière est assimilé à 
l’état final du stade Z (fig. VI, 10, c). On voit sur la figure VI.20, b 
le schéma des efforts et des contraintes adopté pour le calcul à la 
fissuration d’une pièce de section rectangulaire. Pour simplifier, le 
diagramme curviligne des contraintes dans le béton a été remplacé 
par un diagramme rectangulaire approché en zone tendue et par un 
diagramme triangulaire en zone comprimée (pour 6, 0,7 Rt+rrr). 

Immédiatement avant l’apparition des fissures, on admet que la 
contrainte dans le béton est égale à R};,:1r, c’est-à-dire à la résistance 
de calcul à la traction du béton suivant les états-limites d'utilisa- 
tion (voir Annexe IV). 

La pièce se trouve exposée à l’action simultanée des facteurs 
suivants: e 

— un moment fléchissant M. Pour le calculer, on prend les 
charges de calcul et on les affecte d’un coefficient de surcharge 
n>1oun = 1,suivant la catégorie de la résistance à la fissuration 
de la structure ($ III.1); 

— la résultante N,4 des efforts de précontrainte exercés sur les 
armatures F,. et Fh. En calculant cette résultante, on fait interve- 




nir le coefficient de précision de la mise en tension des armatures de 
précontrainte Mmt (Voir $ [II.2). 
Les déformations étant supposées varier de façon linéaire suivant 
la hauteur de section (voir fig. VI.20, c), on a 
It . h—zp—a , 
Éb— bte} zs? pc Ëbtr 7 z  ? 


(VI.65) 




Epc = Eb.tr HT 


Les expériences ont montré que le module de déformation du bé- 
ton soumis à une contrainte de traction maximale est à peu près 
deux fois plus petit que son module d'élasticité initial £,. La défor- 


FIG. VI.20. Schéma des efforts et des contraintes pour le calcul à la fissuration 
d’une pièce fléchie précontrainte: 


a, section de la pièce; b, diagramme des contraintes dans le béton montrant les efforts de 
calcul ; c, diagramme des déformations relatives 


mation du béton au bord de la zone tendue se laisse donc mettre 
sous la forme 


2 Rtriz __ 2Rtril 
Eb.tr — 0,5Ë) TOR é (VI.66) 


Compte tenu de ce qui précède, on exprime la contrainte dans le 
béton au bord de la zone comprimée de la section et la contrainte 
dans les armatures provenant du moment M et de l’effort de précon- 
trainte V, avant la fissuration à l’aide des relations 


Oh = Epeb = 2Rtrn rer ; (VI.67} 
+ Tr. 
Opc = E sep = E ,Eb.tr a — 2nRt+r1r — ; (VI.68) 
Ope — pepe = EaEb.tr 7 = 2nRirrt peer ;  (VI.69) 
n — E,/Eh. 


Les contraintes calculées dans les armatures F,. et F,< sont ajoutées 
aux contraintes provenant de la précontrainte 0, et 0. 




Les efforts produits dans l'acier et le béton de la section par le 
moment À{ et l'effort de précontrainte V, peuvent être calculés à 
l’aide des relations suivantes: 


Npe= FpeTpe; Npe= FpcOpe ; 
No ER No (h—25) DR. 


La hauteur de la zone comprimée de la section se déduit de la 
condition de nullité de la somme des projections de toutes les for- 
ces normales sur l’axe de la pièce: 


No + Noe — Nie + Nitr — N5 = 0; (VI.71} 
on a après quelques transformations 


bh?+2rFpc(hk— a) + 2nFpca' _. Re h 
——7; | (VI.72) 
2bh + 2n (Fpo-+ Fpe) +2 
tril 


La pièce reste exempte de fissures tant que le moment fléchissant 
M dû aux charges exercées reste inférieur au moment des forces in- 
ternes dans la section normale de 
la pièce qui se trouve dans un 
état correspondant à la limite de 
résistance à la fissuration du béton. 
Avec des moments calculés par rap- 
port à un point situé sur la ligne 
d'action de l'effort ÆV, (pour plus 
de simplicité), cette condition se 
laisse exprimer par l'inégalité sui- 
vante: 


Tt — 


MN pce + Nice + 


+N (h—e+a—<) + 
FIG. VI.21. Pour le calcul à la fis- 


_ hs: suration par la méthode des mo- 
E Moitr (e+a 2 je (VI. 75) ments de noyau: 


1, zone comprimée; 2, zone tendue; 
Pour une pièce de profil plus 3, noyau central 
complexe (en T ou en double T, 
voir fig. VI.21), les Normes recommandent une méthode de calcul 
à la fissuration approchée basée sur les moments de noyau: ne 


Mest < Mi, (VI.74) 


où Mit le moment des forces extérieures situées d’un même côté 
de la section considérée, pris par rapport à un axe normal au plan 
de flexion et passant par un point du noyau central plus éloigné de 
la zone de la section dont on vérifie la fissuration (le point C sur la 




figure VI.21); Af4 est le moment des forces internes immédiatement 
avant la fissuration du béton, pris par rapport au même axe. 

La hauteur du point € du noyau et le moment A7, se calculent à 
l'aide des égalités 


ry = 0,8W/Fn (VI.75) 


{on prend 1 au lieu de 0,8 si la pièce fléchie n’est pas précontrainte); 
Mr = Rien Wi + Mat, (VI.76) 


où An% est le moment provenant de l'effort de précontrainte À, 
{après déduction de toutes les pertes) par rapport au même point du 
noyau, compte tenu du sens de rotation; W, est le module de ré- 
sistance de la section par rapport à son bord tendu déterminé par les 
règles de résistance des matériaux élastiques; Wa est le module de 
résistance de la section homogène équivalente fictive par rapport à 
son bord tendu déterminé en tenant compte des déformations ané- 
lastiques du béton de la zone tendue (avec le diagramme rectangu- 
laire, voir figure VI.20, b); le moment M}, peut être calculé sans 
erreur excessive à l’aide de la formule approchée 


Wir &YWa, (VI.77) 


où y est un coefficient égal à 1,75 pour les sections rectangulaire et 
en T à hourdis comprimé. Quant aux sections en double T (voir la 
figure VI.21), le coefficient y est trouvé dans le Tableau VI.2. 


TABLEAU VI.2 


Valeur du coefficient y pour les sections dissymétriques 
en double T (voir fig. VI.21; m—membrure) 


Caractéristique de la section 


b!/b bn/b km/h L 
<< 3 < 2 quelconque 1,75 
de 2 à 6 idem 4,5 
> 6 > 0,1 4,5 
de 3 à 8 < 4 quelconque 4,5 
> 4 > 0,2 4,5 
> 4 < 0,2 1,25 
>8 quelconque 0.3 1,5 
idem < 0,3 1,25 


Dans le cas où la contrainte dans le béton comprimé 0: devient si 
grande que les ordonnées extrêmes maximales du diagramme dépas- 
sent Rhr11 , on doit tenir compte aussi des déformations anélastiques 
du béton comprimé; au lieu du diagramme triangulaire, on considère 
alors un diagramme en trapèze. Ce cas est peu fréquent ; nous omet- 
tons de le traiter ici. 

Exemple VI.9. Calculer à la fissuration une dalle pleine de di- 
mensions suivantes : b — 100 cm, k = 12 cm, F,. — 2,545 cm° (cinq 
câbles torsadés à sept fils 3 mm, voir Annexe VIII), a — 2,2 cm, 
Fie = 0; béton lourd de classe M 400; effort de précontrainte (après 
déduction de toutes les pertes) N, = 21 tf (210 kN); M = 1,8 tf:m 
(18 kN :m). 

Solution. On trouve dans les Annexes III, V, VII les valeurs de 
Rien = 18 kgf/cm°? (1,8 MPa); Rex = 225 kgf/cm° (22,5 MPa); 
En = 33-104 kgf/cm* (33-10% MPa); ÆE, — 18-105 kgf/cm°? (18 x 
x 10% MPa): 


n = EQlE, = 18:105/33.10? = 5,45. 
D'après la formule (VI.72) 


7, = 100 X 42242 X 5,45 X 2,545 (12—2,2) + (21 000/18) 12 _ 9 
on 2 X 100 X 12-42 X 5,45 X 2,545 + (21 000/18) L 


On calcule d’après (VI.67) la plus grande ordonnée des contraintes 
de compression dans le béton: 




= 72 kgfem? (7,2 MPa) < 


<O0,7Rpr11 = 0,7 X 225 = 157 kgf/em?(15,7 MPa). 


Les efforts dans le béton se calculent au moyen des formules 


(VI. 70): 
N, =" — TX FX 0 28 800 kgf (288 kN): 


Ni.tr —= (h — Tt) DR trr1 —= (12 — 8) 100 X 18 — 
— 7200 kgf (72 kN). 


La vérification de la pièce à la fissuration sera faite conformé- 
ment à la condition (VI.73) en posant e = 0 et Ne = 0: 


Op — 2Rirrt = 2 x 18 


MN, (r—a—*+) EN (a Pt ) : 


c'est-à-dire que il 
180 000 kgf-em (18 kN em) < 28 800 [12 —2,2— +) + 


12— 8 


Ainsi donc, la dalle ne risque pas de présenter des fissures normales. 


+ 7200 (2,2— ) = 206 900 kgf-em (20,69 kN -cm). 




Exemple VI.10. Dans les conditions de l’exemple VI.9, faire le 
calcul à la fissuration de la dalle par la méthode des moments de 


noyau. 
Solution. La section homogène équivalente définie par (IITI.3), 




est égale à 
Fég = 12 X 100 + 5,45 X 2,545 = 1214 cm. 


Le moment statique de la section par rapport à son bord infé- 
rieur est 


S = 100 x 12 x 6 + 5,45 X 2,545 x 2,2 — 7230 sm. 


La distance entre le bord inférieur et le centre de gravité de la 
section homogène équivalente est 


S 7230 
y = Fa TM 9,95 cm. 


Le moment d'inertie de la section homogène équivalente par rap- 
port à l’axe central est 


Tég = XE +100 x 12 (6,0 —5,95)2+ 
+ 5,45 X 2,545 (5,95 — 2,2)? — 14 600 cmé. 


Le module de résistance de la section par rapport au bord tendu 
en phase élastique est 


Le module de résistance de la section compte tenu des déforma- 
tions anélastiques se calcule d'après la formule (VI.77) en prenant 


V=— 4,75 
Wir = VW, = 1,75 x 2450 = 4280 cm°. 


La distance du point du noyau éloigné du bord tendu de la sec- 
tion se calcule à l’aide de la formule (VI.75): 


W 4280 
= — DB ae x = 2,82 cm. 


Le moment reporté par la section avant la fissuration, défini par 
la formule (VI.76), est évalué à 
Mi = Ris Wir + Mie = Rtrit Wir + No Y — a + rs) = 
— 18 x 4280 + 21 000 (5,95 — 2,2 + 2,82) — 
= 77 000 + 138 000 = 215 000 kgf:cm (21,5 kN :m). 


Rappelons que la valeur de M; calculée dans l'exemple VI.9 était 
de 206 900 kgf:cm (20,69 KN : m). 
Vérifions la résistance à la fissuration au moyen de la formule 
(VI.74) : 
M'ai < Mr; 18 kN:m < 21,5 kN:m, 


ce qui veut dire que la dalle ne présentera pas de fissures normales. 

Dans les zones soumises à l’action de M et de Q, la pièce fléchie 
risque de présenter des fissures obliques au niveau du centre de gra- 
vité de la section de la pièce, ou bien dans la nervure de la section 
en T, au voisinage du raccordement du hourdis comprimé. Ces fissu- 
res apparaissent sous l’action des contraintes principales de traction 
et de compression : 


Opr.c __ Ox+0y (Ox—0y\2 > 
Opretr UE V (=) F Taus (VI. 78) 


où 0, et 0, sont les contraintes normales suivant l'axe de la pièce 
et sa hauteur respectivement ; t,, sont les contraintes tangentielles 
provenant des charges extérieures et de la précontrainte. 


TABLEAU VI.S 
Valeurs des coefficients m, et m, 


Classe du béton (lourd) | m1 | ma 


M 400 et au-dessous 0,5 2 

M 500 0,375 1,6 
M 600 0,25 1,33 
M 700 0,125 1,14 


Les fissures obliques ne se manifestent pas si les conditions sui- 
vantes ont respectées: 


Opree MRprir: Opr.tr < Rorit (VI.79) 


Opr.e > MiRprlls Opr.tr Ma Rtrrt (1— Ro ] (VI.80) 


les valeurs des coefficients m,, m, étant tirées du Tableau VI.3. 
$ VI.6. CALCUL DES FLECHES « 
Détermination des flèches 


Dans le cas général la flèche d’une pièce travaillant à la flexion a 
pour équation 


y (x) = | Î M (e) + (a) dr?+Cix+C, 




où A (x) est l’équation du moment fléchissant et : (x) l'équation de 


la courbure. 

Pour les pièces en béton armé la courbure n’est pas seulement. 
fonction de la variable axiale x mais aussi de l’état de contrainte et. 
de déformation de la pièce. Dans une pièce où toutes les valeurs de 
M sont de même signe, la flèche se laisse calculer à l’aide des for- 
mules de Résistance des matériaux, en faisant intervenir la relation 


v=r  M()dr+Ciz+c, 


dans laquelle la raideur ET invariable au cours de la mise en charge 
est remplacée par une raideur flexionnelle B qui correspond à l’état 
considéré de la pièce. 

Pour une poutre librement appuyée à simple travée à charge uni- 
formément répartie, la flèche à mi-portée est égale à 


Valeurs du coefficient S 


Cas de charge | S Cas de charge | S 


: M 1 qi … 
Puisque + — = et que pour la poutre en question on a M — S'il 
vient 



Dans le cas général, pour une pièce de section constante chargée. 
comme une poutre librement appuyée ou une poutre cantilever, on a. 


f=— se. (VI.82} 


Courbure d'une pièce sans fissures normales 
en zone tendue 


Les pièces en question se rapportent aux pièces précontraintes dont. 
la résistance à la fissuration doit satisfaire aux exigences des caté-- 
gories 1 et 2. 

La courbure de la pièce 1/p s'écrit sous forme d’une somme 


, (VI.83), 


« 1 4 Lé Q 
où —— et on sont les courbures calculées respectivement pour les: 


surcharges de courte durée et pour les charges permanentes et les. 


surcharges de longue durée à l’aide de la formule 

1 Mc 

non (VI.84). 
dans laquelle A est le moment fléchissant produit par la charge. 
correspondante et c un coeîticient qui traduit l’effet du fluage différé: 
du béton: pour le béton lourd on prend c = 1 en considérant les. 
surcharges de courte durée et c = 2 en considérant les charges per- 
manentes et les surcharges de longue durée (le degré hygrométrique 
de l’air étant supérieur à 40 %). Le coefficient 0,85 tient compte de 
l'effet du fluage rapide du béton. 


La courbure sÈe , qui caractérise la contre-flèche produite par 
une action de courte durée de l’effort de précontrainte W,, est égale à 


1 Hosone VL.85) 
Pet 0,85EpJ 6 ‘ qe 7 


La courbure , qui caractérise la contre-flèche entraînée par le. 


Q cf-p Le ? . 97 . 
retrait et le fluage du béton précontraint s'écrit 


1 1 , 
Pct.p ah (Gp — Gp), De) 




où 0, et 0, sont les contraintes numériquement égales à la somme des 
pertes de précontrainte de l’acier par fluage et retrait du béton, soit 
à Og + 68 + 09 (voir $ III.2), calculées respectivement au niveau 
du centre de gravité de l’armature longitudinale tendue et de la fibre 
comprimée extrême du béton. 
Si la pièce présente des fissures refermées, les valeurs calculées 
1 1 | . x Tee 
— , — , — doivent être majorées de 20 %. 
Pcd Pet  Pid 
Courbure d'une pièce avec fissures normales 
en zone tendue 
Les pièces en question se rapportent aux pièces en béton armé non 


précontraint, ainsi qu'aux pièces précontraintes dont la résistance à 
la fissuration doit satisfaire aux exigences de la 3° catégorie. L'état 


SN / 
Él < 


Oh No, 


FIG. VI.22. Etat de contrainte et de déformation d’une pièce fléchie avec des 
fissures normales en zone tendue: 


1, déformations du béton au bord déla zone comprimée ; 2, déformation de l’armature ten- 


de contrainte et de déformation d’une telle pièce est montré sur la 
figure VI.22. Les déformations relatives moyennes des armatures 
tendues et des fibres extrêmes du béton comprimé peuvent être repré- 
sentées, conformément à la figure, sous la forme 


Ea.moy = VaËa "a = = Ya EFan (VI.87) 


où le coefficient w, est le rapport de la valeur moyenne des déforma- 
tions de l’armature à leur valeur maximale (au droit de la fissure). 
Il caractérise le travail du béton tendu entre deux fissures voisines. 




Le coefficient 1, caractérise la répartition irrégulière des déforma- 
tions de la couche comprimée extrême du béton sur la longueur du 
bloc entre deux fissures voisines. On a pour le béton lourd #}, = 0,9. 
Le coefficient v tient compte de l’état élastoplastique du béton dans 
la zone comprimée. On prend pour le béton lourd v = 0,45 si la 
surcharge est de courte durée et 
v = 0,15 si elle est de longue durée. 

La courbure de la pièce (fig. 
VI.23) se laisse déduire de la simi- 
litude des triangles OAB et CDE : 


4 __ Ea.moy + Eb.moy 
= <eme-tébmer (V1.89) 


Compte tenu des relations (VI.87) 
et (VI.88) et des effets de la pré- 
contrainte, la courbure peut aussi 
être mise sous la forme 


1 M [ Ya Fe Ÿb | 2e 
P hoz1 L EaFa (v' +6) bhvEp 


—-i%e ,  (VIS90) FIG. VL23. Déformation d'une 
to*af a pièce fléchie après la formation 

où À est un moment fictif calculé RES MREUrS 
par rapport à un axe normal au 
plan d action du moment et passant par le centre de gravité de la 
section de 1 armature tendue (en service), dû à toutes les forces exté- 
rieures (y compris l'effort de précontrainte /V,) situées du même 
côté de la section considérée de la pièce. 


Le bras de levier du couple de forces internes z, dans la section 
fissurée se calcule à l’aide de la formule 


- __ v'hh/ho+E 
zh [1 Tr |, (VI.91) 


y nb) hf + Fin/2v 
= — (VI.92) 


Pour la hauteur relative de la zone comprimée d’une section 
normale fissurée £, les Normes proposent une formule empirique 


== : 93) 
CR EE LEE SET 9 
M | | 
L= Re: T=y (A—hi/2h;). (VI.94) 


8—0948 113 


Pour les sections en T à hourdis relativement mince, on peut po- 
ser approximativement 






Pour les structures en béton lourd, le coefficient 1, est calculé à 
l’aide de la formule recommandée dans les Normes: 


1— m° 


(VI.94a) 


dans laquelle (pour Jes pièces fléchies) 


RtrriWt 
<< |, VI.96 
Me — MaoY = ( } 


avec Mist — M (pour les pièces fléchies) et 


MS = Neue + Ty) (V1.97) 


(eope est montré sur la figure VI.21). 

L'excentricité €a.moy de la force N, par rapport au centre de gra- 
vité de la section des armatures tendues (en service) et le rapport de 
Ea.moy à 20 Se calculent à l’aide des formules 


Ms . €asmoy __ Mt — 1,2 | 
Ca. moy — No Ù op — Noho A s (VI.98} 


La quantité s prend dans les formules (VI.95) et (VI.98) les va- 
leurs suivantes: 
s — 1,1 pour les charges de courte durée et les armatures en 
barres à haute adhérence; 
s = 1 pour les charges de courte durée et les armatures en fils 
d'acier ; 
s = 0,8 pour les charges de longue durée, quelles que soient les 
armatures. : 
La courbure dépend de la durée d'action de la charge, puisque 
les coefficients \, et v en dépendent. 
La courbure totale se présente sous la forme d’une somme 
Î 1 1 1 1 
Ho het Pct.p Dre 


où . est la courbure "a à l’ action de courte durée de toutes les 


1 + ins 
charges et surchaïges ; = ja couLbure due à l’action de courte durée 


des charges permanentes et des surcharges de longue durée; = la 
, : 4 


courbure due à l’action de longue durée des charges permanentes et 
la courbure caractérisant la con- 


des surcharges de longue durée; 


tre-flèche due au retrait et au Îluage . béton précontraint (voir la 
formule (VI.86)).. | en. 


114 _ 


La raideur flexionnelle B de la pièce se déduit de (VI.90): 
ho21EaFa 


2e Va (1 —21/€a.moy) + Ÿbra.b ? (VI.100) 
ab = TE) Dhbnv (VI.100a) 


Flèche limite d'une pièce en béton armé 


La flèche d’une pièce en béton armé est déterminée en affectant les 
charges d'un coefficient de surcharge nr — 1. Elle ne doit jamais 
dépasser une valeur limite imposée par les Normes en fonction de 
la portée L exprimée en mètres: | 


Planchers à plafond plat, Flèche limite 
couvertures, en m 


1< 6 1/200 
6<LI1<7,5 3 cm 
1>7,5 1/300 


Planchers à plafond ner- 
vuré, escaliers,{en m 


1<5 1/200 
5<I<10 2,5 cm 
1> 10 1/400 


$ VI.7. CALCUL DE L'OUVERTURE DES FISSURES 


L'ouverture des fissures normales a; sous la charge caractéristique 
est calculée d’après la formule (V.13) en y mettant À — 1 et en pre- 
nant comme 6, les contraintes dans les barres de la file extrême des 
armatures tendues en service: 
___ M 
a Faz ? 


où Z, est le bras de levier du couple interne en stade IT calculé sui- 
vant la formule (VI.91). 
On peut calculer 6, d’après la formule simplifiée 


(VI.101) 


Ca = Ra NT (VI.101a) 
où À est le moment de calcul reporté par la section avec les arma® 
tures du type donné. 

Si la pièce est précontrainte, on retient comme 6, l’accroisse- 
ment de la contrainte dans l’armature dû à la charge extérieure: 


0, = M— No (1 —a.pe) (VI.102) 


Fazi 


8* 115 


où Z, est trouvé d'après la formule (VI.91) et e,., est montré sur la 


figure VI.21. 
Dans une pièce fléchie comportant des armatures transversales, 


l'ouverture des fissures obliques af est calculée en mm dans les 
zones d'action de ÀJ et de Q à l’aide de la formule 
ar= Cak (ko + 30dmax) LL <——, (VI.103) 
hrt Eù 
où ca et n sont les mêmes que dans (V.13); da, est le diamètre de 
la plus grosse barre transversale ou relevée, mm; h, est la hauteur 
de section utile, mm; 


: = (20 — 1200) 1085 > 8.108; (VI.104) 
Ftr Fr 
Uri = tr + Br = + De : (VI.105) 
nie N 
t= 7 — 0,25. (VI.106) 


Dans la formule (VI.106) Q© est le plus grand effort tranchant 
dans la zone considérée de la pièce à proportion d’armatures trans- 
versales constante. Seules sont considérées dans le calcul les sections 
dont la distance à l’appui est non inférieure à ,. 


CHAPITRE VII 


PIÈCES EN BÉTON ARMÉ CHARGÉES 
EN FLEXION COMPOSÉE 


& VIL.{. DISPOSITIONS CONSTRUCTIVES 
DES PIÈCES CHARGÉES EN FLEXION-COMPRESSION 


Soumise à une flexion-compression, la pièce subit à la fois une force 
de compression longitudinale V et un moment fléchissant A7. Ce 
peut être le poteau d’un bâtiment industriel sans étage reportant le 
poids d’un pont roulant (fig. VIL.1, a), la membrure supérieure d'une 
ferme sans diagonales (fig. VII.1, b), la paroi d’un réservoir enterré 


a) b à 
D P, plancher 


| L”2 pont roulant 


FIG. VII.1. Pièces chargées en flexion-compression : 


a, poteau d’un bâtiment industriel; b, membrure supérieure d’une ferme sans diagonales : 
c, paroi d’un réservoir enterré 


de forme rectangulaire qui subit la poussée latérale du sol ou du 
liquide et la pression verticale du plancher (fig. VII.1, c). 

La distance entre la ligne d'action de la force de compression 
et l'axe longitudinal de la pièce porte le nom d'’excentricité e,. Dans 
le cas général, l’excentricité en un point quelconque d'une piètb 
faisant partie d'une structure isostatique est égale à 


= + ee, (VIL.1) 


où ej° est l’excentricité accidentelle (voir $ IV.1). 




Si la structure est hyperstatique, l’excentricité est prise égale à 
la valeur obtenue par le calcul statique de la structure, mais non 
inférieure à ef. 

Il y a intérêt à augmenter la section de la pièce dans le plan 
d'action du moment; la section peut être rectangulaire ou avoir la 
forme d’un T ou d’un double T. 

Le ferraillage d'une pièce chargée en flexion-compression est 
constitué par des barres principales longitudinales (disposées con- 
tre les faces courtes du profil de la pièce), dimensionnées conformé- 
ment au calcul, et des barres transversales ou cadres qui ne sont 




Barres de  Souder 
montage 26 16 


h<600 &| 800=<h<1000 




800 < h < 1000 


FIG. VII.2. Ferraillage d’une pièce 
chargée en flexion-compression : 


a, avec carcasses soudées ; b, avec barres 
isolées réunies par des cadres 


pas calculés mais disposés selon les prescriptions des Normes. Toutes 
les barres sont assemblées de façon à former une carcasse soudée ou 
(moins souvent) ligaturée. 

La proportion optimale des armatures principales contre chaque 
côté court de la section de la pièce est de 0,5 à 1,2 % de la section. 

Les normes établissent une section minimale à donner aux arma- 
tures longitudinales dans les pièces comprimées de chaque côté de 
la section. Exprimée en pour cent, cette section est égale à: 


0,05 si larg < 17; 
0,4 si 17< lo/rg 35; 
0,2 si 30< {lo/rg < 83; 
0,25 si lo/rg > 83, 


où r, est le rayon de giration de la section de la pièce dans le plan 
de l’excentricité de la force longitudinale; Z, est la longueur de 
flambement de la pièce comprimée. 

Les armatures utilisées dans une pièce chargée en flexion-com- 
pression doivent.être conformes aux conditions générales établies 




pour les structures en béton armé (voir $ III.3), mais aussi aux 
conditions imposées à une pièce comprimée par une force axiale 
longitudinale (voir $ IV.) ou à une pièce travaillant en flexion 
simple (voir $ VI.{), suivant que l’excentricité de la force de com- 
pression est grande ou petite. 

Les plans de ferraillage courants sont montrés sur la figure 
VII.2. La proportion des armatures principales peut être différente 
aux deux côtés de la section de la pièce: c’est un ferraillage dissy- 
métrique. On préfère cependant le ferraillage symétrique, même s’il 
entraîne une dépense d'acier un peu excessive. 

Les carcasses tridimensionnelles (cages d’armatures) sont assem- 
blées à partir de carcasses planes soudées (nappes). Les cages liga- 
turées sont formées par des barres longitudinales isolées et par des 
cadres fermés (principaux et éventuellement auxiliaires) entourant 
ces barres. 

Les pièces chargées en flexion-compression sont fabriquées avec 
précontrainte si l’excentricité de la force de compression est grande, 
les moments fléchissants devenant importants et une partie de la 
section travaillant en traction. La précontrainte est utilisée aussi 
lorsque la pièce est très élancée. Elle améliore la résistance à la 
fissuration de la pièce, qualité utile en service, et augmente sa 
raideur qui est nécessaire au cours de la fabrication, du transport 
et du montage. 


$ VII.2. CALCUL D'UNE PIÈCE CHARGÉE 
EN FLEXION-COMPRESSION 


Différents cas de flexion-compression 


En fonction de la nature de l'état de contrainte et du mode de 
rupture de la pièce, on distingue deux cas de flexion-compression. 


! & ,N 
FIG. VII.3. Essai de compression 
fortement excentrée d’une pièce en « 
béton armé : 
1, zone tendue; 2, zone comprimée N 


Premier cas. L’excentricité de la force de compression longitu- 
dinale est relativement grande. L'état de contrainte et le mode de 
rupture de la pièce sont voisins de ceux d'une pièce simplement flé- 
chie (fig. VII.3 et VII.4, a). La partie de la section éloignée de la 




a) e x D) K 




Diagramme | 
Roc Fa 


FIG. VII.4. Schémas des efforts dans une pièce chargée en flexion-compression : 


a, Cas 1 ; b, cas 2: 1, axe géométrique de la pièce au sein de la structure ;: 2, bord de la zone 
comprimée ; 3, centre de gravité de la section du béton dans la zone comprimée ; Fa armatu- 


re plus éloignée de la force de compression longitudinale ; Fa: armature plus proche de la 
force de compression longitudinale 


force est tendue et présente des fissures normales à l’axe longitudi- 
nal de la pièce; l’armature-dispôSe dans cette zone reporte la tota- 
lité des tractions. Dans la section proche de la force, le béton et 
l'acier sont comprimés. La ruine de la pièce commence au moment 
où la limite d’élasticité (apparente ou conventionnelle) est atteinte 
dans l’acier tendu et se termine quand la contrainte du béton et de 
l’acier dans la zone comprimée devient égale à la charge de rupture. 
Si l’acier a un palier d'écoulement, la contrainte dans l’armature 
tendue reste constante; si l'acier n’a pas de palier, la contrainte 
augmente légèrement. La ruine est progressive, continue. 




Deuxième cas. L’excentricité de la force de compression longi- 
tudinale est relativement petite. La zone de compression occupe 
soit la totalité de la section (voir fig. VII.4, b, diagramme 7 en 
pointillé), soit la plus grande partie de la section, plus proche de la 
force longitudinale, la partie opposée de la section subissant alors 
une certaine traction (voir fig. VII.4, b, diagramme 2). La ruine. 
survient lorsque les contraintes dans la partie de la section plus 
proche de la force deviennent supérieures aux résistances limites 
(charges de rupture) du béton et de l’acier. Dans la partie de la 
section éloignée de la force de compression, les contraintes (de com- 
pression ou de traction) restent basses, si bien que la résistance des. 
matériaux n’est pas complètement utilisée dans cette zone. 


Pièce de profil symétrique quelconque 


Les schémas des efforts retenus au calcul de résistance d’une pièce: 
de profil symétrique quelconque soumise à une compression excen- 
trée dans le plan de symétrie sont montrés sur la figure VII.4. 

En calculant la capacité portante selon le cas 1, on admet que 
la résistance de calcul du béton comprimé est constante et égale à 
Rpr, tandis que les résistances de calcul des aciers tendus et compri- 
més sont prises égales à R, et à R,,. respectivement. Au calcul selon 
le cas 2, on remplace les diagrammes des contraintes réels dans le: 
béton (en pointillé sur la figure VII.4, b) par un diagramme con- 
ventionnel rectangulaire d'ordonnée égale à R,, et l’on prend la 
résistance de calcul des armatures comprimées de section F; égale. 
à R,... Dans les armatures de section F, la contrainte ©, est infé- 
rieure à la résistance de calcul. 

Sur la figure VII.4 le schéma a) correspond à E = 2/h) ER 
et le schéma b) à E = x/h, >> En, où ER est la hauteur relative li- 
mite de la zone comprimée (voir formule (VI.5)). 

Quand E = x/h, < ËR (voir fig. VIL.4, a), la position de l’axe 
neutre est déterminée par l'égalité entre la force longitudinale de: 
calcul W, qui provient des charges extérieures de calcul et de la 
somme des projections des forces internes de calcul dans l'acier et 
dans le béton comprimé sur l’axe longitudinal de la pièce: 


N=RyFp + RacFa — RaFa- (VII.2) 


La condition de résistance suffisante de la pièce est résumée par: 
une inégalité qui relie le moment fléchissant M = Ve dû aux ch# 
ges de calcul extérieures, et la somme des moments des forces inter- 
nes indiquées pris par rapport à un axe normal au plan du moment 
fléchissant et passant par le point d’application de la résultante: 
des efforts dans l’armature, tendue par la force extérieure : 


Ne < RorFh2b + Ra.cFaza (VIT.S) 


za = hs — a", (VIL.4) 


Sur la figure VII.4, a on a désigné par e et e’ les distances de la 
force longitudinale V aux centres de gravité des sections des arma- 
tures tendue }", et comprimée /'; par les charges. 

Si la pièce est précontrainte, on introduit dans les formules 
(VII.2) et (VII.3) les efforts supplémentaires dans les armatures de 
précontrainte : 


MagRpeFpe dans l'armature F,., 
Oclpe dans l’armature F,,.. 


Quand £ = x/h, > ER (fig. VII.4, b), la résistance de la pièce 
est calculée comme précédemment d’après la formule (VII.3) mais 
la hauteur de la zone comprimée est déterminée par l'égalité 


N = Rorlp + RacFi — OaFae (VIL.5) 


La contrainte dans l’armature moins sollicitée ©, est déterminée 
en fonction du matériau. Par exemple, dans une pièce en béton de 
classe M 400 et au-dessous, munie d’'armatures non précontraintes 
des classes A-I, A-IT, A-IIT, les contraintes ©, sont déduites de 
l'expression 
1—zx/ho 
1—6rR 


établie en supposant que la relation entre les contraintes de l'acier 
et la valeur de Ë est linéaire dans les limites comprises entre Ë — 
— xlhs = 1 et £ — ER, ce qui est confirmé par les données expé- 
rimentales. Au contraire, dans une pièce fabriquée en béton de 
classe supérieure à M 400 et munie d'armatures de classe supérieure 
à A-III, la contrainte ©, est déterminée à l’aide de la formule expé- 
rimentale 


Oa= (2 —1) Ra (VII.6) 


O = — 0 — (1) | (VII. 7) 


où &, est calculé d’après la formule (VI.6). Pour tenir compte du 
coefficient mp1 — 0,85, on prend 5000 au lieu de 4000. 

La contrainte 6, obtenue--ær moyen des formules (VII.6) et 
{VII.7) est prise en compte avec son signe; sa valeur est contenue 
entre À; et —R;c. 

Pour un acier à haute résistance sans limite d'’élasticité appa- 
rente, la relation (VII.7) reste vraie jusqu'à 0, & 0,8 R,. Si donc 
Ca > 0,8 R,, on calcule la valeur de ©, par la formule 


… Es] — 
0, = (0,8+0,2 Ex) R,. (VIL.8) 




où Ea est calculé à l’aide de la formule (VI.5) en y prenant o, — 
— 0,8 R, ESS Op: 

Une pièce élancée cède au flambement sous l'action du moment 
développé pendant la compression excentrée, si bien que l’excen- 
tricité de la force longitudinale V devient supérieure à la valeur 
initiale e, (fig. VII.5). Le moment fléchissant devient plus fort, 
et finalement la pièce se détruit sous l’action d'une force longitu- 
dinale moins grande que si elle était courte (peu élancée). 

Quand l’élancement de la pièce chargée en flexion-compression 
est L/r >> 14, le calcul peut être fait au moyen des formules citées 
mais en introduisant une excentricité majorée 
(en multipliant l’excentricité initiale e, par un 
coefficient n >> 1). 

La valeur du coefficient n se déduit de l’é- 
quation 


TN IN er ? (VII.9) 
__ 6,4E F[ J 0,11 
Ner= F Le (or +041) +ni | 
(VIL.40) 


Dans cette formule sont prises en considération 
les particularités du béton armé: la coexistence 
du béton et de l'acier au sein de la même sec- 
tion, les propriétés anélastiques du béton 
comprimé, l'existence des fissures dans la zone 
tendue, l'influence de l’action prolongée de la 
charge sur la raideur de la pièce à l'état-limite. pjg. vii5. 1In- 

Les notations utilisées dans (VII.10) sont les  fluencedu flambe- 
suivantes: /l,, longueur de flambement de la ment 
pièce; J, moment d'inertie de la section du 
béton; J,, moment d'inertie de la section de l’acier par rapport 
au centre de gravité de la section du béton; ky, coefficient tradui- 
sant l'influence d'une action de longue durée sur la flèche de la 
pièce à l’état-limite, X,., coefficient introduit pour tenir compte 
de l'influence de la précontrainte de l’armature sur la raideur de la 
pièce à l’état-limite (en supposant que la contrainte est uniformé- 
ment répartie dans la section de l’armature de précontrainte). 

Les coefficients kj4 et k,< sont cherchés en appliquant les rek- 
tions empiriques suivantes: 


ba=1+-; (VII.11) 
ke = 1 + 40 Ho ne (VII.12) 




Dans (VI1.11) on entend par AZ, et M les moments par rapport 
au centre de gravité de la section de l'armature tendue ou la moins 
comprimée (la section étant entièrement comprimée), qui provien- 
nent respectivement de l’ensemble des charges et surcharges ou de 
la charge permanente augmentée d'une surcharge de longue durée. 

Dans (VII.12) on entend par 0, la contrainte créée dans le 
béton par la force de précontrainte après déduction de toutes les 

; pertes. Si la pièce n'est pas précon- 
Ep y N trainte, on met k, = 1. 

La valeur de ?{ dans (VII.10) est prise 

égale à 


t—e/h (VII.13) 
mais non inférieure à 
min = 0,5— 0,01 2 — 0 ,001R5, 
(V]1.14) 


valeur empirique où À,, est pris en 
kgf/cm*. 

Si Lo/r << 14, on pose n — f. 

S'il se trouve que V > WN,,, la sec- 
tion est trop petite. 

Les armatures transversales de la 
pièce chargée en flexion-compression sont 
calculées pour résister à l’effort tranchant 
suivant les sections obliques, en utilisant 
les formules de calcul usuelles des pièces 
simplement fléchies (voir $ VI.4). 


Pièce de section rectangulaire 


On a pour une section rectangulaire 
FIG. VII.6. Pour le calcul (fig, VII.6) 
d’une pièce de section rec- 


] 6 de , Q T 
COR ce en fle F=6bt; Ni=Rprbt; 2 = h0— T: 
pression : 
1, axe géométrique de la pièce; (VII.15) 


2, bord de la zone comprimée; 
3, centre de gravité de la section 


] ans i L 
du héton dans la zone comprimée  _ e= en + —0. (VII.15a) 




La formule de calcul de la capacité portante (VII.3) devient donc 
Ne < Rrbt (ho — 0,97) + RacFa (ko — a).  (VII.16) 
La hauteur de la zone comprimée se définit à partir des égalités 


suivantes : 
a) pour E = zh < ER 


N = Rorbt + RacFa — RaFa; (VII.17) 
1 24 


b) pou E = xh > Er 
N = Rpr0t + RacFa — OaFa (VII.18) 


où 04 est calculé soit d’après (VII.6), scit d’après (VII.7), en fonc- 
tion des matériaux mis en œuvre. 


Vérification de la capacité portante 


Toutes les données sur la section étant connues, on calcule la 
hauteur de la zone comprimée à partir de (VII.17) en admettant 
que E = x/ho < ER. Il vient 
= N—RacFatRala 

Rprô ° 


Ceci fait, on calcule & , à l’aide de (VI.5) et l’on vérifie la condition 
z L'ERho. Si cette condition est satisfaite, on vérifie la capacité 
portante de la pièce à l’aide de la formule (VII.16) en y substituant 
la valeur trouvée de x. Si la formule (VII.19) donne x > £ Lh,, on 
procède à un nouveau calcul de x en utilisant cette fois-ci la formu- 
le (VII.18), c'est-à-dire en admettant que les contraintes dans l’ar- 
mature F, sont égales à 0. 

Le béton étant de classe non supérieure à M 400 et l’acier de 
classe non supérieure à A-IIT, on porte dans (VII.18) la valeur de 
6, obtenue d’après (VII.6). Il vient 


x (VII.19) 


LL ON+C—RaFa—Ra.cFs 
__ 2RaFa i 
C= Fes. (VIL.21) 


La valeur de x ainsi trouvée est portée ensuite dans (VII.16) 
afin de vérifier la capacité portante de la pièce. 

Si l’on reçoit x > ERA pour un béton de classe supérieure à 
M 400 et un acier de classe A-IV et au-dessus, on doit substituer 
dans (VII.18) la valeur de o, obtenue d’après (VII.7), ce qui donne 
une équation quadratique 


N—RacF,—DFa"  DF : 
E2— RTE dr Rnbts E)=0, (VII.22) 
4000 . 
Da, (VIL.23) 


Avec E tiré de (VII.22), on calcule la valeur de x = Eh, et on la 
substitue dans la condition (VII.16) afin de vérifier la capacité 
portante de la pièce. 




Exemple VII.1. Vérifier la résistance d'un poteau en béton armé 
d'après les données suivantes : section À — 40 cm, b — 30 cm, F, — 
— "ji = 7,5 cm* (armatures 3G18 A-IIT contre chaque face de la 
section); a = a — 3 cm; , = 40 — 3 — 37 cm; longueur de 
flambement ?, — 4,8 m; N — 60 if, y compris W ,4 — 40 tf: M — 
— 3,6 tf.m, y compris M4 — 2,0 tf:m. Béton M 300 traité par la 
chaleur, my, — 0,85. 

Solution. Pour le béton M 300 on trouve dans l'Annexe IV R,, = 
— 135 kgf/cm°; compte tenu de m3, = 0,85, on obtient R,, = 
— 115 kgf/cm”. Pour l’acier de classe A-III on trouve dans l’Anne- 
xe VI R;,— Race = 3600 kgf/cem?, E, — 2.106 kgf/cm?; dans 
l'Annexe V on trouve E3, = 0,9 x 2,9.105 = 2,6.105 kgf/cm°?; n — 
=E,/E, = 2-108/2,6.105 — 7,7. 

La section étant rectangulaire, son rayon de giration est r — 
= 0,29 } — 0,29 x 40 — 11,6 cm. L’élancement de la pièce est 
à = lfr = 480/11,6 = 41,5 > 14; on doit donc tenir compte du 
flambement. 

Avant de calculer N,, d'après (VII.10), on cherche: 


JE = XL 160.108 cmt ; 


Ja = Fa (ha)? = 2 x 7,5 (20 — 3)? = 4,35.10° cmt; 


M 3,6 > 
€o ON — 30 —0,06 m—6 cm. 


D'après la formule (VII.13) on a t — eç/h — 6/40 = 0,15. 
D'après la formule (VII.14) on a 


tmin = 0,5 0,012 —0,001R;r = 


= 0,5— 0,01 7 — 0,001 x 115 = 0,265. 
Puisque t << tin, On pose £ = Émin — 0,265. 
Avant de calculer ka, cherchons d’abord 


e = eo + h2 — a = 6 + 20 — 3 — 23 cm; 
M, = Ne = 60 x 0,23 = 13,8 tf.m: 
NM = Niae = 40 X 0,23 = 9,2 ti.m. 


Cherchons à présent kja d’après (VII.11). Il vient 


ld 9.2 _ 
ha =1+ 5 1455 = 1,67. 


La force critique {V,. sera déterminée à l’aide de la formule 
(VII.10) en posant pe — 1 (le poteau n'est pas précontraint): 


= La (or) + ]= 


__ 6,4% 2,6.105 oi Q,11 - 
480? | 1,67 Exenee +0, 1)+7,7 x 4,35.109 | = 


— 920 000 kgf — 520 tf. 
D'après (VII.9) 




1—N/Ner 1—60/520 — 1,15. 


D'après (VII.15a) 


e=en+z—a=6xt, 13+ 20 —3 — 23,8 cm. 


D'après (VII.29) 
N 60 000 


Ro 15%80 — 17,30m; 
T 17,3 
FRET 37 = 0,47. 


D'après (VI.6) 
Éo = 0,85 — 0,0008 R,, = 0,85 — 0,0008 X 115 = 0,76. 


D'après (VI.5), en remplaçant 4000 par 5000 et en mettant 
Oh = Ra — 3600 kgf/cm°, 


: 0.76 
5 Ra E 3600 0.76 

PER £ D RERO a 
1 500 (: s) + 660 (1 11 | 


Puisque E << Ex, la résistance doit être vérifiée en appliquant 
la formule (VII.16): 


Ne < R,0t (ho — 0,5 x) + RacFa (io — 4). 
Il vient 
60 000 x 23,8 < 115 x 30 x 17,3 (37 — 8,65) + 3600 x ” 
X 7,5 (37 — 3); 
1,44.108 << 1,69.106 + 0,94.106. 


La résistance est bonne. | | 
Exemple VII.2. Vérifier la capacité portante de la pièce étudiée 
dans l'exemple VITI.1 mais en prenant N — 80 tf (au lieu de 60 tf). 




Solution. 


== 0, 045 m— 4,5 cm. 


t—eph—4,5/40=0,112; tmin—=0,269; t—0,265. 
e—ey+—a—4, 9 +20—3—21,5 cm. 
M,=Ne—80xX0,215=17,2tf.m. 
MA = Njge = 40 X 0,215 = 8,6 tf-m. 


ka =1+ = 1 + — 1,5. 


6,4 x 2,6.105 F 160.103 0,11 
7 480? — | 1,5 (ose + 0.1 


— 945 000 kgf — 545 tf. 


ro 3 
Wer — 


}+7,7x 4,35.10°] = 


n — 1—80/545 —= 1,17. 
e = en + h/2—a—4,5 X 1,17 +20 —3 — 22,3 cm. 
D'après (VII.21) 


2RaFa 2 X 3600 X 7,5 


a = 110 000. 


D'après (VII.20) 


N+C—RaFa—Ra.cF, 
L = û]——— — 


Rprô+ Ciho 
__ 100 000 + 140 000— 3600 x 7,5— 3600 x 7,5 
115 x 30-- 110 000/37 — = 24,2 cm. 


zx > ERrho = 0,51 X 37 = 18,8 cm. 
D'après (VII.16) 
Ne < Rrdt (ho — 0,5 t) + RacFa (Ro — a). 
Il vient 
80 000 x 22,3< 115 x 30 x 24,2 (37 — 12,1) + 3600 x 
X 7,5 (37 — 3); 
4,7:106 <Z 2,067106 LE 0,91.106. 


La résistance est bonne. 


Section à donner aux armatures 


Les valeurs de W, L,, b et h étant supposées connues, on cherche 
la section à donner aux armatures F, et F; par la méthode des ap- 
proximations successives. On commence par poser n = 1 (car n est 




fonction de W,, qui dépend à son tour de la section de l’armature) 
et l’on détermine les sections nécessaires F, et F,. L'armature 
étant dimensionnée conformément aux sections calculées, on véri- 
fie la capacité portante comme il vient d’être expliqué plus haut 
(voir exemples). Si la capacité portante s'avère insuffisante ou exa- 
gérée, on corrige le plan de ferraillage adopté (en ajustant parfois 
aussi la section à donner ou les classes des matériaux à adopter) et 
l’on fait une nouvelle vérification de la capacité portante. 

Dans une pièce élancée, on peut tenir compte de l'influence du 
flambement dès la première approximation, en introduisant une 
proportion d’armatures 


Fa+F! : 
p=—57— = 0,01 à 0,03 


dans la formule de W... 
Les formules servant à déterminer F, et F; en première appro- 
ximation seront déduites des équations usuelles. 
Au cas où le ferraillage est dissymétrique, on pose £ = Ex X 
zx = ZR). Puisqu'on a, conformément au Tableau VI.1 et à la 


formule (VI.13), 


Ryrbtr (ho) = AnbhiRr, 


on obtient à partir de (VII.16) et (VII.17) 
pi Ne—ArRprbhe (VII.24) 


Ra.cza 


EnRprhho—® + pi ae. (VIL.25) 
La section F, étant déterminée (soit par le calcul, soit en raison 
des dispositions constructives), on calcule à l’aide de la formu- 


le (VII.16) 




Ne—Ra.cla (ho —a") 


Divisons le premier et le second membres‘ par 5. Puisque x/h, = £ 
et qu'on a Ë (1 — É/2) — À, en vertu de (VI.15), il vient 
Ne—Ra.cF!, (ho—a') 
0— Rprbhÿ 


(VII.26) 


En fonction de À, ainsi trouvé, on choisit £ dans le Tableau VI.1. 
Maintenant, connaissant x — Ëh,, on peut calculer la sectioneà 
donner aux armatures à l’aide de (VII.17): 


— N r Ra. 
Fan + Fe De. (VII.27) 


Dans la pratique, on adopte très souvent un ferraillage symétri- 
Lé Q ? L ‘ : 
que, surtout lorsque les moments fléchissants s exercent sui la 


90948 129 


pièce avec les signes opposés mais avec des intensités sensiblement 
égales. Si F, = FX et R,c = Ra, de sorte que R,.cFx = R;Fa, 
on peut calculer x à l’aide de (VII.17): 


TL —= 


R6: (VII.28) 
Pour cette valeur de x, on obtient ensuite à l’aide de la formule 
(VII.16) 
pm __Nle—ho+N/(2Rprb) 
FF; RU ad (VII.29) 


Calcul aux états-limites d'utilisation 


Le calcul à la fissuration d’une pièce chargée en flexion-compression 
est effectué au moyen des formules (VI.74) et (VI.76), compte tenu 
du fait que la force de compression extérieure V, excentrée de & 
par rapport au centre de gravité de la section, fait naître un moment 


Mexè = N (e,— r,) par rapport au point du noyau central éloigné 
du bord tendu de la section. 

Pour connaître l’ouverture des fissures, on applique la formu- 
le (V.13) en prenant k — 1 et en faisant intervenir les contraintes 
Ca tirées de la formule (VI.102) dans laquelle M = N (e; — 2) où 
e, est la distance de la force extérieure V à l’armature tendue. 


La flèche est calculée d’après la formule (VI.82) dans laquelle 
la valeur de la courbure ! est tirée de la formule (VI.90), en pre- 


nant Mr = Ne, + Nota.pes OÙ €a.pe est la distance entre la force 
de précontrainte et l’armature tendue, et en remplaçant W, par 
N; = N + N, dans le deuxième membre de la formule. 


$ VIL3. PIÈCES CHARGÉES EN FLEXION AVEC TRACTION 


Parmi les pièces chargées en flexion avec traction, on peut citer les 
parois des réservoirs (trémies) qui subissent la pression des matières 


FIG. VII.7. Pièces chargées en flexion avec traction: 
1, paroi d’un réservoir (trémie); 2, membrure inférieure d’une ferme sans diagonales 


contenues (fig. VII.7, a), les membrures inférieures des fermes sans 
diagonales (fig. VII.7, b) et certaines autres pièces. Elles sont sou- 




mises à la fois à une force de traction longitudinale W et à un mo- 
ment fléchissant M. Ce cas peut être assimilé à l’action d’une force 
de traction unique V appliquée avec une excentricité € — MIN 
par rapport à l'axe longitudinal de la pièce. 

En fonction de l’excentricité e,, on distingue deux cas d'état de 
contrainte et de ruine des pièces (fig. VII.8). 

Premier cas. La force de traction W est appliquée à l’intérieur de 
za (fig. VIL.8, a). La section en béton de l'élément est traversée 




Na “Are Fr 


fesses 
Ne” or fs 

Na = Ra la 
RS =) 


FIG. VII.8. Schémas des efforts dans les pièces chargées en flexion avec traction: 
a, Cas 4 (la force de traction agit à l’intérieur de za); b, cas 2 (la force de traction agit en 
dehors de za) 


tout entière, de part en part, par des fissures transversales. Dans la 
section fissurée, seule l’armature longitudinale oppose une résistan- 
ce à l’effort extérieur. La pièce se rompt lorsque la contrainte dans 
l’armature longitudinale atteint sa valeur limite. 

Deuxième cas. La force de traction V agit en dehors de z;, 
(fig. VIL.8, b). Une partie de la section est comprimée (du côté du 
bord éloigné de W), l’autre partie est tendue, comme pendant une 
compression fortement excentrée. Après que des fissures se sont 
produites dans le béton tendu, l'effort de traction est reporté tout 
entier, dans les sections fissurées, par l’armature tendue. La ruine 
se produit par épuisement de la résistance de l’acier tendu et du 
béton comprimé; l’armature disposée dans la partie comprimée de 
la section peut travailler à la limite de résistance si la hauteur & 
la zone comprimée est telle que 2, << 24. 

Le ferraillage d'une pièce chargée en flexion avec traction selon 
le cas 2 est réalisé au moyen de barres longitudinales et transversa- 
les, comme pour une pièce chargée en compression excentrée; si la 
pièce travaille selon le cas 1, elle est ferraillée comme une pièce char- 
gée en traction simple. 


és 131 


La précontrainte des pièces de profil symétrique quelconque 
chargées en flexion avec traction s'impose dans les mêmes cas que 
pour les pièces chargées en traction simple (cas 1) et les pièces simple- 
ment fléchies (cas 2). Le calcul de résistance d’une pièce de profil 
‘symétrique quelconque chargée en flexion avec traction s'opère 
en adoptant les schémas d'efforts montrés sur la fig. VIT.8. 

Dans le cas 1 (fig. VII.8, a) les conditions de résistance suffi- 
sante de la pièce peuvent se réduire aux équations des moments des 
forces extérieures et internes, pris par rapport aux axes normaux au 
plan de flexion et passant par les centres de gravité des armatures 
Fa et F, respectivement : 


Ne LL R:Faza; Ne<R;Fiza. (VII.30) 


Dans le cas 2 (fig. VII.8, b) la condition de résistance suffisante 
de la pièce se réduit à la condition du moment fléchissant : 


Ne < Rorl os + Ra.cl ia. (V11.31) 


Il est commode de déterminer la hauteur de la zone comprimée de 
RaFa — RacFa — N = RirFy (VII.32) 


Pour une pièce munie d’armatures de précontrainte de sections 
Foe et Fpe; tes formules indiquées ci-dessus prennent la forme 


e L(RaFa + MasRpcF pc) Zn, Ne<L(RalFa + Mas Rpel pe) ; 
| (VI1.33) 
Ne < < RprEp25 + PR. “FE Za + OF pe£re : , (VII.34) 


RaFa —Racla + MailRpelre — CeFpe — N = RyrFy  (VII.32a) 


Calcul aux états-limites d'utilisation 


Le calcul à la fissuration est effectué au moyen des formules (VI.74) 
et (VI.76), compte tenu du fait que la force de traction extérieure, 


excentrée de e, par rapport au centre de gravité de la section, fait 


naître un moment Mext — N (e, + r,) par rapport au point du 


noyau central éloigné du bord tendu (e, étant la distance entre la 
force V et l’armature tendue). 

Pour connaître l'ouverture des fissures, on applique la formu- 
le (V.13) en prenant À — 1,2 et en faisant intervenir les contraintes 
01 tirées de la formule (VI.102) dans laquelle 17 — N (e; + 2;). 

La flèche est calculée d'après la formule (VI.82) dans laquelle 


la valeur. de la. courbure À est tirée de la formule (VI.90), en pre- 


nant Mr = Nex + Notapcs OÙ Eure est la distance entre la force 
de précontrainte et l’armature tendue, et en remplaçant W, par 
N, = N, — N dans le deuxième membre de la formule (VI.90). 


CHAPITRE VIII 
STRUCTURES EN MACONNERIE 


$ VIIL1. MATÉRIAUX UTILISÉS EN MAÇONNERIE, 
LEUR RÉSISTANCE ET DEFORMATION 


La maçonnerie utilisée pour la réalisation des structurés des bâti- 
ments et ouviages représente un ensemble de pierrès artificielles 
ou naturetles réunies par du mortier au furet à mesure de leur jux- 
taposition. En fonction de la nature du liant, on distingue les mor- 
tiers de ciment, les mortiers de chaux et les mortiers composés (ciment- 
chaux et argile-cimrent)-Ha-chaux et l’ argile"ont là propriété d’aug- 
menter la plasticité et le pouvoir de rétention d’eau du mortier, 
qualités fort utiles pour la bonne tenue dela maçonnerie. Les mor- 
tiers dont la masse volumique à sec y est supérieure ou égale à 
1500 kg/m° sont dits lourds; si y << 1500 kg/m°, on dit que le mor- 
tier est léger. 

La résistance mécanique de la pierre et du mortier est caracté- 
risée par leur classe (ou marque): c'est la valeur de la charge de rup- 
ture .en compression exprimée en kgf/cm°. La méthode de l’essai de 
compression est précisée dans des Normes correspondantes. Les ma- 
tériaux existants sont répartis en catégories suivantes: 

.—-elasses 300 à 1000: pierres à haute résistance (pierre natu- 
relle lourde, brique spéciale à haute résistance); 

— classes 35 à 250: pierres à résistance moyenne (briques diffé- 
rentes, blocs de céramique et de béton, pierres naturelles légères); 

— classes 4 à 25: pierres à basse résistance (calcaires: tendres, 
matériaux bruts). 

Les mortiers utilisés sont des classes 4, 10, 25, 50, 75, 100, 150, 
200. Un mortier fraîchement posé (ou le mortier dégelé d'un massif 
de maçonnerie exécuté par la méthode de congélation) a la résistan- 
ce. nulle, 

Quant à la résistance au 1 gel, les pierres et les bétons sont divisés 
en classes Mp3 10 à Mp3 300. 

Les classes minimales de résistance mécanique et de résistangg 
au gel sont spécifiées dans les Normes, en fonction du type de la 
structure, des conditions de son service et du degré de longévité {). 


—.--.. ss... ee ee. .e—- -. -— .… —.— = —.. —_ 


1) La longévité (ou fiabilité) d’une structure -présume ‘une, durée de service 
minimale déterminée : 100 ans pour le degré 1, 50 : ‘ans “pAUe: le degré 2, 20 ans 
pour le degré 3. re r 




Par exemple, les pierres employées dans les murs extérieurs des 
bâtiments contenant des liquides et dans les encorbellements des 
murs (corniches, parapets, etc.) doivent avoir une classe de résis- 
tance au gel non inférieure à 90; le mortier employé dans les mê- 
mes conditions sera de classe 50 au moins. 

La résistance mécanique de Ia maçonnerie est fonction de la 
taille et de la résistance mécanique des pierres; de la composition 
et de la résistance mécanique du mortier; de l’âge de la construc- 
tion; du soin apporté à l’exécution des travaux. 

Il existe des relations empiriques qui permettent de préciser la 


valeur moyenne (espérée) de la charge de rupture À des différents 




FIG. VIII.1. Tractions exercées sur la maçonnerie: 
a, section aux joints en prolongement; b, section aux joints en découpe 


types de maçonneries, exprimée en kgf/cm? (MPa) !). La résistance 
de calcul est 


R = R!/k, 


où k est un coefficient de sécurité dépendant du matériau. On prend 
k — 2 en compression et k — 2,25 en traction. 

Les Normes citent les valeurs de la résistance de calcul pour 
tous les types de maçonneries. Nous donnons un Tableau condensé 
des résistances de calcul à la compression À. 


TABLEAU VIII.1 


Résistances de calcul à la compression R de la maçonnerie 
de briques de tous types hourdées au mortier lourd, kgf/em°? (MPa) 


Classe du mortier 


Classe des EE L, Résistance 
briques nulle du mortier 
| 100 | 75 50 | 25 | 
150 22 (2,2) | 20(2) |18(4,8)1 454,51 131,3) | 8 (0,8) 
100 18 (1,8) | 17 (4,7) | 15 (4,5) | 143 (4,3) | 10 (1) 6 (0,6) 
75 45 (4,5) | 44 (4,4) | 13 (1,3) 1 11(4,2)| 9(0,9)|[ 5 (0,5) 
50 _ 41 (4,1) | 40 (1) 9(0,9)| 7(0,7)| 3,5 (0,35) 


1) La notion de résistance caractéristique (ou normative) RC (voir Ch. I) 
est inapplicable à la maçonnerie, vu que sa résistance mécanique ne fait pas 
l’objet d’une norme et n'est pas contrôlée par un essai. 




La résistance à la traction de la maçonnerie est différente sui- 
vant que l'effort de traction s'exerce dans une section qui se con- 
fond ou non avec un plan de joint (fig. VIII.1). Elle dépend aussi 
de la nature de la traction. On a: 

— en traction simple R4, = 0,3 à 2 kgf/cm? (0,03 à 0,2 MPa); 

— en flexion-traction Rrt = 0. 4 à 3 kgf/cm? (0,04 à 0 ,3 MPa). 

Dans certains cas la résistance de calcul d'une maçonnerie sera 
réduite en introduisant un coefficient de comportement de la ma- 
connerie Mm. Par exemple, quand il s’agit d’une pile ou d’un entre- 
deux de section F << 0,3 m°, il convient de diminuer la résistance 
de calcul de 20 % en prenant m,, — 0,8. 

On considère à part le cas de compression locale: c’est le cas où 
la section F de la pièce n’est chargée que sur sa partie F, (surface 
d'appui d'une ferme, d’une poutre, d’un poteau, etc.). La partie 
non chargée de la section joue alors le rôle de frette qui s'oppose 
aux déformations transversales de la maçonnerie dans la partie char- 
gée, grâce à quoi la résistance de calcul sur F, est augmentée: 


Récr = YR, où Y = Fe SV: 


Si la surface d’écrasement est située de façon non symétrique, 
il y a lieu de diminuer F en conséquence. Le coefficient y, est fonc- 
tion de la nature de la maçonnerie et du cas de charge locale. Dans 
une maçonnerie de briques pleines on a y, — 2 quand la surface 
d’écrasement est située dans la partie centrale du mur ou du pilier, 
et y, = 1,2 quand elle est située près du bord de la pièce. 

La déformation de la maçonnerie en service est analogue à celle 
‘du béton (voir Ch. II, $ II.2): 


e — Eg] + Ep: 


Le module de déformation Æ sous la contrainte © est égal à la 


tangente de l'angle d'inclinaison de la tangente au diagramme 
O — €: 


_ do 
D'après la formule empirique due au professeur L. Onichtchik 
o ( E ) : 
ici E, est le module d’élasticité (module de déformation initial) 
en kgf/cm? (MPa). « 
Dans les calculs pratiques on pose 
Eo — aR, 


en retenant comme. À la valeur moyenne de la charge de rupture de 
la maçonnerie égale au double de la résistance de calcul: & est la 




constante élastique de la maçonnerie définie dans le Tableau VIII.2 
en fonction du type de la maçonnerie et de la classe du mortier. 


TABLEAU VIII.2 
Constante élastique « de la maçonnerie 


Classe du mortier 


Résistance 

Maçonnerie nulle du 

> 25 10 | 4 mortier 
Briques d'argile, pierres cérami- | 
ques, blocs de béton léger 1000 750 : 500 200 
Briques de grès 750 900 . 390 200 


$ VIII.2Z. CALCUL DES PIÈCES COMPRIMÉES 


La capacité portante d’une pièce comprimée en maçonnerie non 
armée est fonction de la résistance métanique de la maçonnerie, des 
dimensions de la pièce et de l’excentricité de la force longitudinale 
€. Cette excentricité est due à un décalage permanent ou accidentel 
de la force N par rapport au centre de gravité de la section de la 
pièce. Si la pièce subit à la fois l’action d’une force axiale À et d'un 
moment fléchissant A7, on a 


€o — MIN. 


L'excentricité accidentelle ect n’est prise en compte que dans 
les murs portants et autoportants d'épaisseur égale ou inférieure à 
25 cm. Prise égale à 2 cm pour les murs'portants et à 1 cm pour les 
murs autoportants, elle est ajoutée à l’excentricité es. 

Dans la maçonnerie nôn armée, pour les combinaisons fonda- 
mentales des charges, l’excentricité e, doit êtré non supérieure à 
0,9 y et dans les murs d'épaisseur égale ou inférieure à 25 cm 


eo + eat < 0,8 y, 


où y est la distance du: centre de gravité de la section au bord le 
plus comprimé (fig. VIII.2); dans une section rectangulaire on a 
y =. En cas de compression. simple (es = 0) les contraintes sont 
uniformément réparties suivant la section de la pièce (voir 
fig. VIII.2, a). Si la force est légèrement excentrée, la distribution 
des contraintes cesse d’être uniforme, mais la section reste compri- 
mée tout entière (voir fig. VIII.2, b). Une excentricité plus marquée 
fait naître des contraintes de traction 04. dans la section de la pièce 
(voir fig. VIII.2, c). Si ot >> Rr+, des fissures apparaissent dans la 
zone tendue de la section, si bien que l'effort de compression n’est 
reporté que par la partie F, de la section. Dans les calculs, on admet 




que F. est symétrique par rapport à NW et 
que les contraintes sont uniformément ré- 
parties sur #4, la contrainte étant suppo- 
sée égale à Ro > R (voir fig. VIII.2, e). 

Dans une pièce comprimée élancée, on 
doit tenir compte de la diminution de la 
capacité portante à cause du flambement 
et de l'augmentation de la flèche due à 
l’action prolongée de la charge (voir cha- 
pitre VII, fig. VII.5). 

De cette brève analyse de l'état 
de contrainte il ressort que le calcul des 
pièces simplement comprimées se réduit 
à la condition 


N Lm14aqFR, (VIIL.A4) 


où NW est la force longitudinale de calcul: F 
la section de la pièce; À la résistance 
de calcul à la compression de la maçonnerie: 


p < 1 est le coefficient de flambement : : 


Mia S 1 un coefficient .qui tient compte 
de la flèche due à l’action de. la charge de 
longue durée. 

Si la pièce est comprimée et fléchie, 
la formule est légèrement différente : 


N <miagiFeRo,  (VIIL.2) 


où les quantités AN, mia, R sont les 
mêmes que précédemment; F, est la sur- 
face de la zone comprimée de la section 
symétrique par rapport à la force NV. On a 


pour une section rectangulaire (voir fig. 
VIII.2, e) 


Fe=2b (+ e); (VILA) 


& est un Coefficient qui tient compte de 
l'augmentation de la résistance de calcul 
de la maçonnerie sur Fe; on a pour une 
section de forme quelconque 


© = 1 + e/38y & 1,25 (VIII.4) 


FIG. VIII.2 Etats de contrainte des pièces 
comprimées 


Fissures 


 J'ection Lu 
C7 W 


n127 

us É 

4 2(5-4) 




et pour une section rectangulaire 
o—1+ Ter <1,25 (VIIL.5) 


{pour la maçonnerie de pierres naturelles ou de pierres et blocs en 
béton cellulaires et caverneux on prend & = 1); ®, est le coefficient 
de flambement introduit pour tenir compte du travail à la compres- 
sion de la section incomplète de la pièce. 

Pour calculer ®, ®, et M4, on a besoin de connaître l’élance- 
ment À de la pièce. On sait que l’élancement est le rapport de la 
longueur de flambement !, au rayon de giration r de la section: 


À — Lo/r. 


La longueur de flambement /, dépend des conditions de fixa- 
tion des extrémités de la pièce; pour une pièce librement posée de 
hauteur À la longueur de flambement est !, — 2 H, pour une pièce 
articulée ?, — H et pour une pièce partiellement encastrée L,> 
>0,8 H !). 

Une section rectangulaire de côté k a un rayon de giration r Æ 
Æ 0,29 h»; de ce fait, on peut évaluer l’élancement de la pièce di- 


rectement d’après le rapport /,/h. Pour le faire, on introduit les 
notations 


Ar = lors À = Lh (M & 0,29 A7). 


Quant au coefficient de flambement ®, il ne dépend pas seule- 
ment de l’élancement de la pièce mais aussi des propriétés de dé- 
formation de la maçonnerie caractérisées par la constante élasti- 
que «@. 




TABLEAU VIII.s 
Coefficients de flambement 


sols 


re [ue lie 


18 [20 | [os [2e |os | a 




16 |8s | 0 


| | 10 
afas [as fes [aus |s6 | 7 | 104 


ofo;r4|o, 


1) Compte tenu de ces considérations, on met !, = H pour les murs et les 
piliers des bâtiments à étages de hauteur d'étage H; si les murs portent des 
planchers préfabriqués, on à Lo = 0,9 A; si les planchers sont fabriqués en 
béton armé coulé in situ, on prend l, = 0,8 H. Dans un bâtiment industriel 
sans étages, pour les murs et les piliers de hauteur 4, on prend !, = 1,5 H si le 
Donna est à simple travée et l, = 1,25 H si le bâtiment est à travées multi- 
ples. | | 




1 00) 0,02/ 0,89 084 


83 01 0 20,49 0,45 


Le Tableau VIII.3 cite les valeurs de œ en fonction de l'élan- 
cement fictif : 


M Pare 


Le coefficient de flambement , d’une pièce de section rectan- 
gulaire est calculé d'après la formule 


p.=p | 1—#2 (0,062 — 0,2) |. (VIIL.6) 




Pour une section de forme quelconque, on met 55 


A dans (VIIL.6). 

La diminution de la capacité portante des pièces comprimées 
due à l’action prolongée de la charge n’est prise en considération 
que si la section est petite. Ainsi, dans une section rectangulaire 
de k << 30 cm et dans une section de forme quelconque de r < 8,7 cm 
on prend 


au lieu de 


ma =1— np (14 Heu Lui), (VIIL.7) 


où {V est la force longitudinale totale de calcul; N ja la force longi- 
tudinale de calcul déterminée par les charges de longue durée; 
eoia l'excentricité de Va; n un coefficient dépendant de l'élan- 
cement (voir Tableau VIII.4). 

Si k > 30 cm ou r > 8,7 cm, on met mja = 1. 


TABLEAU VIII.4 
Coefficients n 


Ah | < 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 26 
AT | < 39 | 42 | 49 | 06 | 63 | 70 | 76 | 83 | 90 
n | 0 | 0,04 | 0,08 | 0,12 | 0,15 | 0,2 | 0,24 | 0,27 | 0,31 
$ VIIL3. MAÇONNERIE ARMÉE Tee 


On appelle maçonnerie armée une maçonnerie renforcée par une ar- 
mature d’acier. Une telle maçonnerie devient plus robuste ou plus 
stable. Le mortier utilisé en maçonnerie armée doit être d’une classe 
non inférieure à 50, afin d'assurer une protection efficace de l'acier 
vis-à-vis de la corrosion. 




Pour améliorer: la résistance mécanique des pièces en maçonne- 
rie d’élancement À} < 15 qui présentent une excentricité de la 
force longitudinale e, < 0,33 y, on utilise des treillis d'armatures 
(fig. VIII.3, a, b) disposés dans les joints horizontaux. Pendant le 
travail de la pièce soumise à la compression, les treillis s'opposent 
aux déformations transversales de la maçonnerie et augmentent 
ainsi sa capacité portante. | 

Les armatures longitudinales (fig. VIII.3, d) s'avèrent efficaces 
pour reporter les tractions dans une pièce simplement fléchie ou 




SSSR SACS 


FIG. VIII.3. Maçonnerie armée: 


1, maçonnerie; 2, treillis: .3, barres longitudinales; 4, cadres: 5, béton 


comprimée et fléchie à forte excentricité de la. force de compres- 
sion, ainsi que pour améliorer la résistance et la stabilité d’un mur 
mince. Les barres sont placées soit à l’intérieur de la maçonnerie, 
dans ses joints verticaux, soit dans la couche extérieure de mortier 
de ciment et réunies par-des tædres transversaux (placés dans les 
joints horizontaux). 

Parfois on utilise aussi des maçonneries composites: maçonnerie 
de pierres renforcée avec du béton armé (fig. VIII. 3, e) et maçon- 
nerie frettée (fig. VIII. 3, c). 

Les maçonneries armées de barres longitudinales et les maçonne- 
ries composites ne trouvent qu'un emploi assez restreint, car elles 
sont difficiles à exécuter. L'état de contrainte des structures en 
maçonneries de ces types est analogue à celui des structures en bé- 




ton. Les méthodes de leur calcul font l’objet de textes réglementaires 
spéciaux. 

Le type d'armature le plus employé dans une maçonnerie de 
briques et de blocs de céramique (pour une hauteur d’assise non su- 
périeure à 15 cm) est le treillis d'armatures. 

Les barres du treillis peuvent se situer en deux directions (treil- 
lis rectangulaire) ou en une seule (treillis zigzag). Deux treillis 
zigzag posés dans deux joints voisins sont équivalents à un seul 
treillis rectangulaire. Puisque l'épaisseur du joint doit être limitée, 
les barres d’un treillis rectangulaire ont un diamètre de 3 à 5 mm 
et celles d’un treillis zigzag jusqu'à 8 mm. L'’écartement des barres 
du treillis varie entre 3 et 12 cm. La distance entre deux treillis 
voisins ne doit pas être plus grande que cinq assises de briques 
{40 cm). 

La quantité d’armatures est évaluée à l’aide du pourcentage vo- 
lumique d’armatures a, rapport du volume de l’acier V, au volume 
de la maçonnerie V,,: 




Va 100. 


On voit sur la figure VIITI.3, jf que le volume de la maçonnerie 
Vu = C10Cs et celui de l'acier V, = f,C, + f,C,+. On a générale- 
ment C, = CC, = C et f1 = fs =.f, si bien que 


u = 100. (VIIL.8) 


Les Normes prescrivent Umin — 0,1 % et Umax — 1 %. 

La résistance de calcul d’une pièce en maçonnerie armée de treil- 
lis est calculée comme suit: 

— pièce simplement comprimée: 


2UR à 


Rna=R+#%2<1,8R; (VIII.9) 


— pièce comprimée et fléchie: 


2uR 2e 
Rat = R + 2e _ 2) | (VIII. 10) 


Dans ces formules R est la résistance de calcul de la maçonnerie non 
armée ; À; la résistance de calcul de l'acier des treillis. On a R, — 
— 1500 kgf/cm°? (150 MPa) pour les barres de classe A-I. Si les ar- 
matures sont fabriquées en acier de classe B-I, on prend R, © 
— 2000 kgf/cm? (200 MPa) pour d < 5,5 mm et R, — 1800 kgf/cm° 
(180 MPa) pour d > 6 mm. 

La formule (VIIT.10) permet de remarquer que plus la force 
longitudinale est excentrée, moins le treillis est efficace du point 
de vue de la résistance de la maçonnerie. Avec e, — 0,5 y, le treillis 
devient inutile (Rat = R). 




La constante élastique d’une maçonnerie armée de treillis est 


aa=@ — = a — re, (VIIL.41) 
2RT GG 


où « est la constante élastique de la maçonnerie non armée; À est 
la charge de rupture moyenne en compression de la maçonnerie non 


armée; Rm.a est la même grandeur pour la maçonnerie armée. 


En calculant Ana, on pose R; — 2400 kgf/cm? (240 MPa) pour 
les aciers de classe A-I et R; — 3500 kgf/cm* (350 MPa) pour les 
aciers de classe B-I. 

Les procédés de calcul des pièces comprimées armées de treillis 
ne diffèrent en rien du procédé employé pour une pièce en maçonne- 
rie non armée (voir $ VIII.2), sauf que À dans les formules de cal- 
cul est remplacé par RAA et que les coefficients @ (ou ®.) sont dé- 
terminés en prenant la constante élastique «&, au lieu de «&. 

C'est ainsi que la formule (VIII.{) appliquée à une pièce simple- 
ment comprimée devient 


N << m1aPFRm.a ; (VIII.12) 


de même, la formule (VIII.2) appliquée à une pièce comprimée et 
fléchie devient 


N << MmiaP1FeR mat. (VIII.13) 


$ VIIL4. LES STRUCTURES EN MAÇONNERIE 
DANS LE BATIMENT 


Un bâtiment est un système tridimensionnel dont tous les éléments 
constitutifs (murs, piliers; planchers) travaillent ensemble sous la 
charge. 

Les réactions horizontales engendrées lors de la mise en charge 
des murs et des piliers sont transmises sur les planchers qui tra- 
vaillent à la flexion dans leur propre plan, prenant appui soit sur 
les murs, soit sur d’autres structures suffisamment stables en direc- 
tion transversale. 

Si la distance entre les murs transversaux reste inférieure aux 
valeurs indiquées dans les Nouwes {), on admet que les planchers 
constituent des appuis horizontaux fixes vis-à-vis des murs et des 
piliers : on dit que l’ossature du bâtiment est rigide. Tout bâtiment à 
étages doit avoir une ossature rigide. 


1) La distance maximale entre les murs transversaux ou les autres structures 
transversales stables est déterminée en fonction du type de la maçonnerie, 
de la nature du plancher, de la hauteur du bâtiment et de la poussée cinématique 
du vent. Dans un bâtiment aux murs en briques et aux planchers en béton armé, 
cette distance peut atteindre 54 m. 




Dans un bâtiment à ossature élastique les murs et les piliers 
possèdent un appui horizontal mobile en dessus. Ce cas se présente 
dans les bâtiments industriels sans étages où les murs transversaux 
font défaut sur une grande longueur, ainsi que dans le cas où la 
couverture possède une très faible raideur dans son propre plan (hour- 
dis d'amiante posés sur madriers). 

L'épaisseur du mur est choisie de façon à assurer une isolation 
thermique suffisante. Le mur doit être vérifié à la résistance mécani- 
que. Les Normes contiennent des 
valeurs limites du rapport B de la 
hauteur À du mur (pilier) à son 
épaisseur ». Par exemple, on a 
B < 22 pour un mur portant sans 
ouvertures constitué de briques 
de classe égale ou supérieure à 50 
et de mortier de classe 25: dans 
un pilier de la même constitution 
la valeur de f est diminuée de 25 
à 40 % en fonction des dimensions 
de la section. 

Lors du calcul pour les charges 
verticales, le mur d'un bâtiment 
à étages est assimilé, dans les limi- 
tes de chaque étage, à une poutre 
verticale à simple travée articulée gg. vIII.4. Pour le calcul du mur 
en ses extrémités au niveau des en maçonnerie d’un bâtiment à 
planchers (fig. VIII.4). On admet étages multiples à ossature rigide 
que le mur subit la charge ver- 
ticale V, due au poids du plancher au-dessus de l'étage considéré, 
la charge verticale V, engendrée par le poids du mur au-dessus 
de l'étage considéré et de tous les planchers situés au-dessus, et la 
charge verticale déterminée par son propre poids V,,,. 

La charge N, présente généralement une excentricité e, relati- 
vement au centre de gravité de la section du mur et fait naître un 
moment 


M — Ne. 


La charge NV, agit suivant la droite du centre de gravité du mur 

à l'étage au-dessus. Si le mur a une épaisseur constante, la charge 
Nn ne produit aucun moment. Si l'épaisseur du mur varie, on a 


h—kh 
Em = + 2 $, 


où À est l'épaisseur du mur de l'étage considéré et h, l'épaisseur du 
mur à l'étage supérieur; 


Mn — + N men. 


Le moment total à la base du plancher est 


La section à calculer dans un mur est celle de l’entre-deux des 
fenêtres. Dans cette section le moment est un peu plus petit que M 
{voir fig. VIII.4): 

M, = MH,/H. 


L'effort normal est 
N=N, +Nn + Nan 


où Vn est le poids de la partie du mur comprise entre la base du plan- 
cher et le haut de l’entre-deux. 
L’excentricité de À est 
eo = M,/N. 


L’entre-deux est calculé en flexion avec compression d’après 
la formule VIII.2. 


$ VIIL5. EXEMPLES DE CALCUL DES PIÈCES EN MAÇONNERIE 


Exemple VIII.1. Soit un pilier simplement comprimé en maçonne- 
rie de briques de grès de classe 75 hourdée au mortier de classe 
25. Section 51 X 51 cm, longueur de flambement /, — 4,8 m. Force 
longitudinale de calcul (compte tenu du poids propre) V = 18 tf 
(180 kN). Vérifier le pilier à la résistance mécanique. 

Solution. Le Tableau VIII.1 donne R — 11 kgf/cm°. Puisque 
la section du pilier est # — 0,51 x 0,51 = 0,26 m° << 0,3 m°, la 
valeur de R doit être affectée du coefficient de comportement my — 
= 0,8, de sorte que 


R = 11 x 0,8 = 8,8 kgf/cm°. 
Le Tableau VIII.2 donne la constante élastique de la maçon- 


nerie &« — 750. 
L’élancement fictif de la pièce est 


a = de ARE = 9,4 x 1,15 — 10,6. 


Le Tableau VIII.3 donne @ = 0,87. 
La formule (VIII.1) donne-pour m4 — 1 (car k > 30 cm): 
N = FR = 0,87 x 51 x 51 x 8,8 — 19 900 kgf = 19,9 tf — 
— 199 kN, 
19,9 tf => 18 tf (199 KN => 180 kN). 
La résistance est bonne. 
Exemple VIII.2. Déterminer la capacité portante d’un pilier 


simplement comprimé en maçonnerie armée de treillis. Section 
64 x 64 cm, hauteur (longueur de flambement) {, — 5,4 m, maçon- 




nerie de briques d'argile de classe 100 hourdée au mortier de clas- 
se 50. Treillis posés de trois en trois assises de briques (s = 23 cm), 
en fil d'acier de classe B-I, diamètre 4 mm (jf — 0,126 cm°), écarte- 
ment des barres c — 6 cm dans les deux directions. 

Solution. Le Tableau VIII.1 donne À = 15 kgf/cm° (1,5 MPa); 
Fr = 0,64 X 0,64 > 0,3 m°; my = 1. 

D'après la formule (VIITI.8) 


2 2 X 0,126 
pe SE 100 = CT 100 = 0,183 % > fimin = 0,1 %. 


La formule (VIII.9) donne pour À, = 2000 kgf/cm°? 


Ra = Re = 154 EUR L 22,3 kyfem? < 1,8R. 


Le Tableau VIII.2 donne & — 1000. 
D'après la formule (VIII.11) on obtient en prenant R; — 
— 3500 kgf/cm*!: 


2R 2 X15 
D = 000 ES 76 
2R;h 2 X 3500 x 0,183 
2R + 100 An 
L'élancement fictif de la pièce est 
n_ 540, / 1000 
= To — 10. 


Le Tableau VIII.3 donne @ = 0,88. 
D'après la formule (VIII.12), en prenant m4 = 1, on obtient 


N = DFRma = 0,88 x 64 x 64 x 22,3 — 80 000 kgf — 
— 80 tf — 800 KN. 


Exemple VIII.3. Vérifier la résistance mécanique de l’entre- 
deux du mur extérieur montré sur la figure VIII.5. Hauteur d’étage 


d) ÿ ) 


P=504F\1P"I0tf  e,-19. P-10Hf 


il M: AL 
& S M,={6TF-m 
R: « 
EU LS 


FIG. VIII.5. Pour l'exemple VIII.3: 


a, vue en élévation du mur; b, schéma des charges; c, diagramme des moments 


4,2 m, distance entre le haut de l’entre-deux et la base du plancher 
50 cm, épaisseur du mur k — 51 cm, largeur de l’entre-deux b — 


10—0948 145 


— {120 cm, profondeur d'encastrement de la dalle de plancher dans 
le mur a — 20 cm. Blocs de céramique à fentes de classe 100, mortier 
de classe 25. Charges de calcul: poids des étages supérieurs P = 
— 50tf, poids du plancher au-dessus de l'étage considéré P, = 
— 10 tf, poids de la partie du mur située au-dessus des fenêtres 


Q, — | ti. 
Solution. Cherchons l’excentricité de P,: 


er S= À = 25,5—6,7—18,8cm & 19cm. 


Moment fléchissant de calcul agissant à la base du plancher 
M = P,e, = 10 X 0,19 = 1,9 tf-m. 
Moment au niveau de la tranche supérieure de l’entre-deux 
M,=M #=1,9 27 —1,67tf.m. 
Force longitudinale de calcul agissant dans la section choisie 
N,=P+P, +0, = 50 + 10 + 1 = 61 tf. 
Excentricité 


_ Mi 1,67 : 
=, — Gi = 0,027 m — 2,7 cm. 


Résistance de calcul à la compression de la maçonnerie À — 
— 13 kgf/cm? (voir Tableau VIII.1); «& = 1000 (voir Tableau 
VIIL.2); M = À = 8,2; @ æ 0,92 (voir Tableau VIIL.3). 
D'après la formule (VIIL.3) 
h o1 
Fe=2b (5— 69) =2 x 120 (5 —2,7) — 5470 cm?. 
D'après la formule (VHII.5) 


e 2,7 
© = 1 + — 1 dos ET — 1,035. 


D'après la formule (VIII.6) 
P, = P | 1 — 52 (0,064 — 0,2) | — 


— 0,92 [ 1— 27 (0,06x 8,2— 0,2) | — 0,905. 
On prend mia = 1, car k > 30 cm. 
Vérifions la résistance par la formule (VIII.2): 
N< miapiFeRO ; 
61 000< 1 X 0,905 x 5470 x 13 x 1,035; 
61 000 < 66 500. 


La résistance est bonne. 




CHAPITRE IX 
STRUCTURES MÉTALLIQUES 


$ IX.4. MATERIAUX DES STRUCTURES MÉTALLIQUES 


Les structures métalliques sont fabriquées le plus souvent en acier. 
L'acier doit avoir une résistance mécanique suffisante, être assez 
plastique, se souder bien et résister aux sollicitations dynamiques 
sans se rompre en mode fragile. Dans les cas où il est important de 
réduire sensiblement la masse de l'ouvrage et améliorer la tenue à 
la corrosion, on utilise les alliages d'aluminium. 

Les propriétés de l'acier sont déterminées par sa composition 
chimique et par la technologie de son élaboration. Le carbone amé- 
liore la résistance mécanique mais nuit à la plasticité et à la sou- 
dabilité de l’acier. Pour cette raison les structures utilisées en 
bâtiment sont fabriquées en acier à bas carbone (teneur en C non supé- 
rieure à 0,22 %). 

L'introduction de certains éléments tels que le manganèse, le 
silicium, le cuivre, le nickel, le chrome, etc. permet d'augmenter 
la résistance mécanique de l'acier sans diminuer beaucoup sa plas- 
ticité. Les aciers additionnés de ces éléments sont appelés aciers 
faiblement alliés. 

Certains types d'acier peuvent être rendus plus résistants par 
un procédé appelé durcissement thermique. 

Les impuretés présentes dans l'acier exercent une influence né- 
gative sur ses qualités : le soufre rend l’acier cassant à haute tem- 
pérature (fragilité au rouge), le phosphore, à basse température 
(fragilité au bleu). La teneur en impuretés est strictement limitée. 

D’après la technologie d'élaboration, on distingue l'acier effer- 
vescent (symbole Ku), l'acier semi-calmé (nc) et l'acier calmé (cu) 
(pour les aciers à bas carbone). 

L'acier effervescent est coulé immédiatement en lingotière: le 
dégagement gazeux n'a pas le temps de se terminer, si bien que Île 
métal solidifié renferme une certaine quantité de bulles de gaz qui 
nuisent à sa qualité. «» 

Les aciers calmés sont obtenus en retardant légèrement la coulée 
en lingotière (le temps de retard est plus bref dans le cas des aciers 
semi-calmés): l’absence des bulles de gaz augmente la fiabilité du 
travail de l'acier au sein de la structure, surtout vis-à-vis des sol- 
licitations dynamiques et des basses températures. 

Les aciers faiblement alliés sont toujours calmés. 


10* 147 


La résilience de l’acier caractérise sa fragilité. Elle est évaluée 
en mesurant le travail dépensé pour détruire une éprouvette spé- 
ciale (à entaille) par le choc. L’acier est d'autant moins fragile 
que sa résilience est plus élevée. 

La résistance mécanique et les propriétés de déformation de 
l’acier sont mises en évidence par l'essai de traction. 

La figure IX.1 donne les diagrammes de traction (relation entre 
Ghglon2(MPa) " une o et la déformation 

d'un acier à bas carbone (cour- 
be 1) et d’un acier dur (courbe 2), 

Les grandeurs caractéristiques 
de la résistance sont la lJinite 
d'élasticité os et la charge de rup- 
ture en traction o.. 

Pour les aciers dont le diagram- 
me de traction a la forme de la 
courbe 2? de la figure IX.1, on 
D retient comme limite d'élasticité 
02% 6% conventionnelle 6,, la contrainte 
FIG. IX.1. Diagrammes detraction Qui fait naître un allongement 

des aciers : résiduel de 0,2 %. 
1, acier à bas carbone: 2, acier dur Pour les contraintes très infé- 
rieures à la limite d'élasticité, 
la relation entre la contrainte et la déformation est définie par la 
loi de Hooke: 


O = &ËE, 


où Æ est le module d’élasticité de l'acier égal à 2 100 000 kgf/cm° 
(210 O00 MPa). 

L’allongement relatif de rupture e. permet d'évaluer la plasticité 
de l'acier. » 

Les aciéries garantissent soit les qualités mécaniques (aciers du 
groupe À), soit la composition chimique (groupe D), soit les caracté- 
ristiques mécaniques et la composition chimique à la fois (grou- 
pe B). Pour les structures sollicitées, on utilise généralement les 
aciers du groupe B. 

Les aciers faiblement alliés appartiennent toujours au groupe B. 

Les principales caractéristiques des aciers sont spécifiées dans 
les Normes correspondantes. . 

La désignation d’une nuance d'acier comprend: 

— une lettre désignant le groupe de livraison (5 ou B); 

— la désignation symbolique de la nuance (Cr3, 18T...); 

— l'indication du mode d'élaboration (Km, cm ou nc); 

— un chiffre indiquant la catégorie de résilience. 

Par exemple: BCräncs, B18lncs5, BCr 3Kn2, etc. 

Une nuance d'acier faiblement allié est désignée autrement. 
La désignation commence par un chiffre qui indique la teneur en 
carbone en centièmes de pour cent. Viennent ensuite des lettres 




codes des éléments d'’alliage: T pour le manganèse, C pour le sili- 
cium, I pour le cuivre, H pour le nickel, X pour le chrome, etc. Si 
une teneur quelconque dépasse 4 %, la lettre correspondante est 
suivie d’un nombre qui indique la teneur en pour cent arrondie au 
nombre entier. Par exemple, la désignation 15XCHIT correspond 
à un acier contenant 0,15 % de carbone et allié au chrome, nickel 
et cuivre en quantité non supérieure à 4 % pour chaque élément 
d'alliage; l’acier 1472 contient 0,14 % de carbone et jusqu’à 2 % 
de manganèse. 

Les Normes et Règles du bâtiment fixent pour la totalité des 
aciers trois classes de résistance (ou classes d'acier) en fonction du 
comportement à la traction (Tableau IX.1). La désignation d’une 


TABLEAU IX.1 
Classes des aciers utilisés en bâtiment 


Caractéristiques en traction 


ue 0» Ket/em? (MPa) | og, kgt/em? (MPa) | Allongement relatif 
r’ 0 
Valcurs minimales 
C 38/23 3800 (380) 2300 (230) 25 
C 44/29 4400 (440) 2900 (290) 21 
C 46/33 4600 (440) 3300 (330) 21 
C 52/40 5200 (520) 4009 (400) 49 
C 60/45 6000 (600) 4500 (450) 16 
C 70/60 7000 (700) 6000 (600) 12 
C 85/75 8500 (850) 7500 (750) 10 


classe se compose de la lettre C et d’une fraction dont le numérateur 
contient la valeur minimale (d’après GOST correspondant) de la 
charge de rupture 6. en kgf/mm* et le dénominateur, la valeur mini- 
male de la limite d’élasticité o4 en kgf/mm°. 

Chaque classe couvre plusieurs nuances. Ce sont les Normes 
qui guident le choix des nuances d'acier en fonction du type de la 
structure et de l’ouvrage, des conditions d'utilisation, et aussi en 
fonction de la température d'utilisation au-dessous de 0° éventuelle. 
Par exemple, pour les structures soudées des planchers et des cou- 
vertures à t > —30 °C les Normes recommandent dans la classe 
C 38/23 les nuances BCr3nc6, BCr3lnce5, B18lnc5; dans la class® 
C 44/29 la nuance CrTuc; dans la classe C 46/33 la nuance 1472, etc. 

Si la structure est conçue pour être exploitée dans un milieu 
agressif, il convient de prévoir un revêtement protecteur convenable 
pour éviter la corrosion. 

La résistance caractéristique ÀC de l’acier en traction, en com- 
pression et en flexion est prise égale à la valeur minimale contrôlée 


149. 


de la limite d'’élasticité (pour les aciers dont le diagramme de trac- 
tion possède un palier d'écoulement) ou à la valeur minimale con- 
trôlée de la charge de rupture (pour les aciers sans palier). La résis- 
tance de calcul en traction, en compression et en flexion est définie 
par la relation 


R = Rk, 


où kÆ est un coefficient de sécurité dépendant du matériau. 

On a 4 — 1,1 à 1,2 si la résistance caractéristique est définie 
par la limite d’élasticité et À — 1,45 à 1,6 si elle est prise égale à la 
charge de rupture. 

La résistance de calcul au cisaillement et à l’écrasement de la 
face en bout est obtenue en multipliant À par un coefficient de 
transition: Reis = 0,6 R, Rer = 1,5 R. 

Pour les structures qui peuvent être exploitées au-delà de la 
limite d’élasticité du métal (tels que les tubes et les réservoirs où 
les tractions dans le métal sont engendrées par la pression intérieu- 
re), on retient des résistances de calcul à la traction plus élevées: 
2600 kgf/cm? (260 MPa) pour la classe C 38/23, 3000 kgf/cm? 
(300 MPa) pour C 44/29, etc. 

Pour certaines pièces la valeur de À indiquée dans le Tableau 
I1X.2 doit être multipliée par un coefficient de comportement m < 1. 


TABLEAU 1IX.2 
Résistance de calcul de certains profilés d’acier 
Résistance de calcul, kgf/cm2 (MPa) 
Classes d'acier 


C 38/23 | C44/29 | C 46/23 | C 52/40 


Cas de charge 


Traction, compression, | 2100 (210) | 2600 (260) | 2900 (290) | 3400 (340) 
flexion R 


Cisaillement Reis | 1300 (130) | 1500 (150) | 1700 (170) | 2000 (200) 


Par exemple, on pose m = 0,9 pour les poutres pleines et les élé- 
ments comprimés des fermes des planchers des bâtiments publics 
où le poids des planchers’est plus grand que les surcharges prévues, 
pour les poteaux des immeubles d'habitation et des bâtiments pu- 
blics, pour les pylônes des châteaux d’eau ; »7 = 0,75 pour les pièces 
comprimées en cornières isolées attachées par une seule aile, etc. 

L'acier pour les structures est produit sous forme de profilés 
laminés: tôles, bandes, profilés en double T et en U, cornières à 
ailes égales et inégales, tubes, etc. Les catalogues des profilés con- 
tiennent toutes les données sur les sections: dimensions, aire de 
section, moments d'inertie, modules de résistance, rayons de gira- 




tion, ainsi que la masse de 1 m de longueur du profilé. Les Anne- 
xes X, XI, XII, XIII contiennent quelques extraits du catalogue. 

Le projeteur doit chercher à réduire autant que possible la 
gamme des profilés utilisés. 

Les alliages d'aluminium peuvent contenir du manganèse (alliage 
AM), du magnésium (AMr), du magnésium et du silicium (AB, AJI), 
du cuivre et du magnésium (J{). Ces éléments d’alliage confèrent au 
matériau une résistance mécanique comparable à celle des aciers 
tout en conservant une masse volumique trois fois plus petite (y Æ 
Æ 2600 kgf/m°). Par contre, les alliages d'aluminium sont beau- 
coup plus onéreux que l’acier et résistent moins bien aux déforma- 
tions : leur module d’élasticité est Æ — 710 000 kgf/cm° (71 000 MPa), 
donc trois fois moindre que celui de l'acier. Tous ces facteurs dé- 
terminent un domaine d'application particulier des alliages d’alu- 
minium (voir l’Introduction). 

Les profilés en alliages d'aluminium sont produits soit par lami- 
nage (tôles, bandes), soit par filage: cornières, profilés en U et en 
double T (selon un catalogue spécial), tubes, profilés en caisson. 
Les ailes des cornières et des profilés en double T et en U sont munies 
de « boudins » à leur bord, qui améliorent la stabilité locale de 
l’aile. 

Les caractéristiques des alliages d'aluminium et leurs résistances 
de calcul sont indiquées dans les Normes appropriées. 


$ IX.2. ASSEMBLAGE DES PIÈCES DANS LA STRUCTURE 
MÉTALLIQUE 


Joints soudés 


Le procédé principal d'assemblage des pièces en acier est la soudure 
à l’arc électrique à l’électrode fusible. L’arc électrique amorcé 
entre la pièce et l’électrode fait fondre le métal de l’électrode et 
celui de la pièce; les deux métaux mélangés en phase liquide se 
solidifient ensemble. 

En plus du soudage manuel, on utilise le soudage mécanisé 
automatique ou semi-automatique. Pour protéger le métal liquide 
contre l’action nuisible de l'air ambiant, les électrodes utilisées 
au soudage manuel sont munies d’un enrobage qui forme une couche 
de scorie protectrice à la surface du cordon de soudure (électrodes 
942, 942A, 950A, etc.). Au soudage mécanisé l’électrode est nue, 
tandis que la protection du cordon est assurée par une couche de 
flux (laitier granulé) appliquée par la soudeuse automatique en amon 
de l’électrode. Parmi les méthodes plus récentes, on peut citer le 
soudage à l’arc électrique sous gaz protecteur (CO,). Les Normes re- 
commandent différents types de matériaux employés au soudage 
(électrodes, flux, métal d'apport) pour chaque classe d’acier en 
fonction de la catégorie de la structure, de la température et de 
la technologie du soudage. 




Les alliages d'aluminium sont soudés sous atmosphère d’argon. 
Les électrodes fusibles sont utilisées seulement pour les épaisseurs 
supérieures à 6 mm. Si les pièces à assembler sont plus minces, 
on emploie une électrode réfractaire dont le rôle se réduit à l’amor- 
cage de l’arc, tandis que le cordon de soudure est formé à partir 
d’un fil d'apport fusible qu’on introduit dans l’espace entre la 
pièce et l’électrode. 

D'après la construction du joint, on distingue les cordons bout 
à bout (fig. IX.2, a) destinés à assembler les pièces situées dans un 


FIG. IX.2. Différents types de cordons de soudure et de joints soudés 


même plan (le métal apporté remplit l’espace entre deux pièces), 
et les cordons d'angle (fig. IX.2, b) réalisés dans l'angle formé par 
les pièces. Le cordon bout à bout permet de réaliser un joint simple 
et efficace; or, dès que l'épaisseur Ô devient supérieure à 8 mm, on 
est obigé de préparer convenablement les bords des pièces. Un cordon 
d’angle normal a une section en forme de triangle isocèle !) dont le 
côté long présente un bombement égal au dixième de la longueur du 
côté court À. 

L’épaisseur théorique d’un cordon bout à bout est égale à l’épais- 
seur des pièces à assembler ô. L'’épaisseur théorique d'un cordon 
d’angle est égale à BA,, où B est un coefficient dépendant du procédé 
de soudage: on a B — 0,7 au soudage manuel et f = 0,7 à 1 au 

1) Sur les structures en acier à haute résistance sollicitées par des charges 
dynamiques et des vibrations et exploitées dans les conditions de basses tempéra- 
tures, on réalise des cordons à pente plus douce (rapport des côtés 1 : 1,5). 




soudage semi-automatique et automatique, en fonction du nombre 
de passes. La longueur théorique du cordon !, est prise égale à sa 
longueur totale / diminuée de 1 cm afin de tenir compte d’une péné- 
tration incomplète éventuelle aux extrémités, Z, — ! — 1 cm. 

On distingue quatre types principaux des joints soudés : 

— le joint bout à bout: les pièces à assembler sont situées dans 
un même plan et réunies par un cordon bout à bout (fig. IX.2, c); 

— le joint bout à bout avec couvre-joint : le couvre-joint est fixé 
sur les pièces à réunir par des cordons d'angle (fig. IX.2, d); 

— le joint à recouvrement: les pièces à réunir sont posées l’une: 
sur l’autre et assemblées par des cordons d'angle (fig. IX.2,e); 

— le joint en T : les pièces sont assemblées en forme de T et réu- 
nies par des cordons d'angle (fig. IX.2, f). 

La résistance mécanique d’un cordon de soudure est évaluée 
à l’aide de sa résistance de calcul RS (Tableau IX.3). 

Les cordons bout à bout sont calculés à l’aide de la formule 


ER», (IX.1) 


où Ÿ est la force longitudinale de calcul; RS la résistance de calcul 
du cordon bout à bout ; Z. la longueur théorique du cordon; à l'épais- 
seur théorique du cordon. 

Les cordons d'angle sont calculés d’après la formule 


ER: (IX.2} 


Bhele "=" an? 


où BA, est l'épaisseur théorique du cordon d’angle; Rin la résis- 
tance de calcul du cordon d'angle. 

Exemple IX.1. Calculer un joint bout à bout avec deux couvre- 
joints (voir fig. IX.2, d) et déterminer la longueur nécessaire des. 
couvre-joints 2. Acier de classe C 38/23, épaisseur des couvre- 
joints 8, largeur 160 mm. Effort de traction de calcul N — 80 tf — 
— 800 KkN. 

Solution. Le Tableau IX.3 donne Rin — 1500 kgf/cm°. Ad- 
mettons que l'épaisseur des cordons sera égale à celle des couvre- 
joints, k = 0,8 cm. La formule (IX.2) permet de définir la longueur 
nécessaire des cordons sur chaque moitié des couvre-joints en posant 
B = 0,7: 


Le = Gare TOO TN UE — 94cm. (IX. 


Puisqu'on a deux couvre-joints, les cordons à poser sur chaque 
couvre-joint auront comme longueur . \ 


LL = 94/2 = 47 cm. a 


“X suoui) onbisAd 2apodigu sun ded 91npnos e[ »p 9[01ju09 un,p IAINS 750 (onbrewomne ‘onbrewogmne-tmos ‘[mueu) oSepnos al IS 7 


(022) 0022 (UOZ) 000 (085) 0081 (0G+) 0061 Cu WP] o[auu,q 


(00Z) 000% (OLF) 0021 (0GF) 00SF (O£E) 00€: So JUOWATTIESIT) wopl 


I (enbremoyne-1fuos 38 


_ (06) 0062 (0G&) 0072 (085) 0087 My | jonueur o8epnos) uoTJo81L UP] 
(0F£) O)F£ (062) 0062 (092) 0092 (072) 0012 y | uotsso1dw0" qnoq e 1n0g 
0%/26 9 £e/9% 9 62/%% 9 CGI8E 9 
9[0QuUÂS uol1)8}191[10S uopi09 np odÂL 


J0100,P SOSSUI9 So] ANnOd QU 1N90[89 9P 99UESIS9H 


(C4W) :w9/j54 ‘sy einpnos 9p suop109 SIp [N[U9 9p 9JUCISISIY 


F'XI AVATAVI 


1954 


Pour un couvre-joint large de 16 cm, la longueur des cordons 
posés le long de la moitié de couvre-joint sera égale à (47 — 16)/2 — 
— 195,5 cm; compte tenu de la pénétration incomplète aux extrémi- 
tés, on obtient 15,5 + 1 — 16,5 cm. 

Compte tenu d’un espace libre de 1 cm laissé entre les tôles à 
assembler, la longueur totale des couvre-joints sera donc 


Li = 2 x 16,5 + 1 = 34 cm. 


Joints rivés et boulonnés 


Les assemblages par rivets (fig. [X.3, a) sont assez peu répandus. 
On utilise les rivets pour assembler les pièces des structures soumises 
aux sollicitations dynamiques, ou bien les pièces en acier ou en 




TEL ZZZ 
ZAVIZ 


FIG. IX.3. Joints rivés et joints boulonnés: 
1, cisaillement; 2, écrasement 


alliage d'aluminium qui se soudent mal. Les assemblages par bou- 
lons (fig. [X.3, b) sont employés généralement pendant le montage 
des structures. On distingue les boulons bruts, ou normaux (fabriqués 
par emboutissage d’une barre d'acier), et les boulons de précision, 
ou ouvrés (exécutés au tour suivant le diamètre du trou). 

Les trous recevant les rivets ou les boulons peuvent être obte- 
nus par poinçonnage à la presse (groupe C) ou forés (groupe B). 
En règle générale, les rivets et les boulons bruts sont mis dans les 
trous poinçonnés et les boulons ouvrés dans les trous forés. « 

Les rivets et les boulons travaillent au cisaillement suivant 
la ligne de jonction des pièces à assembler, et à l’écrasement suivant 
les surfaces latérales (fig. IX.3, c, d). La surface de cisaillement est 
prise égale à la section du rivet (boulon), et la surface d’écrasement, 
au diamètre d du rivet (boulon) multiplié par la plus petite épaisseur 
totale des pièces ZÔ subissant l’écrasement en un sens quelconque. 




Les rivets et les boulons sont calculés d’après les formules sui- 
vantes : 
au cisaillement 




: nd? < Rois (IX .4) 
nfoeis De 
à l’écrasement 
55 < Récr- (IX.5) 


Dans ces formules ŸV est la force longitudinale de calcul exercée sur 
le joint ; 2 le nombre de rivets (boulons) dans le joint ; »;, le nombre 
de plans de cisaillement sur un rivet (boulon) ; Reis et Récr les résis- 
tances de calcul au cisaillement et à l'écrasement qui dépendent 
de la nuance de l’acier du rivet (boulon), de celle des pièces à assem- 
bler, et de la catégorie des trous (groupe C ou groupe B). 

Les rivets en acier Cr? ont la résistance de calcul au cisaillement 
Reis — 1800 kgf/cm* dans les trous du groupe B et 1600 kgf/cm° 
dans les trous du groupe C; les boulons bruts ont la résistance de 
calcul au cisaillement Rec, — 1500 kgf/cm°?. Les rivets en acier 
C 38/23 ont la résistance de calcul à l'écrasement R4. — 4200 kgf/cm? 
dans les trous B et 3800 kgf/cm°? dans les trous C. Dans un joint 
boulonné avec un grand nombre de boulons Réer — 3400 kgf/cm*. 

Un assemblage particulièrement efficace est procuré avec des 
boulons à haute résistance. Un effort de tension considérable appliqué 
suivant les plans de joint fait naître des forces de frottement sus- 
ceptibles de reporter des efforts de cisaillement très élevés. Les bou- 
lons à haute résistance peuvent être posés dans des trous dont le 
diamètre est de quelques millimètres supérieur à celui du boulon, 
ce qui facilite grandement le montage. 

L’effort de calcul reporté par chaque surface de frottement (à la 
suite du serrage d’un boulon isolé) est 


N} —= Pfm, 


où } est le coefficient de frottement défini par le mode de préparation 
des surfaces et de la nuance de l'acier, f — 0,25 à 0,55; m le coef- 
ficient de comportement égal à 0,9; P le renforcement axial de la 
tension du boulon, 2 

P = 0,650,F,t: 
ici 6. est la charge de rupture du boulon à haute résistance, 6, — 
— 8000 à 13 500 kgf/cm° (800 à 1350 MPa) ; Fh+ la section du bouloi. 
après déduction de l’épaisseur du filetage. 

L'écartement des rivets (boulons) dans le joint (entraxe) est 
pris égal à 3 d. La distance entre l’axe du rivet (boulon) extrême et 
le bord de la pièce est égale à 2 d dans le sens de l'effort et à 1,5 d 
en travers de l'effort. 




$ IX.3. CONCEPTION ET CALCUL DES POUTRES 


Les poutres d'acier sont généralement constituées par des profilés 
en double T, ou poutrelles, qui présentent une bonne raideur à la 
flexion dans le plan de l'âme; on utilise parfois aussi des profilés 
en Ü. Quand les portées et les charges sont élevées, on emploie des 
poutres composées, le plus souvent soudées en forme de double T à 
partir de trois tôles: une âme et deux membrures. 

D'après le schéma statique, on distingue les poutres continues, 
des poutres à travées LbéEr ui et des poutres cantilever (consoles). 


de à 


TL SIM 


Cd LC 


RINANINIENNNNNS 




22273 2227777} SISSSSS SI ST) 




N L| 


Gossiorererrersr rs: SSI SI NT 


FIGs 1X.4, Ossature de poutres: 
1, revêtement du plancher (dalles, platelage); 2, poutres d'étage; 3, solives 


Ce‘’sont les poutres à travées indépendantes qu'on utilise le plus 
souvent, en raison de la facilité de fabrication et de montage, bien 
qu’elles entraînent une dépense d'acier plus grande que les poutres 
continues. 

Les poutres supportant le plancher forment un système appelé 
ossature de poutres. Les poutres qui transmettent le poids du plancher 
aux appuis (murs, poteaux) sont appelées poutres d'étage; les pou- 
tres auxiliaires reposant sur les poutres d'étage et supportant"le 
revêtement du plancher sont appelées solives (fig. IX.4). Le revête- 
ment du plancher peut être constitué soit par une dalle en béton armé 
coulée en place ou des hourdis préfabriqués en béton armé, soit par 
des tôles d'acier soudées sur les poutres (platelage). L’ossature de 
poutres doit être étudiée en fonction du quadrillage de poteaux 
existant, de la configuration des ouvertures dans le plancher, de 




l'encombrement des équipements (machines), de la hauteur cons- 
tructive admissible du plancher, sans oublier les considérations 
d'ordre économique: la résistance mécanique et la raideur requises 
doivent être assurées au prix d’un investissement minimal. 

Les solives peuvent être posées directement sur les poutres 
d'étage (fig. IX.5, a), surélevées (fig. IX.5, b), de niveau avec les 


a) b) 


FIG. IX.5. Attache des solives sur la poutre d'étage 


poutres d'étage (fig. IX.9, c) ou surbaissées (fig. IX.5, d). La pre- 
mière solution est la plus simple, mais elle nécessite la plus grande 
hauteur constructive du plancher. Si les solives sont posées de niveau 
avec les poutres d'étage, la dalle du plancher peut être appuyée sur 
les quatre bords. Les solives surbaissées s'avèrent avantageuses 
pour supporter des dalles épaisses. 

Les poutres sont calculées à la résistance mécanique, à la défor- 
mation (en flexion), et parfois aussi à la stabilité (au flambement). 

La résistance mécanique d’une poutrelle doit être vérifiée sui- 
vant les seules contraintes normales. En effet, la résistance aux 
contraintes tangentielles et principales est garantie par la répartition 
judicieuse du métal dans la section du profilé et n’est presque jamais 
vérifiée par le calcul. 

Le calcul de la résistance mécanique d’une poutre consiste à 
déterminer les contraintes normales aux bords de la section qui 
subit le plus grand moment fléchissant provenant des charges de 
calcul exercées sur la poutre. Ces contraintes ne doivent pas dépasser 
la résistance de calcul À (fig. T'X°6, a): 


MWa<R, (IX.6) 


où À est le moment fléchissant dû aux charges de calcul ; À la résis- 
tance de calcul du métal; W,: le module de résistance de la section 
nette, c’est-à-dire après déduction des trous (s'ils existent). 

Pour les poutrelles, on cherche la valeur de W dans le catalogue 
des profilés. Pour une poutre composée, on calcule d’abord le moment 
d'inertie de la section J, puis on obtient W —J/y, où y est la dis- 




tance du centre de gravité de la section au bord le plus éloigné. 
Si la section est symétrique, on a y — h/2. 

La flèche de la poutre est déterminée pour les charges caracté- 
ristiques en fonction de la portée /, de la distribution des charges et, 


Poutre deversee 


FIG. 1X.6. Pour le calcul des poutres d’acier: 


1, âme; 2, membrure; 3, raidisseurs 


de la raideur £J de la poutre. Pour une poutre à simple travée sup- 
portant une charge aq° uniformément répartie 


f ___ ogcii 
Max 7 384EJ ? 


et pour une poutre à simple travée dont chaque tiers de la portée: 
subit des efforts concentrés P 
23 PI 


Îmas = 56 57 . 


Les Normes définissent les valeurs limites de la flèche relative, 
c'est-à-dire du rapport de la flèche f à la portée Z de la poutre. Par: 
exemple, on a f/1< 1/400 pour les poutres d'étage dans les planchers. 
et f/1< 1/250 pour les solives. 

Si la membrure comprimée de la poutre n’est pas fixée en travée, 
la poutre risque de céder au flambement : il se produit alors le déver- 


159: 


sement, et la poutre s’écarte de son plan de flexion (fig. IX.6, b). 
La diminution de la capacité portante de la poutre à cause du flam- 
bement est prise en compte dans le calcul en introduisant dans la 
formule (IX.6) un coefficient de réduction @, << 1 qui dépend de la 
hauteur de section, de la portée de la poutre, de la distribution de 
la charge ; les valeurs de œ sont indiquées en Annexe XIV. 

Les diminutions locales de la section n'’affectent pas la charge 
critique de flambement, aussi la formule de calcul contient-elle le 
module de résistance de la section brute W,, (sans déductions). La 
formule en question se présente donc comme suit: 


x B. (IX.7) 

La stabilité de la poutre est considérée comme garantie et n’a 
pas à être vérifiée par le calcul dans les cas suivants: 

— la membrure comprimée supporte un revêtement rigide (dal- 
les en béton armé, platelage en tôles plates ou ondulées, etc.) qui 
transmet une charge statique répartie sur la poutre; 

— ]a poutre soudée en T à membrure supérieure chargée présente 
un rapport de la longueur libre /, de la membrure comprimée à sa 
largeur bn non supérieur à 13—17. 

Ces deux conditions se trouvent respectées dans la plupart des 
Cas ; le calcul au déversement ne se fait donc que pour les poutres 
dont la membrure comprimée reste libre (non fixée) sur une lon- 
gueur considérable: le monorail, les poutres de roulement d'un 
pont roulant, etc. 

La résistance mécanique d’une poutre soumise à une charge sta- 
tique et présentant une bonne stabilité vis-à-vis du flambement 
peut être calculée par la méthode de la rotule plastique: après que 
les contraintes dans les fibres extrêmes ont atteint des valeurs limi- 
tes, la poutre reste encore susceptible de supporter une charge grâce 
à la marge de résistance des fibres éloignées du bord. La capacité 
portante de la poutre ne sera épuisée qu’au moment où les contrain- 
tes atteindront leurs valeurs limites en tout point de la section 
(fig. IX, 6, c). 

À l'état de contrainte décrit correspond un module de résistance 
dit plastique WPl. La formule IX.6 devient alors 


— MIWn'< R, (IX.8) 


avec WPrl — 2S< 1,2 W, où S est le moment statique de la demi- 
section par rapport à l’axe passant par le centre de gravité de la sec- 
tion. 

Pour un profilé en double T et en U 


Wri = 41,12 W: (IX.9) 


pour une poutre soudée en double T symétrique formée de trois 
tôles (fig. [X.6, d) 


Ô: nef 
Wei GR (bnôn+ Te) (IX.10) 


La section de la poutrelle à utiliser est choisie comme suit. 
On calcule d’abord le moment fléchissant A7, puis on détermine le 
module de résistance nécessaire soit par la formule (IX.6), soit 
(si la poutre peut être calculée par la méthode de la rotule plastique) 
par la formule (IX.8). Ensuite on choisit un profil convenable dans 
le catalogue, on le vérifie en trouvant la valeur de J, en calculant 
la flèche et en la confrontant avec la flèche admissible. 

La section à donner à la poutre soudée en trois tôles est choisie 
autrement. D'abord on calcule le module de résistance requis à l’aide 
de la formule (IX.6), puis on trouve la hauteur de section optimale 


où Ôame est l'épaisseur de l'âme en cm. 

En déterminant h, il convient de se donner à priori une épaisseur 
de l’âme entre 8 et 10 mm pour la vérifier ensuite au cisaillement sous 
l’action de l'effort tranchant (sans tenir compte de la résistance des 
membrures) au moyen de la formule 


- 54 Qmax 
Oame > 1,9 Reish 6° (IX.12) 

En choisissant l'épaisseur à donner à l'âme de la poutre, il con- 
vient de prévoir des nervures de raidissement transversales dès que 


le rapport */ôame devient supérieur à 100 fois 20, 


autrement 


l'âme risque de céder au flambement 1). 

La section tout entière doit présenter un moment d'inertie 

J = Wh/2, (IX.13) 

La section de l’âme étant déjà connue, on détermine le moment 
d'inertie des membrures : 
On me/® 


Le moment d'inertie des membrures par rapport à l’axe d’inertie*” 


central de la poutre (sans tenir compte des moments d'inertie par 
rapport à leurs axes propres, qui sont négligeables) est égal à 


T2 (2). 


Tim = — Jaime — J — 


(IX.14) 


1) Si la membrure est exposé à une charge roulante, les raidisseurs devien- 
nent nécessaires à partir de k/6,,, > 701 2100/R. 


11—0948 161 


D'où l'on déduit la section à donner à chaque membrurec 


Fa = 27 (IX.15) 


RkR? 


Connaissant Fn, on dimensionne la section de la membrure 
en lui donnant une largeur b, de trois à cinq fois inférieure à et 
une épaisseur ÔÜmn — lm/0m- 

D'après ces éléments on dessine la section de la poutre, on cal- 
cule son moment d'inertie J et son module de résistance WW, puis on 
la vérifie à la résistance mécanique conformément à la formule 
(IX.6) et l’on détermine la flèche. 

Les raidisseurs (fig. IX.6, d) sont disposés à l’aplomb des ap- 
puis et aux droits des charges concentrées; dans les intervalles, ils 
seront espacés de 2 À au maximum si X/ôame >> 100 ou de 2,5 h au 
maximum si A/ôgme 100. 

L'épaisseur de la nervure de raidissement 6,. ne doit pas être 
inférieure au 1/15 de sa largeur b,, Æ b}/2. Les nervures avec les 
parties adjacentes de l’âme longues de 15 ônme des deux côtés doi- 
vent être vérifiées par un calcul supplémentaire à la façon des mon- 
tants comprimés soumis à une réaction d'appui. 

On se dispense de vérifier au flambement l'âme d'une poutre 
composée quand }/ôgme < 110 VW 2100/R ; en présence d'une con- 
trainte locale (provenant d’un effort appliqué entre deux raidis- 
seurs), le calcul au flambement devient inutile quand on a R/ôgme< 
< 80 V/2100/R. 

Les cordons de soudure reliant les membrures à l’âme doivent 
être calculés pour résister à la force de cisaillement 7 qui se mani- 
feste pendant la flexion de la poutre: 


- Te, (IX.16) 


où Q est l'effort tranchant de calcul; S,, le moment statique de la 
section de la membrure par rapport à l’axe neutre de la poutre; J le 
moment d'inertie de la section entière de la poutre. 

La force de cisaillement en question sera reprise par deux cor- 
dons d’angle, de sorte que 


7 Th Rin, 


d'où 


ho >> 100 >, 6 mm. (IX.17) 


Une poutre composée ne peut être calculée par la méthode de 
la rotule plastique que si elle est particulièrement bien garantie 
vis-à-vis du flambement. Pour que cette condition soit respectée, 




il faut que le rapport de la longueur libre /, de la membrure com- 
primée à sa largeur b,, soit compris entre 9 et 12 au maximum, le 
rapport de la largeur de porte-à-faux de la membrure comprimée 


à son épaisseur soit non supérieur à 10 V 2100/R et le rapport de la 
hauteur de l'âme à son épaisseur (en présence des seuls raidisseurs 


transversaux) soit non supérieur à 70 V 2100/R. 

Exemple IX.2. Calculer la poutre porteuse d’une plate-forme 
de travail confectionnée à partir d’une poutrelle d’acier de portée 
l = 4,6 m; écartement entre les poutres 2,2 m. Les poutres portent 
des hourdis préfabriqués en béton armé de 8 cm d'épaisseur et un 
carrelage céramique posé sur une couche de mortier de ciment de 
4 cm d'épaisseur totale. Surcharge caractéristique sur la plate- 
forme 400 kgf/m°, coefficient de surcharge »? — 1,2. Flèche relative 
admissible f/1 — 1/250. Matériau: acier de classe C 38/23. 

Solution. On admet qu'il s’agit d’une poutre à simple travée 
supportant une charge uniformément répartie. Recensement des 
charges: 

— poids des hourdis 


0,08 x 2500 — 200 kgf/m°? (2 kKN/m°); 


— poids de la structure du revêtement 
0,04 x 2000 — 80 kgf/m°? (0,8 kN/m°): 


— poids propre (approximatif) de la poutre 30 kgf/m (0,3 kN/m) 
— charges caractéristiques sur 1 m de longueur de la poutre: 
charge permanente 

ge = (200 + 80) 2,2 + 30 = 646 kgf/m (6,46 kN/m);: 
surcharge 


p° = 400 x 2,2 = 880 kgf/m (8,8 kN/m); 
charge totale 
ge = ge + pc — 646 + 880 — 1526 kgf/m (15,26 kN/m); 


— charge de calcul sur Î m de longueur de la poutre 
a = g°n + p°na = 646 X 1,1 + 880 x 1,2 — 
— 1766 kgf/m (17,66 kN/m); 


— moment fléchissant maximal 
M = ql°18 = 1766 X 4,8°%/8 = 5100 kgf:m (51 kN:m). 


D'après le Tableau IX.2 la résistance de calcul est R — 
— 2100 kgf/cm’. La poutre subit une charge statique uniformément 
répartie et le déversement de sa membrure supérieure comprimée 
est empêché par les hourdis rigides: elle peut donc être calculée 
par la méthode de la rotule plastique. La formule (I1X.8) fournit 


11 163. 


la valeur du module de résistance plastique que doit présenter la 
section : 
1 __ 510000 


pl — FR = 510" “ 242 cmi. 


La condition 
Wol = 1,12W 


nous donne 


242 . 
W=—— RCI — 216 cm*. 
Nous choisissons dans le catalogue (voir Annexe X) la pou- 
trelle n° 22 avec WW, — 232 cm* et J, — 2550 cm‘. 
Flèche de la poutre à mi-portée sous la charge caractéristique 
Sgert_ 5x 15,26 x 4801 | 
Ê = RET 384% 210108 2880 — 199 CM. 


Flèche relative 
f/1 = 1,93/480 = 1/250. 


Exemple IX.3. Calculer une poutre d’acier à simple travée 
composée de deux profilés en U (appui fixe d'une conduite de chaleur) 
chargée au milieu de la portée par une force de calcul concentrée 
P = 8 tf (80 KkN). Portée ! = 2,4 m. Matériau: acier de classe 
C 38/23. 


Solution. 


M = PI4 —=8 x 2,4/4 — 4,8 tf:m (48 kN:m); 


__ 480000 … . 
W — 5100 — 228 cmi. 


Nous choisissons dams le catalogue (Annexe XI) deux profilés 
en U n° 18, de façon à avoir 


W, = 2 x 121 — 242 cm° = 228 cm. 


Exemple IX.4. Calculer la section à donner à une poutre d’acier 
composée de 9 m de portée, supportant en chaque tiers de sa portée 
des charges concentrées PC — 26 tf, P — 32 tf; flèche relative 
admissible f/1 — 1/400..Maténianu: acier de classe C 44/29. 

Solution. Sollicitations de calcul 


M= EE 96 tf.m; Q=P=32ti. 


Module de résistance à assurer pour À = 2600 kgf/cm°? (Ta- 
bleau IX.2) 


a ——————————— — 




Donnons-nous à priori une épaisseur de l’âme ôgme — 8 mm 
et calculons la hauteur de la poutre d’après la formule (IX.11): 


| W 3700 
h=1,15 V 5 —- 4,15 V5 = 78cm. 


Vérifions l'épaisseur de l'âme au cisaillement à l’aplomb de 
l'appui à l’aide de la formule (IX.12) en posant Re, = 1500 kgf/cm°: 


Ôame PEN 1500 x 78 —= 0,41 CM << 0,8 cn). 


Moment d'inertie de la section à assurer (formule (I1X.13)) 
J = Wh/2 — 3100 x 78/2 — 144 000 cm4. 

Moment d'inertie des membrures (formule ([X.14)) 



me 427 000 — LÈXT = 111 000 cmi. 




Section à donner à une membrure (formule (1X.15)) 


27m 2 X111 000 
R2 78? 


Tm = J — 


—= 31 cm°. 


En = 


Posons 


l Z 2 cm. 


bm & + h = 20 em ; ôm = 2 


Dessinons la section d’après les éléments calculés: À — 80 cm, 
Dm = 20 Cm, ôm—2 Cm; Agme — 16 CM, Ôônme — 0,8 cm. 

Cette section aura le moment d'inertie et le module de résistance 
suivants : 


7,= EXT | x 20 x 2 x 392 — 29 400 + 121 600 — 151 000 cms ; 


— X 151 _— 3 
, A ST 3780 cm. 


La vérification à la résistance sera faite d’après la formule (1X.6) 
(la méthode de la rotule plastique est inapplicable, car il y a risque 
de flambement de la membrure et de l'âme): 


HO no. 
2600 — 09 : 


lo ___300 a . Ra me = 76 … 
mg 15>(9 à 12); pe 95 > 70 


= eo — 2540 kgf;em? < 2600 kgf/cm?, . 


la résistance est bonne. 
Flèche de la poutre à mi-portée sous la charge caractéristique 

Pc — 26 tf 
23 26 000 * 9003 


= gr * 2,1.108 X 151 60 — 2»1 GE 




Flèche relative 
f/1 = 2,1/900 — 1/428 << 1/400. 


Force de cisaillement 7 au niveau des cordons de soudure (for- 
mule (1X.16)) 


7 — 25m __ 82 000 x 20 x 2 x 39 


JO 151 000 


Epaisseur à donner au cordon selon la formule (I1X.17) pour 
B — 0,7 et Rin — 1800 kgf/cm° 


ho 5 600 0: 14 cm < 0,6 cm. 


— 3932 kgf/cm°. 


Nous retenons À; = 6 mm. 
Voyons s’il est nécessaire de vérifier l’âme au flambement : 


hame 76 _ 2100 
= gg — 95 < 110 V22=099, 


la vérification est superflue. 

Les raidisseurs (nervures transversales) seront placés à l’aplomb 
des appuis et aux points d'application des charges concentrées : 

: 2100 

en outre, puisqu'on a hame/Oâme — 95 >> 100 Ve —= 90, il 
est nécessaire de prévoir des nervures de raidissement aussi dans 
les intervalles, c'est-à-dire de 1,5 en 1,5 m, espacement inférieur 
à 2,0 h. L'épaisseur des nervures sera prise égale à 8 mm, valeur 


supérieure au 4/15 de leur largeur b,, Æ ma. — 10 cm. 


$ IX4. CONCEPTION ET CALCUL DES POTEAUX 


Poteaux simplement comprimés 


Les poteaux d'acier peuvent être pleins, c'est-à-dire constitués de 
tôles, profilés, tubes (fig. IX.7,a), ou à treillis, c’est-à-dire formés 
de barres isolées réunies par des plats ou par un treillis de cornières 
minces (fig. IX.7, b, c). Un poteau à treillis diminue la dépense d’a- 
cier; par contre, il est moins facile à construire. 

La tête du poteau est conçue en fonction du mode d'appui des 
poutres (fig. IX.8, a, bc). La base évasée du poteau peut être 
constituée par une plaque d'appui simple (fig. IX.8, d), munie 
de nervures (fig. IX.8,e) ou de tôles verticales, ou traverses 
(fig. IX.8, f). La plaque d'appui présente des trous pour les boulons 
de fondation. | 

La résistance d’un poteau est vérifiée dans sa section dange- 
reuse de façon à satisfaire à la condition 


NIFu<R, (IX.18) 


où Ÿ est la charge de calcul; F,4 la section nette (après déduction 
des trous); À la résistance de calcul de l'acier. 

_. La section du poteau étant faible devant sa longueur, le poteau 
risque de céder au flambement avant que la résistance du matériau 


FIG. IX.7. Poteaux simplement comprimés: 


a, sections des poteaux pleins; b, sections des poteaux à treillis; c, différents types de 
treillis; d, pour le calcul des plats; 1, treillis du poteau; 2, lame du poteau 


soit épuisée. Tout poteau doit donc être calculé au flambement, 
généralement d'après la formule 




Fs<E (IX.+9) 


oùfF+- est la section brute du poteau (sans déduction des trous); 
œ le coefficient de réduction de la capacité portante du poteau qui 
dépend de son élancement À et de la classe d’acier. Par exemple, 




pour les pièces simplement comprimées en acier de classe C 38/23 
les valeurs de œ sont les suivantes: 


À 00 


0 so | 70 | #0 | so | 100 | 4m 


20 | 40 50 | 200 


0,82 | 0,77 o.71/0,65/0,58]0.| 0,3 | 0,17 


p | 1 | 0,97 | 0,9 | 0,87 


Par élancement À d’un poteau, on entend le rapport de sa lon- 
gueur de flambement /, (fig. IX.9) au rayon de giration r de la sec- 


FIG. IX.8. Base et pied du poteau: 


1, fût du poteau; 2, poutres, 3, nervures d’appui des poutres; 4, tasseau ; 5, plaque d’ap- 
pui; 6, raidisseurs; 7, traverses , 8, ARCERONS 9, boulons de fondation 




tion, ce dernier étant fonction du moment d'inertie et de l’aire de 
la section: 


l l Ts. 
À — 0x . À — = . = = s — A 
* Tx ? ÿ For ? Fhr : 


Le poteau doit être bai de façon à assurer une stabilité égale 
par rapport à ses deux axes: À, Æ À, 




Dans la section d’un poteau à treillis l’axe æ — x traversant 
les lames (voir fig. IX.7, b) s'appelle axe matériel, et l'axe y — y 
traversant le treillis, axe libre. 

L'élancement du poteau par rapport à son axe matériel est 


ke = lolra (IX.20) 


Dans une section composée de deux profilés identiques le rayon 
de giration de la section totale est égal à celui d’une lame r... 

Pour tenir compte de la flexibilité de la portion de la lame com- 
prise entre deux nœuds du treillis par rapport à l’axe libre y — y, 
on fait entrer dans le calcul l’élan- 
cement fictif A <À,. Pour la sec- | | 
tion formée de deux lames rendues : 
solidaires par un treillis de plats rec- 


tangulaires, l’élancement fictif est | = . 
M=VREM, (xX21) | À À À 


=. M = <40. (IX.22) 


_ FIG. IX.9. Longueur de flam- 
Dans ces formules /, est l’écartement  bement des poteaux simplement 


entre les bords des plats (voir fig. comprimés 
IX.7,c);r\le rayon de giration de 

la lame par rapport à l'axe y, — y, passant par son centre de 
gravité (d’après le catalogue). 

L'élancement limite d’un poteau est Amax — 120. 

Dans la flexion longitudinale du poteau les plats doivent être 
calculés pour résister à un effort tranchant fictif Q; qui, pour les 
poteaux en acier de classe C 38/23, est pris égal à 20F,.. 

Chaque treillis de plats subit un effort tranchant 


Qn1 — Q1/2 — 20F;./2 Ra 10F;,.. (I X.23) 
La condition d'équilibre de la partie isolée du poteau représentée 
sur la figure IX.7, d s'écrit 


où 71 est l'effort tranchant dans le plat; Z l’écartement entre les 
centres des plats; c la distance entre les axes des lames. 


D'où 
Th = Qpil/c. (IX.24) 
Le moment fléchissant exercé sur un plat est 
Mn= Ts 30, (IX.25) 


On donne généralement aux plats une épaisseur 6 entre 6 et 
10 mm et une hauteur 4 entre 0,5 et 0,75 fois la largeur de section 




du poteau. Si la résistance du cordon de soudure attachant le plat 
à la lame a été contrôlée par calcul, on considère que la résistance 
en flexion du plat n’a plus à être vérifiée. 

Le cordon d'angle attachant le plat sur la lame a une longueur 
égale à la hauteur d du plat; la longueur théorique du cordon (com- 
pte tenu de la pénétration incomplète aux extrémités) est LL — 
— d — 10 mm. Le cordon résiste aux contraintes normales 64. dues 
au moment À7/,, et des contraintes tangentielles t, déterminées par 
l'effort tranchant T;:: 


__ Mpr __ 3Qnil . 
Be We — Gel ? (1X.26) 
EC LS (IX.27) 


Fe C X 0,7hele . 


La résistance du cordon de soudure est déterminée en partant 
de la contrainte résultante 


Oeaic = V OÈ+TÈS Rn. (IX.28) 


La base du poteau répartit les pressions sur la fondation (semelle). 

La surface à donner à la plaque d’appui de la base F,,, est cal- 
culée de telle façon que les contraintes engendrées sous la plaque 
soient non supérieures à la résistance de calcul à la compression locale 
(écrasement) du béton de la fondation, 


NIP,5< Récr. (IX.29) 


La valeur de R5. est fonction du rapport de la surface d’'écra- 
sement (surface de la plaque) à la surface totale de fondation F1! 
au droit de la base, ainsi que de la résistance de calcul du béton R,, 


Récr = Rpr V'FilE pb << 2R hr 


Si la base comprend des traverses, des raidisseurs, des boulons 
de fondation, la surface de la plaque d'appui de la base peut être 
surdimensionnée. La hauteur minimale des traverses est définie 
par la longueur des cordons de soudure attachant les traverses au 
fût du poteau. Ces cordons sont calculés avec une certaine marge de 
sécurité !) pour résister à la totalité de la force longitudinale W. 

La plaque d'appui de la base est exposée aussi à la flexion du 
fait de la réaction de la fondation g = N/F,,. La valeur du moment 
fléchissant est déterminée par les rapports des longueurs des côtés 
de la plaque dans ses compartiments limités par les traverses, les 
raidisseurs et le fût du poteau. Si le compartiment de la plaque est 
fixé par un seul bord, il travaille en flexion dans un sens unique, 
à la façon d'une console. S'il est fixé suivant trois ou quatre côtés 
et si un de ses côtés (en plan) est moins de deux fois plus long que 


1) Dans les calculs, on ne tient pas compte du fait qu’une fraction de la 
force longitudinale est reportée par les cordons qui attachent le fût du poteau 
directement à la plaque d'appui de la base. 




l’autre, il convient de considérer le travail du compartiment en 
deux directions; enfin, si un côté est plus de deux fois supérieur à 
l'autre, on fait abstraction de la flexion de la plaque dans le sens 
long et l’on admet que la plaque travaille seulement dans le sens court. 

Dans la plaque d’appui de la base montrée sur la figure IX.8, f 
le compartiment 7 travaille en console ; le moment fléchissant a pour 
équation 


M, a Ti : 


Le compartiment 2 est appuyé sur trois côtés ; le moment fléchis- 
sant maximal a pour équation 


M; — Bga?, 


où a est la longueur du bord libre et B un coefficient qui dépend du 
rapport des côtés : 


b./a 0,7 


0,5 | 0,6 


0,8 0.9 11.0 1.2 


1,4 2,0 | 00 


ï | 060 0,074 


08) oo | 17 | oo | 120 | o,16| 19 0,133 


Le compartiment 3 est appuyé suivant tous les quatre côtés; 
le moment fléchissant maximal a pour équation 


M; = aga?, 


où a est la longueur du côté court et « un coefficient qui dépend du 
rapport des côtés : 




1,0 4 L 12 | 1.3 16 1,5 16 [1,8 [2.0 | 00 




ous | 055 069 000 | 075 084 086 0,054 100 0,125 


L'épaisseur à donner à la plaque d'appui de la base est calculée 
par la formule 


ôpb = V 6M/R, 


où À est le plus grand moment fléchissant dans la plaque d'appui 
et À la résistance de calcul de l’acier à la flexion. 

Les traverses et les raidisseurs seront disposés de telle façon 
que l'épaisseur de calcul à donner à la plaque d'appui de la base 
soit sensiblement la même dans tous ses compartiments, en général 
Ôpp — 16 à 40 mm. 




Exemple IX.5. Vérifier la capacité portante du poteau plein 
en acier montré sur la figure IX.10, a. Le poteau a une section en 
double T formée de trois tôles soudées. Matériau: acier de classe 
C 38/23. Charge de calcul N = 105 tf — 1050 kN. Hauteur du 




FIG. 1X.10. Pour les exemples de calcul des poteaux 


poteau ? — 4,1 m; puisque ses extrémités sont articulées, on a de 
toute évidence Z, = L. 


Solution. Déterminons la géométrie de la section : 
F=924 XxX1x2+18 x 1 = 66 cm°; 

je ee 24 LR — 2305 mi : 
… 15 


ya LE 42 (A +24 x 1 x 9,52) — 4800 emt ; 


_ M _spon 7. = 08,5em; 


lo = 


Tmin 


Jo __ 410 _ — 70 < 120. 


Amax = 


En fonction de À — 70, nous trouvons @ — 0,77 (voir page 168). 
Vérifions le poteau au flambement à l’aide de la formule (IX.19) : 
N 105 000 
la capacité portante du poteau est bonne. 




Exemple IX.6. Calculer la charge de calcul que peut supporter 
le poteau formé de deux profilés en U n° 20 (fig. IX.10, b). Largeur 
du poteau b — 20 cm, hauteur ! — 6 m. Matériau: acier de classe 
C38/23. Ecartement entre les bords des plats du treillis Z, — 70 cm; 
dimensions d’un plat d — 15 cm, Ô — 6 mm. Epaisseur des cordons 
de soudure attachant les plats sur les lames du poteau À, —6 mm. 
L’extrémité inférieure du poteau est encastrée, l’extrémité supé- 
rieure articulée ; on a donc L, = 0,7 I — 0,7 x 6 — 4,2 m. 

Solution. Cherchons dans le catalogue (voir a X D) les carac- 
téristiques du profilé en U n° 20: F — 23,4 cm’; —= 1520 cm“; 
Jyo = 113 cm*, r; — 8,07 cm; ro = 2, 2 cm. Le ‘distance entre 
la face extérieure de l'âme et le centre de gravité de la section est 
2,07 cm. 

Calculons l’élancement du poteau par rapport à son axe maté- 
riel à l’aide de la formule (1X.20) : 


he = lors — 420/8,07 = 52. 


Pour déterminer l’élancement fictif du poteau par rapport à 
l’axe libre È — y, Calculons d’abord 


J, = 2 (113 + 23,4 x 7,93?) — 3220 cm“; 


= V 52-83 cm; à, = = 50,5. 


L'élancement d'une lame est égale, d’après ne à 


À] = Lulryo — 70/2,2 — 31,8. 


Calculons maintenant l'élancement fictif par la formule (I1X.21): 
=VN+M—=V50,5+31,8 —60 > À,— 52. 


Pour À = 60 le coefficient @q = 0,82 (voir page 168). 
‘La charge de calcul supportée par le poteau sera déterminée à 
l’aide"de la formule (1X.19): 


N = RFœ = 2100 x 2 x 23,4 x 0,82 = 80 500 kgf (805 kN). 


Vérifions la résistance des plats. L’écartement entre les axes 
des plats est Z — 70 + 15 = 85 cm. 
D'après la formule (IX.23) 


Qp1 = 10Fhr = 10 X 2 X 23,4 — 468 kgf (4,68 kN); 
d'après la formule (I1X.24) 


= Qui RE X 85 _ 2490 kgf (24,9kN): 


d’après la formule (1X.25) 
Mn = Qpil/2 = 468 X 85/2 = 19 900 kgf-cm (199 000 Nm). 




Vérifions la résistance du cordon d'attache : 


Lt t;= 1571-12: cm: 


= het — 0,7 X X 14 13,7 cm: : 
F. = 0,7hl = 0,7 X 0,6 x 14 = 5,9 em’: 
= Mn 4453 kof/cm? 


ET We 13,7 
(d’après la formule (1X.26)); 


Tp1 2490 


Te = 422 kgf/cm? 


Fe 59 — 
(d'après la formule (1X.27)). On a en somme d’après (1 X.26) 


Ocale = V'0È+ T7 —V 14532+ 4222 — 
— 1513 kgf/cm? (151,8 MPa) Æ Rin -= 1500 kgf/em? (150 MPa). 


La résistance du cordon est bonne. 


Poteaux comprimés et fléchis 


Les poteaux des bâtiments industriels sans étages sont soumis en 
même temps à une force longitudinale V et à un moment fléchis- 
sant {. Reliés entre eux par la toiture, ces poteaux constituent les 
portiques transversaux du bâtiment. Ils peuvent être pleins ou à 
treillis, de section constante ou décroissante vers le haut; dans ce 
dernier cas ils s'appellent poteaux étagés (fig. IX.11, b,c). Les po- 
teaux étagés sont les plus répandus. Dans sa partiehaute (dite baïon- 
nette) située au-dessus de la poutre de roulement du pont roulant, 
un tel poteau présente une section en double T constituée par trois 
tôles soudées; la partie basse du poteau, située au-dessous de la 
poutre de roulement, est composée de deux lames rendues solidaires 
soit par une âme (poteau plein), soit par un treillis. Les lames sont 
généralement fabriquées er profilés d'acier, en double T ou en U; 
elles peuvent aussi être constituées par une tôle d’acier universel. 
Afin d'augmenter la capacité portante de la lame, sa section en 
double T peut être formée de trois tôles soudées, et la section en U, 
d'une tôle et de deux cornières fixées par soudure. 

L'âme d'un poteau plein a une épaisseur très faible, entre 1/100 
et 1/120 de la hauteur. Sa stabilité locale est garantie par des raidis- 
seurs jumelés transversaux soudés à l'intervalle de 2,5k à 3h (voir 
fig. I1X.11, b). 




Le treillis du poteau, disposé en deux plans, est fabriqué géné- 
ralement à partir de cornières isolées; c’est un système triangulé à 
montants supplémentaires (fig. IX.11, c). 

Si le bâtiment n'est pas très élevé et la charge du pont roulant 
est de 15 à 20 t au maximum, on peut utiliser des poteaux pleins de 
section constante (fig. IX.11,a) 
fabriqués à partir de poutrel- 
les à larges ailes ou avec trois 
tôles soudées, 

On emploie des poteaux 
dits jumelés (fig. IX.11, d) 
où une lame s'élève jusqu’à 
la toiture pour la supporter 
(grand montant) et l’autre 
s'arrête au niveau de la pou- 
tre de roulement du pont 
roulant (montant sous poutre). 
Le montant sous poutre est 
solidarisé avec le grand mon- 
tant par des plats horizontaux 
dont l’écartement est choisi 
de façon à conférer au mon- 
tant sous poutre un élance- 
ment sensiblement égal dans 
le plan du portique transver- FIG. IX.11. Poteaux comprimés et flé- 
sal et perpendiculairement à “hiS: 
ce plan. . a, poteau plein de section constante: b, poteau 

Un poteau comprimé et. plein étagé; re, ppteñn nel treillis; d, po- 
fléchi est généralement cal- 
culé au flambement. La for- 
ce longitudinale critique ÂW,. de flambement d’une pièce com- 
primée et fléchie et les contraintes critiques correspondantes 
OÙ << da dépendent de l’excentricité initiale de la force longitudi- 
nale eo — MIN, de l’élancement À de la pièce et de la géométrie 
de la section. 

Le calcul au flambement dans 1e plan du moment (dans le plan 
du portique transversal) se fait d’après la formule 


——<R, IX.30 
PE Fpr — ( ) 
où le coefficient qf < 1 est cherché dans l'Annexe XV en fonctien 
du flambement fictif à — À V R/E et de l’excentricité réduite m 
de la force. 
Le calcul au flambement dans le plan perpendiculaire à celui 
du moment (au plan du portique) se fait d'après la formule 


A <R, (IX.31) 




où le coefficient deflambement de la pièce comprimée et fléchie , 
(voir page 168) est défini en fonction de l’élancement À, (dans le 
plan perpendiculaire au portique); c est un coefficient qui tient 
compte de la variation de la stabilité de la pièce dans le plan per- 
pendiculaire au portique à cause du moment agissant dans le plan 
du portique (voir Annexe XVI). 

Dans un poteau à treillis, on doit en outre vérifier au flambe- 
ment les lames assimilées à des pièces comprimées et fléchies. Si la 
section est symétrique, la force longitudinale développée dans une 
lame est égale à 


Ni = N/2 + Mi, (IX.39) 


où h est la distance entre les centres de gravité des sections des lames, 
Les éléments du treillis sont calculés pour résister à l’effort tran- 
chant Q !) et à l'effort dû au raccourcissement des lames du poteau 
sous l’action de la force longitudinale 2). 
L'effort développé dans une diagonale de section F4 est égal à 


r Q FaN 
Na= + À 


d— 2sinx 


sin?@, (IX.33) 


où « est l’inclinaison de la diagonale (généralement &« = 45°); F 
est la section totale des deux lames du poteau. 

Les diagonales comprimées sont à vérifier au flambement d'’a- 
près la formule (IX.19) en déterminant leur élancement d’après le 
plus petit rayon de giration de la section et en affectant R d’un 
coefficient de comportement m = 0,75, car la diagonale est fixée 
sur la lame par une seule aile. 

La plaque d’appui de la base d’un poteau comprimé et fléchi 
est dimensionnée de façon que les contraintes maximales dans le 
béton de la fondation ne soient pas supérieures à R,.. Pour la base 
d’un poteau plein (fig. IX.12, a) les contraintes sous les bords de 
la plaque sont calculées à l’aide de la formule 


pe (IX.34) 


Fpb 7 Wopp ? 


où W,, est le module de æésist®rtce de la surface de la plaque d’ap- 
pui de la base par rapport à l’axe perpendiculaire au plan d'action 
du moment. 

Le signe positif dans (1X.34) correspond aux contraintes de com- 
pression, et le signe négatif, à celles de traction. Nous avons déjà 


1) Si Q << Qr, on pose Q— Qr = 20F;- (pour un acier de classe C38/23). 
2) La mise en charge des lames provoque en même temps un raccourcisse- 
ment des éléments du treillis. 




vu qu'on doit assurer 6. R,.. Les efforts de traction Z doivent 
être repris par les boulons de fondation : 


M— Na 


où À] est le moment fléchissant de calcul dans la section basse du 
poteau (voir fig. IX.12, a); N la force longitudinale de calcul; a la 
distance du centre de gravité du diagramme des compressions à l’axe 
du poteau; y la distance de l’axe des boulons de fondation au centre 
de gravité du diagramme des compressions. 


Z= , (IX.35) 


a) Ligne des C.G. 
de La section b) 


Axes des 
boulons de 
Fondation 


boulons de 


N fondation | 




Centre de gravité du. 
diagramme de compression  _—- 


ste] ,* 


FIG. IX.12. Bases des poteaux comprimés et fléchis: 
a, poteau plein; b, poteau à treillis 




La section à donner aux boulons de fondation est 




nR}: 


(IX.36) 


où x est le nombre de boulons de fondation; R?, la résistance de cal- 
cul des boulons à la traction, égale à 1400 kgf/cm* (140 MPa) pour 
les boulons de fondation en acier BCr3Kn2. 

Un poteau à treillis sera avantageusement muni de deux bases 
séparées (fig. IX.12, b). La base de chaque lame sera calculée pour 
résister à l’effort de compression maximal Ÿ,, par analogie au cal- 
cul de la base d’un poteau simplement comprimé. 


$ IX.5. CONCEPTION ET PRINCIPES DE CALCUL DES FERMES æ 


Les fermes sont des structures à treillis qu'on utilise le plus souvent 
dans l’ossature du comble du bâtiment. Les éléments longitudinaux 
d’une ferme, parallèles à la portée, sont appelés membrures. Les 
membrures sont reliées entre elles par un treillis formé de montants 
et de diagonales. 


12—0948 477 


On distingue les fermes trapézoïdales (fig. I1X.13, a), triangu- 
laires (fig. IX.13, b) ou à membrures parallèles (de hauteur cons- 
tante, fig. IX.13, c). 

Le système du treillis de la ferme est choisi en fonction de la 
configuration de cette dernière, de sa hauteur, ainsi que de Ia lon- 
gueur du panneau requise (distance entre les détails). On distingue 
les systèmes en V (fig. IX. 13, a, c) et en N (fig. IX.13, b). L'incli- 
naison des diagonales varie généralement entre 35 et 45°. Les élé- 
ments du treillis sont constitués le plus souvent par des cornières 
jumelées ; les détails sont formés par des goussets sur lesquels les 

cornières viennent se fixer par sou- 
a) dure (fig. IX.13, détail À). 

Délail À Le flambement d’une ferme 
plane dans le sens perpendiculaire 
à son plan est empêché par un 
système de contreventements verti- 
caux et horizontaux. Une ferme 
contreventée est un ensemble tridi- 
mensionnel indéformable (fig. 
IX.14). 

Sur le schéma simplifié de la 
ferme chaque élément est repré- 
senté par une ligne qui suit le 
centre de gravité de la section de la 
pièce. Les axes de tous les éléments 
aboutissant à un détail doivent 
concourir dans le point représen- 
tatif du détail. En calculant les 
efforts dans les éléments de la 
ferme, on admet que tous les élé- 
Detail À ments sont articulés dans les détails, 
c'est-à-dire que les charges ap- 
pliquées dans les détails font naî- 
tre uniquement des efforts axiaux 
(compressions ou tractions) dans 
les éléments. La valeur et le sens 
de chaque effort sont cherchés 
soit graphiquement (diagramme de 
Maxwell-Cremona), soit analyti- 

FIG. IX.13. Fermes: —'  ‘““quement (méthode des sections). 

1, membrure supérieure: 2, membrure Dans une ferme de toiture la mem- 
inférieure; 3, diagonale: 4, montant: brure supérieure est comprimée 
et la membrure inférieure ten- 

due. Si la charge est appliquée en 

dehors des détails, la barre subit un moment fléchissant qui vient 
s'ajouter à l'effort axial; en vue d'éviter des sections trop fortes, 
on s'arrange pour que les charges soient appliquées dans les détails. 

Les efforts étant connus, on choisit la section à donner aux élé- 




ments. Les éléments travaillant en compression sont calculés d'’a- 
près la formule (I1X.19). L'élancement À des principaux éléments com- 
primés de la ferme (membrures, diagonales placées à l’aplomb des 
appuis) ne doit pas être supérieur à 120; pour les autres éléments 
comprimés, il peut atteindre 150. En calculant l’élancement, on 
admet que la longueur de flambement /, de la membrure, des diago- 
nales aux appuis et des montants dans le plan de la ferme est égale 
à leur longueur géométrique / entre les centres des détails ; pour les 
autres éléments du treillis on pose , = 0,81. Dans le plan perpen- 
diculaire à celui de la ferme, on admet que la longueur de flambe- 
ment d’un élément est égale à la distance entre les détails dont le 


FIG. IX.14. Contreventements des fermes: 


1, fermes; 2, contreventements horizontaux de la membrure supérieure; 3, contrevente 
ments horizontaux de la membrure inférieure ; 4, contreventements verticaux: #, entretoises 


déplacement par rapport au plan de la ferme est empêché par les 
contreventements, les bords des dalles de couverture soudés sur 
la membrure, etc. 

Les éléments travaillant en traction sont calculés à l’aide de la 
formule 


NIFi< R. (IX.37) 


En dessinant une section, on doit chercher à réduire autant que 
possible la gamme des profilés utilisés (5 à 7 types au plus). 

Les cordons de soudure attachant les éléments des fermes sur 
le gousset du détail sont dimensionnés en fonction de l’effort de 
calcul W, à l’aide de la formule (I1X.2). 

En étudiant l’attache d’un élément sur le gousset, on doit se 
rappeler que le centre de gravité de la cornière est déplacé vers le 
talon et que, par conséquent, le cordon de talon est plus sollicité que 
le cordon d’aile. La surface totale du cordon de soudure nécessaire 
pour attacher l'élément fabriqué en cornières doit être distribuée 
en raison inverse de la distance de son centre de gravité à la rive 
(voir fig. IX.13, détail À). 


12% 179 


Après avoir calculé la longueur des cordons d'attache, on di- 
mensionne le gousset. Les éléments aboutissant au détail doivent 
âtre écartés de 50 mm au moins entre eux; on doit chercher à donner 
au gousset une configuration aussi simple que possible. 


$ IX.6. STRUCTURES MÉTALLIQUES PRÉCONTRAINTES 


Pendant la fabrication d’une structure d'acier précontrainte, on 
communique à celle-ci une contrainte de sens opposé à celle qui 
aura lieu en service. Cela permet d'étendre le domaine élastique et 


a) : I L . c) _ = 
NZNANSN7 


FIG. IX.15. Structures métalliques précontraintes: 
1, câbles mis en tension 


d'utiliser pour les pièces tendues des matériaux à haute résistance 
(câbles, etc.) qui diminuent la dépense d'acier. 

La précontrainte d'une poutre peut être réalisée soit en donnant 
une contre-flèche à la pièce, soit en munissant la pièce de câbles 
résistants mis en tension. 

Le premier procédé est illustré sur la figure IX.15, a qui repré- 
sente une poutre précontrainte constituée de deux éléments aux- 
quels on à donné une contre-flèche avant de les avoir solidarisés à 
l'état fléchi par des cordons de soudure longitudinaux. Le diagram- 
me des contraintes dans la section de la poutre terminée est montré 
sur la figure IX.15, b. Ce diagramme sera superposé au diagramme 
classique des contraintes en charge (fig. IX.15, c). À mesure que la 
charge croît, le diagramnié tan devient sensiblement rectangu- 
laire (fig. IX.15, d). De cette façon la capacité portante de la poutre 
sera épuisée quand les contraintes auront atteint leurs valeurs limi- 
tes en tout point de la section, et non seulement dans la fibre extrême 
comme dans une poutre sans précontrainte. 

La poutre précontrainte par câbles est montrée sur la figure 
IX.15, e. Au cours de la fabrication de la poutre, on met en tension 
les câbles en faisant naître un moment de sens opposé au moment en 
charge, de façon à diminuer la contrainte totale. Puisque les câbles 




sont fixés sur la poutre elle-même, la structure travaille sous la 
charge comme un tout; la haute résistance à la traction du câble 
améliore le comportement de la structure. 

Les fermes sont précontraintes à l’aide des câbles mis en tension 
et fixés sur la ferme de façon à faire naître, dans les principaux élé:- 
ments, des contraintes de sens opposé aux contraintes en service. On 
peut disposer des câbles isolés tendus le long des principaux élé- 
ments travaillant en traction (fig. IX.15, f) ou bien prévoir un 
câble tendu unique pour la ferme tout entière (fig. IX.15, g). 


CHAPITRE X 


LES STRUCTURES DANS LES BATIMENTS 


$ X.1. PRINCIPES DE CONCEPTION DES STRUCTURES 
DU BÂTIMENT 


Les structures utilisées dans les bâtiments se composent d'éléments 
isolés qui sont associés de façon à former un système tridimension- 
nel. Les exigences auxquelles doivent satisfaire les différents élé- 
ments des structures sont conditionnées par leur destination et les 
particularités du travail dans l’œuvre. Par exemple, les pièces cons- 
titutives des planchers entre étages doivent être robustes et suf- 
fisamment rigides, car leur flexion risque de perturber les condi- 
tions d'exploitation normale du bâtiment; les murs et les poteaux 
sous planchers doivent être résistants et avoir une bonne stabilité. 
S'agissant des pièces en béton armé, on limite l'ouverture des fis- 
sures dans le béton tendu, au point d’exclure même la formation de 
fissures pour certaines structures précontraintes. 

Le bâtiment dans son ensemble doit présenter une bonne rigidité 
spatiale; on entend par là qu'il doit opposer une résistance suffi- 
sante aux charges verticales et horizontales de toute nature. 

On distingue des bâtiments à ossature et des bâtiments sans 
ossature. 

Dans un bâtiment sans ossature la rigidité spatiale est assurée 
grâce aux murs longitudinaux et transversaux qui, réunis par les 
planchers, forment un système tridimensionnel et travaillent en- 
semble. Quelques renseignements sur les bâtiments en maçonnerie 
sans ossature ont été donnés dans le $ VIII.4. 

Les bâtiments à ossature sont essentiellement constitués par 
des portiques, contreventés ou non. Un portique se compose de 
barres (poutres et poteaux) qui sont le plus souvent rigidement 
assemblées entre elles dans les nœuds. Le contreventement est assuré 
par les murs en maçonnerie, les{cloisons en béton armé ou des pièces 
en acier. Dans un bâtiment à portiques non contreventés toutes les 
charges extérieures sont reportées par les portiques transversaux 
et longitudinaux réunis par les planchers et la toiture de façon à 
former un système tridimensionnel (fig. X.1, a, b). Dans un bâti- 
ment à portiques contreventés, une partie des charges est reprise 
par les contreventements (fig. X.1, c). 

En chaque phase de construction du bâtiment, on cherche à ga- 
rantir la bonne résistance mécanique, rigidité et stabilité de chaque 




élément isolé et du bâtiment dans son ensemble ; à cet effet on utilise 
des pièces de fixation provisoires telles que tirants, entretoises, etc. 
La déformation du bâtiment présentant une bonne rigidité spa- 
tiale se déroule de telle façon que la mise en charge d’un élément 
quelconque entraîne immédiatement celle de plusieurs autres élé- 
ments qui « facilitent la tâche » de l'élément sollicité. 
Le projet du bâtiment doit être adapté aux conditions d'industria- 
lisation: ce sont les éléments préfabriqués qui permettent de faire 


FIG. X.1. Différents schémas d’ossature des bâtiments : 


1, portique transversal; 2, portique longitudinal; 3, plancher ou toiture; 4, cloison de 
contreventement; 5, contreventements en acier 


le montage le plus vite et de mettre en œuvre des machines et méc#æ 
nismes de chantier appropriés. 

Les usines peuvent fabriquer les éléments de structures de bâti- 
ment en grandes séries et à des cadences très élevées, à condition que 
leur gamme ne soit pas excessivement étendue et que ces éléments 
puissent être employés dans les bâtiments les plus divers. Cette 
condition est garantie par la typification et la modulation : on adopte 
un schéma-type pour chaque genre de bâtiment et l’on réduit les 




dimensions fondamentales (en plan et suivant la hauteur) à une 
série limitée de dimensions normalisées établies sur la base d’une 
modulation réglementaire À). 

Par exemple, les bâtiments industriels sans étages, parmi les- 
quels on trouve de nombreux bâtiments utilisés dans les réseaux 
de distribution et d'évacuation des eaux (salles des pompes, souf- 
fleries, chlorateurs, etc.), et les bâtiments des chaufferies doivent 
avoir des cotes d'implantation multiples du module agrandi 3 m (ou 
6 m), et les cotes suivant la hauteur, multiples du module agrandi 
1,2 m. Leur schéma-type prévoit l’appui articulé de la toiture sur 
les murs ou les poteaux, ce qui permet de réaliser la toiture à par- 
tir d'éléments de même type sans tenir compte de la hauteur du 
bâtiment, de l’existence des ponts roulants ni des parties enterrées 
(voir $ X.4, X.5). 

Pour chaque élément du bâtiment on cherche la solution techni- 
que la plus rationnelle, qui a fait ses preuves dans la pratique, et on 
la retient à titre d'élément-type. Ce sont les éléments-types, destinés 
à être utilisés en masse, qui constituent la fraction la plus importante 
de la production des usines de produits de construction. La gamme 
des éléments-types est périodiquement soumise à des révisions. 

Dans le projet d’un bâtiment, on doit chercher à utiliser les élé- 
ments aussi grands que le permettent les performances des méca- 
nismes de levage et des véhicules existants. Plus les éléments sont 
grands, moins ils sont nombreux et plus le montage sera rapide. 

Les éléments préfabriqués doivent être simples à produire et 
faciles à monter. On en tient compte en choisissant l’élément-type. 
On doit se rappeler également que pendant le transport et le mon- 
tage les éléments peuvent se trouver exposés à des sollicitations 
très différentes de celles prévues dans le projet: un poteau conçu 
pour travailler à la compression dans l’œuvre subit une flexion au 
cours du transport et du montage à la façon d’une poutre chargée 
par son propre poids ; les fermes et les poutres, conçues pour reposer 
sur leurs extrémités dans l’œuvre, sont accrochées en d’autres points 
par les élingues de levage, etc. 

Le cas de charge d’un élément sur chantier doit faire l’objet 
d’un calcul particulier; la charge de poids propre sera affectée 
d'un coefficient dynamique 1,5 au levage et au montage et 1,8 pen- 
dant le transport 2). 

Les cotes retenues dans les projets d'éléments préfabriqués sont 
classées en trois catégories : 

— les cotes nominales définissent les dimensions de la pièce de 
façon à l'adapter aux dimensions fondamentales modulées du bâ- 
timent ; 


1) La modulation consiste à choisir toutes les dimensions multiples d’un 
module 100 mm ou d’un module agrandi multiple de 100 mm. 
2) Dans ce cas aucun coefficient de surcharge n’affecte la charge de poids 


propre. 




— les cotes de projet (seules figurant sur les dessins de la pièce} 
ne diffèrent des cotes nominales que par la valeur des jeux prévus 
dans les joints; 

— les cotes réelles sont établies sur la base des cotes de projet 
en tenant compte des tolérances de fabrication qui varient générale- 
ment entre +3 et +10 mm. 

Par exemple, un hourdis de toiture pour bâtiment industriel 
a les cotes nominales 6 %X 3 m et les cotes de projet 5,96 x 2,98 m. 


$ X.2. PLANCHERS EN BÉTON ARMÉE 


Généralités 


Un plancher en béton armé peut être préfabriqué (complètement. 
ou partiellement) ou coulé en place. On distingue des planchers à 
poutres et des planchers sans poutres, ou planchers-champignons. Un 
plancher à poutres est constitué de poutres et hourdis; un plancher- 
champignon est formé de dalles sans nervures qui reposent directe- 
ment sur les poteaux munis de chapiteaux. 

Le procédé de fabrication et le système du plancher (réseau de 
poteaux, direction et espacement des poutres) sont choisis en fonction 
de la destination du bâtiment, de la solution architecturale, du 
parti constructif, ainsi que de la surcharge prévue sur le plancher. 
Cette surcharge est définie dans les Normes pour les bâtiments pu- 
blics et d'habitation. Pour un bâtiment industriel, la surcharge est 
définie par la technologie de production adoptée. On trouve les 
valeurs des surcharges caractéristiques et des coefficients de sur- 
charge correspondants en Annexe Il. 

Avant de s'établir sur un système définitif du plancher, on fait 
le recensement de plusieurs variantes en les évaluant au point de 
vue de la dépense des matériaux, de la facilité d'exécution et du 
coût. 

Les plaques entrant dans la composition du plancher peuvent 
être appuyées sur deux côtés ou sur les quatre côtés. Une plaque 
appuyée sur deux côtés travaille à la façon d’une poutre. Le cas de 
travail d'une plaque appuyée sur les quatre côtés est fonction du 
rapport de ses côtés (fig. X.2). Si le rapport des côtés est L./l, >3 
(> 2), la plaquetravailleen flexion dans une seule direction (courte) 
l, et s'appelle hourdis; si le rapport des côtés est L,/l, < 3 (< 2), 
la plaque travaille en flexion dans deux directions et s'appelle 
dalle. e 

Lors du calcul des poutres, dalles et hourdis hyperstatiques des 
planchers, on tient compte de la redistribution des efforts internes 
qui peut se produire à cause de la fissuration, des propriétés ané- 
lastiques du béton et des armatures, ainsi qu'à la suite d’une dégra- 
dation partielle de l’adhérence acier-béton. La prise en compte de 
ces facteurs conduit au plan de ferraillage le plus rationnel et, assez 




souvent, permet de diminuer la dépense d'acier. Nous allons étudier 
ce mode de calcul plus en détail. 

À mesure que les charges extérieures augmentent, les contraintes 
dans les sections de la pièce en béton armé deviennent plus grandes. 
Au moment où la contrainte de l'acier tendu dans la section la plus 
sollicitée devient égale à la limite d’élasticité, le béton comprimé 
présente des contraintes élevées et subit des déformations anélasti- 
ques considérables. Un tel état de contrainte manifesté dans une 
section quelconque de la pièce isostatique a pour eïffet une rotation 


FIG. X.2. Hourdis (a) et dalle (b). 




relative des deux parties de la pièce situées de part et d’autre de la 
section; à la suite de cette rotation la contrainte dans le béton 
devient égale à la charge de rupture en compression et la pièce rompt 
(stade III de l’état de contrainte et de déformation, voir chapitre VI). 

Si la contrainte de l'acier tendu devient égale à la limite d’élas- 
ticité dans une section quelconque d’un élément hyperstatique, la 
ruine n'a pas lieu, car la rotation relative des parties de la pièce 
est empêchée par les fixatipns.æxx appuis. Bien que soumise à des 
déformations locales très sensibles, la section considérée reporte 
un moment 


Mi — OPTANTE 


où F, est la section de l’acier ; z, est le bras de levier du couple de 
forces intérieur. 
Dans le calcul, la valeur du moment est prise égale à 


M = RAF a2pe 


La partie de la poutre où se manifeste l’état de contrainte décrit 
est appelée rotule plastique. Malgré la croissance de la charge, le 
moment dans la rotule plastique reste inchangé tout en augmen- 
tant dans les autres sections: il se produit ainsi une redistribution 
des moments. 

Des rotules plastiques peuvent se former en plusieurs sections 
de la pièce, jusqu’à ce que cette dernière devienne isostatique, 
auquel cas l'apparition d’une nouvelle rotule plastique conduit à la 
ruine. 

Afin d'illustrer ce qui vient d’être dit, considérons une poutre 
hyperstatique à simple travée de portée !, encastrée à ses extrémités 
et exposée à une charge q unifor- 
mément répartie (fig. X.3). a) 

Les moments limites dévelop- 
pés dans les sections de la 


poutre sur appui et en travée 
sont respectivement : 1 g 54 Let 


FE FEP 


Mir = dela tr : N À 
ap Zl 14 
Map = CéFa ze. c) L : _) 
La somme des moments en 2 
travée et sur appui dans un mi Map=RaF#22 
système de poutres hyperstatique d) 
est égale au moment d’une pou- 
tre librement posée M, : 
M Man = Mo. (X.1 Mr=Ra FE 2tr 2 
tr + ap 0 ( ) g-q, tr lala £p Mi 
; : je l < 
Si la charge est uniformé- a AY 
ment répartie, on a 
[2 (-g,)L? 
M=<-. al 
Dans le cas considéré FIG. X.3. Pour le calcul d’une poutre 
hyperstatique en béton armé à simple 
Ftretr ou FPzap — 9? travée compte tenu de la redistri- 
Jérass na ST: bution des efforts: 


a, plan de ferraillage de la poutre; b, sché- 
ma des efforts; c, mécanisme de formation 


En se donnant différentes d’une rotule plastique; d, diagramme des 
moments; e, schéma des cfforts et diagram- 


valeurs de FE et de FF? on ob- me des moments provenant de la charge 
tient différentes valeurs des mo- * * LS ue is De 
ments en travée et sur appui. 

Admettant que la poutre considérée travaille en phase élastique, 
on obtient pour les moments sur appui M3, — ql?/12 et pour les 
moments à mi-portée M4, — gl?/24 (My + Map = qll8 = Mo). 
Si la quantité d'armatures dans les sections sur appuis de la poutre 
est moins grande que la valeur calculée en fonction du moment sur 




appui ci-dessus, on verra se former des rotules plastiques dans les 
sections sur appuis au cours de la mise en charge pour une charge 
QG < q, si bien que la charge complémentaire (q — q,) ne fera croître 
que les moments en travée. Par exemple, si le ferraillage de la pièce 
à l’aplomb des appuis a été calculé pour résister à un moment Afan — 
— ql?/16, les armatures en travée doivent être calculées pour résister à 
un moment 


ql? qi? qi? 
Mir Mo Map 6 16 


On voit donc que le mode de redistribution des moments est fonc- 
tion du ferraillage de la pièce et peut être défini dans le projet. 

Afin d'éviter une ouverture excessive des fissures dans une sec- 
tion où une rotule plastique risque de se produire, on doit veiller 
à ce que le moment redistribué A ne s'écarte jamais de plus de 
30 % du moment élastique correspondant. L'intensité du ferraillage 
des sections avec rotules plastiques est limitée par la condition 


E = xlh, < 0,35. 


Planchers à poutres préfabriqués 


Ces planchers sont assemblés à partir de poutres et de panneaux 
préfabriqués. Les poutres peuvent être à simple travée ou à travées 
multiples, elles peuvent être disposées soit dans le sens long, soit dans 


4 | ÿ 






FIG. X.4. Planchers à poutres préfabriqués: 


a, Sans poutres, b, avec des poutres fran: sales à simple travée; c, d, avec des poutres 
longitudinales ou transversales à travées multiples; 1, panneaux; 2, poutres; 3, poteaux 


le sens court du bâtiment (fig. X.4). Les portées dans les bâtiments 
civils sont multiples d’un module agrandi 400 mm; dans les bâti- 
ments industriels le réseau des poteaux est 6 x 6, 6 x 9 et 6 x 
X 12 m. 

Les poutres à travées multiples sont en général continues, grâce 
à un agencement Particulier des aboutements des éléments préfabri- 
qués de la poutre de longueur égale à une travée. On utilise aussi 




des poutres à simple travée articulées sur les poteaux. Les poutres 
ont une section rectangulaire, en T, ou rectangulaire avec des sail- 
lies (consoles) latérales servant d’appuis aux panneaux (fig. X.5, a), 
La hauteur de section À d’une poutre préfabriquée varie générale- 


a) c) 
OT é A 
Jioiciccie 


FIG. X.5. Profils de sections des éléments préfabriqués des planchers à poutres 


ment entre 1/10 et 1/14 de {, où L est la portée; la largeur de section 
b de la poutre est comprise entre 0,3 et 0,4 h. 

Les panneaux de plancher peuvent être creux, avec ou sans 
nervures (fig. X.5, b, c, d). Les ds creux sont utilisés dans 


a) Panneau  , Poutre 


OO OL ce) Re 


__ \L 
} + b"Zbierr 
FIG. X.6, Schéma des efforts et section adoptés pour le calcul des panneaux des 
planchers 


les bâtiments civils où les surcharges des planchers sont peu élevées 
et le plafond doit être lisse. Les panneaux nervurés trouvent leur 
emploi généralement dans les bâtiments industriels. Les panneaux 




sans nervures sont lourds et ne peuvent être employés que pour 
des portées limitées. 

Les panneaux sont fabriqués en béton précontraint (généralement 
en pré-tension) ou non précontraint. La hauteur d’un panneau en 
béton non précontraint varie entre 1/15 et 1/20 de [, et celle d’un 
panneau en béton précon- 
traint entre 1/20 et 1/30 de 1, 
où L est la portée. 

Les panneaux prennent 
appui sur les poutres et les 
murs. Leur cas de charge est 
celui d’une poutre à simple 
travée posée librement sur 
appuis, soumise à une charge 
uniformément répartie com- 
prenant le poids propre, le 
poids du revêtement du plan- 
cher et la surcharge (fig. 
X.6, a). La charge q exercée 
sur À m de longueur du pan- 
neau est égale à 


= jbd 
DE . q Qi p 
her Aa à où g, est la charge sur 1 m? 


Le moment fléchissant ma- 
ximal à mi-portée est A — 
— 0,125 ql°, l'effort tranchant 


FIG. X.7. Pour le calcul de la résistance maximal (près de l'appui) 
de la plaque du panneau à la flexion est Q — 0,5 ql. | 
locale entre les nervures: La section à donner aux 


1, armatures principales de la plaque : 2, ner- armatures longitudinales ten- 
vures transversales du panneau ne 

dues F, est choisie de façon 

à assurer la bonne résistance 
suivant la section normale, par la méthode décrite dans le $ VI.3. 
Dans le calcul, on prend une section rectangulaire de largeur b;, 
car la hauteur de la zone comprimée x (au stade III de l’état de con- 
trainte) est en général moins grande que l'épaisseur de la plaque 
supérieure (hourdis) h; (fig. X.6, b, c). 

Le calcul de résistance-suivant les sections obliques se fait com- 
me il a été décrit dans le $ VI.4. 

Si Q << kRtrbh,, où b est la largeur totale des nervures, les arma- 
tures transversales sont disposées sans calcul, selon les dispositions 
constructives. Si Q > k.R:,bh,, on doit faire le calcul de résistance 
des barres transversales des carcasses prévues dans les nervures. 
Dans un panneau à évidements tubulaires on a généralement Q < 
<< kRt+trdho, aussi les carcasses ne sont-elles posées qu’aux extré- 
mités du panneau, sur une longueur égale à 1/4 de L. 


XL AL IL NL, ! et, la largeur du panneau. 






Le cas de charge de la plaque du panneau (sa partie limitée par 
les nervures) est fonction du rapport de ses côtés. Quand les nervu- 
res transversales sont inexistantes ou séparées par une distance 2 




Trecllis T-2 
(répartition) 
| C-1 


NN NN NN 
Trecllis T-1avec armature 
longitudinale principale Fy 


FIG. X.8. Plans deferraillage d’un panneau creux (a) et d’un panneau nervuré (b): 

1, armature principale F, du panneau; 2, boucles de levage; 3, appareil d’ancrage de F, 

d’armature de précontrainte Fa est réalisée sous forme de barres isolées qui n’appartiennent 
pas au treillis de la carcasse) 


au moins deux fois supérieure à l’écartement /, des nervures longi- 
tudinales, la plaque se comporte comme un hourdis (fig. X.7, a). 
Compte tenu de la redistribution des efforts, le moment fléchissant. 




b) sep 
O0O0O00OQO/S 
bp ES 


FIG. X.9. Pour le calcul des déformations du panneau: 


a, remplacement du trou rond par un trou rectangulaire équivalent : b, section du panneau 
à évidements tubulaires retenue pour le calcul 


s'écrit M — Au, où g, est la charge exercée sur 1 m° de la pla- 
que. 

Si 0,5 < L/l, <2 (fig. X.7, b), la plaque se comporte comme 
une dalle (elle porte en deux directions). La méthode de calcul des 
dalles sera exposée un peu plus tard. Si les nervures transversales 
sont serrées, de sorte que L/l, = 2 (fig. X.7, c), la plaque se com- 
porte comme une poutre portant dans le sens /,. Les nervures trans- 




versales sont calculées comme des poutres à simple travée appuyées 
sur les nervures longitudinales, pour résister à la charge transmise 
par le panneau (plus exactement par sa plaque supérieure). Dans 
les calculs, on donne aux nervures transversales une section en T. 
Le ferraillage des nervures transversales se réduit généralement à 
une simple n ppe d’armatures. 

Les plans de ferraillage des panneaux creux et nervurés sont 
montrés sur les figures X.8. 

L'étape suivante consiste à vérifier l'ouverture des fissures et 
à déterminer la flèche par les méthodes données dans les $ VI.6 et 
VI.7; ce faisant, on assimile la section d’un panneau nervuré à un 
simple T et l’on réduit celle d’un panneau creux à un double T ainsi 
qu'il est montré sur la figure X.9. 

Le calcul de la poutre consiste à déterminer la charge exercée et 
les sections à donner au béton et aux aciers. 

La charge reprise par une poutre est limitée par la zone d'influen- 
ce de largeur À égale à la distance entre deux poutres voisines. Soient 
£1 la charge de calcul sur un m° du plancher provenant du poids 
des panneaux et du revêtement et g,, la charge due au poids propre 
de la poutre; la charge permanente de calcul exercée sur 1 m de 
longueur de la poutre sera g = g, À + g,p. La surcharge exercée sur 
1 m de longueur sera donc p = p,k (où p, est la surcharge de calcul 
sur Î m° du plancher). 

La charge totale est q = £g + p. 

Dans une poutre à simple portée Mimax — 0,125 ql° et Quax — 
= 0,5 gl. 

Dans une poutre continue les moments et les efforts tranchants 
sont calculés en tenant compte de la redistribution des efforts; les 
moments élastiques d’'appuis sont diminués jusqu’à 30 % tout en 
augmentant les moments en travée en conséquence conformément 
à la condition (X.1). Grâce à la diminution des moments sur appuis, 
on peut simplifier la construction de l'appui de la poutre sur le 
poteau. 

Le calcul du travail en phase élastique d’une poutre continue, 
compte tenu de l'influence défavorable de la surcharge À), est effec- 
tué par les méthodes classiques de la Mécanique des structures. Pour 
les poutres à travées égales, le calcul est facilité par des tables spé- 
ciales (voir Annexe XVII). Par exemple, quand la poutre subit une 
charge uniformément répartie, on a 


M = (ag + Br), 


où « et B sont des coefficients qu’on trouve dans les tables. 


1) On considère que la charge permanente g est appliquée dans toutes les 
travées en même temps. Pour déterminer le moment maximal en travée, on admet 
que la surcharge p est appliquée dans la travée donnée, puis dans une travée sur 
deux; pour calculer le moment maximal sur appui, on admet que la surcharge 
est appliquée dans deux travées adjacentes à l’appui en question, puis dans une 
travée sur deux. 




Si la surcharge est très faible devant la charge permanente, on 
peut chercher les moments en phase élastique en faisant agir la charge 
totale q — g + p dans toutes les travées en même temps: 


M = aql?. 


Après avoir redistribué les moments, on cherche les efforts tran- 
chants en assimilant chaque travée à une poutre posée sur deux appuis 
et supportant, en plus de sa charge pro- 
pre, les moments sur appuis retenus. 

Au fur et à mesure que l’on s'éloigne 
de l'axe de l'appui, les moments néga- 
tifs dans la poutre diminuent (fig. X.10). 
Pour dimensionner la section, on retient 
le moment sur le nu du poteau: 


M9 = Map — Qbpot/2. 


Puisque ce calcul prévoit la possibilité 
de formation d’une rotule plastique sur 
l'appui, on doit préciser la géométrie de 
la section de la poutre de façon à avoir FIG. X.10. Moment de cal- 
dans la section sur appui (sur le premier Cul sur appui de la poutre: 
appui intermédiaire) FA RON ES POIERR 

E = xlho < 0,35. 


Connaissant les moments fléchissants, on détermine la section 
à donner aux armatures longitudinales principales en travée et sur 
appuis de façon à assurer la résistance suffisante suivant les sections 
normales. Les armatures transversales (barres transversales des car- 
casses) sont calculées pour résister à l'effort tranchant dans les sec- 
tions obliques. 

L'aboutement des éléments de la poutre assemblés sur l'appui doit 
être organisé de telle façon que la poutre puisse être considérée com- 
me continue. La solution montrée sur la figure X.11, a prévoit la 
fixation des armatures supérieures tendues de la poutre par soudure 
(pendant la fabrication) sur des pièces scellées en acier. Les barres de 
raccordement posées sur chantier sont passées à travers les trous du 
poteau et soudées sur les pièces scellées de la poutre. Ce sont les 
pièces scellées qui transmettent les efforts de compression de la poutre 
sur la console du poteau. Le soudage terminé, le joint est rempli de 
béton. 

La figure ÀX.11, b représente une autre solution. Les aciers en 
attente de la poutre sont reliés à ceux du poteau par bain de fusiof 
à l’aide de courtes barres intercalaires, après quoi les jeux sont rem- 
plis de béton. Les barres intercalaires permettent de laisser en attente 
des portions plus courtes des armatures, ce qui prévient leur détério- 
ration possible lors du transport et du montage des éléments pré- 
fabriqués. Un autre avantage des barres intercalaires est de rattraper 
le défaut de coaxialité éventuel des aciers en attente de la poutre et 


| Lagramme 
des moments 


13—0948 193 


du poteau. Dans la poutre de toiture, les barres de raccordement sont 
assemblées avec les aciers en attente des poutres par bain de fusion 
et soudées sur une pièce scellée prévue dans 
la tête du poteau (voir fig. XII.7). 

L’effort de traction dans les barres de 
raccordement est 


N = MAn/z, 


où zest le bras de levier du couple de forces 
intérieur (voir fig. X.11, a). Connaissant 
cet effort, on détermine la section à donner 
aux barres de raccordement : 


Fr = NIR4 


Les cordons de soudure d'attache doi- 
vent résister à l'effort N majoré de 30% ; 


7 cette majoration a pour but de garantir 
Dos re la bonne résistance des cordons de soudure 


T8 34 10 T 


FIG. X.11. Aboutements 
des parties de la poutre 
continue sur le poteau: 


1, poutre; 2, pièces scellées 
en acier; 3, barres de rac- 
cordement, 4, poteau; 5, 
soudure sur chantier: 6, bé- 
ton coulé sur chantier; 7, 
aciers en attente de ja pou- 
tre: &, barres intercalaires; 
9, aciers en attente du po- 
teau; 10, soudage des aciers 
par bain de fusion 


en cas de formation d’une rotule plastique 
dans la section de la poutre à l'aplomb 
de l'appui. 

Le plan de ferraillage d'une poutre 
continue est montré sur la figure X.12. 
En vue de diminuer la dépense d'acier, 
il y a intérêt à interrompre une partie 
des armatures longitudinales avant l'appui 
conformément à la diminution des mo- 
ments fléchissants. Les points d'interruption 
des barres sont déterminés d’après le dia- 


gramme des matériaux (voir $ VI.4). 


Planchers à poutres et hourdis coulés en place 


Un plancher à hourdis !) coulé en place est constitué par une dalle, 
des solives et des poutres principales (fig. X.13) bétonnées dans un 
coffrage commun et formant un système intégral. 

La dalle transmet la charge Aüx solives, ces dernières’ sur les pou- 
tres, et les poutres prennent appui sur les poteaux et les murs. L’épais- 
seur de la dalle des planchers d'étage ne doit pas être inférieure à 6 cm 
dans les bâtiments civils et à 7 cm dans les bâtiments industriels. 
L'écartement des solives est généralement choisi entre 1,8 et 2,5 m, 


1) Le compartiment de la dalle limité par les poutres et les soïives présente 
un rapport de côtés l/l, > 3 et représente à ce titre un hourdis; il travaille à la 
flexion entre les solives. 




celui des poutres, entre 5 et 7? m. La hauteur d’une solive varie entre 
1/12 et 1/16 de la portée, et celle d'une poutre, entre 1/10 et 1/12 de 
la portée; la largeur des solives et des poutres varie de la moitié au 
tiers de la hauteur. 


COCO EEE OEEEEEE CETTE OO ETES 


Intercalaires 
Carcasses C-1 el C-1a 


Barres du poteau 


FIG. X.12, Plan de ferraillage d’une poutre continue 




Dalle supprimée par 
convention 






2 J 2 


F1G. X.13. Plancher à poutres et hourdis coulés en place: 
1, dalle; 2, solives: 3, poutres: 4, poteaux 


Au calcul des hourdis, on considère une bande de largeur b — 
— 100 cm découpée dans la dalle parallèlement à ses côtés courts 
(fig. X.13). La charge exercée sur le hourdis se compose de son poids 
propre et du poids du revêtement du plancher g et de la surcharge p. 




La charge totale est donc g = g + p. Les moments fléchissants 
(fig. X.14, a, b) sont cherchés en tenant compte de la redistribution 
des efforts: on a dans toutes les travées intermédiaires et sur les 
appuis intermédiaires 


M = al°/16 
et dans les travées de rive et sur le premier appui intermédiaire 
M = gl°/11. 


Dans le calcul, on donne au hourdis une section rectangulaire de 
largeur b = 100 cm. 

La dalle est ferraillée avec des treillis en rouleaux (fig. X.14, c); 
en travée le treillis est disposé près de la face inférieure de la dalle 


FIG. X.14. Dalle du plancher à hourdis nervurés coulé en place: 


a, schéma des efforts; b, diagramme des moments, c, plan de ferraillage; 1, armatures 
principales; 2, armatures de répartition 


et au droit d'un appui il est relevé près de la face supérieure, confor- 
mément au changement du signe des moments fléchissants. 

Dans les compartiments de la dalle bordés de poutres et de solives 
suivant le pourtour, la section des armatures est diminuée de 20 % 
grâce à l'effet favorable des poussées qui se manifestent pendant la 
redistribution des efforts. 

La vérification de la résistance de la dalle aux efforts tranchants 
dans les sections obliques est superîlue, car la condition (VI.35) est 
garantie. E 

Les solives sont soumises à une charge uniformément répartie 
ramassée dans une bande de la dalle de largeur égale à l’entraxe des 
solives c ; à cette charge vient s'ajouter le poids propre g,. La charge 
exercée sur 1 m de longueur d'une solive s'écrit 


Ls = (£ + p)c + gi 


où (g + p) est lasomme des valeurs de calcul de la charge permanente 
et de la surcharge appliquées sur 1 m° de la dalle. 




O6gl 05gl 05 Sal Bal 
ee 3 


Carcasses C-2 


ne Re US RS een 
D == 00 = = = ee = 


DER SSSR EE — — 
TTT) 


—| Barres de Poutre 

EE T raccordement principale 
CARLSLRSRRRAÎRRR2L22::: BLaRLSsLReRen] 

Solive | 


2 2 13 


Solive 


FIG. X.15. Solive à travées multiples d’un plancher à hourdis: 


a, Schéma des efforts; b, diagramme des moments; c, diagramme des efforts tranchants; 
d, plan de ferraillage de la solive; 1, armatures principales en travée; 2, idem, sur appui 


Le cas de charge des solives à travées multiples est analogue à celui 
de la dalle. Les moments fléchissants et les efforts tranchants sont 
cherchés en tenant compte de la redistribution des efforts, d’après les 
formules citées sur la figure X.15. 

La hauteur utile de la section de la solive est choisie de façon 
à avoir & < 0,35 sur le premier appui intermédiaire à partir du bord, 
là où la redistribution des efforts risque de se traduire par la forma- 
tion d’une rotule plastique. 

La section à donner aux armatures principales tendues en travée 
est déterminée comme pour une section en T à largeur de hourdis 
bh = c, car le hourdis (plaque) est situé dans la zone comprimée ; 
sur appui, la section des armatures est calculée comme pour une sec- 
tion rectangulaire de largeur égale à celle de la nervure b, carlehourdis 
est situé dans la zone tendue. 

En travée, le ferraillage est réalisé sous forme de carcasses soudée 
dont les barres longitudinales sont calculées pour résister au moment 
en travée et les barres transversales, pour résister à l’effort tranchant 
correspondant dans les sections obliques (la largeur de section étant 
égale à la largeur de la nervure b). Sur appui, on pose deux treillis 
en rouleaux décalés à barres principales transversales au-dessus de 
la poutre principale. La section totale des barres transversales de ces 




treillis sur la longueur c est égale à la section des armatures de la 
poutre au droit de l'appui. 

Le plan de ferraillage d'une solive est montré sur la figure X.15. 

Les poutres principales reportent des charges concentrées aux 
points d'appui des solives, ainsi que la charge provenant de leur 
poids propre. On cherche les moments fléchissants et les efforts 
tranchants compte tenu de la redistribution des efforts, comme pour 
les poutres des planchers préfabriqués. 


Planchers à poutres et dalles coulés en place 


Les poutres qui soutiennent les dalles de ces planchers sont disposées 
en deux directions et appuyées sur des poteaux (fig. X.16, a). On 
adopte généralement un quadrillage 
dé poteaux de 4 X4 à 6 x 6 m. 
L'épaisseur de la dalle varie entre 
8 et 14 cm. La dalle travaille à la 
flexion en deux directions. Elle 
est armée avec des treillis soudés. 
En travée, les treillis sont placés 
près de la face inférieure, et au 
droit des appuis (à l’aplomb des 
. dre su poutres), relevés vers la face supé- 
: rieure de la dalle. 

Puisque les moments en travée 
décroissent du milieu de la portée 
vers les appuis, l’armature inférieu- 
re de la dalle est constituée par 
deux treillis comportant des barres 
principales placées dans les deux 
sens, la section des barres porteu- 
ses étant la même dans les deux 
Armature principale de p25, gs, treillis. Un treillis est interrompu 


La dalle (sur gppui) : à 1/4 de Z, avant les appuis inter- 
ere me ee médiaires et à 1/8 de L; avant les 
ni | ui appuis libres de rive (2, étant le 


. petit côté de la dalle). Les treillis 

FIG. rte Plancher à poutres et supérieurs de la dalle possèdent des 
alles coulé en place:  . noie 

a, schéma du plancher; b, plan de fer- "barres principales (portantes) pla- 

raillage de la dalle, 1, dalles, 2, mur;  cées dans un sens unique; ils sont 

DR eee disposés de telle façon que les bar- 

res principales, orientées en travers 

des poutres, soient prolongées à l’intérieur de la travée d’une FORBUAUE 

égale à 1/4 de L, (fig. X.16, b). 
Sous l’action de la charge extérieure on voit apparaître sur La face 
inférieure de la dalle des fissures dirigées suivant les bissectrices des 


angles (fig. X.17, a), et sur la face supérieure, le long des poutres 




Esse 
Boss 


(fig. X.17,b). La charge devenant encore plus grande, on voit la dalle 
se casser suivant ces fissures. À l’état-limite, la dalle peut être con- 
sidérée comme un système articulé dont les éléments sont assemblés 
entre eux par des rotules plastiques 
suivant la ligne de rupture (fig. X.17, c). 
Le moment de calcul dans la rotule plas- 
tique rapporté à l'unité de sa longueur 
(1 mètre) dépend de la section des arma- 
tures principales F, sur 1 m de longueur 
de la dalle et se laisse définir par la 
formule 




M — RaF ape 


Si dans le cas général les sections des 
armatures sur tous les appuis et en travée 
dans les deux sens sont différentes, les 
moments de calcul seront différents eux 
aussi. Désignons les moments de calcul 
en travée par M, et M,, et les moments 
de calcul sur appui, par Mr, Mi, Mixx, 
Mir (fig. X.17, c). 

Le calcul de la dalle se fait par la 
méthode de l’état d'équilibre limite, en 
partant du fait que la charge appliquée 
a pour effet de déplacer le système arti- 
culé (la dalle) avec ses rotules plastiques. 
La charge extérieure g, tout en se dépla- pr. x.17. Pour le calcul 
çant avec la dalle, effectue un travail d'une dalle (aux quatre cô- 


Wa égal au travail des forces intérieures tés encastrés) : 
- 1, rotule plastique sur l’appui 
Win, c'est-à-dire au travail des moments evrant vers le AUUE #2 idem 


fléchissants correspondant aux angles de  entravée (ouvrant vers le bas) 
rotation . 

Comme la moitié des barres des treillis inférieurs de la dalle sont 
interrompues à 1/4 de /, avant les appuis (voir fig. X.16, b), la 
formule de calcul se présente comme suit : 


[2 (31. —1 ; 
RE) (2H + Mi Mi) la 


3 1 , 
+5 Mes Mit Mu+ Mi) UT (X.2) 


Si une moitié des barres des treillis inférieurs sont interrompues 
à 1/8 de Z, avant les appuis, on a 


EC) (2M + Mi + Mi + (TL M3 ——+ LM,+Mu -Mti) li. 
(X.3) 


Les formules ci-dessus contiennent six moments inconnus. En se 
donnant à priori leur rapport, on obtient un seul moment inconnu qui 




permet de dégager les cinq autres en faisant intervenir les rapports 


retenus. . 
Le calcul est grandement facilité dans le cas où Z, — l, = l; on 


admet en plus que tous les moments agissant dans les panneaux inter- 
médiaires sont égaux. La formule (X.2) donne alors 
ql/6 = 1M, 
d'où 
M —= ql2/42 = M travée — M appui: 


Dans une dalle librement appuyée tous les moments sur appuis 
sont nuls. Si Z, — !, — Let tous les moments en travée sont égaux, 




CAE CS 5) 

: Æ RE HÉHOUOTNIT 
S RS 21 sus LEON SE INR a 
ÉD En 


Barres de raccordement 


FIG. X.18. Pour le calcul des poutres du plancher à dalles: 
a, Schéma des efforts: b, plan de ferraillage 


on à M, = M: = Mitravéea Puisque la moitié des barres du treillis 
inférieur sont interrompues à 1/8 de 1, avant l’appui, on a d’après (X.3) 


Mtravée = 9l2/21. 


La section à donner aux armatures tendues F, est calculée de la 
même façon que pour une section rectangulaire ordinaire de largeur 
b — 100 cm; les treillis sont dessinés en conséquence. Grâce aux 
poussées qui se manifestent dans les dalles bordées de nervures, la 
section à donner aux armatüréS"peut être diminuée de 20 %. 

Les poutres de planchers à dalles sont calculées pour résister à une 
charge triangulaire ou trapézoïdale ramassée dans une zone d’influen- 
ce limitée par les bissectrices des angles de la dalle (fig. X.18, a). 
Si l’écartement des poteaux est le même dans les deux directions, les 
poutres posées dans les deux sens subissent une charge triangulaire. 

Compte tenu de la redistribution des efforts, on admet que le 
moment dans la travée de rive et au-dessus du premier appui à partir 
du bord est M, = 0,7 M, et les moments dans toutes les travées inter- 




médiaires et au-dessus de tous les appuis intermédiaires sont M, = 
— 0,5 A1,, où À, est le moment dans la poutre déterminé par la 
charge triangulaire ou trapézoïdale respectivement. 

On rencontre les dalles (plaques appuyées suivant leur contour) 
dans la composition des panneaux nervurés des planchers à poutres. 
préfabriqués s'ils comportent des nervures transversales (fig.X.7, b), 
ainsi que dans les panneaux préfabriqués carrés bordés de nervures 
(fig. XII. 4 et XIT.5). Les plaques de ces panneaux sont calculées par 
la méthode que nous venons d'exposer, tandis que leurs nervures sont 
assimilées à des poutres à simple travée soumises à une charge trian- 
gulaire. 


Planchers-champignons 


Plancher-champignon coulé en place. Ce type de plancher sans poutres. 
est montré sur la figure X.19, a. Il repose généralement sur des po- 




| um | ii 




FIG. X.19. Plancher-champignon: ni 


a, vue d’ensemble ; b, cotes du chapiteau; ec, plan de ferraillage de la dalle; d, plan de fer-- 
raillage du chapiteau 


teaux disposés suivant un quadrillage de 6 X6 m. La dalle a une 
épaisseur de 18 à 22 cm. Grâce à la suppression des nervures saillantes. 
le plancher a une faible hauteur constructive et facilite l’aération 




du local couvert. Ce facteur détermine l’implantation massive des 
planchers-champignons dans les réservoirs souterrains (fig. XI.1, 
XI.25), dans les bâtiments des entrepôts frigorifiques, magasins, 
garages. 

Les poteaux présentent des chapiteaux aux faces inclinées sous 45°. 
Leurs côtés au niveau de la tranche inférieure de la dalle ont une 
longueur c qui varie entre 0,2 et 
0,3 de Z, et au niveau de la nappe 
d'armatures supérieure de la dal- 
le, une longueur a = c + 2h, 
(fig. X.19, b). Les chapiteaux sont 
dimensionnés de façon à vérifier 
la condition de résistance au poin- 
çonnement de la dalle suivant les 
faces de la pyramide désignée par 
mm'nn' sur la figure X.19, b. 

On considère que la résistance 
au poinçonnement est suffisante si 


P< Ribnoyhor 


où P est la charge totale exercee sur 
le panneau de plancher diminuée 
de la partie située sur la base 
supérieure de la pyramide: 


P=q(i— a); 
moy est le périmètre moyen des 


bases de la pyramide de poinçon- 
nement : 


TE —2(a+c). 


bmoy = 


La dalle du plancher] sans pou- 
tres est calculée par la méthode de 
l'état-limite d'équilibre, compte 
tenu de son schéma de rupture. La 


FIG. X.20. Pour le calcul dela (Charge étant appliquée par ban- 
dalle d’un plancher-champignon “des, il se forme dans les panneaux 


par la méthode de l’état-limite 
d'équilibre : 
a, b. Schéma de rupture de la dalle 


Chargée par bandes; c, diagramme 
des moments; d, schéma de rupture 
de Ja dalle chargée suivant toute 


la surface 


intermédiaires deux fissures lon- 
gitudinales sur la face supérieure 
(espacées de c, Æ 0,1!) et une fis- 
sure sur la face inférieure à mi-portée 
(fig. X.20, a). A l’état-limite, on 
voit se former, le long des fissures, 


des rotules plastiques linéaires entre deux éléments de la dalle 
(fig. X.20, b). Les moments fléchissants développés dans les rotules 




plastiques sont 
Map = RaFaa; My = RaFizi. 


La somme des moments sur appui et en travée (fig. X.20, c) est 
égale au moment dans la poutre Àf,: 


Map + Mir = Mi. (X.4) 
Si la charge de calcul est q, la largeur de la bande /, et la portée 
théorique 2, — 2c,, on a 


M, _ lo (l Ar 


Portons dans (X.4) les valeurs de M4,, MA, et M,. La formule se 
présente alors comme suit: 


qlo GmeR, (Far zap + Fiat). (X.0) 


En se donnant le rapport des sections F#P/FY = 0,5 à 0,67, on 
ne laisse dans (X.5) qu’une seule inconnue. 

Le procédé de calcul à la rupture de la bande exposé ci-dessus est 
fondamental et s'impose dans tous les cas. On est parfois amené en 


FIG. X.21. Planchers-champignons Pre (a) et partiellement préfabri- 
qué (b): 


1, chapiteau; 2, panneau de travéc; 3, panneau d'appui 


outre à vérifier la résistance de la dalle selon un schéma qui prévoites 
l'application de la charge dans deux panneaux voisins en même temps. 
La configuration des rotules plastiques linéaires correspondant à ce 
cas est illustrée sur la figure X.20, d. 

Plancher-champignon préfabriqué. Il comprend trois types d’élé- 
ments préfabriqués (fig. X.21, a): 

— chapiteaux prenant appui sur la saillie (console) du poteau; 




— panneaux d'appui posés sur les chapiteaux dans deux directions 
perpendiculaires ; 

— panneaux de travée appuyés suivant leur contour sur les 
panneaux d'appui. 

Le chapiteau a la forme d’une pyramide tronquée ou d'un parallé- 
lépipède droit. Les panneaux d'appui et de travée peuvent être nervu- 
rés, creux ou plats. 

Les jonctions des éléments préfabriqués sont réalisés par soudage 
sur les pièces scellées en acier, suivi de la coulée du béton dans les 
jeux. 

Admettant que les éléments sont partiellement encastrés dans les 
joints, on prend le moment pour un panneau de travée de portée L, 
égal à A] — qglf/27 et le moment en travée pour un panneau d’appui de 
portée l, égal à Mi+r = ÿéal2/12; les moments d'appui sont pris 
égaux à Map = Géal3/24, où geq est la charge équivalente uniformé- 
ment répartie. 

Le chapiteau est calculé comme une console qui subit la réaction 
du panneau d'appui et une charge répartie dans les limites du cha- 
piteau. 

Plancher-champignon partiellement préfabriqué. Ce type de 
plancher (fig. X.21, b) est réalisé en posant une nappe d’armatures 
supplémentaire par-dessus les chapiteaux et les panneaux d'appui et 
de travée préfabriqués et en coulant une couche de béton. L'intérêt de 
ces planchers consiste dans le fait qu'ils se comportent comme des 
planchers coulés en place mais ne nécessitent pas d’échafaud ni de 
coffrage sur le chantier. 


$ X.3. FONDATIONS DE POTEAUX EN BÉTON ARMÉ 


La fondation a pour but de transmettre la pression du poteau sur le 
sol de telle façon que la pression exercée sur le sol soit suffisamment 
petite pour éviter l’affaissement inadmissible du sol. 


a) b) 
1600 
2110 1200 
200 | 1200 | 2000 5 
UT 2400 | 


FIG. X.22. Fondations de poteaux en béton armé: 
u, Semelle à gradins; b, semelle filante; c, fondation-dalle; d, dimensions 


Les poteaux en béton armé reposent généralement sur des fonda- 
tions isolées sous forme de semelles à gradins (fig. X.22, a) ; si le sol 




est meuble et les charges élevées, on prévoit des semelles filantes 
(fig. X.22, b) ou des fondations-dalles (fig. X.22, c). La fondation 
peut être préfabriquée en un bloc ou composée de plusieurs éléments 
préfabriqués (fig. X.22, d); elle peut aussi être coulée en place. 
L’exécution d’une fondation coulée en place ne présente généralement 
aucune, difficulté, aussi ce type de fondation est-il largement répan- 
du surtout quand les dimensions sont importantes. 

La semelle destinée à recevoir un poteau préfabriqué possède un 
logement dont la profondeur ne doit jamais être inférieure au côté de 


c) N 


Pression sous Semelle 


FIG. X.23. Semelles à gradins: 


a, semelle d’un poteau préfabriqué ; b, semelle d’un poteau coulé en place; c, flexion de la 

semelle sous la charge; d, pour le calcul de la surface à donner à la fondation; 1, poteau: 

2, armature du poteau; 3, aciers en Frontier la fondation; 4, armatures principales de la 
fondation 


la section du poteau (plein) ni à la longueur d'ancrage de l’armature 
du poteau. La section du logement est majorée de 100 mm en bas et 
de 150 mm en haut par rapport aux dimensions de la section du poteau 
(fig. X.23, a). Une fois le poteau installé et placé d’aplomb, les 
jeux du logement sont remplis de béton. Si la semelle est destinée 
à recevoir un poteau coulé dans l’œuvre, elle possède des aciers en 
attente sur lesquels viennent se souder les armatures du poteau 
(fig. X.23, b). 

L'armature principale d'une semelle à gradins est réalisée sou#” 
forme d'un treillis dont les barres portantes sont disposées en deux 
directions. Le treillis est posé en bas sur une couche d’enrobage 
épaisse de 3,5 cm (si l’on a prévu une sous-couche de sable et gravier) 
ou de 7 cm (en l'absence de la sous-couche). Cette armature reprend 
les tractions engendrées dans la partie basse de la fondation pendant 
son travail à la flexion dû à la réaction du sol (fig. X.23, c). 




Une fondation est dite centrée si elle ne subit qu'une force de 
compression longitudinale. Soumise à une force longitudinale, à un 
moment fléchissant et à un effort tranchant à la fois, la fondation est 
dite excentrée. 

Les semelles à gradins étant très rigides, on admet que la pression 
sous la semelle (et aussi la poussée réactive du sol) est répartie de 
façon linéaire. La base inférieure de la semelle est dimensionnée de 
façon à limiter l’affaissement du sol conformément aux Normes 
prévues pour la catégorie de l’ouvrage en question. Pour toute une 
série de bâtiments industriels et civils reposant sur un sol peu com- 
pressible !), on peut se passer de calculer l’affaissement, à condition 
que la pression sous la semelle soit non supérieure à la pression de 
calcul sur le sol À. déterminée à la suite des travaux de prospection 
géologique effectués sur le terrain de construction. 

Pour certains types de sols on trouve en Annexe XVIII les pres- 
sions de calcul À, qui, pour des fondations de largeur b, = 1 m et 
de profondeur À, — 2 m, peuvent être retenues comme À,.. Si 
h<2metbÆim,ona 


Ra= Rf1+8 (4) (SE) : 


pou hk>2metb—-imona 


R,=R, [1 +k, (== | | +havn (R—h,), 


où À, — 0,125 pour les terrains détritiques à gros morceaux et les 
sols de sables (sauf les sables pulvérulents); 4, — 0,05 pour les sols 
argileux et les sables pulvérulents; k, — 0,25 pour les terrains 
détritiques à gros morceaux et les sols de sables ; k, = 0,2 pour les 
sables argileux et les limons sableux; k, — 0,15 pour les argiles; 
Yr est le poids volumique du sol situé plus haut que la tranche 
inférieure de la semelle, tf/m°. 

Puisque la valeur retenue de À, a pour but de limiter l’affaisse- 
ment du sol (état-limite d'utilisation), les charges intervenant dans 
le calcul de la pression sous la fondation sont prises en valeur caracté- 
ristique, c'est-à-dire affectées d'un coefficient de surcharge n = 1. 

Calcul des fondations centrées. La pression sous la fondation est 
engendrée par la force VC transmise par le poteau et le poids propre 
de la fondation et du sol sur les tranches de cettedernière (fig. X.23, d). 

Admettons que la masë#ë volumique moyenne du matériau de la 
fondation et du sol aux tranches de celle-ci soit Ymoy = 2 t/m°; 
pour la section de la fondation F et la profondeur F,, le poids total 
de la fondation et’du sol sera égal à ÿmoy/1/, et la pression produite 
par ce poids, à 


Y FtH 
— 7 —— = Ymoy A. (X.6) 


1) Module de déformation E > 300 à 500 kgf/cm? (30 à 50 MPa). 


Diminuant À, de Ymoy/1, on obtient la pression de calcul maxi- 
male qui peut être développée par laseule force VC transmise par le 


poteau. On a donc 


F; LR, — YmoyA, (X.7) 

d’où 
F 1 X.8 
Remo ee 


Les fondations centrées ont généralement la forme d’une semelle 
carrée de côté 


a= VF. (X.9} 


La poussée réactive du sol provoquant une flexion de la fondation 
n'est engendrée que par la charge communiquée par le poteau, tandis 


MauTents 


IL Diagrapute DA) 




FIG. X.24. Pour le calcul au poinçonnement d’une fondation centrée (a) et le 
calcul du ferraillage de la fondation (b): 
1, pyramide de poinçonnement ; 2, base inférieure de la pyramide de poinçonnement 


que le poids propre de la fondation et la poussée correspondante se 
font mutuellement équilibre sans entraîner de flexion. La valeur de 
calcul de la poussée réactive du sol produite par la force longitudina-æ 
le de calcul W est 

Ps = N/F1. (X.10) 


La fondation doit avoir une hauteur suffisante pour assurer sa 
résistance au poinçonnement suivant les faces latérales de la pyra- 
mide inclinées sous 45° (voir fig. X.24, a). On retient comme force de 




poinçonnement P la force V communiquée par le poteau diminuée de 
la poussée réactive totale du sol exercée sur la base inférieure de la 
pyramide de poinçonnement. La section du poteau ayant la forme 
d'un carré de côté b, la surface de la base supérieure de la pyramide 
est égale à b?et celle de sa base 
inférieure à (b + 2h,)°, d'où 


P=N—p,(b + 2h). (X.11) 




Armutures principales 


Tpot_ reportant L£ momênt My 


Si la fondation est fabriquée en 
béton lourd, on considère que sa 
résistance au poinçonnement est 
garantie à condition que 


P< Rtrômoytos (X.12) 


où R+, est la résistance de calcul 
du béton à la traction et bn, le 
périmètre moyen des bases de la 
pyramide de poinçonnement, 


Armatares principales 
reportant le momeni M; 


bmoy = En — 4(b+ ho). 
(X.13) 


Portant dans (X.12) la valeur 
de P tirée de (X.11) et celle de 
bmoy tirée de (X.13), on obtient une 
formule qui permet de calculer la 
hauteur à donner à la fondation de 
façon à éviter le poinçonnement : 


h.—=— LS ASE LEE . 

FIG. X.24A. Fondations excen- si 2 ° 2 Rtr+Pmoy ” 
trées en béton armé (X.14) 
He=ho+a. (X.15) 


Dans certains cas la hauteur à donner à la fondation est déterminée 
de façon à assurer la profondeur suffisante du logement k,,: 


Hy = hiog + 200. 


La semelle est divisée dans le sens de la hauteur en gradins hauts 
de 30 à 50 cm. La hauteur du gradin le plus bas sera vérifiée dans la 
section I-I (fig. X.24, a) afin d’assurer la résistance suffisante sui- 
vant la section oblique sans barres transversales. 

Après avoir choisi les dimensions de la semelle (côtés et hauteur), 
on cherche la section à donner aux armatures principales en assimi- 
lant la partie de la fondation au-delà de la face du poteau à une 
console de porte-à-faux (a — b)/2 et de largeur a soumise à une charge 
uniformément répartie pa (fig. X.24, b). 


.208 


Le moment fléchissant qui agit suivant le nu du poteau est égal à 


ps (5) G—by: 


= —— 5" ——#% Pa —— 




La section à donner aux armatures se laisse déduire de la condi- 
tion bien connue 


(X.16) 


M = RaFathb 
en posant 21 & 0,9 ; 
Fa= Tor (X.17) 


En fonction de F,, on dimensionne les barres du treillis inférieur 
(diamètre 10 à 16 mm, écartement 10 à 20 cm). 

Calcul des fondations excentrées. Si le moment est relativement 
faible, la fondation excentrée peut se présenter sous la forme d’une 
semelle isolée carrée (fig. X.24A) ; si le moment est grand, on donne 
à la semelle la forme d’un rectangle dont le côté long est orienté 
dans le sens du moment. La surface de la semelle est calculée en admet- 
tant que la pression est répartie de façon linéaire, la pression maxi- 
male aux bords due aux charges caractéristiques n’excédant pas 
1,2 R,. 

La ‘surface à donner à la semelle est déterminée à l'aide de la 
formule (X.8) en introduisant un coefficient de 1,2 à 1,8 afin de tenir 
compte de l'influence du moment ; la hauteur est choisie de la même 
façon que pour une fondation centrée. Disposant de ces éléments, on 
dessine la semelle et l’on vérifie la pression exercée sur le sol au 
moyen des formules qui suivront. 

Introduisons quelques notations: 

äp, Côte de la section du poteau dans le plan du moment; 


At, — — de la fondation = en 
Dps — — du poteau dans le plan perpendiculaire : 
br, — — de la fondation = 


H hauteur de la fondation. 
Moment au niveau de la tranche inférieure de la fondation déter- 
miné par les charges caractéristiques: 


M = M° + Qc. (X.18) 


Force normale au niveau de la tranche inférieure de la fondation 


déterminée par les charges caractéristiques: ee 


Ns = NC + FiYmoyH1 (X.19) 
où À, est la profondeur de la fondation. 
Excentricité 
= ve (X.20) 


L4—0948 209 


Si << + (la force normale agissant dans les limites du noyau 


central), toutes les pressions présentes sur le diagramme des pressions 
sous la fondation sont de même signe (fig. X.24A, b). La pression 
aux bords p£ est cherchée par la formule 


(X.21) 


Le signe « + » dans (X.21) correspond à pn,, et le signe « — » 
à Pmin. Comme on l’a signalé plus haut, il doit y avoir 


mas < 1,2 R;, 


sinon il y a lieu de changer les cotes d'implantation de la semelle et 
de faire un nouveau calcul. 


Si >, l'effort normal se situe en dehors du noyau central: 


la pression + distribuée alors sur une partie de la surface de la 
semelle, le reste de celle-ci se trouvant décollé du sol (fig. X.24A, c). 
On détermine la pression aux bords ph: en admettant que le centre 
de gravité du diagramme des pressions triangulaire se confond avec 


la direction de la force excentrée Ms. 
La distance entre la force VS et le bord de la semelle f — _. — €. 


Ce point doit se confondre avec le centre de gravité du diagramme des 
pressions, aussi sa longueur sera-t-elle égale à 3f. Il est conseillé de 
faire en sorte que 3f > 0,75 at. 

La résultante du diagramme des pressions triangulaire, égale 
3f bt 


à Pmax , doit faire équilibre à V£, si bien que 


2N° k 
Par = mr S12R6. (X.22) 


Si le poteau subit des charges provenant d’un pont roulant, les 
fondations présentant un diagramme triangulaire sont à proscrire. 

Pour diminuer l’excentricité, il est parfois rationnel de décaler 
la fondation d'une longueur c par rapport à l’axe du poteau. Pour 
= s on retrouve une fondation centrée. On fait généralement 
e = 2/2. 

Pour déterminer la section à donner aux armatures d’une fonda- 
tion excentrée, on cherche lä poussée du sol provenant des charges de 
calcul M, N, 0 transmises par le poteau (sans tenir compte du poids 
de la fondation et du sol à ses tranches). Le moment de calcul au 




niveau de la tranche inférieure de la fondation est M, — M + QH, 


et l’excentricité e, — +. 


Si T on a 


N Ge . 
Ps arbt (1 ut 2.) ? (X.23) 
si € > on a 
Ps — 3btf . (X 24) 


D’après le diagramme de p, on cherche la valeur de la poussée 


sur le nu du poteau p?°*, puis sa valeur moyenne: 


max : ,pot 
moy — Ps T Pa 


moy = +, (X.25} 


Le moment fléchissant qui agit suivant le nu du poteau dans le 
plan du moment est calculé comme pour une fondation centrée: 


moy — 2 
Re (X.26) 


Le moment fléchissant qui agit dans le plan perpendiculaire Mr 
est déterminé en fonction de la poussée du sol p£f calculée sans tenir 
compte du moment fléchissant : 




Ps = Pr (X.27) 
Our (be— be)? 
M EE, (X.28) 


Les moments étant connus, on calcule la section à donner aux 
armatures dans chaque direction à l’aide de la formule (X.17). 


$ X.4. BATIMENTS INDUSTRIELS SANS ÉTAGES COMPOSÉS 
DE STRUCTURES PRÉFABRIQUÉES EN BÉTON ARMÉ 


Parmi les structures préfabriquées en béton armé utilisées dans les: 
bâtiments industriels à ossature sans étages (fig. X.25), on trouve. 
les poteaux avec fondations, les structures supportant la toiture sous 
forme de poutres, fermes, arcs, les panneaux de toiture, les panneaux 
de mur, les poutres de roulement (si le bâtiment est équipé d’un pont 
roulant) et éventuellement les éléments des lanterneaux d'éclairage: 
et d’aération. L’écartement des poteaux est choisi multiple du module- 
agrandi 6 m: on prend 12, 18, 24, 30, 36 m dans le sens transversal 


14% 211. 


(portée) et 6 ou 12 m dans le sens longitudinal (espacement). Si 
l'espacement des poteaux est de 12 m et la longueur du panneau de 
mur est de 6 m, on prévoit des poteaux intermédiaires (de carcasse du 
mur) dans les rangées extérieures. 






FIG. X.25. Bâtiment industriel sans étages avec ponts roulants composé de 
structures DE RAMEE en béton armé: 


1, panneau de toiture; 2, lanterneau; poutre de ROME 4, DAMPTES de roulement; 6, 
poteaux ; 6, Cote ente ments: , toitur 


La rigidité du bâtiment sans étages en direction transversale est 
assurée par le portique transversal formé par les poteaux encastrés 
dans la fondation et la poutre de toiture articulée aux poteaux 
(fig. X.25, b). La rigidité en direction longitudinale est créée par les 
portiques longitudinaux formés-par les mêmes poteaux avec la toi- 
ture et les poutres de roulement, ainsi que par les contreventements 
verticaux des poteaux (fig. X.25, c). On adopte l'articulation des 
poutres sur les poteaux malgré le fait que cette solution fait naître 
des moments fléchissants plus prononcés dans la poutre que la varian- 
te avec l’'encastrement (fig. X.26), car, comme on l’a signalé au 
$ X.1, elle permet d’adopter des solutions-types indépendantes pour 
les poutres et les poteaux ; les bâtiments industriels .étant construits 
en masse à partir de structures préfabriquées en béton armé, la typi- 
fication de celles-ci revêt une importance de premier plan. 




Si le bâtiment a la portée égale à 12 ou à 18 m, sa toiture est soute- 
nue le plus souvent par des poutres précontraintes en double T 
(fig. X.27). Elles sont fabriquées généralement par pré-tension, en 
béton des classes M 300 à 
M 500. L’armature de précon- 
trainte À,. est constituée par 
des barres à haute adhérence 
des classes A-IV à Ar-VI ou 
des fils à haute résistance. La 
section à donner à cette arma- 
ture est choisie de façon à 
assurer une résistance suffi- 
sante suivant la section nor- 


Fe d svenir la fi FIG. X.26. Diagrammes des moments 
n vue de prevenir 14 118-  Gans le portique d’un bâtiment industriel 
suration de la partie haute de sans étages: 


la poutre à cause des efforts a, les poteaux sont encastrés dans la poutre; 
de compression, on place quel- b, les poteaux sont articulés à la poutre 
quefois une armature de pré- 

contrainte aussi dans la zone comprimée (armature 4,.). L'âme 
de la poutre est armée d’une ou de deux nappes soudées dont 
les barres: transversales sont calculées pour résister dans les sections 
obliques à l'effort tranchant. Les zones d’about de la poutre sont 


FIG. X.27. Poutres de toiture précontraintes : 


a, vue d'ensemble et plan de ferraillage; b, disposition des armatures de précontrainte; 
1, armature de précontrainte longitudinale; 2, carcasses soudées de l'âme; 3, carcasses 
soudées de la membrure supérieure: 4, pièce scelléce d'appui; 5, carcasses supplémentaires 
dans les consoles d’appui; 6, treillis: 7, barres transversales soudées sur la pièce scellée & 


d’appui 


renforcées avec des barres transversales supplémentaires soudées sur 
une pièce scellée en acier, afin d'éviter la formation des fissures 
longitudinales lors de la mise en tension. La membrure comprimée 
supérieure contient une nappe d’armatures soudée. 




Chaque poutre est calculée en l’assimilant à une poutre à simple 
travée, exposée à une charge uniformément répartie provenant du 
poids de la toiture, de la neige et du poids propre. 

Si le bâtiment est équipé de poutres roulantes suspendues aux 
poutres de toiture, on doit, en calculant le moment fléchissant de 
calcul et l'effort tranchant de calcul, prendre en compte la charge 
de la poutre roulante sous forme d'efforts concentrés aux points de 
4) suspension des poutres de rou- 
lement. Les poutres doivent 
aussi être calculées suivant 
les états-limites d'utilisation 
(d'ouverture des fissures et 
de déformation). 

Fermes en béton armé. Les 
fermes sont utilisées pour sou- 
tenir la toiture aux cas où 
les portées sont de 18, 24 ou 
30 m fig. X.28). La mem- 
brure supérieure de la ferme 
FIG. X.28. Fermes de toiture en béton 2h pensent polygonale 

Re (fermes en segment), à l’excep- 

a, ferme polygonale monobloc; b, idem, {en tion du cas où la couverture 

deux pièces; e. ferme À membres paralllls. est plate : on utilise alors des 

sur chantier fermes à membrures paral- 

lèles. La hauteur de la ferme 

varie entre 1/7 et 1/9 de la portée. Le panneau (écartement des 

nœuds) est pris égal à 3 m, de telle façon que les panneaux nervurés 

de couverture, larges de 3 m, communiquent la charge à la ferme dans 

les nœuds de la membrure supérieure. Dans ce cas la membrure supé- 

rieure travaille en compression axiale uniquement. La membrure 

inférieure de la ferme subit une traction axiale, et les éléments du 

treillis (montants, diagofales), une compression ou une traction 
axiale. 

Les efforts engendrés dans les barres par les charges appliquées 
dans les nœuds sont cherchés par les méthodes classiques de Mécani- 
que des structures: graphiquement (diagramme de Maxwell-Crémo- 
na) ou analytiquement (méthode des sections). Dans les calculs, on 
admet que les barres sont articulées entre elles dans les nœuds; 
cette méthode n'est pas absolument rigoureuse (car en réalité les 
nœuds de la ferme sont, rigides), mais l'erreur n'est pas grande. 

Les membrures supérieures, les montants et les diagonales des 
fermes sont armés avec des carcasses soudées ; la membrure inférieu- 
re est précontrainte par pré- ou post-tension. En cas de pré-tension 
les armatures de précontrainte sont uniformément distribuées suivant 
la section de la pièce et entourées avec des cadres. En cas de post- 
tension les armatures de précontrainte sont placées dans les canaux 
qui, après mise en tension et ancrage, sont remplis de coulis de ciment 
sous pression (injectés). Les fermes sont fabriquées en une seule pièce 


ZINZNANAINIZIN 






Detatl 2 


Détail 3 
Détail 1 


Armature de précontrainte 
J000 2920 


2930 
30000/2 


S g 6AI esp 200 
ve [à 
[17 240 
26 20AÏ 
45 en canaux 
Détail 1 Détail 2 
320 Detail 3 
100 N 


Ancrages ELA Cadres $ $ esp 200 


FIG. X.29. Détails d’une ferme polygonale (membrure inférieure précontrainte 
‘en post-tension) 


(pour des portées non supérieures à 24 m) ou composées de deux moi- 
tiés. Dans ce dernier cas les parties de la ferme sont assemblées sur 
chantier, par soudage des pièces scellées en acier. | 

La figure X.29 représente une ferme en béton armé à membrure 
supérieure polygonale, précontrainte par post-tension des câbles 
à fils droits. 

Panneaux de toiture. La toiture est constituée par des panneaux 
précontraints nervurés de 3 x 12, 3 x 6, 1,5 x 12 ou 1,5 x 6 m, 
posés sur des poutres (pannes). Ils sont dessinés et calculés par analo- 
gie aux panneaux nervurés des planchers (voir $ X.2). | 

Si les poteaux sont espacés de 12 m dans le sens longitudinal, on 
peut employer les poutres et les panneaux pour l’espacement de 6 m 
à condition de prévoir des sablières longitudinales (poutres ou fer- 
mes, fig. X.30). 

On utilise de plus en plus souvent, dans la toiture des bâtiments 
industriels sans étages, des grands panneaux de3 x 18etde3 x 24m 
posés sur des poutres longitudinales appuyées sur les poteaux ou sur 




les murs portants longitudinaux (fig. X.31, a). Une telle solution 
permet de réduire le nombre d'éléments préfabriqués et de diminuer 
la dépense des matériaux et la main d’œuvre. 

Il existe deux types de grands panneaux précontraints: les 
panneaux nervurés à faible pente (fig. X.31, b) et les panneaux- 
voûtes K?KC (fig. X.31, c). 

Poteaux des bâtiments industriels sans étages. Les poteaux sont 
pleins (de section rectangulaire) ou à treillis, fabriqués de deux la- 
mes entretoisées (fig. X.32). 
La largeur de section b du 
poteau est choisie entre 40 
et 60 cm. La dimension de 
la section du poteau dans 
le plan du portique trans- 
versal (en présence des 
ponts roulants) est 

— dans la partie supé- 
rieure (baïonnette) A, = 
— 38 à 60 cm, afin d’as- 
surer un appui convenable 
aux poutres; 

— dans la partie infé- 
rieure (montant sous pou- 
tre) hi — 1/10 à 1/14 de 
, H}, de façon à assurer une 
FIG. X.30. Toiture à sablières d’un bâti- Lideur suffisante du poteau 


ment industriel sans étages: 2 
1, ferme de toiture : 2, ferme sablière; 3, panneaux (Hi étant la hauteur du 


de toiture; 4, poteaux poteau entre la tranche 

supérieure de la fondation 

et la partie basse des poutres de roulement). Dans un poteau 

plein on a généralement h, — 60 à 80 cm, et dans un poteau à deux 

lames k; — 120 à 160 cm. La dimension de la section d’une lame est 

h1 = 25 à 35 cm, la distance séparant les entretoises voisines s — 
= 2 à 3 m. 

Soumis à une force de compression longitudinale et à des moments 
fléchissants dans le plan du portique transversal, les poteaux travail- 
lent en flexion avec compression. Les armatures principales longi- 
tudinales sont placées près des faces perpendiculaires au plan du 
moment. 

Les moments fléchissants dans les poteaux sont déterminés lors 
du calcul du portique amie Si les poutres sont situées à un 
même niveau dans toutes les travées, il est commode de faire le 
calcul par la méthode des déplacements, car, quel que soit le nom- 
bre de travées, on n’a qu’une seule inconnue: c'est le déplacement 
linéaire de la tête des poteaux. 

On obtient le système fondamental en introduisant une liaison 
linéaire horizontale qui s'oppose au déplacement horizontal de la tête 
des poteaux (fig. X.32A, a). Ainsi donc, tous les poteaux (montants) 




Suivant I-I 
30 30 3,0 30 


Suivant I-IT 


L30_ À 
CL 00 


23960 


FIG. X.31. Toitures à grands panneaux des bâtimentsfindustriels sans étages: 
1, poteau; 2, poutre longitudinale; 3, grand panneau 




du système fondamental sont encastrés à une extrémité (dans la 
fondation) et articulés à l’autre. On trouve en Annexe XIX les réac- 
tions qui se produisent dans les montants de ce type pour différents 
cas de charge, calculées par les méthodes classiques de Mécanique 
des structures. Un déplacement unitaire À = 1 fait naître des mo- 
ments dans les montants et des réactions BA dans la liaison 
(fig. X.32A, b). De même, les charges extérieures font naître des 
moments dans les montants sollicités et des réactions B, dans la 
liaison (fig. X.32A, c, d, e). Pour chaque cas de charge on établit 
une équation canonique qui traduit la nullité de toutes les réactions 
dans la liaison linéaire horizontale, car cette liaison est inexistante 
en réalité. Soit r, la réaction dans la liaison provoquée par le dépla- 
cement de tous les montants d’une quantité À = 1. Elle est égale 
à la somme des réactions de tous les montants du portique au dépla*” 
cement linéaire, ry, — 2B4. 

Le déplacement étant égal à une quantité concrète À, la réaction 
dans la liaison sera égale à r,,A. 

Soit r1p la réaction engendrée dans la liaison par les charges 
exercées sur les montants. Elle est égale à la somme des réactions B, 








UE ILE TIR 
COL LL OL L L 1 


LL ELULELLLELLILIIITETTILT 
= €] + 






nus te M Ge 20 un nn 


3 | : 
jante sue 
En! 2 It E dI 
hinf 
Rine FRS 


fran 






FIG. X.32. Poteaux des bâtiments industriels sans étages: 


a, Sans pont roulant;:b, avec pont roulant; ce, idem, à deux lames; 1, armature longitu- 
dinale principale; 2, cadres 


de tous les montants sollicités du portique, r,, = 2B,. L'équation 
canonique s’écrira donc sous la forme 


r11À + ip — 0. 


Le coefficient de l’équätion canonique r,, — 2B\ reste constant, 
quel que soit le cas de charge du portique. Le coefficient r,, — 2B;, 
doit être calculé séparément pour chaque cas de charge (compte tenu 
des signes de B;,); de même, on doit calculer pour chaque cas de char- 
ge le déplacement 




Après avoir déterminé: À das’ chaque montant, on calcule la 
réaction élastique 
Ba Fe BAAÂ + B}. 


Si le montant en question ne subit aucune charge, on a B, = 0. 

Le diagramme des moments sur chaque montant est construit 
comme pour une console encastrée dans la fondation dont l’extré- 
mité libre subit la force Ba et sa propre charge extérieure. 




En calculant la résistance du portique aux surcharges de pont 
roulant, on prend en considération le travail de l’ossature en trois 
dimensions, vu que les portiques transversaux non sollicités parti- 
cipent au travail de l’ossature à cause du disque rigide de la toiture. 
Pour en tenir compte, on introduit dans l'équation canonique un 
coefficient spatial c,, égal à 4 (pour 
l'espacement des portiques de 6 m) 
ou à 3,4 (pour l'espacement des 
portiques de 12 m): 


re ! *. — 
Capl11À E lip = O. 


On peut poser sans grande erreur 
pour les surcharges de pont rou- 
lant À = 0. 

Après avoir tracé le diagram- 
me des moments pour chaque cas 
de charge, on compose le tableau 
des efforts de calcul dans les sec- 
tions caractéristiques du poteau: 
au-dessus de la console de pont 
roulant, immédiatement sous la 
console et au niveau de la tranche 
supérieure de la fondation. Si le 
poteau est de section constante 
(sans pont roulant), on retient pour 
le calcul la section basse. On 
inscrit dans le tableau pour cha- 


P vent 


FIG. X.32A. Pour le calcul du 
portique transversal d’un bâtiment 


que section le moment et l'effort 
normal (et aussi l'effort tranchant 
si le poteau est à deux lames) 
provenant de chaque cliarge, après 


industriel sans étages: 


a, Système tondamental; 4, réactions 
et diagrammes des moments dans les 
montants, engendrés par un déplacement 
A =1:c, réactions et diagrammes des 
moinents provenant de la surcharge ver- 


ticale de pont roulant; d, idem, de l’ef- 


quoi on s'établit sur une combinai- 
fort de freinage; e, de l’a:tion du vent 


son défavorable possible des char- 
ges. 

Le choix de la section à donner aux poteaux consiste à calculer 
la section à donner aux armaturés F, et F; dans les sections retenues 
d’après les formules de flexion avec compression. Les longueurs de 
flambement des poteaux sont prises égales à 

L = 1,9 À pour une travée unique et Z, = 1,2 H pour deux ou 
plusieurs travées si le bâtiment n’a pas de pont roulant ; 

l — 1,9 Hinr dans le montant sous poutre et !, — 2,5 H,4, dans 
la baïonnette si le bâtiment est équipé d’un pont roulant qui & 
déplace sur des poutres de roulement à travées indépendantes (comp- 
te tenu de la charge de pont roulant, on a l, — 2H,un). 

Si le poteau est à deux lames, on commence par calculer les efforts 
dans les lames. La force de compression longitudinale W est répartie 
à raison égale sur les deux lames, tandis que le moment fléchissant 
commun M du poteau a pour effet d'augmenter l'effort dans une 




lame et de diminuer celui dans l’autre d’une quantité A/c, où c est 
l’entraxe des lames. Compte tenu du flambement du poteau, on prend 
le moment égal à An, où la quantité n est calculée selon la for- 
mule VII.9. On a donc 




Si Mn/c > N/2, il se produit une traction dans l’une des lames. 

Les moments fléchissants dans les lames du poteau sont définis 
par l'effort tranchant Q. On les cherche en admettant que les points 
zéros du diagramme des moments sont situés à mi-longueur des pan- 
neaux s$: 


Me SX = 


La section à donner aux armatures d’une lame est calculée d’a- 
près les formules de flexion avec compression (ou avec traction), 
compte tenu de l'effet cumulé des efforts N,et M. 

Les entretoises d’un poteau à deux lames travaillent en flexion. 
Les efforts dans une entretoise sont 

s 2M s 
Mont = ; Qent = EL =. 

Le flambement du poteau dans le Tr perpendiculaire à celui du 
portique transversal est vérifié en tenant compte de la force longitu- 
dinale W appliquée avec une excentricité accidentelle. 


$ X.5. BATIMENTS DES RÉSEAUX DE DISTRIBUTION 
ET D'ÉVACUATION DES EAUX ET BATIMENTS 
DES CHAUDIÈRES 


Les réseaux de distribution des eaux comportent des bâtiments 
destinés aux stations de pompage de première et de deuxième éléva- 
tion et de circulation, aux filtres, bassins de clarification, adoucis- 
seurs, etc. ; les réseaux d'évacuation des eaux comprennent les bâti- 
ments qui ‘abritent les stations de pompage, les soufflantes, les pom- 
pes à boues, etc. 

Il est recommandé d’implanter des installations d'usage diffé- 
rent, autant que possible, dans un même bâtiment, afin de dimi- 
nuer le volume de construction, la surface bâtie et la longueur des 
canalisations souterraines, ce qui permet de réduire le coût et les 
délais de la construction. 

On distingue des bâtiments de surface, semi-enterrés (le plancher 
étant situé légèrement au-déssous du niveau du sol), enterrés (plan- 
cher nettement plus bas que le sol) et souterrains. 

La plupart des bâtiments sont équipés de moyens mécaniques de 
levage et de manutention, tels que le monorail, la poutre roulante, 
le pont roulant, prévus pour assurer le montage et le service des 
équipements technologiques. 

Les bâtiments incorporés dans les réseaux de distribution et d’éva- 
cuation des eaux peuvent avoir les murs portants en briques et Îles 


2 20 


CSS AN 
ER ER RRRIEE RSR Enr 


— 1,65 


> _ + Nappe 
_4A Phréatique 




LL SSD NS SI 


pe | 
NRA Ve 7 


N SU S TAN AR 


CAL. 


FIG. X.33. Station de pompage dans un réseau d'évacuation des eaux 


planchers en béton armé. La partie enterrée du bâtiment est clôturée 
par des murs massifs en maçonnerie ou en béton; si elle est très 
profonde ou si la nappe phréatique (plan des eaux souterraines) est 
proche de la surface dusol, la partie enterrée du bâtiment est réalisée 
sous forme d’un caisson ouvert (fig. X.33). 

Le projet-type de bâtiment utilisé dans les réseaux de distribu- 
tion et d'évacuation des eaux est un bâtiment à travée unique aux 




portées de 6, 9, 12 ou 18 m. La hauteur de la partie de surface (mesu- 
rée entre le sol et la tranche inférieure de la toiture) varie entre 3,6 m 
et 9,6 m (de 1,2 en 1,2 m) si le bâtiment est équipé d’une poutre 
roulante et est égale à 12,6 m si le bâtiment est doté d’un pont rou- 


_—_ 7 Fini 
Poutre y 
roulante 2 


To LS du bâtiment semi enterré — ro 
es 7. | à; RE — 
Ale 6000 EE 




FIG. X.34. Schémas-types des bâtiments de 6 m de portée (de surface et semi- 
enterrés) utilisés dans les réseaux de distribution et d'évacuation des eaux 


lant. La profondeur de la partie souterraine des bâtiments semi- 
enterrés est de 1,2 m, enterrés de 2,4 à 6 m (de 1,2 en 1,2 m), souter- 
rains de 6 m. La partie de surface est réalisée selon le projet-type 
de bâtiment industriel sans étages (voir $ X.4) composé d’éléments- 
types préfabriqués en bé- 
ton armé (poteaux, pou- 
tres, panneaux de toiture, 
panneaux des murs). La 
partie enterrée est compo- 
sée de panneaux préfabri- 
qués en béton armé utili- 
sés pour les réservoirs et 
les installations d’épura- 
tion rectangulaires (voir 
$ XI.4). Si le bâtiment 


FIG. X.35. Schéma-type d’un bâtiment de rencontre la L cr D 
9, 42 ou 18 m de portée utilisé dans les ré- due, on emploie du béton 
seaux de distribution et d'évacuation des Coulé sur place pour le 

eaux fond, et parfois pour la 


partie enterrée tout entière. 
Si la portée est égale à. 6 m>-la partie de surface du bâtiment 
possède les murs extérieurs portants (généralement en maçonnerie 
de briques) qui supportent les dalles de toiture en béton armé de 
3 x 6 ou de 1,5 x 6 m (fig. X.34). Si la portée est de 9, 12 ou 18 m, 
la partie de surface est dotée d’une ossature constituée de poteaux 
espacés de 6 m, de poutres de toiture à simple travée et de panneaux 
de toiture de 3 x 6 ou de 1,5 %x 6 m. Du côté extérieur des poteaux 
sont disposés des murs-rideaux constitués de panneaux des murs sus- 
pendus. Les poutres roulantes sont accrochées aux poutres de toiture 
(fig. X.35). 




Le bâtiment d'une station de pompage de 18 m de portée équipé 
d’un pont roulant présente des poteaux à deux lames. 

Les murs de la partie enterrée du bâtiment sont constitués par 
des panneaux préfabriqués en béton armé de longueur nominale 
(dans le sens de la longueur du bâtiment) 3 m et de hauteur conforme 
à la profondeur : 2,4; 3,6; 4,8 
ou 6 m. Les panneaux sont 
fixés dans la rainure longi- 
tudinale d'une semelle filante 
en béton armé; les jeux de 
la rainure sont remplis de bé- 
ton à pierres cassées de faible 
granulométrie. Un tel mode de 
fixation garantit un bon encas- 
trement des panneaux dans FIG. X.36. Murs enterrés en panneaux 
la fondation; les panneaux préfabriqués : 
sont susceptibles de reporter … }: als en attente agudés et enropés de béton: 
la pression latérale du sol à ciment sous pression 
la manière d’une console 
(fig. X.36). Les panneaux hauts de 2,4 m ont une épaisseur constan- 
te de 15 cm; les panneaux de hauteur 3,6; 4,8 et 6 m ont une épaisseur 
de 20, 28 et 36 cm respectivement dans leur partie inférieure et de 
14 cm dans leur partie supérieure À). 

On voit sur la figure X.37, a, b quelques schémas-types adoptés 
pour les bâtiments enterrés qui ne rencontrent pas la nappe phréa- 
tique. 

Les poteaux sous toiture sont engagés dans le logement d’une 
semelle individuelle en béton armé aménagée entre deux portions 
voisines de la semelle filante des panneaux (fig. X.37, détail À). 
Afin d'éviter que les poteaux reportent la pression du sol, un espace 
libre de 50 mm est prévu entre les panneaux des murs de la partie 
enterrée du bâtiment et le poteau. Les murs portants de surface 
reposent sur les panneaux enterrés. 

Si la partie enterrée rencontre la nappe phréatique, le fond est 
constitué par une dalle (radier) en béton armé munie de rainures pour 
recevoir les panneaux des murs (fig. X.38, a, b). Si la nappe phréati- 
que est très élevée (2 ou 3 m), on est obligé de construire toute la 
partie enterrée (le fond et les parois) du bâtiment de 12 et de 18 m de 
portée sous forme d’un caisson en béton armé coulé en place 
(fig. X.38, c). 

Les murs enterrés ne rencontrant pas la nappe phréatique sont 
recouverts extérieurement d'un enduit d'étanchement (bitume chaud);* 
en présence des eaux souterraines, les murs sont garnis d’une couche 
étanche collée jusqu’à une hauteur d’au moins 0,5 m supérieure au 
niveau maximal de la nappe phréatique. Sur les faces latérales, la 


4) Ces panneaux seront décrits en détail dans le $ XI.4. 






EP Æ — AUNNNNRANNNAAN 




FIG. X.37. Bâtiments des réseaux de distribution et d'évacuation des eaux non 
exposés à la pression des eaux souterraines: 


«, bâtiments de 9 à 18 m de portée; b, bâtiments de 6 m de portée; 1, panneaux des murs 
enterrés; 2, poteau; 3, semelle filante en béton armé; 4, semelle individuelle d’un poteau: 
5, plate-forme de service en panneaux préfabriqués 




Noppe phr. 


RS: RE QU 






Le 1 


FIG. X.38. Bâtiments des réseaux de distribution et d'évacuation des eaux ren- 
contrant la nappe phréatique 






PP LD PP DD PTT T LE LIL 
NS ISII II IIIIIT 


e pars 




EE ESS 






OO pustsnr CO CLONE 
É Tor AT 


FIG. X.39. Stations de pompage souterraines: 


a, en l’absence des eaux souterraines; b, en présence des eaux souterraines; 1, panneaux de 

plancher; 2, panneaux des murs; 3, semelles filantes; 4, fond en béton armé exposé à la 

pression des eaux souterraines; 5, muret en briques; 6, couche de matériau calorifuge ; 

7, tapis d’étanchement ; 8, poutrelles transversales; 9, poutre roulante; 10, couche d'étan- 
chéité: 11, couche de propreté en béton:.12, muret de protection 


15—0948 225 


couche étanche collée est protégée par un muret en maçonnerie de 
briques épais de 1/2 brique. 

Les bâtiments souterrains des stations de pompage ont une portée 
de 6 m et une profondeur de 6 m. La solution retenue est la même 
que précédemment; les panneaux des murs hauts de 6 m (5,4 m) 
sont engagés dans les rainures des semelles filantes ou, en présence 
des eaux souterraines, dans celles du radier coulé en place (fig. X.39). 
Les dalles de toiture sont posées directement sur les panneaux des 
murs. Les poutrelles transversales en acier servant à accrocher le 




Surcharge P 


Psot Rurt 


FIG. X.40. Charges horizontales exercées sur la partie enterrée du bâtiment: 
a, en l’absence des eaux souterraines; b, en présence des eaux souterraines 


monorail sont appuyées sur des tasseaux soudés sur les pièces scellées 
des panneaux des murs. 

La partie de surface des bâtiments utilisés dans les réseaux de 
distribution et d'évacuation des eaux est calculée selon la méthode 
exposée dans le $ X.4. 

Les panneaux des murs enterrés subissent une charge horizontale 
due à la pression latérale dy sol p,,, et une surcharge due à la pres- 
sion du sol en surface Deurr; en présence des eaux souterraines, ils 
reprennent également la pression des eaux Peau (fig. X.40). Le 
mode de détermination de ces sollicitations est décrit dans le $ XI.8. 

Pour le calcul du moment fléchissant, on assimile le panneau de 
mur à une console verticale (large de 1 m) encastrée dans la fonda- 
tion. Connaissant le moment, on cherche la section à donner aux arma- 
tures verticales tendues près de la face supérieure du panneau. Si les 
panneaux des murs reprennent une charge verticale provenant du 
poids des murs de surface, ils"$e trouvent exposés à un moment 
fléchissant et à un effort normal à la fois : dans ce cas le pourcentage 
des armatures suivant les deux faces du panneau est cherché d’après 
les formules de flexion avec compression (voir $ VII.2). 

La fondation des panneaux des murs est toujours excentrée : elle 
éprouve la résultante des pressions latérales du‘sol £, le poids des 
panneaux des murs et des structures superposées À, le poids propre 
de la fondation Q;, ainsi que le poids du sol situé sur la tranche de 


la fondation Q, (fig. X.41). 
226: 


La fondation est généralement excentrée vers l’extérieur, afin 
que le moment produit par ©, soit de signe opposé à ceux engendrés 
par E, Net Q:: de cette façon la pression sous la semelle devient plus 
uniforme. 

Si le bâtiment rencontre la nappe phréatique (fig. X.42), son 
fond éprouve une pression supplémentaire en direction ascendan- 
te Pasc. On a par unité de surface du fond 


Pase — Ÿ H, 


où y est la masse volumique de l’eau et X la distanice entre la surface 
inférieure du fond et le niveau maximal (compte tenu des fluctua- 
tions saisonnières) de la nappe phréatique. 


Nappe 
phréatique 


FIG. X.41. Charges exercées FIG. X.42. Pour le calcul de flottabi- 
sur la semelle filante des pan- lité du bôêtiment rencontrant la nappe 
neaux des murs dans un bô- phréatique 


timent enterré 


Puisque y = 1, la pression ascendante est égale en valeur à J. 
On calcule la plaque en béton armé du fond à la flexion sous l’action 
de pas; en outre, le bâtiment dans son ensemble doit faire l’objet 
d'un calcul spécial de flottabilité d’après la formule 


G< P, 
où G est le poids du bâtiment affecté d’un coefficient 0,9 et P la 
résultante des poussées ascendantes affectée d’un coefficient das 
surcharge 1,1: 
P = 1,1 pascFt 
où F! est la surface du fond. 


En calculant le poids du bâtiment s’opposant à sa remontée dans 
l’eau, seuls seront pris en considération les éléments qui seront 


15* 227 


construits pendant l'abaissement de la nappe phréatique réalisé 
artificiellement pendant la durée des travaux. On conçoit donc que 
le fond peut avoir une épaisseur considérable. 

Les bâtiments des chaudières sont construits à partir d'éléments 
préfabriqués en béton armé qu'on utilise dans les bâtiments indus- 


Suivant I-I 


16,20 


10,20 


16350 




6000 


FIG. X.43. Bâtiment des chaudières: 
1, plates-formes de service; 2, poteaux supportant lcs plates-formes de service 


triels sans étages (voir $ X.4). [ls ont une portée de 12 à 24 m et une 
hauteur de 6 à 14,4 m. Des étagères spéciales aménagées dans les 
bâtiments facilitent le service des chaudières. La figure X.43 montre 
une variante de bâtiment abritant des chaudières dutype JAKBP-20-13. 


CHAPITRE XI 


OUVRAGES SPÉCIAUX DANS LES RÉSEAUX 
DE DISTRIBUTION ET D'ÉVACUATION DES EAUX 


s XI. GÉNÉRALITÉS 


En construisant un réseau de distribution et d'évacuation des eaux, 
on prévoit un grand nombre de bâtiments du type réservoirs qui 
servent au transport, au stockage et à l’épuration des eaux et des 
effluents. Ces ouvrages sont fabriqués généralement en béton armé. 
Ils peuvent être cylindriques ou rectangulaires, situés en surface ou 
être enterrés (complètement ou partiellement), être couverts ou non, 
avoir un fond plat ou conique. 

La configuration et les dimensions sont dictées par le procédé 
technologique utilisé. Dans les cas où la technologie n’impose que la 
capacité (réservoirs à eau), on choisit la forme et les dimensions 
d'après les considérations technico-économiques. 

En choisissant entre la solution cylindrique et la solution rectan- 
oulaire, on doit se rappeler que, la contenance étant la même, la 
longueur développée des parois d’un réservoir cylindrique est plus 
petite que celle d’un réservoir rectangulaire. En outre, la pression 
hydrostatique interne fait travailler la paroi cylindrique à la trac- 
tion simple et la paroi plane à la flexion (avec traction). De ce fait, 
les réservoirs à eau en acier ont toujours une forme cylindrique et 
sont confectionnés à partir de tôles minces. La forme cylindrique 
offre d’ailleurs beaucoup d'avantages dans le cas du béton armé 
également, car elle facilite la réalisation de la précontrainte (fret- 
tage). Une paroi précontrainte résiste mieux à la fissuration et per- 
met de diminuer la dépense de béton (moindre épaisseur) et d'acier 
(armatures à haute résistance). 

Dans la paroi cylindrique les efforts de traction sont directement 
proportionnels au diamèêtre ; plus le diamètre est grand (la profondeur 
restant la même), plus la paroi doit être épaisse et plus la section 
des armatures principales sera importante. 

Dans le mur d’un ouvrage rectangulaire, les moments fléchissants 
sont définis uniquement par la hauteur; on peut donc, sans changef” 
l'épaisseur du mur ni la section donnée aux armatures principales, 
réaliser des réservoirs dont les cotes d'implantation sont nettement 
différentes. 

Ün devis estimatif comparé montre que les réservoirs en béton 
armé de forme cylindrique permettent de réduire la dépense des 
matériaux par rapport aux réservoirs rectangulaires tant que la 




capacité ne dépasse pas 2000-3000 m°. Avec une capacité plus 
grande la dépense des matériaux devient sensiblement égale, et 
à partir d’une capacité de 5000 à 6000 mÿ la situation est inversée 
au profit de la forme rectangulaire. Il y a aussi des cas où, même pour 
une contenance modeste, le réservoir rectangulaire est à préférer 
à un réservoir cylindrique. Par exemple, les décanteurs (clarifica- 
teurs) installés dans les stations d'épuration occupent moins de place 
au sol en cas de forme rectangulaire, ce qui permet de diminuer le 
volume du bâtiment. L'implantation serrée des appareils est très 
économique dans tous les cas: surface occupée plus petite, moins de 
frais d'aménagement, clôture moins longue, 

Les paramètres technico-économiques des réseaux de distribution 
et d'évacuation des eaux sont sensiblement affectés par la hauteur 
(la profondeur) des ouvrages (réservoirs) enterrés. Plus la hauteur est 
importante, plus les pressions exercées sur les parois sont fortes, plus 
les conduites d’adduction et de collecte sont profondes, et plus les 
travaux de chantier sont difficiles. Exception faite du cas où la 
hauteur de l'ouvrage est assujettie à la technologie de traitement, on 
choisit généralement une hauteur de 4,8 m; si la capacité du réser- 
voir n’est pas grande, on descend même jusqu’à 3,6 m. 

Les réservoirs en béton armé incorporés dans les réseaux de distri- 
bution et d'évacuation des eaux peuvent être coulés en place ou 
préfabriqués. Ils peuvent aussi être partiellement préfabriqués: par 
exemple, le fond est coulé en place mais les murs et la toiture sont 
composés d'éléments préfabriqués. On rencontre également des murs 
coulés en place et une toiture préfabriquée. La préfabrication permet 
de diminuer la main d'œuvre, la dépense des matériaux, les délais des 
travaux. 

Les dimensions modulées et les schémas-types retenus pour les 
réservoirs les plus courants permettent d'adopter une gamme assez 
restreinte d'éléments préfabriqués qui, combinés avec les éléments- 
types existants des bâtiments industriels, couvrent la totalité des 
ouvrages utilisés dans les réseaux de distribution et d'évacuation des 
eaux. 

En vue d’assurer l'étanchéité à l’eau, le fond et les parois des 
réservoirs sont fabriqués en béton dense et lourd qui a une classe de 
résistance à la compression non inférieure à M 200, une classe d’étan- 
chéité à l’eau non inférieure à B4-B8 et une classe de résistance au gel 
non inférieure à Mps3 100-Mp3 150. Les joints entre les éléments pré- 
fabriqués sont scellés avee’du béton au ciment expansif. 

Afin d'améliorer encore l’imperméabilité des réservoirs, on garnit 
leur surface intérieure d’une couche d’enduit en ciment, de béton 
projeté ou de polymère (vernis Ethynol, etc.). Si le liquide contenu 
est agressif vis-à-vis du béton (eau acide ou faiblement acide), on 
protège le béton avec du verre soluble, des enduits polymères à base de 
résines époxydes, etc. Si le réservoir souterrain est implanté dans un 
sol à bonne capacité de drainage en l'absence des eaux souterraines, il 
est isolé extérieurement par deux couches de bitume; pour certains 




appareils (bassins de boues activées, décanteurs) on prévoit une cou- 
che d’asphalte ou deux couches d’isol (hydroisol) au mastic de bitume 
entre la couche de propreté en béton et le fond du réservoir en béton 
armé. Si par contre le fond de l'ouvrage descend plus bas que la nappe 
phréatique, il y a lieu de protéger le fond par trois couches étanches 
collées au moins, et les parois par deux couches au moins, jusqu’à 
0,5 m au-dessus du niveau maximal des eaux souterraines. La couche 
isolante sur les parois est protégée par un muret en maçonnerie 
épais de 1/2 brique. Au-dessus des couches étanches collées, les parois 
sont protégées avec un enduit de bitume. 

Toutes les structures métalliques, les pièces scellées et les pièces 
de raccordement en acier sont protégées contre la corrosion en les 
recouvrant de vernis au perchlorure de vinyle, de pâte amiante- 
vinyle (mélange de vernis Ethynol et d'amiante), etc. Toute pièce qui 
ne peut pas être périodiquement enduite de peinture protectrice doit 
être zinguée. Dans un ouvrage couvert, tous les éléments delatoiture 
en béton armé seront également recouverts de peinture protectrice, car 
ils sont exploités dans les conditions d'humidité anormale. 

En faisant le choix du terrain de construction, on doit se rappeler 
que les réservoirs ne peuvent pas être implantés dans les sols affais- 
sés qui sont très sensibles au trempage. [1 faut éviter que le fond de 
l'ouvrage descende plus bas que la nappe phréatique, car cela com- 
plique singulièrement les travaux (nécessité d’abaisser le niveau des 
eaux souterraines) et oblige de donner une épaisseur supplémentaire 
au fond qui doit résister aux pressions verticales de l’eau souterraine. 
On se trouve obligé en outre, dans le cas signalé, de prévoir des 
couches étanches collées supplémentaires, ainsi que de prendre des 
mesures spéciales en vue de s'opposer à la remontée de l’ouvrage par 
flottation : faire un remblai plus épais sur la toiture (celle-ci devant 
être plus résistante), poser une couche de béton supplémentaire sur 
le fond et, pour certains ouvrages sans toit, les remplir obligatoire- 
ment d’eau pendant la période où la nappe phréatique est proche de 
la surface du sol, ce qui risque de perturber les conditions d’exploita- 
tion normale de l'ouvrage. 


$ XI.2. CONCEPTION DES RÉSERVOIRS CYLINDRIQUES 
EN BÉTON ARMÉE 


En plus des réservoirs à eau proprement dits, on range sous ce titre 
les décanteurs, clarificateurs, digesteurs de boues, aérofiltres, etc. 

Les réservoirs à eau remplissent les fonctions de régulation ou 
d'emmagasinage dans les réseaux d'alimentation en eau des agglomés 
rations et des entreprises industrielles. Ils sont généralement souter- 
rains, couverts, avec un fond plat. Un remblai de sol sur la toiture 
assure le calorifugeage nécessaire. En fonction de la température 
enregistrée en hiver, l'épaisseur du remblai varie entre 0,5 et 1 m. 
Dans certains cas on met en œuvre des matériaux particuliers à capa- 
cité d'isolation thermique accrue (bétons cellulaires, béton d'argile 




expansée, etc.). Les réservoirs surélevés (châteaux d’eau) ou posés 
sur les planchers des bâtiments sont généralement ouverts ). 
Les dimensions des réservoirs à eau cylindriques sont unifiées : 
— volume V = 50, 100, 150, 250, 500, 1000, 2000, 3000 ou 
6000 m° ; 
— diamètre (respectivement) D = 4,5, 6,5, 8, 10, 12, 18, 24, 
30 ou 42 m: 
— hauteur H = 3,6 m pour V< 250 m° et 4,8 m pour V > 
> 900 m°. 
Le fond est généralement coulé en place; les parois et la toiture 
sont en éléments préfabriqués. Si V< 2000 m°, le réservoir tout 
entier peut être réalisé en béton 
SI IL coulé en place. La paroi est pré- 
FPh contrainte par la mise en tension 
des frettes (cerces) disposées exté- 
rieurement. La paroi coulée en 
place peut être laissée sans pré- 
contrainte pour V << 500 m°. 
La toiture coulée en place du 
réservoir souterrain est générale- 
ment du type plancher-champi- 
gnon, appuyée sur les parois et 
les poteaux intérieurs munis de 
chapiteaux (fig. XI.1). Une telle 
toiture possède une faible hau- 
teur constructive et assure une 
bonne aération de l’espace au- 
dessus du plan d’eau. 
Les parois préfabriquées des 


: IN Ne x 
Fe ra 6000 réservoirs cylindriques sont ob- 
tenues par assemblage de pan- 


FIG. XI.1. Réservoir ain cylin- neaux dont la longueur est 
drique en béton armé coulé en place égale à la hauteur du réservoir. 


avec plancher-champignon Chaque panneau est mis verti- 
calement dans une rainure ap- 
propriée du fond (radier coulé en place) et fixé au moyen du mortier 
coulé dans les joints entre les panneaux. Après que le mortier dans les 
joints entre panneaux à durci, on met la paroi en tension par les 
frettes (cerces) qu'on recouvre ensuite d’une couche de béton projeté 
(fig. XI.2). Les poteaux fritérieurs ‘sous toiture sont posés sur des 
semelles disposées au-dessus des portions renforcées du fond. 

La toiture préfabriquée est généralement constituée par des pou- 
tres posées sur les poteaux et supportant des panneaux (fig. XI.3, a). 
Elle peut aussi être formée de panneaux carrés bordés de nervures 
directement posés sur les poteaux (fig. XI.3, b), ou encore de pan- 


1) Ou munis d’une toiture légère qui n’ajoute rien aux efforts exercés 
sur le réservoir. 




neaux nervurés de forme trapézoïdale en plan, posés radialement sur 
des poutres annulaires supportées par les poteaux (fig. XI.3, c). 

Dans les réservoirs à eau préfabriqués (fig. XI.4) les panneaux 
des murs sont tirés du catalogue des éléments préfabriqués pour les 
ouvrages des réseaux de distribution et d'évacuation des eaux, et 


Co nt M 


CSSS ST 


FIG. XI.2. Constitution de la paroi précon- 
trainte d’un ouvrage cylindrique en éléments 
préfabriqués : 


1, frettes de précontrainiec; 2, panneau du mur; 3, 
fond; 4, couche de béton projeté 




les poteaux, les poutres et les panneaux de toiture, du catalogue 
général des éléments préfabriqués pour les bâtiments industriels 
à étages. 

Les décanteurs verticaux (fig. XI.5) sont des réservoirs cylindri- 
ques ouverts à fond conique. L’eau clarifiée est évacuée par déver- 


FIG. XI.3. Constitution des toitures préfabriquées des réservoirs cylindriques: 
1, panneaux; 2, poutres; 3, parties coulées en place; 4, poutres annulaires 


sement annulaire. Une passerelle de visite est aménagée au-dessus duæ 
décanteur. Le fond conique est coulé en place. La paroi cylindrique 
peut être coulée en place ou préfabriquée. Elle n’est pas précontrain- 
te, vu le volume limité de l'appareil : diamètre entre 4 et 9 mètres, 
hauteur de la partie cylindrique 3,6 ou 4,2 m. 

Le même schéma est utilisé pour d’autres appareils: bioflocula- 
teurs, réservoirs à contact, capteurs de boues. 




QUAUIIO 9P J1FIOUI ‘OT 
‘919101 EI 9P 9OUId U9 S29[N09 5017 
-Jed ‘6 ‘91ef01d u0794 9p 9u9n09 ‘sg 
‘aqures}u099Jd 9p Sa)991j ‘£ : 217109 
op nvouuved ‘9 :orgnod ‘£ :Jnui np 
neouued ‘p ‘nvojod ‘£ ‘nvoiod 9p 
apouias ‘Z3 ‘998[d Uÿ 91N02 puoy ‘T 


-sonbriqeyord squows1o ue onb 
-HPUITAD HOAISSOU ‘Y'IX OL 


ROLE 


ÉQ_ E ! 


ÿ 710790 




% F7 
L'>7x2 DLL LL ZT A1 Le 


j 110}20 


2 710790 


/ 12078 


Les décanteurs radiaux sont des réservoirs ou bassins cylindriques 
ouverts de grand diamètre et de faible hauteur. Le fond présentant 
une pente douce de la périphérie vers le centre est généralement en 
béton coulé en place. La paroi peut être coulée en place ou préfabri- 
quée. L'eau clarifiée est éva- 
cuée par déversement annu- 
laire. Le schéma-type montré 
sur la figure XI.6 a les di- 
mensions unifiées: diamètre 
entre 18 et 42 m, hauteur 
I = 3, 3,6 ou 4,2 m. Pour 
H = 3,6 et 4,2 m la paroi 
est précontrainte. 

Le même schéma est adop- 
té pour les épaississeurs. 

Les  clarificateurs-diges- 
teurs ont un schéma analogue 
à celui des décanteurs verti- 
caux, à ceci près qu'ils com- 
portent une gaine cylindrique 
intérieure terminée par un 
fond conique et appuyé sur 
des montants appropriés (fig. 
XI.7). Les cotes unifiées sont 
indiquées sur la figure. 

Les aérofiltres cylindri- 
ques ont un fond plat coulé 
en place ave cun puisard cen- 
tral, une paroi préfabriquée 
et un faux-fond à claire-voie 
(fig. XI.8) formé par des 
barreaux normalisés posés sur 
des poutres préfabriquées. Di- 
mensions unifiées: diamètre 
6 à 30 m, hauteur 3 ou 4,8 m. 

Les digesteurs de boues 
sont des cylindres à toiture FIG. XI.5. Décanteur secondaire d’un 
conique. Leur capacité peut réseau DRÉMASUSEOE ee eaux en béton 
aller jusqu’à 3000, voire Te rte 
9000 m°. Fabriqués jusqu’à 
un temps assez récent à partir du béton armé coulé en place, ils 
peuvent désormais être confectionnés en éléments préfabriqué 
grâce à la précontrainte. 

La paroi coulée en place d’un réservoir cylindrique est armée 
avec un treillis double. L'épaisseur de la paroi ne sera jamais infé- 
rieure à 19 cm, afin d'assurer les conditions favorables de mise en 
place du béton. Les raccordements de la paroi avec le fond sont munis 
de congés qui améliorent la liaison. L’épaisseur du fond coulé en 




place pour les ouvrages de tous types sera non inférieure à 12 cm 
dans le sol sec et à 16 cm dans le sol imprégné d’eau. 

La paroi préfabriquée, comme nous l'avons déjà dit, est confec- 
tionnée à partir des panneaux verticaux engagés dans la rainure du 
fond dont la profondeur ne sera jamais inférieure à 1,5 fois l'épaisseur 
du panneau. 

La hauteur À des panneaux est choisie en fonction de la hauteur 
de l'ouvrage. Conformément au catalogue des éléments-types pour 


FIG. XI.6. Décanteur radial en éléments préfabriqués : 
1, fond coulé en place; 2, panneaux des murs; 3. déversoirs 


les ouvrages unifiés des réseaux de distribution et d'évacuation des 
eaux, on a À = 3 à 4,8 m (de 0,6 en 0,6 m). La largeur du panneau 
est prise multiple de x = 3,14; afin que n'importe quelle paroi 
puisse être réalisée avec un nombre entier de panneaux: b = x/2 — 
= 1,57 m, ou b — 3/4 x — 2,35 m. L’épaisseur ô à donner au pan- 
neau est déterminée par le calcul à la fissuration ; les épaisseurs nor- 
malisées sont Ô — 12, 14 et 16 cm. 

En section horizontale les panneaux peuvent avoir le profil en 
coquille (convexe-concave, fig. XI.9, a) ou plan-convexe (à surface 
intérieure plane et surface extérieure convexe, fig. XI.9, b). Les 
panneaux coquille nécessitent moins de béton que les panneaux plan- 




convexes (surtout quand le diamètre de l’ouvrage n’est pas grand); 
par contre, ils sont plus difficiles à fabriquer. 

Le catalogue indique pour les panneaux coquille les rayons À — 
— 3,6 et 9 m; ils sont utilisés pour des ouvrages jusqu'à 18 m de 
diamètre. Quant aux panneaux plan-convexes, ils conviennent aux 


1 D=6a30m 




JE? °°: Ésry Fue VOIV MP ! er 5 


H=3644,8m 


FIG. XI.7. Clarificateur-digesteur: FIG. XI.8. Aérofiltre cylindrique 


1, panneaux réfabriqués de la paroi exté- en éléments préfabriqués : 
rieure; 2, idem, de la paroi intérieure; 7, panneaux des murs préfabriqués; 2, treil- 
3, frettes de précontrainte lis Me barreaux; 3, fond couléen place; 
4, poutres 


ouvrages'dont le diamètre varie entre 24 et 42 m (le rayon de courbure 
de la surface étant R — 20 m). _ 

Les faces en bout verticales des panneaux des murs portent des 
rainures de profil triangulaire. Le scellement du joint entre pan- 
neaux avec du mortier de ciment refoulé sous pression fait naître une 
clavette de section en losange dans le joint, qui subit une compres- 
sion au cours de la mise en tension des frettes. Un panneau de mur est 
montré sur la figure XI.10. 




Les panneaux sont dotés de pièces scellées en acier destinées à la 
fixation des déversoirs annulaires (fig. XI.11) et des éléments de 
toiture (fig. XI.4, détail 7). 

Les panneaux des murs préfabriqués peuvent être assemblés avec 
le fond d'une façon rigide ou d’une façon mobile. L'assemblage rigide 
interdit tout déplacement radial 
de la paroi par rapport au fond; 
il est obtenu en remplissant le jeu 
entre les panneaux et les faces de 
la rainure annulaire du fond avec 
du béton à pierres cassées de faible 
granulométrie (fig. XI.12, a). 
Pour obtenir un assemblage mo- 
bile, on remplit le jeu de mastic 
FIG. XI.9. Vue en coupe horizon- de bitume froid qui se déforme 
_ tale des panneaux des murs préfa- pendant les déplacements de la pa- 

PRANÉFAPOUI CES eh ES cylindri-  »oi sans compromettre l'étanchéité 

q du joint (fig. XI.12, b). L'assem- 

blage rigide convient généralement 

aux réservoirs à eau, et l’assemblage mobile, aux décanteurs, clari- 

ficateurs et autres appareils incorporés dans les réseaux d'évacuation 
des eäâux. 

Pendant la durée des opérations de montege et d'ajustement des 
panneaux assemblés rigidement avec le fond, la rainure annulaire 


7 300 ) 4 Suivant 1-1 
2  1 S 
1500-1540 , : 
MO A 
R = 3000 - 93000 
à EURE, 
R = 20000 
FIG. XI.10. Panneaux des murs PPADEIQUES pour les ouvrages cylindriques 
unifiés : 


a, vue d'ensemble ; b, plan de ferraillage; 1, panneau coquille; 2, panneau plan-convexe 


sera provisoirement garnie de sable propreetsec, afin d'éviter l’encras- 
sement des jeux ; en outre, la paroi peut se déplacer alors au cours de 


238. 


la mise en terision des frettes (cerces), ce qui permet d'éviter l'appa- 
rition des moments fléchissants dans la paroi précontrainte (dans le 


plan vertical). La mise en contrainte 
terminée, on enlève le sable par souf- 
flage et l’on remplit les jeux de béton. 

Les frettes en fils de haute résis- 
tance sont mises en tension avec des 
engins spéciaux appelés spiraleuses 
(fig. XI.13). 

Les frettes en barres d’acier sont 
généralement mises en tension par les 
moyens  électrothermiques. (Chaque 
cerce est constituée de plusieurs bar- 
res aboutées dont chacune est munie 
de pièces d'extrémité courtes soudées 
bout à bout; une pièce d'extrémité 
est filetée, l’autre (lisse) est soudée 
sur un butoir d'ancrage particulier. 
Les pièces d'extrémité sont réunies 
dans le butoir au moyen d’écrous 


FIG. XI.11. Constitution du déversoir an- 
nulaire d’un ouvrage cylindrique: 


1, panneau du mur; 2, élément préfabriqué du 

déversoir; 3, pièces scellées en acier; 4, tasseau; 

5, aciers en attente soudés des éléments du déver- 

soir; 6, joint scellé avec du béton aux pierres 
cassées de faible granulométrie 


1350-2150 


(fig. XI.14). Après avoir positionné la cerce conformément au plan 
de ferraillage, on rattrape le mou des barres et l’on procède au chauf- 
fage électrique. Les barres s’allongent par dilatation; des jeux appa- 




4 5 : 
FIG. XI.12. Assemblage de la paroi cylindrique avec le fond: 


a, assemblage rigide ; b, assemblage mobile: 1, paroi; 2, héton aux pierres cassées de faible : 
granulométrie; 3, fond; 4, couche de propreté en mortier; .5, frettes de précontrainte; 
6, mastic de bitume; 7, mortier. d’amiante-ciment 






239 : 




— SERA 




FIG. XI.13. Mise en tension des frettes en fil de haute résistance au moyen de 
la spiraleuse AHM-5 


FIG. XI1.14. Accessoires des barres de précontrainte mises en tension par les 
moyens électrothermiques : 


a, mise en place des armatures de précontrainte sur la paroi cylindrique; b, barre isolée 

(élément de la cerce): c, butoir d’ancrage; 1, paroi: 2, frette de précontrainte; 3, butoir 

d'ancrage ; 4, pièce d'extrémité de gros diamètre; 5, pièce d'extrémité filetée; 6, boulon de 
‘ serrage; 7, pièce de retenue 




raissent entre les écrous et les butoirs. A cet instant on serre les écrous 
pour rattraper les jeux. Une fois refroidie, la cerce se trouve tendue, 
et la paroi, précontrainte. 

Il existe d'autres procédés de frettage de la paroi cylindrique: 
relevage des barres par vérins au-dessus du béton (diminution du 
frottement), calage des cerces 
fermées sur la surface conique Plan 
extérieure de la paroi, etc. 

Pour un réservoir de faible 
volume, on peut mettre en ten- SL 
sion les armatures (frettes) par = 
les moyens mécaniques (fig. 
XI.15). La cerce est constituée 
de plusieurs barres munies de 
pièces d'extrémité soudées et 
filetées; ces pièces d'extrémité 
sont assemblées sur des mon- 
tants métalliques verticaux et 
mises en tension par serrage des 
écrous avec une clé dynamomé- 
trique ou des vérins. Avant de 
procéder à la mise en tension des 
frettes, on attend que le mortier 
injecté dans les joints verticaux 
devienne suffisamment dur (70% 


au ES de sa résistance x1G. xI. 15. Mise en tension des fret- 
Rose e). tes par les moyens mécaniques: 
L'écartement des cerces peut 1, frettes de précontrainte: 2, pièce d’ex- 


varier largement, entre 15 ou trémité FRÉRSARE DRE OUUEE 3, mon- 
20 cm et 10 mm (cerces en fils . 
d'acier). 

Les frettes mises en tension sont protégées contre la corrosion par 
quelques couches d’enrobage en béton projeté ; l'épaisseur d’enrobage 
totale (mesurée à partir de la génératrice extérieure de la barre 
d'armature) est égale à 25 mm. La première couche d’enrobage est 
appliquée immédiatement après la mise en tension des frettes, et les 
autres, après la mise en eau, afin d'éviter la fissuration du béton 
projeté pendant les mises en eau ultérieures. La projection du béton 
ou l'application de l’enduit sur la surface intérieure de la paroi 
cylindrique est faite avant la mise en tension, afin de communiquer 
la précontrainte à la couche intérieure. 

En ce qui concerne le fond, sa résistance à la fissuration pet 
aussi être accrue par la mise en tension des armatures annulaires. 
Si la jonction fond-paroi est réalisée de la façon montrée sur la figu- 
re XI.16, le fond sera mis en précontrainte par les spires inférieures 
des frettes de la paroi. Cette solution convient aux réservoirs destinés 
au stockage du mazout et des hydrocarbures légers. Pour diminuer 
le frottement entre le fond et la couche de propreté en béton pendant 


16—0948 241 


la mise en précontrainte, on interpose une couche de sable. Deux 
couches de carton-feutre imprégné doivent être posées sur le lit de 
sable, afin d’éviter toute fuite de coulis de ciment pendant la coulée 
du fond. 

À mesure que les structures préfabriquées en béton armé devien- 
nent plus courantes, elles font l’objet de perfectionnements nou- 
veaux. Une nouvelle gamme d'’élé- 
ments-types pour les réservoirs dans 
les réseaux de distribution et d'’é- 
vacuation des eaux est à l'étude; 
elle prévoit l'usage des panneaux 
des murs du type coquille pour un 
seul diamètre de l'ouvrage (réser- 
voir cylindrique) D = 4,5 à 9 m 
(rayon de la surface courbe À — 
— 3 m); si l’ouvrage est plus grand, 
on utilisera des panneaux plan- 
convexes de À — 7,9 m pour D=9 


FIG. XI. 16. Mise en tension du 
fond par les frettes de précontrainte 
de la paroi : 


1, panneau du mur; 2, frette; 7, élé- 
ment préfabriqué du fond ; 4, fond coulé 
en place; 5, carton feutre imprégné; 
6, Sable; 7, couche de propreté en béton 


à 18 met de À — 15m pour D — 
— 24 à 50 m. La largeur du panneau 
est b — 1,5 m pour D<L18 m et 
b = 2 m pour D >= 18 m. Les pan- 
neaux sont assemblés entre eux par 


soudage des pièces scellées, puis 
le joint est injecté avec du mortier de ciment et de sable de classe 
M 300. Les panneaux coquille sont rigidement assemblés avec le 
fond ; l'assemblage des panneaux plan-convexes est mobile, obtenu 
grâce à l’utilisation de la pâte d'obturation au thiocol ou du bitume. 


$ XI.3. CALCUL DES RÉSERVOIRS CYLINDRIQUES 


Les parois des réservoirs cylindriques subissent la pression hydrosta- 
tique du liquide qui, on le sait, croît de façon linéaire avec la pro- 
fondeur (fig. XI.17, a). 

La pression caractéristique du liquide pt à la profondeur À comp- 
tée à partir de sa surface est égale à 


p® = yh, (XI.1) 


où y est la masse volumique du liquide. 
Le coefficient de surcharge pour la pression hydrostatique du 
liquide est n = 1,1, aussi la pression de calcul est-elle p — 1,1 y. 
On a pour l’eau y = 1, donc 


p=tih. (XI.2) 


La pression intérieure uniformément répartie sur la paroi fait 
naître une traction axiale dans cette dernière. On détermine sans 




difficulté l'effort de traction annulaire dans la paroi 7, en coupant 
par la pensée la section horizontale d'un cylindre de rayon r rempli 
de liquide suivant sa ligne de diamètre (fig. X1.17, b). La résultante 
de la pression hydrostatique p-2r est 
équilibrée par les efforts dans la paroi 
2T;5, d'où 


T, = pr =1;1 hr. (XI.3) 


Ainsi donc, abstraction faite de la 
liaison paroi-fond, les efforts de traction 
annulaires T, croissent de façon linéaire 
avec la pression hydrostatique. La paroi 
se déforme dans le sens radial d'autant 
plus fortement que les efforts annulaires 
sont plus élevés (fig. XI.18, a). En cas 
d'assemblage rigide de la paroi avec le 
fond les déformations de la paroi sont (ERER EELEEEE EP EEEEE ETS 
gênées dans ses parties adjacentes au 
fond et pratiquement inexistantes au \ 2r 7] 
niveau du fond, car ce dernier est inex- 
tensible. On voit donc la paroi s’incur- 
ver (fig. XI.18, b) et un moment fléchis- FIG. XI.17. Pour la déter. 
sant A7 et un effort tranchant (poussée) Q©  mination des efforts de trac- 
se produire suivant la génératrice du  t0n Re dans Ja paroi 
cylindre (dans le plan de la section sp ne 
méridienne). Les sollicitations À et Q 
prennent leurs valeurs maximales sur le contour (près du fond) et 
s'évanouissent rapidement avec la hauteur. 

Le diagramme de T, est semblable à celui de la pression hydro- 
statique : autrement dit, il a la forme d'un triangle d’ordonnée nulle 


a) b) 


Diagramme de To 
Diagramme de P Diagramme de T 






Diagramme de M 


FIG. X1.18. Efforts et déplacements engendrés par la pression hydrostatique 
intérieure dans les parois des réservoirs cylindriques ouverts: 
1, état initial; 2, état déformé 


en haut el d'ordonnée maximale près du fond. Quand la paroi est 
rigidement assemblée avec le fond, le diagramme des efforts annulai- 


res TZ est incurvé et présente des valeurs nulles en haut et en bas 
(fig. XI.18, b). " 


16+ 243 


La paroi est un voile mince cylindrique fermé symétrique par 
rapport à son axe. Une bande verticale de largeur b — 1 découpée 
dans ce voile mince peut être assimilée à une poutre encastrée en 
bas et sollicitée suivant toute sa 
longueur par des forces élastiques: 
ce sont les composantes radiales des 
efforts annulaires T (fig. XI.19). 
La flèche de cette bande est propor- 
tionnelle à la réaction élastique, ce 
qui permet de considérer la bande 
comme une poutre reposant sur 
un sol élastique caractérisé par un 
module de réaction unique. 

Les formules pour le calcul se 
FIG. XI.19. Pour le calcul de la laissent déduire de l'équation diffé- 

paroi cylindrique rentielle de flexion de la poutre 

reposant sur un sol élastique en se 

donnant des conditions aux limites correspondantes. L'effort de 

traction annulaire 7 dans une section quelconque de la paroi située 
à une distance x du fond est égal à 


T = To — Pmaxr M1 + No (À — s/1)], (XI.4) 


où 7, est l'effort annulaire dans la section considérée calculé d’après 
la formule (XI.3), c’est-à-dire sans tenir compte de la liaison entre 
le fond et la paroi; r, le rayon de l’ouvrage; /, la hauteur de la paroi; 
Pmax, la pression hydrostatique au point le plus bas de la paroi; 
s, la raideur caractéristique de la paroi: 


s — 0,76 V rô, (XI.5) 


où Ô est l'épaisseur de la paroi; n, et n, les coefficients intervenant 
dans le calcul d’une poutre reposant sur un sol élastique: 


M1 = 679 Cos pp; 2 — e”® sin . 


On trouve dans le Tableau XI.1 les valeurs de ces coefficients en 
fonction du paramètre @ = x/s, où x est la distance qui sépare le 
fond de la section considérée. 
L'épaisseur de la paroi peut être à priori prise égale à 
Ô = 0,5 rl > (12 à 15). (XI.6) 
Les valeurs de r et de / sont exprimées en mètres ; la formule donne Ô 
en centimètres. 


Le moment fléchissant dans la paroi est maximal au niveau du 
fond : 


M = RE s2 (1 — s/l). (XI.7) 


En cas d'assemblage mobile de la paroi avec le fond (la rainure 
annulaire étant garnie de mastic de bitume), les déplacements ra- 


‘244 


diaux de la paroi sont empêchés par la force de frottement Q,, qui 
agit à la base de la paroi: 


Qr = Nf, (XI.8) 


où {V est l'effort normal exprimé en kgf/m (N/m) et jf le coefficient 
de frottement pris égal à 0,5. 


TABLEAU X1.] 
Coefficients n, et 1: 


e [ol 0,1 | 0 0,3 | 0,5 0,8 1 | 1,2 1,4 
u [4 0,9004 | 0,7078 | 0,5323 | 0,313 | 0,1988 | 0,1092 | 0,0419 
»  0,0903 | 0,2189 | 0,2908 | 0,3223 | 0,3096 | 0,2807 | 0,243 


SUITE DU TABLEAU XI.1 


P | 16 | 1,8 | 2 22 | 21 5) 3,9 
M1 | 0 0059 0.087 00564 -0.0652 -0.0508 00408 0.02 
M2 | | 0,2018 | 0,161 | 0,1231 | 0,0896 | 0,0287 | 0,007 | 0,0106 


SUITE DU TABLEAU XI.1 


P | | 4 | 4,9 | 5 | 6 7 
M1 | | —0,012 | —0,0024 | 0,002 | 0,0024 0,0007 
M2 | | 0,0139 | 0,0109 —0,0065 | -—0,0007 —_0,0006 


Dans un ouvrage ouvert la force de frottement est due unique- 
ment au poids de la paroi, et dans un ouvrage couvert elle est produit8 
aussi par le poids de la toiture et du remblai (considéré dans une 
bande d'influence correspondante). En calculant la force de frotte- 
ment, deux cas sont à distinguer: 

1° le remblai est inexistant (cas de l'épreuve hydraulique de 
l'ouvrage) : 

2° le remblai est en place (cas de travail normal de l'ouvrage). 




Les efforts de traction annulaires dans la paroi sont 


T=T,— æ Qrri. (XL.9) 
Si l’on obtient d'après (XI.8) 
Qtr > PmaxS/2; 
il convient de poser *) dans (XI.9) 


Qfr — Pmaxs/2. (XI.10) 
Le moment maximal dû à Qf, se définit comme suit: 
M = QrrSne. (XI.11) 


Ce moment agit dans la section dont la distance au fond est 
z= 0,6 V rëô. (XI.12) 


Dans un ouvrage de faible contenance (non supérieure à 100 mÿ), 
on peut chercher les efforts de traction annulaires dans la paroi 
sans tenir compte de sa liaison avec le fond, c’est-à-dire en appliquant 
la formule (XI.3). 

Les formules citées pour le calcul des efforts de traction annulai- 
res et des moments fléchissants dans la paroi cylindrique provoqués 
par la pression hydrostatique intérieure caractérisent l’état de 
contrainte en service s'il s’agit d’un ouvrage de surface. Pour un 
ouvrage souterrain, elles sont applicables à l'épreuve hydraulique 
de l’ouvrage (absence de remblai). 

Le remblai fait naître des efforts de compression annulaires dans 
la paroi. On omet cependant de les calculer, car, lorsque l’ouvrage 
est rempli de liquide, ils ont pour effet d’atténuer les efforts de 
traction annulaires, et quand le réservoir est vide, ils sont repris 
par le béton de la paroi. 

L'ouvrage étant sans liquide, le remblai n'intervient que dans 
le calcul du moment fléchissant dans le plan méridien et de la sec- 
tion à donner aux armatures verticales correspondantes. La poussée 
latérale du sol, de même que la pression de l’eau, croît de façon 
linéaire avec la profondemr. A"üné profondeur À au-dessous de la 
surface du sol, la pression de calcul du sol est égale à 


Ps = Yshkn, (X1I.13) 


1) Cette restriction tient à ce que la formule (XI.9) donne 7 = 0 pour 
Qtr = Sn au niveau du fond. Par contre, si Qfr > ar , l'effort T chan- 


ge de signe: on a alors une compression au lieu de la traction, ce qui est évidem- 
ment absurde. 




où y, est la masse volumique du sol; », le coefficient de surcharge 
{égal à 1,2 pour le sol de remblai) ; #, un coefficient qui tient compte 
de la cohérence du sol, 


k = tg°? (45° — p/2) (XI.14) 


(g est l’angle de frottement interne). 

Au lieu de la surcharge exercée en surface du sol purs (de 1 à 
2,5 tf/m°?, ou de 10 à 25 kKN/m°), on introduit une épaisseur de sol 
équivalente hsurt = Psurt/Ys- Si la distance du sol (compte tenu de 


FIG. XI.20. Pression du sol sur un ouvrage souterrain 


hsurr) à la tranche supérieure de la paroi est k,, et à sa tranche infé- 
rieure, , (fig. XI.20, a), la poussée latérale du sol est en haut de 
la paroi 


Par = YshiAn 
et au bas de la paroi 
Ps2 = Yshohin. 


La paroi étant rigidement assemblée avec le fond, cette poussée 
fait naître un moment maximal 


s2 (1-2) s 
Ma= | 1 — 5 — |, (XI.15) 


Si l'ouvrage rencontre la nappe phréatique, la poussée latérale 
exercée sur la paroi au niveau du fond se compose (fig. XI.20, b) 
de la pression p, de la couche du sol de hauteur Æ7, (entre la nappe 
et le sol), de la pression pu, des particules du sol imbibé d’eau 
(dans les limites de la hauteur },) et de la pression de l’eau p.æ: 


Po = YsHink ; (XI.16) 

Paus = YsusAonk, (XI.17) 

où Ye: est la masse volumique du sol en suspension dans l’eau, 
Vous = (Ÿ' — Yean) (1 — M). 



où y; est la masse volumique des particules du sol; Veau, la masse 

volumique de l’eau (égale à 1); m, la porosité du sol en fractions 
d'unité ; 

Peau = Yeau?H) = 1,1H,tf/m° (11H,kN/m°);  (XI.18) 

Ps2 = Po + Paus + Peau: (XI.19) 


Les valeurs de Y%, nm, @ sont déterminées pendant la reconnaissan- 
ce du sol de fondation. Pour un terrain sablonneux on peut poser 
approximativement y, — 1,8 t/m°; Yu — 1,1 t/m° (avec y — 
— 2,7 t/m° et m — 0,35); œ@ — 40°. 

La résultante de la pression ascendante des eaux souterraines 
sur le fond de surface F} est égale à 


PS = YeauHoFr = H,Ft. (XL.20) 


Le poids de l'ouvrage sans eau G© (tenant compte du remblai sur 
la toiture), affecté d’un coefficient #7 — 0,9, doit être supérieur 
à la résultante de la pression ascendante affectée d’un coefficient 
de surcharge n = 1,1: 


0,9Ge > 1,1P°. (XI.21) 


On a déjà vu dans le $ XI.1 que cette condition ne peut être 
respectée pour certains ouvrages sans toit. De ce fait, l'ouvrage 
doit être rempli d’eau en permanence pendant la période où la 
nappe phréatique est située près du sol. 

Les efforts de traction annulaires dans la paroi du réservoir 
cylindrique sont calculés pour les sections échelonnées de 1 m (ou 
de 0,5 m) dans le sens de la hauteur. Pour chaque ceinture haute 
de 1 m, en partant de la valeur maximale de calcul de l’effort annu- 
laire (légèrement majorée), on détermine la section à donner aux 
armatures (frettes) : ; 


Fa = TIR. (XI.22) 


D'après cette section, on choisit le nombre nécessaire de barres 
pour 1 m de la hauteur de la paroi (dans la ceinture considérée). 

Si la paroi est fabriquée en béton non précontraint coulé en place, 
les frettes sont posées des deux côtés en respectant l'épaisseur d’enro- 
bage nécessaire. 

Si la paroi est précontrainte, les frettes font office d’armatures 
de précontrainte et se situent dù côté extérieur. 

Le calcul à la formation des fissures ou à leur ouverture est 
effectué pour la ceinture la plus sollicitée, conformément aux pres- 
criptions citées dans le chapitre V. On ne doit pas oublier que l'effort 
de traction 7 est une charge de longue durée. 

Les parois précontraintes !) doivent satisfaire aux conditions 
de résistance à la fissuration de première catégorie. La condition 


1) Si les frettes de précontrainte sont fabriquées en acier de classe A-IV ou 
des classes supérieures. 




de fissuration de la paroi sous l'effort annulaire de calcul T s'écrit. 
T < Ni, 


où West l'effort reporté par la paroi au moment de la fissuration. 
Si la paroi est coulée en place, on calcule W; d’après la formule 
(V.27). Pour une paroi préfabriquée, on cherchera V} sans tenir 
compte des frettes sans précontrainte (c'est-à-dire des armatures 
horizontales des panneaux) interrompues aux joints, ni de la contri- 
bution du mortier de scellement des joints. La formule s'écrit alors 
comme suit : 


TENo où TL Mmt0oF pe: (XI.23) 


où V, est la force de précontrainte; 0,, la précontrainte dans les. 
frettes de précontrainte après déduction de toutes les pertes; 7, 
la section des armatures de précontrainte; mm+, le coefficient de 
précision de la mise en tension égal à 0,9. 

Si le pourcentage des armatures n’est pas élevé, nu == F,c/F, 
<< 0,25 %, les valeurs retenues de F,. et de ©, doivent être vérifiées 
en outre en s’assurant qu'il se produit dans la paroi du réservoir 
plein (sans remblai) des compressions non inférieures à 8 kgf/cm° 
(0,8 MPa). 

Pour obtenir la formule de calcul, divisons les deux membres 
de (XI.23) par F, = 1006 cm°: 


Op = MmtOoù > 8 kgf/cm° (0,8 MPa). 


Une paroi sans précontrainte munie de frettes en acier des classes 
A-I, A-II, A-IIT doit satisfaire aux conditions de résistance à la 
fissuration de 3° catégorie. 

L'ouverture des fissures produites par l'effort annulaire dû 
à la charge caractéristique T° — T/1,1 ne doit pas dépasser 0,1 mm 
(at. 1a < 0,1 mm). 

La méthode de détermination de a; pour les pièces simplement 
tendues a été donnée dans le chapitre V. 

Les armatures verticales de la paroi sont calculées pour résister 
au moment fléchissant maximal. Les armatures situées du côté 
intérieur reportent les efforts de traction engendrés par le moment A 
de la pression intérieure du liquide (en l'absence du remblai), et 
les armatures situées du côté extérieur, les efforts de traction pro- 
duits par le moment M, du remblai (le réservoir étant vide). e 

On cherche la section à donner aux armatures en considérant 
une section rectangulaire de largeur b — 100 cm. Le plan de ferrail- 
lage de la paroi coulée en place est représenté sur la figure XI.21. 

Dans les panneaux préfabriqués les armatures verticales doivent 
en outre résister à la flexion du panneau pendant son transport et 
montage. Si les armatures verticales du panneau préfabriqué calcu- 




lées pour les sollicitations de montage s'avèrent insuffisantes pour 
résister au moment fléchissant en service, on prévoit un treillis 
supplémentaire dans la partie basse du panneau (fig. XI.10, b). 

Afin d’améliorer la résistance à la fissuration des panneaux de 
hauteur considérable pendant le transport et le montage, on prévoit 
des barres longitudinales supplémentaires précontraintes. 

Le fond d'un réservoir cylindrique est une dalle (radier) plane 
ou conique reposant sur un sol élastique et rigidement assemblée ov 
articulée avec la paroi suivant le pourtour. 

Si la pression ascendante des eaux souterraines n’est pas à crain- 
«re, le poids propre du fond et le poids du liquide se trouvent équi- 
librés par la réaction correspon- 
dante du sol. On voit des mo- 
ments fléchissants se manifester 
dans les parties du fond adja- 
centes à la paroi cylindrique et 
aux semelles des poteaux. 

Les formules citées plus haut 
pour la détermination des calculs 
dans la paroi cylindrique ont été 
déduites en supposant que la pa- 
roi est encastrée (ou fixée de 
façon mobile) dans le fond. Or, 
en réalité, la paroi, l'anneau 
d’assise prévu à la jonction de 
M, M la paroi avec le fond et le fond 

se déforment ensemble, si bien 
FIG. XI.21. Ferraillage de la paroi qu’on est obligé de les considé- 
d'un ouvrage Eu coulé en rer ensemble en déterminant les 
1, frettes ru, résister à l’effort efforts dans les éléments isolés 
T:2, armatures verticales calculées pour (fig. XI.22). [l en est de même 


liquide: 3, anabares verticales caleutécs Pour le travail du fond avec 
pour résister à MS dû à la pression du sol les semelles individuelles des 

poteaux. Puisque le calcul précis 
est assez délicat dans le cas considéré, on utilise en pratique des 
méthodes approchées. Par exemple, en étudiant la jonction paroi- 
fond, on envisage seulement le travail en commun de l'anneau 
d’assise et du fond sous les efforts V et M transmis sur l'anneau 
par la paroi (fig. XI.23, a), le fond étant assimilé à une poutre de 
forte longueur, de largeur”i, reposant sur un sol élastique et limitée 
par deux sections parallèles au diamètre. Les mêmes efforts sont 
pris en considération en étudiant la jonction du fond avec les se- 
melles des poteaux (fig. XI.23, b). 

La partie découpée de l’anneau d’assise (partie renforcée du 
fond sous la semelle du poteau) représente généralement une poutre 
rigide. Par poutre de forte longueur reposant sur un sol élastique, 
on entend une poutre présentant un rapport l/s > 8, et par poutre 
rigide, une poutre présentant un rapport li/s, < 0,75, où ZL (l) 


Di agramme de Ms 
Diagramme de M 




est la longueur de la poutre et s (s,) la raideur caractéristique ?): 
447 4EJ 


nt bc ? 


où Æ est le module d’élasticité du matériau; J, le moment d'inertie 
de la section ; b, la largeur de section (égale à 1 dans le cas considéré); 
c, le module de réaction du sol qui 
varie entre 1 et 3 kgf/cm° pour les 4) 
sols peu denses et entre 3 et 8 kgf/cm° 
pour les sols de densité moyenne. 

On calcule les efforts M, et Q, à 
la jonction de deux parties du fond 
en annulant leurs déplacements rela- 
tifs. On obtient ainsi des équations 
canoniques ordinaires 


uMi + G1oQ1 + Gp = 0, b) 
QMi + Q29Q1 + Gop = 0. 


Les déplacements d’une poutre 
de forte longueur (multipliés par EJ) Q; = 
provenant du moment À7, = 1 appli- 
qué à son extrémité comprennent un 
angle de rotation afl — s et un affais- nee | de 
sement afl — —$5°/2, et ceux prove- | | ( ta} Î 
nant de la force Q, = 1 appliquée 7 
à son extrémité sont un angle dero- FIG. XI.22. Schéma des efforts 


fl — pfl dans la jonction de la paroi, du 
EU “. pate se un fond et dé l'anneau d'assise: 
Asa — Se. n à cles éplacements a, système défini; b, système fon- 


nalogue our une utre rigide  damental:p, pression de l'eau; N, 
analogues  p : DOME: MSIE pression de la paroi sur la jonction: 


— 4/73 = — o] | 
ai D 3s;/l, is me dy M —1,5s1/1}, q, réaction du sol; M1, @1, moment 


T — gl A eu fléchissant et effort tranchant dans 
Ao — si/l. Les éplacements totaux la paroi au niveau de la jonction; 
sont «3, = aîfl 


+ &;; Ayo —= os — Mo, Qo, idem, dans le fond 
= af + a, Go = al + a, 


Les termes de la charge provenant du moment M et de la force N 


ZT — 


itttttitt 


appliqués sur l’anneau d’assise (fig. IX.23, a) sont &ip = —M X 
X 31/0, aop = —M X 1,580 — NII x si/4. 


FIG. XI.23. Pour le calcul approché du fond 


1) La raideur caractéristique de la paroi cylindrique indiquée ci-dessus 
4 JLET 


3 4 V'&EJ E6 
(formule XI.5) est déduite de l’expression s — 4 7 en mettant c — ES et 
_ di 
7 12° 




À la jonction du fond avec la semelle de poteau (fig. IX.23, b), 
en vertu de la symétrie, l’angle de rotation est a,» — 0 et l'affais- 
sement (produit par V —20,) 
est égal à 


Nappe phréatique (V—2Q,) EJ 
= Sen 
| | Gp — libe | 


Les armatures du fond sont 
disposées contre les surfaces 
supérieure et inférieure. Aux 
endroits où le fond rencontre 
la paroi (ou les anneaux d’as- 
sise), l’armature est calculée 
pour résister au moment cor- 
respondant. Dans les autres 
parties du fond les armatures 
supérieure et inférieure sont 
dimensionnées conformément 
aux considérations construc- 
tives: elles ont un diamètre 
de 8 à 10 mm et sont espa- 
Plan du ford cées de 15 à 20 cm dans les 
| deux directions. 

Le fond plat exposé à la 
pression ascendante des eaux 
souterraines subit une pres- 
sion de calcul uniformément 
répartie sur toute sa surface 
(dirigée de bas en haut) 


p = 1,14, tf/m° (kN/m°). 


RTE es Pour déterminer les mo- 
18 D ments fléchissants produits 
RS par cette pression dans le 
SANS fond, on peut assimiler ap- 
RSS proximativement ce dernier 
ER" à la dalle d’un plancher-cham- 


=" * pignon renversé appuyé sur 

des poteaux intérieurs; les 

FIG. XI.24. Fond conique semelles jouent le rôle de 
chapiteaux. 

Le fond conique sollicité par la pression ascendante, qui croît 

de façon linéaire de l’anneau d’assise vers le sommet (fig. XI.24, a), 

subit essentiellement des compressions ?). Les armatures radiales 


1) Les efforts méridiens et annulaires sont cherchés comme pour un voile 
mince conique de révolution. 




et les frettes du fond sont posées des deux côtés (fig. XI.24, b); 
elles sont constituées généralement de barres de classe A-IT, de 
10 mm de diamètre, espacées d'environ 15 cm. 

Les pièces constitutives de la toiture — panneaux et poutres — 
sont à calculer par la méthode exposée dans le Chapitre X. Les 
poteaux intérieurs sont calculés à la compression d’après les formules 
du Chapitre IV. 

Quelques exemples de calcul des structures des réservoirs cylin- 
driques seront étudiés dans le Chapitre XII. 


$ XI.4. CONCEPTION DES RÉSERVOIRS RECTANGULAIRES 
EN BÉTON ARMÉ 


Parmi les réservoirs rectangulaires, on compte des réservoirs à eau, 
des décanteurs de types variés, des clarificateurs, des bassins de 
boues activées, des mélangeurs, des pièges à pétrole, des dessa- 
bleurs, des filtres, des épaississeurs de boues... La plupart de ces 


a) 1 2: 8B 


> ERA E 
Er PT 


Fond 


FIG. XI.25. Schémas des réservoirs rectangulaires : 


1, dalle du plancher-champignon; 2, dalle (radier) du fond; %, chapitcau; 4, poteau; 
5, paroi; 6, paroi nerv urée : 7, panneaux préfabriqués de la toiture 


ouvrages sont ouverts, à l'exception des réservoirs à eau et de quel- 
ques types de décanteurs et de filtres qui possèdent une toiture. Le 
béton préfabriqué est utilisé dans les murs, les poteaux, la toiture, 
les déversoirs; quant au fond, il est très généralement coulé en 
place. 

Les réservoirs à eau ont le fond plat et la toiture reposant sur 
des poteaux intérieurs. Ces derniers sont disposés le plus souvent 
suivant un quadrillage de 4 x 4 à 6 x 6 m. Si la hauteur de la 




paroi du réservoir rectangulaire en béton coulé en place ne dépasse 
pas 4 m (fig. XI.25, a), la paroi est unie et encastrée dans la toiture 
et le fond au moyen de congés armés dans les angles. Si la paroi est 
plus haute, elle est dotée de nervures tournées vers l'extérieur 
(fig. XI.25, b). Le fond peut être relevé aux bords, afin de diminuer 
la hauteur de la paroi (fig. XI.25, c). La toiture coulée en place est 
généralement du type champignon. 

La contenance des réservoirs rectangulaires normalisés à eau 
(fig. XI.26) varie entre 50 et 20 000 m*. Leurs cotes d'implantation 
sont multiples du module 6 m, la hauteur égale à 4,8 m (à 3,6 m 
si la contenance ne dépasse pas 500 m°). 

Les cotes d'implantation du réservoir, choisies en fonction de 
la contenance, sont les suivantes: 


Conan eu réservoir, 50 | 100 250 | 500 | 1000 

Cotes d'implantation, m | 3X6 | 6X6 | 6x 12 | 12 X 12 | 12X18 
SUITE 

CORDON AR RO lon 3000 6000 10000 | 20 000 

Cotes d'implantation, m| 18X24 24 X 30 | 36 X 36 | 48 X 48 | 66 X66 


Le fond du réservoir est coulé en place, d'épaisseur constante 
non inférieure à 12 cm, renforcé au droit des poteaux et des panneaux 
des murs. Un panneau de mur a une hauteur de 4,8 m (3,6 m) et une 
largeur nominale de 3 m. 

Les poteaux, de section carrée, sont engagés dans les logements 
des semelles. 

La toiture préfabriquée est composée de poutres-types et de 
panneaux nervurés 1,5 X 6 m fabriqués industriellement pour les 
planchers des bâtiments industriels à étages (voir fig. XI.26). Le 
calorifugeage est assuré généralement par une couche de sol recou- 
vrant la toiture. On utilise aussi des matériaux thermo-isolants effi- 
caces tels que le béton mousse, verre expansé, etc., qui diminuent 
considérablement la charge exercée sur les éléments de la toiture. 

Dans un réservoir couvert calorifugé la température est stable, 
ce qui rend inutiles les joints de dilatation. 

Les décanteurs horizontaux sont des réservoirs rectangulaires 
allongés compartimentés,; le liquide coule lentement dans le décan- 
teur, et les particules en suspension descendent. sur le fond. 




CLIN OA] PI ANS JMIJUOU 989 F [IU}9P 01 :9]UY}}C U9 SJO19P SP JAEPUOS ‘SL : UOISNJ 9h UIEq ue 
nu S)PNos SI) ‘LL *IOIRULUO ANS AOU[A Uo SIUI U0}94 ‘OL : S99[100S So9gid ‘6 ‘o1n}10) op Xnvouued ‘8 :a4N0d ‘Z : UOI}EDUOZ 9P 2[[OUIS ‘9  2J181P 
-JUHdJU, neajod ‘ç ‘otug13Xo neojod ‘F ‘sinu Sop XNvouued ‘£ : (PUOJ Up JUPUIYIIOUII) 9W91}X9 NBIJOU np aT[9W9S ‘Z ‘o2e[d U9 9[N09 pUuOJz ‘Tr 


:QUIe u039q uo senbriqezard sjuowu99,p 9s0dw09 artepnsu8/281 IIOAISOY ‘OZ'IX OI 


NDS DS ND CL TN IE ME TT, SSSR L à 


NE TS 


5 BOTCL PAYS AI PT à 


€ 1122790 } 720790 


Les décanteurs employés dans les réseaux de distribution des 
eaux sont généralement couverts, munis d’une toiture calorifugée, 


2 T-I 




sont montrés sur la figure XI.35 




9000 
| A<84000 | 


FIG. XI.27. Décanteur horizontal cou- 
vert composé d’éléments-types : 


J, panneaux des murs; 2, panneaux de toiture; 
3, panneaux des cloisons; 4, fond coulé en 
place ; 5, talus en béton : 6, déversoir : les détails 


Les décanteurs horizontaux 
dans les réseaux d’évacua- 
tion sont ouverts. 

La hauteur des décan- 
teurs horizontaux couverts 
constitués  d’éléments-types 
préfabriqués (fig. XI.27) est 
4,8 m, la largeur d'une cel- 
lule est 6 m et la longueur, de 
36 à 75 m. Le fond est coulé 
en place, les panneaux des 
murs préfabriqués, de largeur 
nominale 3 m. Les hourdis 
de toiture sont posés directe- 
ment sur les murs longitudi- 
naux. 

Les décanteurs horizontaux 
sans toit constitués d'éléments 
préfabriqués de béton armé 
ont une hauteur de 3,6 ou 
de 4,8 m. Ils sont composés 


de cellules de 6 ou de 9 mètres de large, de 36 ou de 48 m 
de long (fig. XI.28). Chaque compartiment du décanteur a de 


ie 7 Re 
15) < 
DE 771 2 
Plan CE EE 






Jeu de dilatation 


FIG. XI. 28. Décanteur horizontal sans toit composé d’éléments-types préfabriqués: 


1, panneaux des murs: 2, panneaux des cloisons; 3, fond coulé en place; 4, pOFtons des 
murs coulées en place; les détails C sont montrés sur la figure XI.3 


deux à neuf cellules, sans que la largeur du compartiment soit 
supérieure à 54 m, sinon on est obligé de prévoir des joints de dila- 




FIG. XI.30. Bassin de boues activées composé d’éléments-types préfabriqués : 


1, panneaux des murg{ £, panneaux des cloisons; 3, fond coulé en place; 4, portions des 
murs coulées en place: 5, déversoir 


17—0948 257 


tation. Les panneaux des murs des décanteurs peuvent être entre- 
toisés de 6 en 6 m dans leur partie haute. 

Les pièges à pétrole, aménagés dans les raffineries, les exploita- 
tions, les stations pétrolières, ont pour mission de capter les pro- 


2 200 30 200 J 4 


Ne 2 




LTD PT LEE LA NE es) À le 




TR TS CL (0 :/0 ? KA 
RTS ENSERRSRSSENNTTESN CREER 


D) 4 40 3 9 


LAIT IS 
ZT og 701 






Q NS 


FIG. XI.31. Détails des joints de dilatation: 


a, avec compensateurs en acier ; b,"#vec clavette en caoutchouc; I, face intéricure ; II, paroi; 

III, fond; 1, compensateur: 2, matage avec de l’amiante-ciment ; 3, fils d'amiante, 4, en- 

duit appliqué par projection ; 5, asphalte ; 6, sable; 7, carton bituminé; 8, couche de pro- 
preté en béton; 9, clavette en caoutchouc à trois branches 


duits pétroliers contenus dans les eaux usées. Ce sont des ouvrages 
rectangulaires compartimentés analogues aux décanteurs horizon- 


taux. 
Composés d'éléments-types préfabriqués, les pièges à pétrole 
ont une hauteur normalisée de 2,4 m, une largeur de cellule de 2,3 




ou de 6 m et une longueur entre 12 et 36 m (multiple du module 
6 m). Les panneaux des murs sont préfabriqués, le fond coulé en 
place. 

Les bassins de boues activées sont des réservoirs rectangulaires 
ouverts compartimentés. Leur fonction est l’épuration biologique 
des eaux d'’égoût. Chaque compartiment du bassin (fig. XI.29) 
est divisé en couloirs par des cloi- 


sons (chicanes) longitudinales qui à 
n'atteignent pas le mur en bout. à 
Le plus souvent, chaque comparti- \È 
ment possède trois couloirs. La + 
dégradation biologique des boues |_2%0 | Dre 


est favorisée par l’air amené dans 
le bassin. 

Les bassins de boues activées 
sont constitués de compartiments- 
types à deux, trois ou quatre 
couloirs. La largeur du couloir est 
4,5, 6 ou 9 m, la hauteur 4,8 ou 
6 m, et la longueur, de 42 à 132 m 
(multiple du module 6 m). Le fond 2980 
est coulé en place. Les panneaux 160-540 SEX 
des murs et des cloisons sont préfa- 
briqués, larges de 3 m (fig. XI.30). c) 


H = 3000 - 500 


Compte tenu de la longueur È 
considérable des bassins, ils sont É: 
dotés de joints de dilatation espa- È 
cés de 54 mètres, qui comportent ù 
des compensateurs en acier ou des | | e) 2980 
clavettes spéciales en caoutchouc 
(fig. XI.31). Afin de diminuer le : Fo 


frottement dû à la dilatation, une 
couche de sable est interposée entre FIG. XI.32. Panneaux-consoles des 
le fond du bassin et la couche de murs et des cloisons pour réservoirs 
propreté en béton. rectangulaires : 

Il existe d'autres réservoirs 2 lp denrde hauteurs 220 
rectangulaires (clarificateurs, sépa-  c, panneaux des cloisons; 1, aciers en 
rateurs de pétrole, mélangeurs, nn 
réservoirs à contact, dessableurs, 
filtres biologiques, filtres rapides, etc.) qui ne se distinguent que 
par les dimensions, le profil du fond, la présence ou |’ absence deg, 
déversoirs, etc. Leur schéma-type est analogue à ceux qu'on vient 
de considérer. 

Dans les réservoirs rectangulaires, on utilise deux types de 
panneaux des murs unifiés, en fonction de la résistance qu'ils doi- 
vent opposer aux sollicitations horizontales (pression du liquide ou 
pression du sol). Les panneaux-consoles (fig. X1.32) sont simplement 
encastrés dans le fond ; les panneaux-poutres sont en outre articulés 


17% 259 


à leur bord supérieur (fig. XI.33). On réalise l’encastrement en 
faisant descendre le panneau dans la rainure du fond de 1,56 au 
moins (Ô étant l'épaisseur du panneau) pour les panneaux-poutres 
et de 26 au moins pour les panneaux-consoles (voir fig. XI.26, 
détail 3). 

L'appui supérieur d’un panneau-poutre est assuré par le fait 
que l'ouvrage tout entier travaille à la façon d’un système fermé 
(fig. XI.34, a); en effet, dans 
un ouvrage couvert les murs et 
les poteaux sont reliés en haut 
par la toiture, et dans un ouvrage 
ouvert, par les entretoises en 
béton armé placées entre les murs 
et les cloisons (fig. XI.34, b). 
Les panneaux-poutres sont mu- 
nis dans leur partie supérieure 
d'un renforcement de 300 x 
x 200 mm qui, après l'assem- 

| blage des panneaux entre eux, fait 

| 2800 (1800) | 6-/49-240  Oftice de ceinture de consolida- 
ES tion qui travaille à la flexion 
dans le plan horizontal entre les 

FIG. XI.33. Panneaux-poutres des Cntretoises (ou les poutres de 


murs pour réservoirs rectangulaires: toiture). 
1, aciers en attente En plus des panneaux des murs, 
le catalogue des éléments-types 
pour ouvrages rectangulaires prévoit des panneaux des cloisons qui, 
à la différence des premiers, sont conçus pour travailler sans avoir 
à supporter la pression du liquide, vu que celui-ci se trouve toujours 
des deux côtés de la cloison. 

Les panneaux-consoles, des murs et les panneaux des cloisons 
ont une largeur de 2,98 m. Leur face en bout supérieure est munie 
d’une rainure de profil triangulaire, destinée à former une clavette 
de section en losange après le bétonnage du joint. Les panneaux- 
consoles sont en outre reliés par soudage des aciers en attente et 
par bétonnage en haut et à la mi-hauteur. 

La hauteur À des panneaux-consoles varie entre 1,2 et 5,4 m, 
échelonnée de 0,6 en 0,6 m. Pour H = 1,2, 1,8 et 2,4 m le panneau 
a une épaisseur constante Ô — 100, 130 et 150 mm respectivement. 
Pour H > 3 m le panneatw a uné épaisseur de 440 mm dans sa partie 
supérieure; en bas, il a une épaisseur de 160 mm pour H = 3 m, 
de 200 mm pour H = 3,6 m, de 240 mm pour H = 4,2 m, de 
280 mm pour H = 4,8 m et de 340 mm pour À = 5,4 m. 

Les panneaux des cloisons ont une hauteur H — 3,6, 4,2 et 
4,8 m pour une épaisseur constante Ô — 120, 140 et 160 mm respecti- 
vement. 

Les panneaux-poutres des murs sont reliés dans le joint vertical 
par soudage des aciers horizontaux en attente. Le jeu entre les 






panneaux est rempli de béton (voir fig. XI.26, détail 5). Pour facili- 
ter le bétonnage, on laisse un jeu de 200 mm, ce qui fait que la lar: 
geur des panneaux est 3—0,2 = 2,8 m. Les ouvrages de faible 
contenance comportent des panneaux-poutres complémentaires de 
1,8 m de large (largeur nominale 2 m). La hauteur des panneaux est 
H = 2,4 à 6 m (échelonnée de 0,6 en 0,6 m), l'épaisseur est constan- 
te, de 140 (pour H = 2,4 m) à 240 mm (pour H — 6 m), échelonnée 
de 20 en 20 mm. 

Aux angles, les panneaux des murs sont assemblés par des por- 
tions de béton coulées en place longues jusqu'à 1,5 m (fig. XI.35). 


a) J 


FIG. XI.34. Réservoirs constitués de panneaux-poutres : 


a, réservoir couvert ; b, réservoir sans toit ; 1 panneaux des murs; 2, poteaux; 3, toiture : 
4, fond; 5, entretoises ; , panneaux des cloisons 


Les panneaux des murs travaillent à la flexion dans le plan 
vertical uniquement s'ils sont suffisamment éloignés des murs ou 
des cloisons perpendiculaires, auquel cas les armatures verticales 
sont porteuses et les barres horizontales sont placées d’après les 
dispositions constructives. Dans les portions voisines des mur® 
perpendiculaires ont lieu aussi des moments fléchissants légers 
dans le plan horizontal, d’où la nécessité de renforcer les barres 
horizontales. La longueur de ces portions est prise égale à la hauteur 
du panneau (pour les panneaux-poutres) et à 1,5 fois la hauteur du 
panneau (pour les panneaux-consoles). On prévoit donc plusieurs 
variantes de ferraillage pour chaque type de panneau de mur. 




Nous avons déjà dit dans le $ XI.2 que les nouveaux projets-types 
de réservoirs préfabriqués en béton armé pour les réseaux de distri- 
bution et d'évacuation des eaux prévoient un nombre plus restreint 
de types d'éléments préfabriqués, permettent d'obtenir une écono- 
mie considérable des matériaux et de faciliter le montage. Par 


Détail 4 - Variante 1 { 


Détail 5 


— Pa' 




Détail C 


FIG. XI.35. Détails des assemblages des panneaux des murs des réservoirs 
rectangulaires (voir fig. XI.26, XI.27, XI.28.): 


1, panneau du mur (armatures horizontales renforcées près des angles); 2, armature de Ja 
portion coulée en place; 3%, aciers en attente des panneaux: 4, pièces scellées : 5, mortier 
de ciment 


exemple, dans les pannëäux-poutres, le joint vertical bétonné est 
remplacé par un joint à clavette avec soudage des pièces scellées, 
ce qui rend le montage plus facile. Les panneaux de hauteur 4 > 
> 3,6 m ont une épaisseur inégale, d’où économie des matériaux. 
Une solution originale de l’assemblage aux angles est le joint « flexi- 
ble » (fig. XI.36). Un tel joint ne s'oppose pas aux déformations 
des murs; on peut donc utiliser les panneaux des murs de même 
type pour la totalité de l'ouvrage, alors que le joint rigide (compor- 
tant des portions coulées en place) nécessite des armatures renforcées 




au voisinage des angles. L’étanchéité du joint flexible est assurée 
par l'emploi du mastic d’étanchement au thiocol. 

Les déversoirs sont fréquemment utilisés dans les réservoirs. 
Ils sont disposés soit le long des murs (décanteurs, clarificateurs, 
épaississeurs de boues), soit au-dessus des 
parois (bassins de boues activées), soit 
sur le sol (trémies dessableuses). Les dé- 
versoirs rectangulaires normalisés ont une 
longueur nominale de 3 ou 6 m, une lar- 
geur (dans l’œuvre) de 20 à 60 cm et une 
hauteur de 20 à 90cm; l'épaisseur des 
parois (en bas) est de 8 à 11 cm. Ils sont 
posés dans les manchons d'assemblage en 
béton armé qui reposent sur des petites FIG. XI.36. Joint « flexi- 
poutres transversales en béton armé mises bles des panneaux des 
à cheval sur les panneaux des murs (ou murs dans les angles : 
des cloisons) (fig. XI.37, a). Les poutres mastic  d'étanchement - 
transversales sont fixées à l’aide de cales en RS Éd 
acier. Tous les éléments sont réunis par ciment 
soudage des pièces scellées en acier. 

Comme passerelles de service (pour le personnel affecté aux ouvra- 
ges), on emploie les panneaux nervurés de toiture des bâtiments 


Fan DIS PS» DID ÉL' I III IT 


FIG. XI1.37. Déversoirs et passerelles de service des réservoirs rectangulaires: 


a, déversoir avec passerelle; b, passerelle; 1, panneau du mur; 2, poutre transversale ; 
manchon; 4, panneau; 5, déversoir; 6, cales d’acier; 7, soudage des pièces scellées: 8, 
mortier de ciment 


industriels. Les panneaux sont posés soit sur les petites poutres 
transversales en béton armé (fig. X1[.37, b), soit sur les manchons 
d'assemblage des éléments du déversoir (fig. XI.37, a). 




$ XI.5. CALCUL DES RÉSERVOIRS RECTANGULAIRES 


Le cas de charge et les méthodes de calcul des parois d’un réservoir 
rectangulaire dépendent de son schéma et du rapport des côtés. 
Les murs des ouvrages ouverts dont la hauteur est très inférieure 

à la longueur (bassins de boues activées, pièges à pétrole, décan- 
teurs ...) sont des consoles encastrées 


a) b) €) dans le fond. 
Pour les murs extérieurs, deux cas 
Nappe de travail sont à considérer: 

phréatique 4° le remblai étant absent, le mur 
résiste à la pression hydrostatique du 

liquide (fig. XI.38, a); 
/ | - 2° le liquide étant absent, le mur 
no résiste à la poussée latérale du sol 


(fig. XI.38, b, c). 
a oo do done La surcharge exercée en surface 


d’un réservoir rectangulaire de du sol autour de l'ouvrage est prise 
forte longueur sans toit: égale à 1 tf/m° (10 kN/m°). 

a, le réservoir est rempli de liquide, Les formules définissant la pres- 

le remblai est absent ; b, le réservoir 3 RUREe : : 

est vide, le sol agit sur les murs: c,  SlOn Caractéristique du liquide et du 

idem, avec en plus la poussée des  remblai et les coefficients de surcharge 
correspondants sont donnés dans 
le SXI.3. 

Après avoir déterminé les moments fléchissants de calcul qui 
proviennent des charges indiquées (rapportées à 1 mètre de longueur 
du mur), on calcule la section à donner aux armatures verticales en 
considérant une section rectangulaire de hauteur utile À, = Ô — 
— 2 cm et de largeur b — 100 cm. La pression du liquide déter- 
mine la section à donner aux armatures placées du côté intérieur 
Fa.int, et la pression du spl, celle à donner aux armatures placées 
du côté extérieur Fa.ezxt; On a toujours d’ailleurs Fh.ext < Fa.inte 

Les parois intermédiaires, sur lesquelles le liquide agit tantôt 
d’un côté, tantôt de l’autre (cas de vidange du compartiment voisin), 
ont une armature de section F, int des deux côtés. 

Afin de réduire la gamme des produits, on pose dans les pan- 
neaux-Consoles préfabriqués les mêmes armatures Fh.int des deux 
côtés. Après avoir calculé les armatures verticales du panneau pré- 
fabriqué, on doit vérifier aussi le cas de travail du panneau à la 
flexion sur chantier sous4’action de son propre poids. 

Une fois la section à donner aux armatures déterminée, on vérifie 
l'ouverture des fissures selon la condition at < 0,2 mm. Ce calcul 
sera fait d’après la méthode du $ VI.7 en admettant que l’ensemble 
des charges agit pendant une longue durée. 

Dans les murs que l’on vient d'étudier, les barres horizontales 
sont des armatures de répartition. Dans les portions extrêmes des 
murs de longueur 1,54, en cas d’encastrement dans les murs 
d'extrémité, on doit augmenter la section de ces armatures de telle 




façon qu'il y ait Fa.hor > Umin0ho. Cette augmentation, comme 
nous l’avons signalé dans le $ XI.4, est nécessaire pour résister aux 
légers moments fléchissants qui agissent dans le plan horizontal 
aussi. ' 

Les cloisons des ouvrages qui sont toujours sollicitées des deux 
côtés par la même pression du liquide (cloisons entre couloirs dans 
les bassins de boues activées, chicanes des décanteurs, etc.) sont 
calculées pour résister à la charge verticale due au poids des déver- 
soirs (remplis de liquide) qu’on monte sur les cloisons, des passerel- 
les, des conduites technologiques, ainsi qu’à la poussée du vent 
exercée sur la cloison en l’absence du liquide. 

La section à donner aux armatures verticales est déterminée 
selon les formules de calcul des pièces comprimées et fléchies (voir 
chapitre VII). Quant aux armatu- 


res horizontales, elles sont déter- FRE 
minées comme précédemment. Si asp. 
le mur est confectionné à partir | 

des panneaux préfabriqués, il con- Ÿ H 
vient de vérifier la résistance des 


armatures en considérant le cas de D 
transport et de montage du pan- | 


neau, quand celui-ci travaille à la + 

flexion sous l’action de son propre Æ 5 

poids. f PPT a, 1 7 CL. “ 
Les murs des ouvrages avec ou 


sans toit au rapport des CÔtÉS FIG. XI.39. Cas de charge des murs 
l/l, 3 (fig. XI.39) représentent travaillant en deux directions: 


des plaques encastrées en bas 1, bord libre; 2, bord articulé; 3, bord. 
et latéralement. Quant au bord FRAUPÉ 

supérieur, sa fixation dépend du 

schéma de l'ouvrage. En l'absence du toit le bord supérieur est. 
libre (fig. XI.39, a), en présence d’un toit préfabriqué il est arti- 
culé (fig. XI.39, b), et en présence d’un toit coulé en place il est 
encastré (fig. XI.39, c). Le diagramme des efforts exercés sur ces 
murs par le liquide ou le sol a la forme d’un triangle ou d’un trapèze 
dont l’ordonnée maximale est en bas. Les moments fléchissants 
sont cherchés au moyen des tables de calcul des plaques rectangu- 
laires isotropes (voir Annexe XX). En fonction des moments, on 
détermine comme d'ordinaire la section à donner aux armatures 
et l’on vérifie l'ouverture des fissures. 

Les murs des ouvrages couverts de forte longueur (fig. XI.40) 
possèdent des appuis au niveau du fond et du toit. Le mur sans. 
nervures coulé en place représente un hourdis fixé élastiquement en 
haut et en bas et sollicité par une charge triangulaire provenant de 
la pression du liquide (le remblai étant absent) (fig. X1.40, b). 
L'ouvrage étant vide, les moments dus à la poussée lätérale dù sol 
ont le même diagramme mais de signe inverse. En fonction: de va- 
leurs de calcul des moments, on détermine la section à donner ‘aux 




3 FN \ 
| ss A {D ù 1 
PART US \ Si de du ur 265: 








FIG. XI1.40. Pour le calcul du mur coulé d’un bloc avec le toit et le fond d’un 
réservoir rectangulaire de forte longueur: 
1, toiturez £, mur; 3, fond 


armatures verticales, puis on vérifie l'ouverture des fissures. Le 
plan de ferraillage est montré sur la figure XI.40, c. 

Notons qu’en plus des moments fléchissants, le mur d’un ouvrage 
rectangulaire couvert est soumis à une force longitudinale due au 
poids de la toiture, ce qui fait qu'il est à la fois comprimé et fléchi. 
Dans le calcul, on ne tient pas compte de l’influence de la force 
longitudinale et l’on considère le travail du mir à la flexion unique- 
ment : la section de l’armature s’en trouve légèrement surdimension- 
née, mais la structure devient moins précaire, car, pendant l’exploi- 
tation, il y a des périodes où l’on enlève le remblai sur le toit et la 
orce longitudinale diminue brusquement. 

Si le mur coulé en place possède des nervures verticales espacées 
de c > 0,5k ou de c > 2h, on assimile la plaque limitée par les 
nervures à une dalle encastrée suivant le périmètre et on la calcule 
d’après les tableaux indiqués ci-dessus; la nervure est assimilée 
à une poutre fixée élastiquement dans le fond et le toit est soumis 
aux réactions qui proviennent de la plaque. 

Le mur sans nervures d’un ouvrage couvert de forte longueur 
à toiture préfabriquée (fig. XI.41) est considéré comme encastré 
dans le fond et muni d’une articulation fixe en haut. Dans le calcul 
du mur, on considère des poutres verticales de 1 m de large. 




F Le même schéma (voir fig. XI.41) est adopté dans le calcul d’un 
panneau-poutre de mur préfabriqué. Pour les panneaux-types, on 
prend}le moment en travée légèrement plus grand que le moment 


FIG. XI.41. Pour le calcul du mur articulé avec la toiture d’un réservoir rectan- 
gulaire de forte longueur: 
a. vue d’ensemble: h. schéma des efforts: c. diagramine des moments 


représenté sur la figure, afin de tenir compte d'une rotation possible 
de la jonction mur-fond (en calculant le moment f;,, on a diminué 
Mint de 20 %). 


AA 7 


NN 2 




] \ Po=P-c 


FIG. XI.42. Pour le calcul du mur nervuré d’un ouvrage rectangulaire couverèt 


a, vue d'ensemble ; b, cas de charge de la nervure pour c > 2h: c, cas de charge de la plaque 
entre nervures pour h > 2c; d, idem, pour c < 2h 


En déterminant la poussée latérale du sol, on admet que la 
surcharge en surface est égale à 1,5 tf/m°? (15 kN/m°), et si l'ouvrage 
est Calorifugé par une couche de sol, à 2,5 tf/m° (25 kN/m°). Pour les 
panneaux-poutres types des murs, une telle surcharge est retenue 




pour H = 3,6 et H = 4,8 m. En fonction des moments trouvés, 
on cherche la section à donner aux armatures verticales du mur sui- 
vant ses cas de charge possibles : la paroi intermédiaire est sollicitée 
des deux côtés par le liquide, tandis que le mur extérieur subit 
la pression du liquide d’un côté et la poussée du sol de l’autre. 
Ensuite on vérifie l'ouverture 
des fissures de façon à satisfaire 

P la condition af 0,2 mm. 
Si le mur possède des ner- 
Pr vures verticales (fig. XI.42, a), 
P le rapport des côtés étant À > 
> 2c, on doit multiplier par c 
les moments calculés selon les 
formules indiquées sur les figures 
XI.40 et XI.41 et dimensionner 
les armatures des nervures en 
fonction de ces nouvelles valeurs 
des moments. La plaque bor- 
dée de nervures est assimilée 
dans ce cas à une poutre conti- 
nue horizontale reposant sur ses 
nervures (fig. XI.42, c). La char- 
ge exercée sur la plaque étant 
variable suivant la hauteur, on 
divise la plaque en zones larges 


Pression Pression 
Léguide intér.P  dusol Fe 


CE P 2 
pe SÈ : ” PRE de 1 m et on calcule chaque 
È Ê s Peu zone séparément en tenant comp- 
Mir 7 . ME te de la charge exercée dans 
y. Pa 2 cette zone particulière. 
2 Me L'espacement des nervures 


FIG. XI.43. Pour le calcul dû mur étant ce <2h, la nervure est assi- 
d’un ouvrage rectangulaire de hauteur milée à une poutre encastrée en 
très supérieure aux cotes d’implan- bas, articulée en haut et sou- 
tation mise aux réactions des dalles 

voisines (fig. XI.42, d). 

Si les cotes d'implantation de l’ouvrage sont beaucoup moins 
grandes que la hauteur, on divise les murs en zones larges de 1 m 
suivant la hauteur et on les assimile à des cadres fermés qui résistent 
à une pression maximale p pour chaque zone (fig. XI.43, a). L’allure 
du diagramme des moments et Îes valeurs des moments et des forces 
normales sont montrées sur la figure XI.43, b. L'ouvrage étant 
rempli de liquide et le remblai étant absent, les murs éprouvent 
une traction excentrée ; l'ouvrage étant vide et le remblai en place, 
ils travaillent à la compression excentrée. 

Les éléments de la toiture et du fond sont calculés par la méthode 
indiquée dans le $ XI.3 pour les ouvrages cylindriques. Quelques 
exemples de calcul seront donnés dans le Chapitre XII, 




$ XI.6. CONCEPTION ET CALCUL 
DES RÉSERVOIRS CYLINDRIQUES EN ACIER 


Les réservoirs en acier représentent des coques minces constituées 
de tôles planes ou gauches reliées par soudure de façon à former une 
structure mince tridimensionnelle. Les jonctions des tôles doivent 
être non seulement résistantes mais aussi étanches, pour assurer 
l'étanchéité de l’ouvrage. Leur état de contrainte est caractérisé 
le plus souvent par l'absence des moments et la présence des seuls 
efforts axiaux (généralement des tractions) qui font naître dans les 
tôles des contraintes uniformément distribuées suivant l'épaisseur. 
Les moments fléchissants n'apparaissent qu'aux endroits de jonction 
avec les raidisseurs annulaires, les fonds plats, etc. Vite amortis, 
ces moments n'affectent que des portions limitées de la structure 
(effet de rive). 

Une structure en tôles sollicitée en traction par la pression inté- 
rieure (conduite, réservoir cylindrique, etc.) conserve ses qualités 
d'utilisation même après que les contraintes dans les tôles sont 
devenues égales à la limite d’élasticité. Pour tenir compte de ce 
cas, les Normes prennent la résistance de calcul de l’acier à la trac- 
tion égale à la charge de rupture (voir Chapitre IX). 

Les réservoirs cylindriques en acier sont montés généralement 
sur des châteaux d’eau. Leur fond peut être plan ou gauche (fig. XI.44, 
XI.45). Ils ont le plus souvent une toiture légère qui n’affecte aucu- 
nement le travail de la paroi. 

Un réservoir à fond plat est plus facile à fabriquer, mais il pré- 
sente certains inconvénients en exploitation: la visite et la répara- 
tion du fond sont délicates, les précipitations s'accumulent et 
favorisent la corrosion de l’acier. 

Les tôles doivent avoir une épaisseur non inférieure à 4 mm, 
afin d'assurer une soudure efficace et une bonne résistance à la 
corrosion. Si la contenance du réservoir est relativement faible 
(100 à 1000 m°), la paroi et le fond plat ont une épaisseur constante 

— 4 mm. Si la contenance est plus importante (2000 à 5000 m°), 
l'épaisseur de la paroi varie entre 4 mm en haut et 10 mm en bas: 
le fond a une épaisseur constante dans sa partie centrale, de 4 ou 
5 mm, et les tôles de rive ont une épaisseur de 6 à 8 mm. La paroi 
est composée de ceintures isolées. Les tôles de la ceinture sont sou- 
dées entre elles bout à bout. Dans les ceintures voisines, les cordons 
de soudure sont décalés de la mi-longueur de la tôle, ou de 500 mm 
au moins. Les ceintures sont soudées entre elles bout à bout a 
à recouvrement (voir fig. XI.44). 

Le fond plat est formé de bandes qui, à leur tour, sont 
par des tôles d'acier soudées bout à bout ou à recouvrement; les 
bandes sont soudées entre elles à recouvrement. 

La paroi et le fond du réservoir sont reliés bout à bout par deux 
cordons annulaires continus (voir fig. XI.44). Il est déconseillé 
de renforcer la jonction par une cornière ou un couvre-joint, ainsi 




que de prolonger le fond de plus de 50 mm au-delà de la paroi, car 
ces solutions font naître des concentrations de contraintes préjudi- 
ciables. 


{ 300 mm mini 


Detail À Détail 5 


Diagramme 
du moment 
de rive 


FIG. XI.44. Réservoir en acier à fond plat: 


I, joint des ceintures bout à bout; II, idem, à recouvrement; 1, cordon bout à bout; 
2, cordon continu; 3, cordon interrompu 


Si le fond est gauche, un anneau d'’assise particulier doit être 
prévu au droit de la jonction fond-paroi (fig. XI.45). 

Sur les chantiers modernes, on utilise de plus en plus souvent 
les éléments de réservoirs fabriqués en usine et amenés à pied d'œuvre 


Détail 4 & 


1 ù Détail B 
2 . | 




FIG. XI.45. Réservoirs en acier à fond gauche appuyé suivant le périmètre: 


a, fond splérigue ; b, fond conique; 1, pero 2, anneau d’assise; 3, cordon bout à bout; 
4, fon 


à l’état enroulé. Sur chantier, les éléments sont déroulés et assem- 
blés par soudure !). Dans ce cas l'épaisseur donnée aux tôles doit 


1) Les réservoirs en rouleaux sont actuellement les plus répandus pour le 
stockage des produits pétroliers. 




être limitée, afin de permettre l’enroulement. La paroi d’un réser-- 
voir de grande contenance peut être précontrainte: on réalise la 
précontrainte par la mise en tension d’un fil à haute résistance et 
par l'application d’une couche de béton par projection. 

La pression hydrostatique du liquide contenu dans le réservoir 
fait naître une traction axiale dans la paroi de celui-ci. L'effort 
de traction annulaire de calcul 7 à la profondeur À comptée à partir 
du haut de la paroi de rayon r est cherché à l’aide de la formule 
(XI.3). Par exemple, si le réservoir est rempli de liquide, on a 


T1; thr: 


Pour chaque ceinture on prend À égal à la distance entre le haut 
de la paroi et le bas de la ceinture (fig. XI.46, a). 


4) }) 


Diagramme M Diagramme T 


Ceinture 1 | 
[ceinture 2 
Ceinture 3 
(cintre + 
ceinture 5 | 
6h - 
(rare 8 






O6VrÔp 


FIG. XI.46. Pour le calcul d’un réservoir cylindrique en acier: 
a, paroi; &, cordon de soudure entre la paroi et le fond 


La résistance de la paroi d'épaisseur 6, est vérifiée en contrôlant 
la résistance des cordons verticaux bout à bout entre tôles de la 
ceinture : 


TIS, € Re (XI.24) 


Au droit de la jonction avec le fond, les cordons de soudure 
s'opposent à la libre déformation de la paroi en faisant naître dans 
celle-ci un moment fléchissant de rive M, dont la valeur se laisse 
déterminer approximativement par la formule 


M, & 0,11Hrô,, (X1.25) 


où À est la hauteur de la paroi cylindrique. Pa 

Le moment de rive s’évanouit rapidement dans le sens de la 
hauteur de la paroi (fig. XI.46), n’affectant que les cordons de la 
jonction fond-paroi. La contrainte induite par le moment de rive 
dans les cordons de soudure est vérifiée d’après la formule 


sen (XI.26) 




où W, est le module de résistance de deux cordons d'angle en cmi 
{voir fig. XI.46, b): 


= (XI.27) 


Dans cette dernière formule J, est le moment d'inertie des cordons 
de soudure en cm“: 


__ [1 (0, 7h) O,The | Op \2 XI.28 
2 (0 iron (Me +de)]  GUL2 


Ces contraintes ne se superposent pas aux tractions subies par 
le cordon au sein de la ceinture inférieure de la paroi, vu que ces 
contraintes ont les vecteurs réciproquement perpendiculaires. 

Le fond plat reposant sur un sol uni n’éprouve que des efforts 
insignifiants; on omet généralement de les calculer. 

Dans un fond sphérique appuyé suivant le périmètre (fig. [X.45), 
la pression hydrostatique fait naître des efforts de traction. Sa 
résistance est déterminée par celle du cordon de soudure dans la 
ceinture inférieure où les contraintes de traction passent par le 
maximum : 


my (1-0) ro CE mes. (XI 29) 


où n est le coefficient de surcharge ; y, la masse volumique du liqui- 
de; les quantités À, c, r,, Ô sont les mêmes que sur la figure XI.45. 
Dans un fond conique de pente « (voir fig. XI.45, b), les con- 
traintes de traction annulaires passent par le maximum au droit de 
l'anneau d’assise. La résistance du cordon bout à bout y est vérifiée 
par la formule 
nHyr cotg & 
ner (XIL.30) 
Dans l’anneau d'’assise du réservor appuyé suivant le périmètre 
apparaissent des efforts de compression axiaux: 
N — 9x tg Œ, (XI.31) 


où G° est le poids de l’eau et du fond 
On admet que la résistance. de l'anneau est bonne si 


NlFan <R, (XI.32) 


où Fan est la section de l'anneau. 
L'anneau d’assiso doit aussi être vérifié à la stabilité: 


N< Non (X1.33) 


8EJ, 


cr = x 3 
Fanrîn 


(X1.34) 




dans cette formule Æ est le module d’élasticité longitudinale de 
l'acier ; J,, le moment d'inertie de la section de l’anneau par rapport 
à l'axe vertical traversant le centre de gravité de la section; ran, 
le rayon de l'anneau. 


$S XI.7. TUYAUX ET PUITS EN BÉTON ARMÉE UTILISÉES DANS 
LES RÉSEAUX DE DISTRIBUTION ET D'ÉVACUATION DES EAUX 


Les tuyaux en béton armé sont utilisés dans les conduites gravitaires 
ou forcées. Les conduites gravitaires sont aménagées pour évacuer 
les eaux-vannes et les pointes d’averse. Les conduites forcées sont 
caractérisées par une surpression hydrostatique intérieure qui peut 
atteindre 20 kgf/cm*. 

Les tuyaux pour conduites gravitaires sont fabriqués sans pré- 
contrainte. Ils ont une longueur jusqu’à 5 m, un diamètre D — 400 


toos'ss/8 34 AJITS AVR LT VAT. DATA L') 


L STE —r— Le 

R——— 

À = LS pe 7) ON 
EE ————————_—— 


. j 72 CR AIT EE D PO MER — — Sodispéesre 




masse nm dns 00 ee DS 660 
0000 D See. 
_————————— 






DR SIIS ES 
SSL LL LITE 


SSI SSI SN SN SSD SD IS ST 


FIG. XI.47. Tuyaux en béton armé pour conduites gravitaires : 


a, tuyau à emboïtement à épaulement; b, idem, àemboîtement conique ; c, idem, à embhoite- 
ment à mi-épaisseur ; d, plan de ferraillage eo tuyau; 1, frette spirale ; 2, barres longitudi- 
nales 


à 2500 mm, leurs parois sont épaisses de 50 à 150 mm. Ils sont armés 
d'une (pour D < 900 mm) ou de deux carcasses cylindriques avec 
frettes en spirales (fig. XI.47). Les joints de tuyaux à emboîtemen 
à épaulement dans les conduites d'évacuation des eaux de pluie 
sont garnis de mélange amiante-ciment, et dans les collecteurs 
d'égoûts, aussi d’une corde goudronnée (fig. XI.48, b, c). Les joints 
de tuyaux à emboîtement conique (fig. XI.48, a) sont réalisés avec 
des garnitures en caoutchouc. Les joints de tuyaux à emboîtement 
à mi-épaisseur (fig. XI.48, d) sont matés d’un mélange amiante- 
ciment ou d’un mortier de ciment projeté. 


18-0948 273 


Le mode de pose des conduites a une influence considérable sur 
leur capacité portante, l’affaissement du sol et, par conséquent, sur 


l'étanchéité des raccords. 


Les tuyaux types pour conduites gravitaires conçus pour être 
protégés par un remblai de 4 ou de 6 m peuvent être simplement 


FIG. XI.48. Joints de tuyaux des 
conduites gravitaires : 
1, garniture d’étunchéité en cavutchouc : 
2, mélange amiante-ciment, 5, enduit 
bituminé: 4, mortier de ciment ; 5, corde 
goudronnée matée 


posés sur le sol naturel aplani et 
recouverts de la terre. Cette solu- 
tion ne s'applique cependant que 
pour D < 500 mm. Pour un dia- 
mêtre D > 600 mm, il convient 
de ménager une rigole dans le sol 
afin que le tuyau soit entouré de 
sol sur un angle de 90° au moins 
(fig. XI.49, a); le remblai à la hau- 
teur de l’axe de la conduite doit 
être fait avec du sable damé par 
couches successives. Si le sol est 
meuble (pression de calcul inférieu- 
re à 1,5 kgf/cm*, ou à 0,15 MPa), 
on posera les tuyaux sur un lit de 
béton (fig. XI.49, b); si un affais- 
sement irrégulier du sol est à crain- 
dre, le lit sera fait en béton armé. 
Sur les roches à gros morceaux, les 
argiles dures, les glaises sableuses, 
on fait un lit de sable avant de 
poser les tuyaux. 

Les tuyaux des conduites for- 
cées doivent résister bien à la fissu- 


ration; de ce fait, ils doivent être précontraints. La précontrainte 
transversale est obtenue par la mise en tension des frettes (spirales), 
et la précontrainte longitudinale, par celle des barres longitudinales. 


Les tuyaux types pour 
conduites forcées sont fabri- 
qués en usine par vibropres- 
sage hydraulique. Ils ont un 
diamètre de 500 à 1600 mm, 


une paroi épaisse de 99 à 


105 mm, une longueur de..." 


5 m. Les armatures spirales 
(frettes) sont confectionnées 
en fil à haute résistance de 
classe B-II, les armatures lon- 
gitudinales, en fils de classe 


&) b) 




S : Lit béton 
On. ECS: | 


FIG. XI.49. Différents modes de pose des 
tuyaux 


Bp-II. Munis d'un emboîtement conique, ces tuyaux sont abouchés 
à l’aide d’une garniture en caoutchouc (fig. XI.48, a). Les modes 
de pose des conduites sont les mêmes que pour les conduites gra- 


vitaires. 




Un tuyau en béton armé pour conduite forcée peut posséder une 
âme (tube) d'acier. Dans ce cas le tuyau est fait sans précontr ainte 
si les pressions prévues ne dépassent pas 10 kgf/cm°, et muni d'un 
frettage spiral si les pressions en service sont de 10 à 20 kgf/ém°. 

Les tuyaux pour conduites forcées sont à calculer à la résistance 
mécanique et à la fissuration ; les tuyaux pour conduites gravitaires 
doivent être calculés à la résistance mécanique et à l’ouverture des 
fissures. 

Les tuyaux éprouvent les sollicitations suivantes: 

— la pression intérieure du liquide compte tenu d’un coup de 
bélier éventuel; 

— Je poids propre comprenant le poids du liquide; 

— la pression du sol; 

— la surcharge en surface due au passage des véhicules. 

Les facteurs énumérés font naître des moments fléchissants et 
des efforts longitudinaux tant dans les sections transversales (annu- 
laires) que dans les sections longitudinales. 

Les méthodes de calcul des tuyaux sont indiquées dans des 
Manuels de calcul particuliers. Les tuyaux sont choisis dans le 
catalogue industriel en fonction de la pression, de la profondeur 
et du mode de pose, en utilisant les barêmes insérés au catalogue. 

Les puits en béton armé des regards de visite des réseaux de 
distribution et d'évacuation des eaux ont le plus souvent une forme 
circulaire en plan (fig. XI.50, a). Les diamètres normalisés inté- 
rieurs sont 1000, 1500 et 2000 mm, pour un diamètre du goulot de 
700 mm. La profondeur du puits, fonction de celle de la conduite 
à desservir, peut varier dans de larges limites. Elle est prise multiple 
de 300 mm. 

Les éléments annulaires des parois en béton armé du puits, ou 
ceintures, ont une hauteur de 600 ou de 900 mm, l'épaisseur de la 
paroi est de 80 à 100 mm. Les ceintures inférieures possèdent des 
ouvertures des quatre côtés pour les conduites entrante et sortante. 
Le montage terminé, les ouvertures restées vides et les jeux entre 
tuyaux et ceintures sont remplis de béton. 

Les ceintures sont posées sur un radier plat épais de 100 à 120 mm 
et recouvertes en haut d’une dalle plate épaisse de 150 mm munie 
d'une ouverture de 700 mm de diamètre au-dessus de laquelle est 
disposé le goulot. Le diamètre du radier, de 500 mm supérieur au 
diamètre intérieur des ceintures, est égal à 1500, 2000 et 2500 mm; 
le diamètre de la dalle supérieure est égal au diamètre extérieur 
des ceintures (1160, 1680 ou 2200 mm). 

Le goulot est recouvert d’une dalle en béton armé de 840 mnt 
de diamètre, épaisse de 70 mm, percée d’un trou de diamètre d — 
— 580 mm protégé par une plaque standard en fonte. Si le puits 
est situé sur la voie publique ou dans une entreprise industrielle 
avec circulation de véhicules lourds, la dalle circulaire recouvrant 
le goulot est remplacée par une dalle routière de 1150 x 2500 mm 
épaisse de 220 mm, percée en son centre d’un trou de puits de 580 mm 


18% 275 


s_e..cee LENLE= " [mt LLLIIEPS 
, , Ya td . 




RE DNA 


AE REZ CPRAPUEZLU 
Lomme ER 


& CAT LAIR ORNE ANS 


FIG. XI.50. Puits en béton armé: 


a, puits rond; b, puits rectangulaire; 1, ceintures: 2, dalle supérieure; 3, ceinture de 
goulot; 4, talus, 5, plaque métallique; 6, anneau d’assise de la plaque; 7, crampons: 
8, radier : 9, béton coulé en place autour des conduites; 10, panneaux des murs plats 


de diamètre. Autour du goulot, la dalle routière repose sur un sol 
de sable compacté de 250 mm d'épaisseur. 

La partie basse du puits peut avoir une forme rectangulaire 
(fig. XI.50, b); on utilise à cet effet des panneaux-types des murs 
pour réservoirs rectangulaires (voir $ XI.4). 

La capacité portante des structures-types en béton armé permet 
de placer le radier à une profondeur de 7 m, et la dalle supérieure, 


de 0,5 à 3 ou 4 m, en fonction de la surcharge en surface. 


$ XI8. CONCEPTION ET CALCUL DES CHATEAUX D'EAU 


Les châteaux d’eau ont pour fonction de régler la pression dans les 
réseaux de distribution des eaux. 

L'élément principal de tout château d’eau est le réservoir. Sa 
contenance et hauteur d'implantation sont choisies en fonction de 
l'intensité de la consommation d’eau et de la pression à assurer au 
réseau. 

Les châteaux d’eau sont très variés d’après leur contenance (de 
15 à 3000 m°) et d’après la hauteur de la structure d'appui, appelée 


pylône (de 6 à 50 m). 


On distingue les châteaux d’eau avec enceinte de protection 
(fig. XI.51, a), dont le réservoir est enfermé dans une espèce de 
coque appelée à maintenir une température requise, et les châteaux 
d'eau sans enceinte (fig. XI.51, b) où la couche thermo-isolante 
(quand elle existe) est appliquée directement sur les parois. Les 
châteaux d’eau sans enceinte de protection (ou d’un type mixte) 
sont plus avantageux, car ils sont plus faciles à construire, leur 
pylône est moins lourd et le coût de la construction est plus bas. 

Le château d’eau peut avoir un réservoir unique (fig. X1.51, a, b) 
ou plusieurs réservoirs (fig. XI.51, c). 

Les calculs technico-économiques montrent que, la hauteur et 
le schéma du château d’eau étant les mêmes, le coût de la construc- 


FIG. XI.51. Différents types de châ- FIG. XI.52. Réservoirs des châteaux 
teaux d’eau: d’eau 


1, pylône; 2, réservoir; SZ, enceinte de 
protection 


tion ne dépend presque pas de la contenance du réservoir : une aug- 
mentation de la contenance de 30 à 40 % ne fait augmenter le coût 
que de 3 à 6 %. Les réservoirs étant les mêmes, le coût est propor- 
tionnel à la hauteur. 

Les données de l’analyse technico-économique ont conduit à une 
série de paramètres normalisés des châteaux d’eau: hauteur de 
9 à 27 m pour une contenance de 25 à 50 m° et hauteur de 12 à 42 m 
(multiple de 3 m) pour une contenance de 150, 250, 500 et 1000 m°. 

Le réservoir est fait en béton armé ou en acier. Le réservoir le 
plus simple en béton armé à une paroi cylindrique et un fond porteur 
plat reposant sur le plancher plein en béton armé de la structure 
d'appui (fig. XI.92, a). Ce sont les réservoirs à paroi cylindrique 
en haut et tronconique en bas, à fond porteur, qui procurent l’écono- 
mie la plus grande (30 à 40 %) et la dépense de matériaux la plus 
faible. LS 

Si le réservoir en béton armé a une contenance élevée, sa paroi 
doit être précontrainte afin de résister convenablement à la fissura- 
tion. La précontrainte étant difficile à réaliser à une grande hauteur, 
on préfère souvent des réservoirs métalliques (voir $ XI.6). 

Le pylône est généralement en béton armé. Si la contenance du 
réservoir n’est pas grande, en fonction des conditions d'implanta- 




tion, on utilise aussi des pylônes métalliques, et si la hauteur est 
de 9 à 12 m, le pylône est construit en briques sous forme d’un fût 
cylindrique aux parois épaisses de 250 à 380 mm. La figure XI.53 
représente un château d’eau sans enceinte de protection, à réservoir 
métallique et sur pylône en briques. 

Le pylône en béton armé a la forme d’une coque cylindrique 
pleine coulée en place (fig. XI.54, a) ou d’un système de barres 
tridimensionnel (fig. XI.04, b); il existe 
aussi des systèmes réticulés (fig. XI.55). 
Ce sont les pylônes préfabriqués en béton 
3 armé du type réticulé qui assurent le 
minimum de frais: leur coût est 1,5 à 
2 fois moins grand que pour les pylônes 
pleins en béton coulé en place et 2 à 3 
fois moins grand que pour les pylônes en 
briques; quant aux pylônes métalliques, 
ils ont sensiblement le même prix. 

Les châteaux d’eau à pylône en béton 
armé sous forme de coque coulée en place 
(fig. XI.54, a) sont construits au moyen d’un 
coffrage glissant réutilisable. La nécessité 
d’assurer un déplacement correct du cof- 
frage impose une épaisseur de la paroi beau- 
coup plus grande que celle qui est néces- 
Le. saire d'après les calculs, ce qui augmente 
le coût de la construction. Un pylône de ce 
type n’est rationnel que pour une hauteur 
considérable (24 m au moins) et une con- 
FIG. XI.53. Château tenance élevée (800 m° au moins). Le fût 
d'eau sur pylône en bri- du pylône prend appui sur une fondation 

ques : en béton armé coulée en place, munie 

gpondation: 2, pylône et d'une nervure annulaire entourant le fût. 

"| lique Un pylône en béton armé du type à 

portiques (fig. XI.54, b) diminue la dé- 

pense des matériaux, mais il est moins facile à construire qu’un 

pylône à paroi pleine: ce sont les nœuds rigides qui s'avèrent les 
plus délicats. 

Le pylône réticulé préfabriqué en béton armé (fig. XI.55, a) 
est constitué par des losanges (fig. XI.55, b) et des ceintures 
(fig. XL.55, c). Un losange sè forme à partir de montants inclinés 
et d'éléments de ceinture assemblés sur le sol. Tous les éléments 
préfabriqués sont munis d’aciers en attente qui viennent se souder 
sur des goussets dans les nœuds. Les joints sont remplis de béton 
(fig. XI.55, d). 

Les structures d'un château d'eau qui font l’objet d’un calcul 
spécial sont le réservoir, le pylône, la fondation et l’enceinte de 
protection. Les réservoirs cylindriques sont calculés comme il a été 
dit dans les $$ XI.3 et XI.6, et les éléments de l’enceinte de protec- 






ASS SSSSSSSSSSSSSSSSSSSESSSSSSSS 


RE \ 
-e  d li 


à NN Se 


—— "1 






SEL 1 
DU IL 


FIG. XI.54. Château d’eau sur pylône en béton armé: 


a, avec pylône à paroi pleine coulé en place; b, avec pylône à portiques; 1, fondation en 
béton armé: 2, prions 3, enceinte de protection surbaissée (galerie calorifugée), 4 réser- 
voir (en héton armé); 5, couche thermo-isolante sur la paroï du réservoir ; 6, toit 


Schéma d'assemblage 


FIG. XI.55. Château d’eau sur pylône réticulé préfabriqué en béton armé: 
1, soudage sur chantier; 2, limite du bétonnage de scellement 




tion, de la toiture du réservoir et des plates-formes de service, comme 
il a été dit dans les Chapitres IX et X. 

Au calcul du pylône et de la fondation, on adopte comme charges 
fondamentales (fig. XI.56) le poids du réservoir rempli d’eau G,, 
le poids propre du pylône G,, le poids de la fondation avec remblai 
G; et les efforts horizontaux provenant 
de la pression du vent sur l'enceinte de 
protection (le réservoir) P, et sur le 
pylône P.. 

Le pylône dans son ensemble tra- 
vaille à la compression et à la flexion 
sous l’action des charges G,;, G; et du 
moment fléchissant (dû à P,, P;) dont 
la valeur maximale est enregistrée au 
niveau de Ja fondation. Si la paroi du 
pylône est pleine, le calcul est fait pour 
une section transversale annulaire. Un 
pylône à portiques et un pylône réticulé 
sont considérés comme des systèmes de 
barres tridimensionnels. 

Les cotes d'implantation de la fon- 
FIG. XI.56. Pour le calcul dation sont calculées compte tenu de la 

d'un chateau” d'eau pression maximale sur le sol sous la fon- 

dation due à l’action cumulée de la force 
normale et du moment. 

La stabilité de l'ouvrage dans son ensemble est vérifiée en envi- 
sageant son basculement imaginaire du côté sous le vent autour du 
nu de la fondation (fig. XI.56, point À). Le moment de basculement 
dû au vent et le moment antibasculement dû au poids propre des 
éléments de l’ouvrage sont calculés par les formules 


L'effet du vent est pris en compte avec un coefficient de surcharge 
n —= 1,3, et le poids propre des structures (en supposant que le 
réservoir est vide), avec un coefficient de surcharge diminué n = 
= 0,9. 

Le coefficient de stabilité au basculement est 


k= Med 15, 


CHAPITRE XII 


QUELQUES EXEMPLES DE PROJETS DE STRUCTURES 
EN BÉTON ARMÉE 


$ XIL.1. GÉNÉRALITÉS 


Le lecteur trouvera dans ce chapitre quelques exemples caractéristi- 
ques de calcul et de conception de structures en béton armé utilisées 
dans les ouvrages des réseaux de distribution et d'évacuation des 
eaux. La plupart des pièces étudiées ont été conçues pour la construc- 
tion des réservoirs rectangulaires en éléments préfabriqués. Il s’agit 
plus particulièrement d’un réservoir de 6000 m* de capacité, de 
dimensions 36 X 36 m en plan (fig. XII.1). Conformément au pro- 
jet, ce réservoir reçoit une toiture en éléments préfabriqués qui existe 
en deux variantes: 

19 toiture de hourdis nervurés sur poutres, supportée par un 
quadrillage de poteaux de 6 %X 6 m (fig. XII.1, b); 

29 toiture de dalles reposant directement sur les poteaux au 
quadrillage de 4 x 4 m (fig. XII.1, c). 

En première variante, nous calculerons : 

un panneau de toiture non précontraint ($ XII.2); 

un panneau de toiture précontraint ($ XII.3); 

une poutre à travées multiples préfabriquée ($ XI1I.5). 

En deuxième variante, nous nous proposons de calculer: 

un panneau de toiture carré bordé de nervures ($ XII.4); 

un poteau avec semelle ($ XII.G); 

un mur en panneaux préfabriqués en béton armé ($ XII.7). 

Nous étudierons en outre le mur précontraint d'un réservoir 
cylindrique enterré en éléments préfabriqués en béton armé ($ XII.8). 


$S XII.2. PANNEAU DE TOITURE NERVURE SANS PRÉCONTRAINTE 


Ce panneau fera partie de la toiture montrée sur la figure XII.1, b. 
Il est représenté sur la figure X11.2, a. La masse de 1 m° du panneau 
est 275 kg. Béton de classe M 300, coefficient de comportement, 
Mp1 = 1. Armatures principales des nervures en acier de classe A-TIT. 
Longueur de flambement, recensement des charges. On se donne 


à priori les dimensions de la section de la poutre : h — JL Le _ 600 — 


— 60 cm; b — 0,54 — 0,5 x 60 — 30 cm. Puisque le panneau 
repose sur les consoles des poutres (voir fig. XI1.6), on prend comme 
longueur du panneau !, — 555 cm, et comme longueur d’appui sur 




JL En 


TOUTE ISSN 
AIN Er 
HE a: 
6000 | 6000 JE 000 |4000 


S6000 2000 
.. —————— 5,40 
nn nn ns en nn 
<[ os” CEE 
_ 540 
À UE 3) 
5,00 


FIG. XII.1. Réservoir nuits en éléments préfabriqués en béton armé 
(pour illustrer les exemples de calcul): 
a, vue en plan; bet c, vues en coupe 




la console de la poutre, 10 cm. La longueur de flambement (portée 
libre) sera donc L, = 555 — 10 — 545 cm. 

Les charges caractéristiques et de calcul sont résumées dans le 
Tableau XII.1. 

La charge totale de calcul, déterminée suivant les états-limites 
ultimes, pour 1 m de longueur du panneau de 1,5 m de largeur nomi- 
nale est 


q — 2640 x 1,5 — 3960 kgf/m (39 600 N/m). 


Les charges caractéristiques par 1 m de longueur du panneau, 
exprimées en kgf/m (N/m), sont: 

— charge permanente g° — 2040 x 1,5 — 3060 (30 600): 

— surcharge de longue durée (effet de la neige) pra — (100 — 
— 10) 1,5 = 45 (450); 

— surcharge de courte durée (le panneau étant assimilé à une 
plate-forme de service) pa — 150 x 1,5 — 225 (2250); 

— charge caractéristique totale maximale qg° = 3285 (32 850). 

Données sur les matériaux. Pour le béton M 300, on trouve 
dans les Annexes III, IV et V les valeurs de Re = Rrrr — 
— 170 kgf/cm? (17 MPa); Rie = Ryrrr = 15 kgf/em? (1,5 MPa); 
Rpr = 135 kgf/cm° (13,5 MPa): R+r = 10 (1 MPa), E}, — 
—= 290 000 kgf/cm°? (29 000 MPa). 


TABLEAU XII.I1 


Charges caractéristiques et de calcul (suivant les états-limites ultimes) 
sur i m? de la toiture 


Charge caracté- |Cocfticient RE . tte 


Charges Tera kgf/m? de sur- limites ultimes, 
(N/m?) charge kgt/m? (N/m?) 
Charges permanentes : 
panneaux préfabriqués en béton 
armé 275 (2750) 1,1 303 (3030) 
coulée de liaison en ciment 
0,025 x 2200 59 (550) 1,3 74 (710) 
tapis imperméable 10 (100) 1,3 13 (130) 
remblai sur le toiture 1700 (17 000) 1,2 2040 (20 400) 
Total : charges permanentes 2040 (20 400) 2430 (24 300), 
Surcharges : 
effet de la neige 100 (1000) 1,4 140 (1400) 
{ou) surcharge comme sur pla- 
te-forme de service 150 (1500) 1,4 210 (2100) 
Charge totale maximale | 2190 (21 900) | | 2640 (26 400) 










Boucles de 


19224" Suivant 2-2 


200 Fe 
- Ù, à . 
T2 p.500 ne 
CA, 1 C-1 S 
25 |1l25 


ae} Le 


4, A 
FAI RENTE 
145 |\ 1 1200 2700 (e5e-300) "1 1350 1451S 
{esp 150) 5540 (esp 150) 
Suivant 3-3 


3 1485 


Armature des nervures (carcasses soudées): armatures longitudi- 
nales principales en barres d'acier de classe A-III de diamètre égal 
ou supérieur à 10 mm, À, — 3600 kgf/cm? (360 MPa), E, — 
— 2 000 000 kgf/cm°? (200 000 MPa); armatures transversales et de 
montage en acier de classe A-I, R, = 2100 kgf/cm? (210 MPa), 
R;.tr = 1700 kgf/cm? (170 MPa), E;.tr = 2 100 000 kgf/cm° 
(210 000 MPa) (Annexe VI). Armature du hourdis (treillis soudé) en 
acier de classe B-I, R, — 3150 kgf/cm° (315 MPa) (Annexe VII). 


Calcul aux états-limites ultimes 


Section à donner aux nervures. La hauteur de la nervure (sans pré- 
contrainte) est choisie empiriquement entre k — 1/14 et h — 1/18 
de la portée libre /,. Puisque la charge est grande, on retient k — 
= [,/14 = 545/14 Z 40 cm et l’on donne à la nervure une largeur 
{au bas de la section) égale à 8,5 cm. 

Hauteur utile de la nervure À, = h — a = 40 — 7 — 33 cm 
(en supposant que les aciers tendus seront disposés en double file). 
Largeur totale des nervures du panneau (valeur moyenne, compte 
tenu de la dépouille) b Æ 22 cm. 

Vérifions les conditions (VI.44) et (VI.45): 


kR{trdho < Q L'0,35R,,;bh, (avec Q = 0,5ql); 
0,6 x 10 x 22 x 33 < 0,5 x 3960 x 5,45 < 0,35 x 135 x 22 X 33; 
4350 kgf (45,3 kN) << 10 800 kgf (108 KN) << 34 300 kgf (343 kN). 


La section choisie est donc convenable: les armatures transver- 
sales prévues dans les nervures reporteront une fraction de l'effort. 
Calcul de résistance suivant les sections normales. Le moment 
fléchissant maximal (à mi-portée) est 
2 Q 2 
M = = OX L 14700 kgf-m(147 kN-m). 

On retient pour le calcul une section en T (fig. XII.3) en prenant 
la largeur totale du hourdis bj — 150 cm (voir $ VI.3). Supposant 
que x < hx, on assimile la section à un profil rectangulaire b} X ho. 
D'après la formule (VI.13) 

M 1 470 000 
Ào = HER — 180% 88x18 — Ur0bT 


En fonction de À, — 0,067, le Tableau VI.1 donne £ — 0,07 
et n — 0,965. Ainsi donc, la hauteur de la zone comprimée 245= 
— £h, — 0,07 x 33 — 2,3 cm est bien inférieure à An = 5 cm. 


<— FIG. XII.2. Panneau de toiture nervuré: 


a, dimensions du coffrage; b, plan de ferraillage sans précontrainte; ce, idem, avec pré- 
contrainte; 1, plaque de scellement en acier 




D’après la formule (VI.14), la section de l’armature longitu- 
dinale est 


M 1 470 000 : 2 
Fa Re = 0,068 35 x 3 600 = 12,8 cm 


On retient comme armatures longitudinales 2 G 20 + 2 @ 22 de 
classe A-III avec F, — 13,88 cm? (Annexe VIII). Les barres seront 
disposées en double file (voir 
fig. XII.2, b). 

Calcul de résistance suivant les 
sections obliques. L'effort tran- 
chant maximal (sur appui) est 


Q = 0,5ql, = 0,5 x 3960 x 5,45 — 
— 10 800 kgf (108 KkN). 


Chaque nervure sera armée par 
une carcasse soudée (fig. XII.2, b). 
Chaque barre transversale aura com- 
me diamètre dt — 8 mm (ftr = 
—= 0,5 cm°); on a au total » = 2 barres (deux nervures) avec F4, = 
= fyn = 0,5 X 2 = 1 cm. 

L’effort de calcul à l’unité de la longueur de la nervure repris 
par les barres transversales est égal, conformément à la formule 
(VI.53), à 


FIG. XII.3. Section retenue lors 
du calcul du panneau 


tr = Tbihe = 2X2x22x 888.10 — 01 kgf/cm (610 N/cm). 
I1 ne doit pas être inférieur à 
Que = = = 110 kgf/em (1100 N/em). 


L'écartement des barres transversales se déduit de l'égalité (VI.54): 


Ra. trFtr 4700 X 1 
die Tr AD —= — 15,5 cm. 


La condition (VI.55) donne 


L'—= 


L'’écartement dicté par les dispositions constructives (voir $ VI.1) 
est u < h/2 = 40/2 — 20 cm; u<L15 cm 

On retient donc u — 15 cm, conformément à la plus petite 
valeur de l’écartement des barres transversales pour les portions 
des nervures voisines aux appuis de longueur {/,1,. 

Au milieu de la travée on prendra uw — %/,h — 3 x 40/4 = 
— 30 cm (voir fig. XII.2, b). 




Calcul du hourdis. La longueur du panneau entre nus des nervures 
longitudinales est 1, — 148,5 — 2 X 12 Æ 125 cm, et entre nus 
des nervures transversales 7, — 135 — 2 x 5 = 125 cm. Le rapport 
l/l, = 1 permet d’assimiler le hourdis à une dalle encastrée suivant 
le contour et possédant la même armature en travée et sur appui. 

La charge de calcul sur { m°? du hourdis de 5 cm d'épaisseur, 
compte tenu de sa propre masse et des données du Tableau XII.1, 
est égale à 


g = 0,05 x 2500 x 1,1 + (71 + 13 + 2040) + 210 
% 2475 kgf/m°? (24,75 kN/m°). 


Le moment fléchissant de calcul sur appui et en travée sera 
calculé comme il a été dit dans le $ X.2 pour le cas des treillis soudés 
en rouleaux : 


M = APN 84 kof.m (810 N-m). 


Le calcul de la section du hourdis donne k, = h — a = 5 — 2 — 
— 3 cm, b — 100 cm. D'après la formule (VI.13) 
M 8100 
A0 = ER — 0x x 135 — UyU67, 
En fonction de cette valeur de À,, le Tableau VI.1 donne n = 
= 0,965. La section à donner aux armatures, définie par (VI.14), 


Me 8100 
— nhoha 0,965 X 3 X 3150 


Grâce à la contribution des nervures disposées suivant le péri- 
mètre, cette section peut être diminuée de 20 % (voir Chapitre X). 

Nous disposerons donc en travée un treillis soudé présentant les 
mêmes armatures principales F, — 0,98 cm’? dans les deux sens du 
type 200/200/5/5, de 1300 mm de large et de 5400 mm de long. Au- 
dessus des nervures longitudinales seront placés des treillis avec 
des armatures transversales principales (porteuses) F#, — 0,84 cm° 
du type 250/150/3/4, de 550 mm de large et de 5200 mm de long. 


F, — 0,89 cm2. 


Calcul aux états-limites d'utilisation 


La surcharge caractéristique de courte durée, comparée à la 
charge caractéristique totale, ne fait que 


po,[e = 100 6,8%. 




Nous admettons donc que toute la charge agit pendant une longue 
durée. 

Calcul de la flèche du panneau. La charge de calcul est égale 
à la charge caractéristique multipliée par un coefficient de surcharge 




n —= 1. La charge totale, égale à la surcharge de longue durée, est 
11 = 3285 kgf/m. 

Cherchons la flèche à mi-portée où le moment fléchissant est 
Mir = qul/8 = 32,85 X 545°/8 — 1 220 000 kgf-cm (122 kN -m). 


Calculons les caractéristiques géométriques pour la section en T 
retenue (fig. XII.3). L'existence de l’armature sera négligée, car elle 
influe très peu sur les résultats des calculs. 

La section est égale à 


F,=F=22 x 40 + 128 X 5 — 880 + 640 — 1520 cm°. 
| Le moment statique par rapport au bord inférieur de la section 
S, & S = 880 X 20+640 X 37,5 — 17 600 +24 000 = 41 600 cms. 
La distance entre le bord inférieur de la section et le centre de 
gravité de cette dernière est 
Yeg = S/F = 41 600/1520 = 27,4 cm. 


Le moment d'inertie de la section est 
I, & J= 2XT +22 X 40 x 7,424 


+ RS + 428 x 5 x 10,12 — 226 520 cmt. 


Le module de résistance par rapport au bord tendu de la section 


__ J 226530 | : 
ae 27e — 8250 cm°. 


Calculons le module de résistance de la section, compte tenu 
des déformations anélastiques du béton en zone tendue, à l’aide de la 
formule (VI.77) en tirant la valeur de y = 1,5 du Tableau VI.2: 


Wi = YW, = 1,5 x 8250 — 12 380 cm°. 
La distance e,,. (voir fig. VI.21) est égale à 
Egpe = Yeg — 4 = 27,4 — 7 = 20,4 cm. 


Calculons les grandeurs auxiliaires d’après les formules (VI.91) 
à (VI.96) et les dimensions-de t-section retenue (voir fig. XIT.3), 
compte tenu de l'absence de l’armature comprimée F; = 0 et de la 
nullité de la force longitudinale et de l'effort de précontrainte: 


Mi= Mes =M; N,=0; Mie —0; 


NN TR NN 249. 




PhéRprir  22X38xX 170 — 


ET 1 — 
LS Dion 
7 14,8+1[1+5(0,3+0,81)]/10 X 0,019 x 6,9 
_ V'hh/ho+E 0,88 x 5/38+-0,1472 7] 
a he] 1 on | 
= 33 X 0,92 — 30,3 cm ; 


la formule approchée (VI.91a) donne 


Z = ho — hp/2 = 33 — 2,5 — 30,5 cm; 


_ RtrtzWr __ 15X 12380 | 
dde) MN9Y 1220000 = 0,152 ; 


Va = 1,25 — sm = 1,25 — 0,8 x 0,152 = 1,13 => 1; 
on pose donc Ya = li. 


La raideur caractéristique flexionnelle du panneau se calcule 
suivant les formules (VI.100) et (VI.100a): 


B — ho21Eal'a __ 33X30,3X2X 105X 13,88 
7 Val—z/e, c)+birab 1+0,9X0,8 
= 15,6-10? kgf-cm? (1,56 -10°MPa:cmi), 


— 0,147 ; 


OÙ ea, — © (la précontrainte est inexistante, NV, = 0); v = 0,15 
(action prolongée de la charge); #1 = 0,9; 


: EaFa : 2.106 x 13,88 _—.. 
lab TO EE) bhoEpv — (0,88-+0,147) 22 x 33 X0,29.106x 0,15  *?0: 

La flèche maximale à mi-portée du panneau sous la charge 
uniformément répartie qrr — 3285 kgf/m (32,85 kN/m) est calculée 
à l’aide de la formule établie pour une poutre à simple travée libre- 
ment posée sur deux appuis: 


5 grr£ 5 32,85x 545 | 
Î=3m p 3m 15,610 —2410cm; 

autrement dit, la flèche reste en dessous de la valeur limite admis- 
sible f — 2,5 cm pour 5 m << 10 m (voir $ VI.6). 

Calcul de l’ouverture des fissures dans les nervures du panneau. 
La structure en question doit avoir une résistance à la fissuration 
de la 3° catégorie, ce qui revient à dire que l'ouverture des fissures 
sous une charge de longue durée ne doit pas dépasser af. 14 = 0,3 mm 
avec un coefficient de surcharge n égal à 1. 


19—0948 289 


La contrainte dans l’acier à mi-portée se calcule à l’aide de la 
formule (VI.101) en y posant V, = 0 (car il n’y a pas de précontrain- 
te) : 

___ Myr __ 1220000 | 
Ca = Fr 13.88 x 30.3 — 2 900 kgf/cm? (290 MPa). 

Calculons l'ouverture des fissures normales à l'aide de la rela- 
tion (V.13) en y posant À = 1, c1a = 1,5 (action prolongée de la 
charge); n — 1 (barres à haute adhérence); nu — 0,019. Il vient 


ay (mm) = kcjan DA 20 (3,5 — 1001) ” d (mm) — 


= 1x 1,5 x 1-20 20 (8,5 — 100 x 0,019) 22 — 0,195 mm. 
Autrement dit, l’ouverture reste en dessous de la limite admissible 
At.]d — 0,3 mm. 

Calculons l’ouverture des fissures obliques dans la nervure au 
moyen des formules (VI.103) à (VI.106) en tenant compte de l’action 
prolongée de la charge, en posant V, = 0 (iln'ya De de  Précon- 
trainte), pr = 0 (il n’y a pas d’armatures relevées), das = di, = 
— 8 mm (diamètre des cadres) et en admettant que la section consi- 
dérée se trouve à la distance h, de l'appui: 


Qrr = QI (0,54, 2 Lo) — 32,85 (0,5 2 545 —— 33) — 7870 kgf (78,7 kN); 


_ Qrr ___7870 
ln = xs — 10,8 
Hp = Utr = Ftr/bu = 1/(22 X 15) = 0,00303; 
k = (20 — 1200u,) 10% = (20 — 1200 x 0,00303) 108 = 16,3-10; 


at (mm) = Cia [ho + 30dmax (mm)] FT = 


— 1,5 x 16,3:105 (80-80 x 92 012 mm: 


autrement dit, l'ouverture des fissures reste inférieure à la valeur 
limite admissible at. j14 — 0,3 mm. 

Autres calculs. En plus des grandeurs indiquées plus haut, il 
y a lieu de calculer aussi: 

— les longueurs d'ancrage des armatures longitudinales des 
nervures du panneau sur Tes appuis; 

— les dimensions des cordons de soudure qui fixent les armatures 
longitudinales sur les plaques de scellement en acier; 

— la résistance du hourdis du panneau vis-à-vis des surcharges 
qui peuvent se manifester lors des opérations de manutention sur le 
chantier ; 

— la section à donner aux boucles de levage du panneau; 

— la résistance du panneau dans les conditions de montage et 


de transport ; 




— certains autres facteurs. 

Malgré leur importance, ces calculs n’interviennent pratiquement 
jamais dans la solution technique retenue. Nous les omettons ici 
en soulignant qu'ils sont absolument indispensables dans la pratique 
du projet. | 


$ XIIS. PANNEAU DE TOITURE NERVUREÉ PRECONTRAINT 


Ce panneau, dont les nervures comportent des armatures longitudi- 
nales précontraintes, fera partie de la toiture montrée sur la figu- 
re XII.2, a. 

Béton de classe M 400, avec R,, = 175 kgf/cm? (17,5 MPa), 
Rrix = 225 kgf/em*? (22,5 MPa), R4 = 12 kgf/em° (1,2 MPa), 
Rtrir = 18 kgf/cm? (1,8 MPa), E, = 0,33:10$ kgf/cm? (0,33 x 
X 10° MPa) (Annexes V et VI), my, = 1 (l'humidité supposée du 
milieu d'utilisation est supérieure à 75 %); résistance de précon- 
trainte du béton Ro — 300 kgf/cm° (30 MPa). 

Armatures longitudinales principales des nervures du panneau 
en barres à haute résistance, acier de classe A-IV, avec R, — 
— 5000 kgf/cm°? (500 MPa), Arr — 6000 kgf/cm°? (600 MPa), E, — 
— 2.105 kgf/cm° (2.105 MPa) (Annexe VI). Coefficient de comporte- 
ment de l'acier m,, > 1 (acier sans palier). Armatures mises en 
précontrainte par pré-tension par le procédé électrothermique. 
Béton traité par la chaleur, différence des températures de l’arma- 
ture et du moule (communiquée par l’usine) At = 20 °C. Armatures 
de précontrainte en zone comprimée (en charge) Fr. == 0. Résistance 
à la fissuration exigée: 3° catégorie (ouverture des fissures admise 
at. 14 — 0,3 mm pour les charges affectées d’un coefficient de sur- 
charge n — 1). 


Calcul aux états-limites ultimes 


Le dimensionnement des nervures, leur calcul à la résistance suivant 
les sections obliques et le calcul du hourdis sont les mêmes que dans 
le $ XII.2. 

Faisons le calcul à la résistance suivant les sections normales. 
Les calculs préliminaires (omis dans ce paragraphe) donnent pour 
l’armature longitudinale 4 G 16 mm A-IV avec Fc = 8,04 cm° (voir 
Annexe VIII). Vérifions la résistance du panneau à mi-portée sui- 
vant la section normale. 

Cherchons d’abord la hauteur de la zone comprimée pour ma, = 1 
à l’aide des équations (VI.2) ou (VI.9): … 


___ FpcRamMmas __ 8,04 X 5000 X 1 _, 
aa 0 DRpr A190X17 1,54 cm. 
Posant k, — 35 cm, calculons la hauteur relative de la zone com- 
primée : 


E = zlho = 1,54/35 — 0,044. 
19% 291 


Calculons £x d’après les formules (VI.5) à (VI.7) en posant 
à priori Oo — Aa: 


O1 = Ra + 4000 — ©, — 4000 kgf/cm°? (400 MPa); 
£o — 0,85 — 0,0008R,, — 0,85 — 0,0008 x 175 = 0,71; 


Ep = — {1 Re 
à 0 LE +) +00 (: F7.) 


Le coefficient de comportement de l'acier à haute résistance 
Ma, sera calculé à l’aide de la formule (VI.4); pour l’armature A-IV, 


nous poserons dans cette formule m,, — 1,2 (voir $ VI.3): 
Mau = Mas — (Mas — 1) ÉlEr = 1,2— (1,2 — 1) 0,044/0,52 — 1,18. 


La formule (VI.9) nous donne la hauteur de la zone comprimée x 
pour Ma, —= 1,18. La valeur de x ainsi obtenue est 1,82 cm, donc 
inférieure à Erho — 0,92 X 39 — 18,2 cm. 

Vérifions la résistance du panneau à l’aide de (VI.11). La capacité 
portante de la section du panneau déterminée par la condition du 
moment est égale à 


FrcRaMayg (Ro — 0,57) = 8,04 X 5000 X 1,18 (35 — 0,5 x 1,82) — 

—= 1 615 000 kgf/cm (161,5 kN:m), 

donc supérieure à la valeur de calcul du moment fléchissant A1 — 
— 1 470 000 kgf:cm (147 KkKN-m). 

Le calcul du panneau à la résistance suivant une section oblique 


et le calcul du hourdis entre nervures sont parfaitement analogues 
aux calculs décrits dans le $ XIT.2. 


Calcul aux états-limites d'utilisation 


Détermination de l'effort de précontrainte. Conformément aux 
prescriptions du $ III.2, nous admettons que la précontrainte de 
traction 0, créée dans les armatures de précontrainte est égale à la 
plus grande valeur admissible pour les barres d'acier de longueur 
1 6 m mises en précontrainte par pré-tension avec l'emploi des 
moyens électrothermiques. D'après la formule (111.10), le calcul 
doit tenir compte de l’imprécision de la mise en tension égale à 


p = 300+ 7 — 300 scoot — 900 kgf/em? (90 MPa). 


La formule “ti fournit la valeur de la précontrainte: 
Co = Rarr — p —= 6000 — 900 = 5100 kgf/cm° (510 MPa). 


Pertes instantanées: par relaxation des tensions dans les barres 
mises en précontrainte par les moyens électrothermiques 


01 = 0,030, = 0,03 x 5100 = 153 kgf/em? (15,3 MPa): 


par différence des températures pendant le traitement du béton 
O9 = 12,5 At = 12,5 x 20 = 250 kgf cm° (25 MPa). 


Les pertes par déformation des appareils d'ancrage offdh) et 
des moules 6, ne sont pas à calculer, car elles ont été prises en compte 
lors du calcul de l'allongement total des armatures tendues par les 
moyens électrothermiques. 

Après déduction des pertes signalées, la contrainte créée dans 
les armatures de précontrainte 6,, et l'effort de précontrainte W,,; 
deviennent 


Oo1 — O9 — O1 — Oo — 91400 — 153 — 250 — 
— 4697 kgf/cm* (469,7 MPa); 
No = Goilpe = 4697 X 8,04 = 37 800 kgf (378 kKN). 
La contrainte dans le béton au niveau du centre de gravité de 
l’armature tendue se calcule à l’aide de la formule suivante (dans 


laquelle les valeurs de F, J et y, sont les mêmes que dans le 
$S XII.2): 


Où. ne = | el + a) 


=(- rs 37 800 X 22,4? 
LL 1520 226 530 
OÙ €o1 = Yeg — pc — 27,4 — 5 — 22,4 cm. 

Puisque 65.pe/Ro = 108,6/300 = 0,36 << 0,6, les pertes par flua- 
ge instantané seront calculées d’ après la première des formules 
(II1.21), en faisant intervenir le coefficient 0,85 qui tient compte 
du traitement du béton par la chaleur: 


04— 0,85 x 500 PE — 0,85 x 500 x 0,36 — 153 kgf/em? (15,3 MPa). 


| — 108,6 kgf/cm? (10,86 MPa), 


Ainsi donc, les pertes instantanées (premières) sont évaluées à 
Op = O1 + O2 + 08 = 153 + 250 + 153 — 556 kgf/cm° (55,6 MPa). 
Pertes différées: par retrait du béton, selon le Tableau IITI.2 
o{adh) — 350 kgf/cm°? (35 MPa); 

par fluage différé du béton, selon la formule (111.22) et compte 
tenu des calculs précédents, 
o{adh) — 0,85 x 2000 x 0,36 — 611 kgf/cm* (61,1 MPa). 
Les pertes différées (secondes) s’évaluent donc à 
Ope = ofadh) + otadh) = 350 + 641 — 961 kgf/cm? (96,1 MPA). 
Après déduction de toutes les pertes, la précontrainte créée dans 
l’armature est égale à 
O2 = O0 — (Op1 + Ope) = 9100 — (556 + 961) — 
— 3583 kgf/cm*? (358,3 MPa). 


, .Effort de précontrainte 
No = Goalpe = 3583 X 8,04 Æ 29 000 kgf (290 kN). 


Calcul à la formation des fissures normales dans les nervures 
du panneau. D’après la formule (VI.75) (voir fig. VI.21 et les valeurs 
de W, et F indiquées dans $ XII.2) 


ry = 0,8W/F, & 0,8 X 8250/1520 = 4,4 cm. 


Moment des forces internes immédiatement avant la formation 
des fissures dans la zone tendue (en service) (voir formule (VI.76)) 


Mi = RynWr + Mic = RieuiWi + MmtNos X 
X (eo1 + ry) = 18 X 12 380 + 0,9 X 29 000 (22,4 + 4,4) — 
— 293 000 -- 700 000 — 923 000 kgf-cm (92 kN-m). 


Moment des forces extérieures Méxt — Air — 1 220 000 kgf:cm 
(122 KN:m) (voir $ XII.2). Puisque M4XŸ > Mr (Voir la condition 
(VI.74)), il se produit des fissures normales dans le panneau. 

Calcul de la flèche du panneau. Le moment de calcul et les 
caractéristiques de la section du panneau ont été trouvés dans le 
$ XII.2: 

M, = 1 220 000 kgf.cm (122 kKN-m); F# — 1520 cm°; 
— 41 600 cm*; 
Yeg = 21,4 cm, J = 226 530 cm"; 
W, = 8250 cm”; 
Wy = 12 380 cm°; espece = 20,4 cm. 
Calculons les grandeurs auxiliaires d’après les formules (VI.91) 


à (VI.98): 


#5. DA A ___ Fa ___ 8,04 
RTE, — 0,33-108 HUE bho 22 X 35 a 
7 Ch—b)hi  (150—22)5 | 
V=—— =" yes  — 0,88; 

_ ki À 5 
T=7 (1—-5) = 0,83 (1 — LE | 0,77: 
__ Myr 41220000 hu. 
Re Ds — 0,2; 
= LEXU ES (LED) ion — 
: — 0,088 ; 


—14,8-+[1-+5(0,2+0,77)]/10 X 0,01 x 6,1 


V'hplho TE 7 0,83 X 5/35+4-0,0883 1 _ 
ah — | = 35 [1 — 2 (0,83 +0,088] = 


— 85 X 0,93 + 32,5 cm; 


ea.e = Mt/No = 1 220 000/29 000 = 42 cm; 
Ea.clho = 42/35 = 1,2; 
or, conformément à (VI.98), cette valeur ne doit jamais être infé- 


rieure à 1,2/s = 1,2/0,8 = 1,5 (en prenant s — 0,8, car la charge 
est de longue durée). Nous retenons donc 


elle =" 1,9: 
…. RtriiW1f LL 18 X 12 380 … 
— MAY moy — 1220000 —720 000 = 0,45, 


MAS = No (Eope + ry) = 29 000 (20,4 + 4,4) — 
— 120 000 kgf-cm (72 kN:m); 


1 — m° 
Va =1,25—5m— ne = 1,25 — 0,8 X 0,45 — 


14 — 0,45? 
ESC x 0,48 18 — 1,29 — 0,36 — 0,2 — 0,69. 


La raideur caractéristique flexionnelle se définit au moyen de 
{VI.100a) et (VI.100): 


EF, _ 2.109 x 8,04 0.46: 
Tab "(YLE) bhoËpv — (0,83-+ 0,088) 22 x 35 x 0,33: 108 x 0,15 — ; 
B ho4EaFa 35 x 32,5 x 2:10 X 8,04 


7 Va 2e. c)+Vbra.b 0,69 (1—32,5/42)+0,9 X 0,46 
— 32,2.10° kgt/cm2(3,22.10° MPa). 


La flèche maximale du panneau à mi-portée, pour qy; = 
— 32,85 kgf/cm (328,5 N/cm), est égale à 


Autrement dit, la flèche reste inférieure à la limite admissible 
f = 2,5 cm (voir $ VI.6) pour 5 m << ! < 10 m, même sans tenir 
compte de la contre-flèche produite par la précontrainte (le calcul 
de cette contre-flèche devenant donc inutile). 

Calcul de l’ouverture des fissures normales dans les nervures du 
panneau. La contrainte de l’armature longitudinale sera calculée 
d'après la formule (VI.102) en y prenant M = My, Le My; 
€a.pe = 0 (distance entre NV, et l'armature tendue) : 


È M—N5(21— ea. po): 1 220 000 — 29 000 x 32,5 
a. Fa  _  B04X3,5 


— 1070 kgf/em2(107 MPa). 


Calculons l'ouverture des fissures normales d'après la rela- 
tion (V.13) en prenant À = 1, cia = 1,5, n = 1, u = 0,01, d — 
= 16 mm: 


ar (mm) = kcian-pe 20 (8,5 — 1004) ÿ (mm) = 


—1 x 1,5 x 1-90 20 ..… x 0,01)%/16—0,1 mm, 
valeur inférieure à la limite admissible a 14 — 0,3 mm. 
Calcul à la formation des fissures obliques dans le béton. Les 
Normes demandent de calculer l’ouverture des fissures obliques dans 
une section dont la distance à l’appui est non inférieure à L,. À cette 
distance, pour x — 1, l'effort tranchant (voir $ XII.2) est égal 
à Or = 7870 kgf (78 700 N). Vérifions la formation des fissures 
obliques au niveau du centre de gravité de la section. La contrainte 
normale dans le béton (engendrée par l'effort de précontrainte) est 


Ox = No2/Fy & 29 000/1520 = 19 kgf/cm* (1,9 MPa). 
Les contraintes tangentielles sont 


: QuiSp | 7870 X 41 600 
xU 7 Jpb À 596 530 % 22 


Calculons les contraintes principales de traction et de compres- 
sion d’après la formule (VI.78) en y mettant o, = 0 


— 65,7 kgf/em2(6,57 MPa). 


e | = 0,50 2 V 0,2502 + ty — 0,5 x 19 + 0,25 x 192-+ 65,72 — 
pr.tr 
: 75,2 kgf/cm?(7,52 MPa) en compression ; 
—- 56,2 kgf/cm2(— 5,62 MPa) en traction. 


Puisque Opr.tr — 96,2 kgf/cm° (5,62 MPa) > Rirrx = 18 kgf/cm° 
(1,8 MPa), nous faisons la tonclusion qu'il se produit des fissures 
obliques dans le béton. 

Calcul de l'ouverture des fissures obliques dans le béton. L'ouver- 
ture des fissures obliques dans la nervure sera calculée à l’aide des 
formules (VI.103) à (VI.106) en introduisant les mêmes caractéristi- 
ques des armatures transversales que dans le $ XII.2, soit un, = 0; 
Utr = 0,003; k — sal d'inx 8 mm: 


_ @ __ 7870 29 000 : 
t= 0,25 = 025% — 10,2 —4,8— 


— 5,4 tn (0,54 MPa); 
at = Ciak (Ro + 80dmax) Er de — 1,5 x 16,4-103 (350 + 30 x 8) x 


1 K SA 
0,003 ”  (2,1-106)? 


valeur inférieure à la limite admissible af.14 = 0,3 mm. 


X — 0,032 mm, 




Autres calculs. Les calculs de capacité portante et de résistance 
à la fissuration des portions des nervures adjacentes aux appuis, 
les calculs de capacité portante et de résistance à la fissuration du 
panneau pendant la mise en précontrainte, le montage, le transport, 
etc., seront omis. 


$ XII.4 PANNEAU DE TOITURE CARRÉ 


Utilisé dans la toiture du réservoir, ce panneau carré de dimensions 
4 x 4 m en plan est bordé de nervures et repose en ses angles direc- 
tement sur les poteaux (voir fig. XII.1 et XIT.4). 


ll M 


| lo =3830 | 


3980 


FIG. XI1.4. Pour le calcul d’un panneau de toiture carté 


Donnons-nous les dimensions des nervures: 
h=-1=-5 40040 em; b=0,4h —0,4 x 40—16 cm. 


La nervure aura 15 cm d'épaisseur en bas et 20 cm au niveau de 
la tranche inférieure de la dalle. La dalle du panneau aura 10 cm 
d'épaisseur. La masse de { m° de la dalle est 250 kg (2500 KkN). 

Béton de classe M 300, avec R,, — 135 kgf/cm° (13,5 MPa), 
Rtr = 10 kgf/cm*? (1 MPa) (voir Annexe IV); my = 1. Treillis 
soudés de la dalle et armatures longitudinales principales des carcas- 
ses soudées dans les nervures en barres à haute adhérence de classe 
A-TII avec À, = 3400 kgf/cm° (340 MPa) pour d entre 6 et 8 mm 
et Ra = 3600 kgf/cm* (360 MPa) pour d entre 10 et 40 mm; armatu- 
res transversales et de montage en acier de classe A-I avec À, — 
— 2100 kgf/cm*? (210 MPa) et R,;+t, — 1700 kgf/cm° (170 MPa} 
(Annexe VI). 

Calcul à la résistance de la dalle. La charge de calcul exercée 
sur 1 m° de la dalle est déterminée de la même façon que pour le 
panneau nervuré (Tableau XII.1): on obtient qg — 2640 kgf/mé& 
(26 400 N/m°) (états-limites ultimes). 

La portée libre (longueur de flambement) de la dalle sera prise 
égale à la distance entre nus des nervures, l, = 398 — 20 x 2 — 
— 358 cm. 

Les moments fléchissants de calcul en travée M, et sur appui M,, 
seront calculés comme il a été dit dans le $ X.2, en admettant que 




le moment en travée est égal au moment sur appui et que la moitié 
des armatures inférieures sont interrompues à la distance de 1/4 de 
la portée avant l'appui: 


M=M=M ag = 5 = HORS 800 kgf-m (8000 N-m). 


Hauteur utile et largeur de calcul de la dalle: 
ho =h—a—=10 — 2 = 8 cm; b = 100 cm. 


La formule (VI.13) et le Tableau VI.1 donnent 


M 80 000 
A0 ne — 15x00 x 87 — 0098; nm —0,992. 
D'après la formule (VI.14) | 
M 80 000 : 
Fan = H00% 0, 2x8 — 21 Cm*. 
On adopte comme armature: 
. po : 200/200/7/7 _, 200/200/7/7 
en travée, deux treillis soudés des types 3800 X 3800 Qi 3500 X 2200 
avec la = 1,93 x 2 — 3,86 cm°; 


sur appui, un treillis soudé du type avec la —= 
— 3,86 cm:. 


Le plan de ferraillage de la dalle est représenté sur la figu- 
re XII.5, a. 


Calcul des nervures du panneau 
auxétats-limites ultimes 


Charge de calcul sur 1 m de longueur au milieu de la nervure du 
panneau (voir fig. XII.4): 


g = 2620 x 2 = 5240 kgf/m (524 kN/m); 
charge uniformément répartie provenant du poids propre de la ner- 
vure du panneau : 
Epp = UE 0,3 x 2500 x 1,1 — 168 kgf/m (1,68 kN/m). 
Longueur libre de la nervure: 
1, =400 — 15 = 385 cm. 


Moment fléchissant et effoft tranchant provenant des charges 
de calcul: 


12 £pnlà 2 à 852 
M = ti pe L BOXSE | MEXIS _ 6180 + 310 — 


— 6790 kgf-m (67,9 kN-m); 


£ppl 
Q= + De = ORRES 4 MEXLEE _ 5050 + 325 = 


— 5375 kgf (53,75 kN). 




Calcul suivant les sections normales. Conformément aux pres- 
criptions énoncées dans le $ VI.3, on fait entrer dans le calcul la 
largeur du hourdis de la section en T: 

b, = b + 6h — 20 + 6 x 10 — 80 cm, mais 
<< 1,/3 — 385/3 — 128 cm. 
Hauteur utile de la nervure 
ho = h — a = 40 — 4 — 36 cm. 

La section en T sera assimilée à un profil rectangulaire de lar- 

geur b — 80 cm, car l’axe neutre passe de toute évidence dans le 


hourdis, et calculée d’après les formules (VI.13), (VI.14) et à l’aide 
du Tableau VI.1. Il vient 


M 679 000 _. 
A = he — 15x80 x 867 00495 n=0,975; 
F ET cm2. 


On adopte comme armature 128 A-III avec F, = 6,16 cm° 
(Annexe VIIT). 

Calcul de la nervure suivant les sections obliques. Vérifions les 
conditions (VI.44) et (VI.45) en prenant b, = 17,5 cm (largeur 
moyenne de la nervure): 


kiRtrônho < Q LL 0,35R)hrbnho; ou 
0,6 x 10 x 17,5 x 36 << 5375 << 0,35 x 135 x 17,5 x 36; 
3780 kgf (37,8 kN) << 5375 kgf (53,75 kN) << 29 700 kgf (297 kN). 


On voit donc qu'il est nécessaire de calculer la résistance des 
armatures transversales et que la section de la nervure choisie pré- 
cédemment est suffisante. Chaque nervure sera armée d’une carcasse 
soudée (n = 1) (voir fig. XII.9, b) comportant des barres transver- 
sales de — 10 mm (7; — 0,785 cm°) en acier de classe A-I (la 
condition de soudage solide sur la barre longitudinale @28 mm est 
respectée, voir $ II1.3). La formule (VI.53) impose une valeur de 
qtr égale à 


Qu = TS 16 kgf/em (160 N/cm) 
WU 4k bhèRtr 4 X2 X 17,5 X 362 x 10 , 
mais non inférieure à 


tr — Frn = PERS — 87,5 kgf/cm (875 N/cm). 




M TCETITI 
MÉTTE es IUNEROURE El 
LRRE: HE 
TT TTE HE 
MERE: = 
1 FE = 
200) HE Ba — 
200/200/1/ É CE = 
[ F800 F0? SLLTÉ CE = 
CERN 
Lune _ HS 
50 D 
SR. en T-{(4pces) _p184"1 
S S D 10A-I 
s >. HE 
$ 6 1050 (esp 150)|_ 1800 esp 300)_ 1050 (esp 150) }_d 28A-IT 
| TT | 


FIG. XII.5. Panneau de toiture carré: 
a, plan de ferraillage de la dalle; b, plan de ferraillage de la nervure 


Ecartement des barres transversales : 
d’après (VI.54) 
 RactrFtr 1700 X 0,785 : 
gs — 19,5 cm ; 
d’après (VI.55) 
_0,75k:Rtrbhg 0,75 X 2 x 10 x 17,5 X 362 
Umax 9 SE 5375 


d’après les dispositious- constructives 


— 63 cm ; 


u < h/2 = 40/2 = 20 cm; u << 15 cm. 


Nous retenons comme écartement des barres transversales près 
des appuis u — 15 cm (la plus petite des valeurs trouvées) et au 
milieu de la travée u — */ah — 30 cm. 

Le plan de ferraillage de la nervure est montré sur la figure 
XII.5, b. 




Calcul du panneau aux états-limites 
d'utilisation 


Ce calcul est superflu. En effet, la pratique montre qu'une structure 
de ce type vérifie toujours les conditions de calcul aux états-limites 
d'utilisation. 


$ XII.S5. POUTRE DE TOITURE 


La toiture du réservoir montré sur la figure XII.1, a, b repose sur 
des poutres porteuses à six travées. La longueur de chaque travée 
(l’espacement des axes des poteaux) est 6 m. Béton de classe M 300, 
my = 1, avec À,, = 135 kgf/cm°? (13,5 MPa), Ri,= 10 kgf/cm° 
({ MPa) (Annexe IV). Armature longitudinale principale en barres 
à haute adhérence de classe A-TII avec R, — 3600 kgf/cm° (360 MPa) 
pour d > 10 mm; armature transversale en acier de classe A-II 
avec Ra = 2700 kgf/cm? (270 MPa), R,; 4 — 2150 kgf/cm* (215 MPa) 
(Annexe VI). Les charges exercées sur 1 m° de la toiture sont résu- 
mées dans le Tableau XIT.1. 

Le calcul sera fait aux états-limites ultimes uniquement; en 
effet, la pratique montre qu'une structure de ce type vérifie toujours 
les conditions de résistance aux états-limites d'utilisation. 

La contribution de la surcharge étant faible, on admet que la 
poutre est exposée à une charge permanente de longue durée. 

La charge de calcul exercée sur 1 m de la longueur de la poutre 
(la distance entre deux poutres voisines étant prise égale à 6 m) 
se compose des charges suivantes: 

charge due au poids de la toiture, 2640 x 6 — 15 840 kgf/m 
(158,4 kN/m); 

charge due au poids propre de la poutre, 0,4 x 0,7 x 2500 x 
X 1,1 — 770 kgf/m (7,7 kN/m). 

La charge totale est donc qg — 16 610 kgf/m = 16,6 tf/m — 
— 166 kN/m. 

Au calcul de la poutre, on adopte comme longueur libre la distance 
entre les axes des appuis (poteaux), soit ! = 6 m. 

Détermination des valeurs de calcul des moments fléchissants 
et des efforts tranchants. La poutre étant à travées multiples, on 
retient pour le calcul un schéma à cinq travées (fig. XII.6, a). Le 
travail de la structure étant considéré dans le domaine élastique 
(Annexe XVIT), les moments fléchissants sur appuis intermédiaires 
BP, C sont « 


Mn = Qpql? = —0,105 x 16,6 x 6? — —62,7 tf-m (627 KN-m); 
Me = aq? — —0,079 x 16,6 x 6° — —41,8 tf.m (418 kKN-m). 
Dans une structure hyperstatique en béton armé, une certaine 


redistribution des moments internes est admise. Afin de pouvoir 


30 1 




a - mm. C-1(3pces) 2 6 EUR 
ee LE HnPshe 
“EL 162841 AT dt à Ê 1B281I 
S 7” qe à Dr 
AT 2 l-H(2pces) p5B-1 


| D | | d'1 S | 
N : SE: 
S Le __ 
ER ne Ÿ-TA1(2pces) | & [ 
75 300 115 175 300 175. S 
j 650 L__ 65 _: . a 


FIG. XII.6. Poutre de toiture: 


a, schéma adopté dans les calculs; br -diartemme des moments fléchissants et des efforts 
tranchants dans les travées intermédiaires; ce, élément préfabriqué de la poutre utilisé dans 
les travées intermédiaires 


uniformiser les joints de tous les éléments préfabriqués de la poutre, 
on peut admettre que les moments sur appuis sont égaux entre eux; 
la valeur ajustée du moment sera prise égale à 


MŸ= Me = —41,8 tf.m (418 kN-m). 




Calculons les efforts tranchants en tenant compte des moments 
fléchissants ajustés: 


MA 46,6x6 4,8 


Qa= += — TE = 49,8 — 7 — 42,8 t£ (428 kN): 
QE= 45 XSL IDE 49,84 7 — 56,8 tf (568 kN): 
Q= QE == XL 19,8 tt (498 KN). 


Calculons les plus grands moments fléchissants en travée A7,, 
AM, et A1. Le moment fléchissant maximal de la travée de rive M, 
est appliqué à la distance x, de l’appui extrême: 


To = Q4/q = 42,8/16,6 = 2,58 m; 


M, = Qaro— 5 = 42,8 x 2,58— BXL 55,2 tf.m(552 KN-m). 


Les moments dans les travées intermédiaires sont 


My=Ms= M | = 41,8 — 32,8 tf.m(328 KN-m). 


Les diagrammes de calcul des moments fléchissants et des efforts 
tranchants dans les travées intermédiaires sont montrés sur la fi- 
gure XII.6, b. On y distingue les ordonnées qui correspondent aux 
nus des appuis. Admettant que la section d’un poteau est 40 x 40 cm, 
on obtient 


Mayen = IMÈ|—QS x 0,2 = 41,8 — 49,8 x 0,2 — 
— 31,8 tf:m (318 kN :m); 


Gen = QUEUE 49,8 UE = 46,5 tf (465 kN). 


L'effort tranchant maximal dans la travée de rive est 


L— z9) — 0,2 6— 2,58) —0,2 
QEin = QE EU 56,8 CPI OE 2 58,5 tf (535 KN). 


Détermination de la section à donner à la poutre. La poutre sera 
dimensionnée pour résister aux moments et efforts dans les travées 
de rive où ils prennent leurs valeurs maximales. Conformément 
aux prescriptions sur la hauteur relative optimale de la zone com- 
primée (voir $ VI.3), nous posons £ — 0,4; en fonction de cette 
valeur, le Tableau VI.1 donne À, — 0,32. Pour b = 30 cm, on ob- 
tient à l’aide de la formule (VI.17) 


= 7 Abrp — V Gaxax rss — 60 Cm. 




Hauteur totale de la poutre À = h, + a = 65 + 5 — 70 cm. 

Nous retenons définitivement une hauteur égale à 70 cm, car 
elle correspond à une dimension normalisée. La hauteur utile de la 
poutre sera k, — 65 cm. 

Vérifions les dimensions données à la section à l’aide des condi- 


tions (VI.44) et (VI.45) pour Q;: 


kRirdho < QHn < 0,35R»rbho; 
0,6 x 10 x 30 x 65 << 53 500 << 0,35 x 135 x 30 x 65; 
11 700 kgf (117 KN) << 53 500 kgf (535 kN) < 
<< 92 000 kgf (920 KN). 


Les conditions (VI.44) et (VI.45) sont respectées, ce qui signifie 
que la poutre est correctement dimensionnée et qu’il est nécessaire 
de calculer la résistance de l'armature transversale. Les mêmes di- 
mensions seront retenues dans les travées intermédiaires. 

Calcul de résistance suivant les sections normales. On a dans la 
travée de rive, d’après les formules (VI.13), (VI.14) et les données 
du Tableau VI.i: 


My 5520000  —…. 
A0 fe — Sox ex mes 0028; 10,797; 
F, = M 5 520 000 _ 29 6 cm2. 


— Moka 0,797 X 65 x 3600 


On choisit comme armature 3 G 28 + 322 A-III avec F, = 
— 29,9 cm° (voir Annexe VIIT). 
Dans les travées intermédiaires on a 


3 280 000 | 
0 = 30x65 x 135 — 0192; n =0,892 ; 


p, 3280 000 
a 0,892 x 65 x 3600 




—= 19;7 cm2. 


On choisit comme armature 3 @ 28 A-III avec F#, — 18,47 cm°. 

Le moment sur appui M, = 31,8 tf:m (318 kN-m) est voisin 
de M, = 32,8 tf:m (328 kKN:m), on choisit comme armature égale- 
ment 328 A-III. je 

Calcul de résistance suivant les sections obliques. Nous nous bor- 
nerons à considérer une travée intermédiaire de la poutre (voir 
fig. XII.6, c). Nous admettons que la carcasse soudée à barres longi- 
tudinales d — 28 mm est munie d’armatures transversales d4. = 
— 10 mm avec ft, — 0,785 cm? (Annexe VIII); un tel diamètre 
procure les bonnes conditions de soudage (voir $ [1.3). Le nombre de 
barres transversales dans la section (le nombre de carcasses) est 
n = 3. On a donc Ft = ftrn —= 0,785 X 3 — 2,855 cm°. 




D'ayres la formule (VI.53), l'effort de calcul à l'unité de la lone 
gueur de la poutre reporté par les barres transversales est égal à 
= EE 213 kgf/em (2130 N 
Dr ZEbhiRw  AXLXEOX OX I0 — gi/em ( /em) 


sans être inférieur à 


qu = te = 0X 20 150 kgfiem (1500 N/cm). 


L'écartement des barres transversales sera: 
d'après l'égalité (VI.54) 
Ra. trFtr 2150 X 2,355 


D nn cm ; 


d'après la condition (VI.55) 


Umax = 0, RÉ — __ 0,75 X2 ES 30 X 65 41 cm: 


d’après les dispositions constructives (voir $ VI.1) pour h > 


> 45 cm 
u <hl3 = 70/3 = 23 cm. 


Nous adoptons le plus petit écartement uw = 20 cm sur le quart 
de la poutre adjacent à l'appui. Au milieu de la travée nous prendrons 
u = 2 x 20 = 40 cm, valeur inférieure à #/4h — 52 cm. 

L'organisation de la travée intermédiaire de la poutre est repré- 
sentée sur la figure XII.6, c. 

Définissons le point d’interruption de l’armature longitudinale 
principale supérieure posée dans la poutre au-dessus de l’appui. La 
distance a entre le milieu de la portée et la section où l’armature 
en question cesse d’être théoriquement nécessaire (voir fig. XII.6, b) 
se laisse calculer à l’aide de la formule 


2(M:+M 9 (99 : 
A ( a+ 8032) _ 2 (32.8+ 5,5) — 2,14 m, 
q 16,6 
où 3312 est le moment reporté par les barres supérieures de répar- 


tition d = 12 des trois carcasses (les calculs sont omis, voir 
fig. XII.6, c). 

L'effort tranchant dans cette section est Qa=ou —= 39,6 tf 
(356 kN). 

Les formules (VI.63), (VI.61) nous fournissent la longueur à don- 
ner aux barres interrompues au-delà de leur point d'interruption théo- 
rique : 


RaFtr 2700 X 2,355 


tr. DE gp — 916 kgf/cm (3180 N/cm) ;: 
Le=s.1 ) 35 600 
De =3.14 nn = eg t 9 X 2,8=— 56 + 14—70 cm : 


w —= 204 = 20 x 2,8 — 56 cm. 
Nous retenons w = 70 cm (valeur maximale). 


20—0948 305 


Calcul de l’attache de la poutre sur le poteau. Les éléments pré- 
fabriqués de la poutre prennent appui sur les consoles des poteaux 
(fig. XIL.7). Dans l’attache sur poteau, le couple de forces du moment 
d’appui est reporté en haut par les barres de raccordement, et en bas 


Barres de Souder au fl 1 
raccordement bain de fusion FT JÉ28AT 


JO28A TT 


ee Lil. 
« bb & .. 


: | 150 150) # 




Cordon de 




Soudure 




J30 400 J30 : 
FIG. XII.7. Attache de la poutre sur le poteau 


par les joints soudés des plaques d’appui en acier scellées dans la 


poutre et dans le poteau. 
Le bras de levier du couple est z — 70 — 5 — 65 cm. Les forces 


composantes du couple sont 


N = Myn/z = 31,8/0,65 = 49 tf (490 KN). 


La section minimale à donner aux plaques d’appui de la poutre 
et de la console du poteau fabriquées en acier de classe C 38/23 avec 
R = 2100 kgf/cm°? (210 MPa) est égale à 


Fpea = N/R = 49 000/2100 = 23,4 cm°. 


L'effort de cisaillement, déveleppé entre les plaques d'appui de 
la poutre et de la console du poteau est 


Nes = N — Qf = 49 — 46,5 x 0,15 = 42 tf (420 KN), 


où © est l'effort sur appui; f, le coefficient de frottement acier sur 


acier. 
Le joint soudé réunissant les plaques d'appui doit être calculé 


pour résister à la valeur indiquée de js. 




$ XII6. POTEAU ET SEMELLE 


Le poteau supporte la toiture du réservoir de la figure XII.1. La 
semelle est posée sous le poteau. Le poteau a une section (normalisée) 
de 40 x 40 cm pour une hauteur libre (longueur de flambement) 
l) = 5 — 0,6 — 0,2 = 4,2 m. Béton de classe M 200, m1 = 1, 
Rx — 90 kgf/em° (9 MPa), Rty = 7,5 kgf/cm°(0,75 MPa) (Annexe IV). 
Armature en barres d'acier à haute adhérence de classe A-II avec 
Rae = 2700 kgf/cm? (270 MPa) (Annexe VI). Le sol de fondation 
est un gros sable compact. D’après l'Annexe X VIII la pression conven- 
tionnelle de calcul sur le sol est R, — 6 kgf/cm* (0,6 MPa). 

Calcul du poteau. Nous admettons que le poteau résiste à une 
charge permanente de longue durée, car la contribution de la sur- 
charge de courte durée est faible. La charge totale se compose de la 
réaction de la poutre (valeur maximale sur le premier appui inter- 


médiaire à partir de la rive Q6 et Q%, voir $ XII.5): 
06,8 + 49,8 — 106,6 tf (1066 kN) 
et du poids propre du poteau 
0,4 x 0,4 x 5,1 x 2,5 x 1,1 — 2,2 tf (22 kN), 
de sorte que 
N a Æ 109 tf (1090 kN). 


Le poteau est sollicité par une force axiale longitudinale. Il fait 
partie d’une structure hyperstatique, aussi l’excentricité de calcul 
de la force longitudinale est-elle égale à l’excentricité accidentelle 
(voir $ IV.1). Le rapport /,/h — 420/40 = 10,5. Dans ces conditions 
le calcul peut être fait suivant les prescriptions du $ IV.2. 

Voyons s’il est nécessaire de mettre une armature de résistance 
contrôlée. Conformément aux formules ([V.2) et (IV.3), il doit y 
avoir l'inégalité 


N <qRyF 


pour F, = 0 et m = 1 (le côté de la section étant supérieur à 20 cm). 
Le coefficient ® = 1 = 0,882 est trouvé dans le Tableau IV.1. 
Portant les valeurs numériques dans cette condition, on obtient 


109 000 kgf (1090 kN) < 0,882 x 90 x 40 x 40 = 
— 127 000 kgf (1270 kN). 


# e. A Ld e. . « 
L'armature de résistance contrôlée est donc inutile. 


Les dispositions constructives imposent cependant un pourcen- 
tage d’armature minimal u = 0,4 %, l’armature en question pré- 
sentant une section non inférieure à F, — 0,004 x 40 x 40 — 
— 6,4 cm°. Nous retenons comme armature 4G 16 mm A-II avec 
F; = 8,04 cm° (Annexe VIII). Les barres transversales de la carcas- 
se soudée auront un diamètre d4, — 6/mm, conformément aux con- 


20+* 307 


(esp J00) 






400 | 




FIG. XII.8 Poteau: 


a, cotes du coffrage ; b, plan de ferraillage ; c, carcasse soudée 




ditions de soudure efficace (voir $ II.3). L'écartement des barres 
(voir $ IV.1) doit être égal à u < 204 = 20 x 1,6 — 32 cm; nous 
prendrons u — 30 cm. 

Le poteau ainsi dimensionné et ferraillé est représenté sur la 
figure XITI.8. 

Calcul des consoles. La plus grande réaction provenant de Ia 
poutre est transmise sur le poteau intermédiaire du côté de la travée 


de rive (voir $ XII.5), Q$ = 56:8 tf (568 kN). Lorsque les dalles 
de la toiture sont disposées comme il est montré sur la figure XII.1, b, 
une partie de la charge (1/8) est directement appliquée sur le poteau. 
La console reporte la pression due au poids de la poutre: 


Qcons = 56,8 x 718 = 49,7 tf (497 kN). 


La plaque d'appui de la poutre est définie par les dimensions 
bpoutre — 30 Cm et bhiaque — 22 Cm (fig. XII.7 et XII.9). La pres- 




sion sous la plaque est 
= — = 9 — 75 kgf;cm? (7,9 MPa) << Ror — 
— 90 kgf/cm?2(9 MPa). 


La plaque d’appui de la poutre est soudée sur son armature lon- 
gitudinale. Celle de la console est soudée sur son armature horizontale 
supérieure. 

Si les consoles sont courtes (Lons  0,9%ocons), elles sont calcu- 
lées à l’aide de deux conditions définies dans les Normes: 


4,25 X 1,2 X Rtrbhôcons 


Cine a — 9 Qcons <2,9Rtr0h0cons- 
La hauteur utile de la console est donc 
= Qconsa _ 49700X17 
Rocons = 1,5Rtrd TEXT.5 x 40 — 49 ce 
Qcons _— 49 700 


hocons = 5 5RIE — 3,5% 7,5 x 40 — OÙ cm. 

La console doit avoir comme hauteur h,on — 69 cm (pour 
Ro cons — 60 cm). 

L'armature horizontale de la console #, subit une compression 
engendrée par l'effort Njoutre défini par l’action du moment du 
côté de la poutre: 


M 8. n 1,8 
N'poutre= = US — 48 tf(--480 LN) 


(voir $ XII.5 et fig. XII.9). Elle subit en même temps une traction 
engendrée par l'effort Voons défini par l’action du moment dans la 
console. En posant n Æ 0,9, ce 
dernier moment est égal à 

Qa __46,5X 0,17 
Nhocons 0,9X0,6 


— 14,7 tf(147 KN). 


N cons = 


Puisque Moutre > ÂVconss l'ar- 
mature horizontale de la console 
recevra une section F, définie par 
les dispositions constructives mais 
RE me 20 Virus FIG. XII.9. Ferraillage de la tête 

. ? du poteau 
choisit comme armatures 2 20 
A-II avec F, — 6,28 cm°. 

Si la console est telle que k > 2,5a, les Normes prescrivent de 
mettre, indépendamment des résultats des calculs, des barres rele- 




vées et des cadres horizontaux suivant toute la hauteur de la struc- 
ture. Ces barres devront avoir une section non inférieure à F, — 
— 0,002 Dh, cons — 0,002 X 40 x 60 = 4,8 cm°. On choisit comme 
armatures relevées 4@ 16 A-II de section F, — 8,04 cm°. Les cadres 
de diamètre dt, — 6 mm en acier A-IT seront placés suivant la hau- 
teur de la console avec un écartement de 100 mm. 

Le ferraillage de la tête du poteau est montré sur la figure XII.9. 

Cotes d'implantation de la semelle. Les dimensions à donner à 
la semelle seront définies à partir de la pression de calcul sur le sol 
R, déterminée par la charge caractéristique affectée d’un coefficient 
de surcharge nr — 1 

Supposant à priori que le côté de la semelle est b Æ 1,5 met la 
profondeur de la fondation À — 0, nous cherchons la pression de 
calcul sur le sol à l’aide de la formule citée dans le Chapitre X en 
posant À — 0,125 (sable) et b, = 1 m: 


R=R [148 (4) | (SE) =6[1+0,125 (| 5 = 
— 3,2 kgf/em2(0,32 MPa). 


Les charges exercées sur le sol de fondation sont : 

charge caractéristique V,, = 92 tf (920 KN) (compte tenu de la 
masse de la semelle); 

charge de calcul N = 109 tf (1090 KN) (sans tenir compte de la 
masse de la semelle). 

La surface et la longueur du côté de la semelle (de forme carrée) 
seront respectivement 


Fr = NyxlRs = 92/32 = 2,87 m°; 
a=V Fr=V 2,87—1,7 m. 


La semelle aura comme dimensions 170 x 170 cm avec Fr = 
— 2,89 m°. 

Calcul de la semelle. La semelle est calculée à la résistance mé- 
canique. Sous la charge de calcul, la poussée du sol de bas en haut 
la semelle (sans tenir compte de la masse de celle-ci) est égale à 

— N/F; = 109 000/170 x 170 = 3,8 kgf/cm° (0,38 MPa). 

" La hauteur utile de la semelle, définie par la condition de ré- 
sistance au poinçonnement,-ést Tficulée d’après la formule (X.14) 
en mettant R+. = 7,9 kgf/cm°. Il vient 


ko = — 0,580 + 0,5 VE ü 


_ —0,5x40+0, 5/0 = 29 cm : 


hr = ho + a = 29 + 5 — 34 cm. 




Les dispositions constructives (profondeur d'encastrement du 
poteau dans son logement augmentée de l'épaisseur minimale de la 
plaque dans le logement) imposent la hauteur de la semelle 


he = h, + 20 cm = 40 + 20 = 60 cm. 


La hauteur totale de la semelle sera k; — 60 cm (pour k, = 53 cm); 
les autres dimensions sont indiquées sur la figure XITI.10. 




230 250 400 250 250 


Boucles 
de montage : 


FIG. XII.10. Semelle du poteau: 


a, vue en élévation et en coupe; b, vueen 
ælan et schéma de ferraillage au niveau 


119 12A-I 
inférieur de 150 en 150 mm 


1700 


Les moments fléchissants dans les sections Z — Z (nu du poteau) 
et ZI — IT (encastrement du rebord inférieur de la semelle) se cal- 
culent à l’aide de la formule (X.16): 


Mi = 0,125p, (a — b,)*a = 0,125 x 3,8 (170 — 
— 40)? x 170 = 1 360 000 kgf-cm (136 KN-m); 
Mir = 0,125p, (a — b;)* a = 0,125 x 3,8 (170 — 120}? x 
X 170 = 202 000 kgf-cm (20,2 kN : m). 


La quantité d’armatures nécessaire à la semelle est cherchée à 
l'aide de la formule (X.17): 


_____ Mr __ 136000 2 . 
Fa = 0,9Raho 0,9 X 2700 X 53 — 10,6 cm?; 




… Mir 202 000 . 2 
Far GR — 0,5% 2700 % 18 — 04 CM? 


Nous adoptons comme armatures 11 512 A-II avec F, — 12,4 cm? 
{Annexe VIII). 




Les pourcentages des armatures dans les sections Z — Z'et II — II 
seront respectivement 


F 12,4 
pa = get 100 = pres 100 = 0,19% > min = 0,1% ; 


12,4 
Mo r 100 1s 75 100 =0,56% © limin — 0,1%. 


$ XII.7. MUR DU RÉSERVOIR RECTANGULAIRE 


Ce mur est destiné au réservoir en éléments préfabriqués représenté 
sur la figure XII.1, a, b. L'épaisseur du mur est 20 cm. Les panneaux 
du mur ont la largeur nominale 3 m (suivant les axes des joints) 
et la largeur constructive 2,8 m. Les joints verticaux des panneaux 
auront une largeur de 20 cm. Ils seront garnis de béton M 300 et 
d’une bande de béton projeté de l’intérieur large d'environ 50 cm. 
Les panneaux seront encastrés en bas dans les rainures du fond et 
réunis en haut par les éléments préfabriqués de la toiture par soudage 
des pièces scellées. 

Les panneaux seront constitués de béton M 200 (m,, = 1) avec 
Ryr = 90 kgf/cm°? (9 MPa) (Annexe IV) et munis de treillis soudés à 
armature principale verticale en acier de classe A-IIT avec R, — 
— 8600 kgf/cm°? (360 MPa) pour d > 10 mm (Annexe VI). 

Charges exercées sur le mur. Le réservoir étant vide, le mur subit 
la poussée du sol de l'extérieur. Pendant l'épreuve de pression hy- 


É 9 À P-Lté/m 


h-4,3m 


Q 2m 


Map" 38tf.m Map "65tfm 
Pau “4741 M F2" 42m = 


Ps =431f/m 


FIG. XII.11. Pour le calcul du mur du réservoir rectangulaire: 


a, vuc en coupe du mur; b, schéma “es efforts et diagramme des moments déterminés par 
la pression d’eau; c, idem, par la poussée du sol 


draulique, le mur subit la pression d’eau de l’intérieur en l'absence 
de toute poussée du sol. 

Le panneau du mur doit être calculé séparément à la flexion sous 
la poussée du sol et à la flexion sous la pression de l’eau, en l’assi- 
milant à une poutre à simple travée encastrée dans le fond et articu- 
lée avec la toiture (fig. XII.11, a). La charge verticale sur le mur 




provenant de la toiture n'étant pas toujours présente, on l'’omet dans 
les calculs. 

Calculons 1 m de longueur du mur. La charge de calcul prove- 
nant de la pression d’eau au niveau de l’encastrement inférieur 
(fig. XII.11, b) est 


Peau = nyh = 1,1X1X4,3—4,7tf/m (47 kN/m). 
La charge de calcul provenant de la poussée du sol est déterminée: 
séparément au niveau de la tranche supérieure du panneau (p,1) 


et au niveau de l’encastrement inférieur (p.,). Ces deux valeurs: 
(fig. XII.11, c) sont respectivement 


Pat = nYshy tg? (45° -— p/2) = 
—1,2x18x1,4te (45) — 1,1 tf/m(11 KN/m): 
Ps2 = Ps2 + Psi = nYsh tg? sr P/2) + Pa = 
—1,2x1,8(4,8— 0,5) tg2 (45°—* D) +112 8,2+1,1 = 
— 4,3 tf/m(43 kN/m). 


Moments fléchissants dans le mur. Section à donner aux arma- 
tures. La pression de l’eau contenue dans le réservoir (voir $ XI.5, 
fig. XI.41) fait naître (fig. XI1.11, b): 

un moment fléchissant au niveau de l’encastrement inférieur 


Map eau = — 2 = DRE D 5,8 tf.m/m(—58 KN-m/m) ; 


un moment fléchissant (maximal) en travée à la distance x, = 
= 0,45h — 0,45 X 4,3 — 1,92 m du bord supérieur du panneau 


2 4 4,32 
Mir. eau = Par = TT — 2,6 tf-m/m (26 kN :m/m). 


La poussée du sol exercée de l'extérieur du réservoir fait naître 


(fig. XII.11, c): 
un moment fléchissant au niveau de l’encastrement inférieur 


Psoh®  psyh? 3,2X4,32 1,1 X 4,32 


— —6,5 tf-m/m(—65 kN-m/m); 


un moment fléchissant (maximal) en travée o 
Ps2 3  Psi 2 
Mir. s— (5 10 Ps + 8 à Pa) ht — & To — D To — 
— (1 s_1,1 2 _ 
= (5 32+51,1)4,8 x 1,8— ne rs 1,8 —"5 x 1,8 — 


= 3,15 tf-m/m(31,5 kKN-:m/m), 


où la distance x, — 1,8 m entre le bord du panneau et le point d’ap- 
plication de la charge a été calculée à l’aide de la formule 


4 , 3 Ps 
710 Ps2h + & Pal — un ti — PsTo = 0. 


Voyant que les moments fléchissants dans le mur provenant de 
la pression d’eau et de la poussée du sol sont peu différents entre 
eux, nous placerons une même quantité d’armatures verticales près 
de la surface intérieure et près de la surface extérieure du mur. Ce 
sont les valeurs maximales des moments que nous prendrons en 
compte. Le calcul à la résistance du mur se fait suivant une section 
normale, en l’assimilant à un hourdis de dimensions b — 100 cm, 
ho =hkh—a—20 —3—17 cm. 

Pour la section au niveau de l’encastrement inférieur, les formu- 
les (VI.13), (VI.14) et le Tableau VI.1 nous donnent 


M 650 000 
A = ER = 0x 1m7x 00 0,20; 10,852; 
M 650 000 à 
Fa = nhoha O0, 852 x 17 x 3600 — 1219 CIM. 


1 400 Treillis T-1 
FT à 12 1 (2 pces) à 
HE T ” = CI = 
NS BEBE 
EE SL _ . d | 


EEE | 
IHBRRRRI | 
lIRRRRUI | S | 
ITTTTT US à | 
IT S à en 
HOT RIES ES 
HLLITI | È Se 
H TTL ST 
TOUTE 
LITE 


{000 


201 2600(esp 200) 12011270 
| j 2760 
J/00 sv.æ gear Ireillis T-1(2pces) 
OGA-I 

CRIEES RUE SIBRBREBESSUEE 

15, HOT 

HEBRBEBEE 



Cm pe nl 400 


FIG. XII.12. Panneau du mur du réservoir rectangulaire 


à ; 1 
nn 2760 4 | 




Pour la section en travée 


315 000 —— : 

4 = Toxic oo — 0,121 , 1 mers 0,935 8 
F.— 315 000 

8 0,935 X 17 X 3600 


Le mur recevra comme ferraillage deux treillis doubles parallè- 
les à chaque côté de la section: 

un treillis 5 @ 12 A-IITI avec F, = 5,65 cm° suivant toute la 
hauteur du mur; 

un treillis 52 14 A-III avec F, = 7,69 cm° dans la partie de 
base du mur. 

L'emplacement des barres horizontales sera défini par les dispo- 
sitions constructives. 

Le calcul du mur à la fissuration est omis. 

Le panneau du mur est représenté sur la figure XII.12. 


— 5,5 cm2. 


$ XIL8. PAROI DU RÉSERVOIR CYLINDRIQUE PRÉFABRIQUE 


Cette paroi constitue l'enceinte d’un réservoir cylindrique semi- 
enterré couvert entouré d’un remblai de terre. Diamètre du réservoir 
18 m (rayon r = 9 m), hauteur H = 4,8 m. La paroi est formée 
d'éléments préfabriqués en béton précontraint d'épaisseur Ô — 14 cm. 
Elle est articulée dans le fond. La pression verticale sur un mètre 
de longueur de la base de la paroi à prendre en compte dans les cal- 
culs est V,= 3 tf/m (30 KN/m) sans remblai et V,= 10 tf/m (100 kN/m) 
avec remblai. 

Les panneaux de mur préfabriqués sont confectionnés avec du 
béton M 200 (m1 = 1). Les joints sont scellés avec du béton M 300. 


FIG. XII.13. Pour le calcul de la paroi du réservoir cylindrique: 


a, division en ceintures : b, diagramme des efforts de traction annulaires dans la paroi (en tf); 
c, diagramme des moments fléchissants verticaux 


La paroi est ferraillée avec des frettes (cerces) constituées de barres 
en acier précontraint à haute adhérence de classe A-IV avec Ray = 
— 6000 kgf/cm? (600 MPa), R, — 5000 kgf/cm? (500 MPa), £; = 
— 2.106 kgf/cm° (2.105 MPa) (Annexe VI). Chaque cerce est compo- 




S X 5 
S'IEYS È 
'È S È 
| LS S Ÿ 
RS _ tu, S] 
' “ rs 
' à x ST TN 
S à , LG 
D EST 
S. Ÿ LG 
& SÈ PS 
Le LE 
à SÈS © 
elSISE DÉS à 
SISISS$ ÊLTS 




Equerre d'appui 
D = 18000 en L 40*°40 


FIG. XII.14. Organisatioh de la paroi du réservoir cylindrique: 


a, vue en coupe verticale; b, vue en plan de la pars avec indication des joints des pan, 
neaux, des jonctions des barres précontraintes et des équerres d’appui des frettes; ce, détail 
de fixation de la frette 


sée de trois éléments (fig. XII,14, b). La précontrainte est réalisée 
en post-tension par les moyens électrothermiques. 

La précontrainte est transmise sur la paroi dès que le béton des 
panneaux a atteint la résistance R, — R — 200 kgf/cm° (20 MPa) 
et le béton vibré dans les joints=a résistance À, — 0,7 R = 0,7 x 
X 300 = 210 kgf/cm°? (21 MPa). 


Efjforts annulaires et moments fléchissants 
verticaux dans la paroi 


Les efforts de calcul (tractions) annulaires dans la paroi sont déter- 
minés à l’aide de la formule (XI.9): 


T = To — (2r/s) Qi 


où 7, et Q7r. sont à calculer d’après (XI.3) (et (XI.8) et le coeffi- 
cient n, est à chercher au Tableau XI.2. 

Divisons la paroi en ceintures de 1 m de haut, à l’exception de 
la ceinture supérieure qui aura une hauteur de 0,8 m, et admettons 
que l'effort de calcul dans chaque ceinture soit égal à l'effort qui 
se manifeste à mi-hauteur de la ceinture. Le schéma de division en 
ceintures est illustré sur la figure XII.13, a. 

Calculons la raideur caractéristique de la paroi s d’après la for- 
mule (XI.5): 


s=0,76V rô—=0,76V 9 x0,14—0,86 m. 


Cherchons la force de frottement à la base de la paroi Q7, sans 
et avec remblai, en admettant que le coefficient de frottement de la 
paroi sur le fond est f = 0,5: 


Qtrei = Ni = 0,5 X 3 = 1,50 tf/m (15 kN/m); 
Qtrez = /N2 = 0,9 X 10 = 5 tf/m (50 kN/m). 
Vérifions la condition 


Qre PRES = SEXES 2,28 tf/m(22,8 KN/m), 
Pmax =nVH —=1,1 xX1 X 4,8 — 5,28 tf/m (52,8 kKN/m). 


Puisque Qr.., = 9 tf/m (50 kN/m) >> 2,28 tf/m, nous prendrons 
dans nos calculs, conformément à (XI.10), la valeur de Q:,, = 
— 2,28 tf/m (22,8 kN/m). Les résultats du calcul des efforts dans 
les ceintures sont résumés dans le Tableau XITI.2. 

TABLEAU XII.2 
Efforts de traction annulaires dans la paroi du réservoir 


» | | ren #70 0r//tnne 
30 £ SE E oo 
23 12:21 2 [+ 
SE | 56 | ES | © [o=xe) m Ti T2 
Se | SA | sel & e à 
Se | [ei _— 
ZZ | <5 | ae | tf/m, ou KN/mx10 
1 | 0,4 | 4,4 | 3,96 | 5,1 | 0,0022 0,069! 0,1 | 3,89 | 3,4 
I | 1,3 | 3,5 [12,87 | 4,06 |—0,0114|—0,036 | —0,54 | 12,91 | 43,41 
nt | 2,8 | 2,5 [22,77 | 2,9 |—0,0535/—41,58 |-2,54 | 24,35 | 25,31 
IV | 3,3 | 1,5 [32,67 | 4,75 |—0,0292|—0,91 | 1,39 | 33,56 | 34,06 
v | 4,3 | 0,5 [42,67 | 0,58 | 0,488 | 15,28 | 22,28 | 26,58 | 20,29 
4,8 | O |47,52 | 0 1 31,32 | 47,52 | 16,2 | 0 




Le diagramme des efforts de traction annulaires dans la paroi 
est montré sur la figure XII.13, b. 

Le moment fléchissant vertical (méridien) dans la paroi se laisse 
calculer par la formule (XI.11): 


M = QrrSiss 


où n, est un coefficient tiré du Tableau XI.2. 

Le moment méridien maximal dans la paroi (fig. XI1.13, c) se 
manifeste pour Qfr — Qrre — 2,28 tf/m (22,8 kN/m) et agit dans 
la section d’ordonnée x, correspondant à la valeur maximale du coef- 
ficient 192, notamment à max = 0,322 (selon le Tableau XI.1) pour 
p = 0,8; on a donc x, = ps — 0,8 x 0,86 — 0,69 m, d'où 


Mmax = Qfr  suymaz — 2,28 x 0,86 x 0,322 — 
= 0,63 tf:m/m (6,3 kN :m/m). 


Calcul aux états-limites ultimes 


La section à donner aux frettes est déterminée conformément à la 
condition (V.26) en appliquant la formule 




Ra. pc” 


dans laquelle R;ipe = Raay = 9000 X 1,2 — 6000 kgf/cm° 
(600 MPa) (pour la valeur de m,4 = 1,2, voir $ V.3). 

Puisque la structure en question doit présenter une excellente 
résistance à la fissuration, il convient de majorer la section à donner 
aux frettes d'environ 40 % (voir Tableau XIT.3). 


Fpe= 


TABLEAU XIl.3 
Section à donner aux frettes de la paroi du réservoir 


di Constitution des frettes et 


n° de la ceinture Fe = X : i 2 
T, tf pc leur section F,, cm*, pour 

UE L x1,4 cm?/m chaque ceinture 
I 3,86 0,9 1220 3,14 
Il 13,41 3,1 2920 6,28 
III 25,91 9,9 29 20 6,28 
IV 34,06 se . 39 20 9,41 
V 20,29 4,7 2 20 6,28 

Nota. Ra.pe = 6000 kgf/cm2 (600 MPa). 


La disposition des frettes dans les ceintures de la paroi est montrée 
sur la figure XII.14, a. 

En ce qui concerne l’armature verticale, le diagramme des mo- 
ments fléchissants (fig. XII.13, c) permet de voir qu'un très petit 




| Treillis’ Treillis 
Boucles de levage intérieur T1 extérieur T-2 
6 4A-IT F7 6641 |  6WAX 


ŒCANTIIT 




4790 


DBANI, L=350 
n__L LL 
CEA BON EX 
DRE EN EE 
—— L- =] 

_ es 

1 1 En 

=) ÉEn 

ER FE 
300 » 15 




BRRBIIRRRE 
25 9*150 Q 
1400 4 






FIG. XII.15. Panneau du mur pour réservoir cylindrique 


nombre de barres verticales suffit. De ce fait, les barres verticales 
seront mises en place conformément aux dispositions constructives 
(sans contrôle de résistance), à moins d’être calculées pour résister 
aux efforts qui risquent de se produire sur le chantier au cours de 
l'assemblage. Le panneau de mur préfabriqué est représenté sur la 
figure XII.15. 


Calcul aux états-limites d'utilisation 


La résistance à la fissuration de la structure envisagée doit réponde 
aux exigences de la {re catégorie (voir $ III.1 et $ XI.3). Dans le 
cas considéré on doit empêcher la fissuration sous les efforts engendrés 
par les charges de calcul, c'est-à-dire en faisant intervenir le même 
coefficient de surcharge nr >> 1 que pendant le calcul à la résistance 
mécanique (voir $ III.1). Nous ferons le calcul de la ceinture IV 
(la plus sollicitée) en faisant agir l'effort 7 (voir Tableau XII.2). 




Effort de précontrainte. La précontrainte maximale (traction) 
des armatures sera calculée en faisant intervenir la condition (I[II.8), 
compte tenu des écarts admissibles évalués par la formule (III.10), 
en supposant que la longueur de la barre mise en précontrainte est 
égale à la distance entre deux joints des barres ! = 2nr/3 = 2 X 

X 3,14 X 9/3 = 18,8 . 


p = = 00 TE A 490 kgf/cm2(49 MPa); 
Oo = Rarr — p = 6000 — 490 = 5510 kgf/cm° (551 MPa). 


Pertes instantanées : 
par déformation des appareils d'ancrage, conformément à la 
formule ([II.18), 


g{eno) À + E, = 2 000 000 == 212 kgf/em2(21,2 MPa); 


par frottement de l'acier sur le béton: néant (car les armatures 
sont mises en tension par les moyens électrothermiques). On a donc 


Op1 = Ofant) — 212 kgf/cm° (21,2 MPa), 


Pertes différées: 
par relaxation des tensions dans les barres (mise en tension par 
les moyens électrothermiques) 


O1 = 0,03 o, = 0,03 x 5510 = 165 kgf/cm* (16,5 MPa); 
par retrait du béton M 200 (voir Tableau III.2) 
otanc)— 300 kgf/cm? (30 MPa); 
par fluage différé du béton, d’après la formule (III.22), 
otanc) = 2000] o5.pc/Ro — 2000 X 33,7/200 = 


— 337 kgf/cm* (33,7 MPa), 


= 337 es (3,37 MPa), 
valeur inférieure à 0,6R, — 0,6 x 200 = 120 kgf/cm° (12 MPa); 


En 24100 
ne Emma, 
ÉOR ppm 


Les pertes différées (secondes) s'’évaluent donc à 
Opo = 01 + ofane) + ofanc) = 165 + 300 + 337 — 
— 802 kgf/cm*° (80,2 MPa). 
Pertes totales: 
Op = Op1 + Ope = 212 + 802 = 1014 kgf/cm°? (101,4 MPa). 


Cette valeur est supérieure à la valeur minimale 1000 kgf/cm° 
(100 MPa) qui est obligatoirement introduite dans le calcul. 

Compte tenu des pertes de précontrainte totales et du coefficient 
pe précision de la mise en tension mt, l'effort de DIÉCORREQIE est 
égal à 


N5 = Mmt (00 — Op) Fpe = 0,9 (5510 — 1014) 9,41 = 
— 38 100 kgf (381 kN). 
En calculant la valeur de mnt, on a d’abord calculé Am,+ par la 


formule (111.25) pour la mise en tension par les moyens électrother- 
miques : 


Amnmt = 0,5 _ (1—— = 


) = 0,525 (1— 3) — 0,07 ; 




or, puisque la plus petite valeur de Am»+ à prendre en compte est 
0,1, on a pris conformément à la formule (111.24) 


Mmt = À — Ammr = 1 — 0,1 = 0,9. 


Vérification à la fissuration de la paroi. Vérifions la condition 
T< N, (formule (XI.23)). On a dans la ceinture IV qui est la plus sol- 
licitée (voir Tableau XI1.3) T — 34060 kgf (340,6 kN), valeur inférieure 
à N,= 38 100 kgf (381 kN). Il ne se produit donc aucune fissure dans 
la paroi; la condition de résistance à la fissuration est respectée. 

Dans les autres ceintures la condition T << V, est aussi vérifiée 
(les calculs sont omis). 


21—0948 


CHAPITRE XIII 


OUVRAGES DES SYSTÈMES DE TRANSPORT 
DE LA CHALEUR  - 


& XIIL.1. GÉNÉRALITÉS 


L'approvisionnement en chaleur des agglomérations et des Seb ises 
industrielles est assuré en installant un réseau de conduites de cha- 
leur principales et de distribution: ce sont des tubes d'acier calori- 
fugés véhiculant l'eau surchauffée ou la vapeur. Afin d'éviter les 
contraintes dues aux déformations thermiques (cycle chauffage- re- 
froidissement), toute conduite de chaleur doit pouvoir se déplacer 
sans difficulté. 

Les conduites de chaleur sont généralement posées dans le sol. 
Pour préserver la couche isolante et permettre un déplacement libre 
des conduites lors des variations de la température, on les place 
dans des galeries appropriées ou dans des collecteurs. Posées direc- 
tement dans le sol, les conduites sont munies de gaines protectrices. 
: Un -collecteur commun où la conduite de chaleur est posée à 
côté d’autres canalisations souterraines (électricité, téléphone, eau,. 
égoût) diminue beaucoup le coût de la construction et de l’exploita- 
tion des réseaux souterrains dans les villes et les localités. Les con- 
duites de chaleur peuvent aussi être placées au-dessus du sol, sur des 
pylônes, rampes, mâts, supports; cette solution est mise en œuvre 
dans les entreprises industrielles, lorsque la nappe phréatique se 
trouve à faible profondeur, en pergélisol. 

Le long du tracé du réseau sont prévus des chambres pour vannes, 
appareils de mesure, etc., des appuis fixes et mobiles des conduites, 
ainsi que des niches pour lyres: ce sont des compensateurs flexibles 
en forme de U qui rendent possibles les dilatations des tuyaux entre 
deux appuis fixes. 

Toute conduite de chaleur doit présenter une pente longitudinale 
de 0,002 au moins, afin de permettre la vidange de l’eau dans les 
points bas et l'échappemeñt de l'air dans les points hauts. La pente 
assure également l'évacuation des eaux d'infiltration du collecteur 
dans des fosses spéciales aménagées tous les 100 à 150 m, d’où l’eau 
est évacuée vers des égoûts de pluie ou vers des bassins. Si la conduite 
souterraine rencontre les eaux souterraines, on prévoit généralement 
un drainage parallèle constitué par des tubes et destiné à abaisser 
la nappe phréatique. On adopte dans ce cas une pente longitudinale 
de 0,003 et l’on donne au fond de la galerie une pente transversale 
de 0,01 vers le tube de drainage. 




Les surfaces extérieures des-parois et des planchers des galeries 
dans le sol sec et les surfaces des galeries munies d’un système de 
drainage doivent être garnies de deux couches de bitume 
à chaud afin de garantir l’étanchéité. 

Si, dans un endroit quelconque, la conduite passe dans un sous- 
sol gonflé d’eau sans qu’il soit possible de mettre en place un dräi- 
pagé, la galerie est dotée d’une couche étanche collée. 

‘Aux abords d’un bâtiment, on donne une certaine rampe à la 
conduite afin d'éviter la pénétration de l’eau dans la cave et l’humi- 
dification du sol de fondation. 

Si la hauteur de la galerie n'est pas supérieure à 1200 mm, on 
dit qu'elle est surbaissée. Haute de 1400 à 2100 mm, la galerie est 
dite semi-passante. L'accès dans une galerie surbaissée pour visite 
et réparation de la conduite n’est possible que par le haut, en enle- 
vant le sol et les hourdis du plancher. S'il s’agit d’une galerie semi- 
passante, on peut y accéder à partir des chambres dont les planchers 
sont percés de trous qui communiquent avec la surface. Si la hauteur 
du souterrain est comprise entre 2100 et 3000 mm, il s’agit d’une 
galerie passante ou tunnel. Si le souterrain en question est commun 
pour des canalisations de nature différente, il est appelé collecteur. 
Sa hauteur permet le déplacement du personnel chargé de monter, 
visiter et réparer les canalisations. 

Les galeries et les collecteurs doivent être enterrés à une profon- 
deur d’au moins 0,7 m dans le sol ; sous une chaussée, ils peuvent se 
trouver à 0,5 m sous le sol. En pratique, on installe souvent des 
conduites de chaleur semi-enterrées qui débordent de 200 à 400 mm 
au-dessus du sol. Une telle galerie est calorifugée par un remblai de 
laitier autour des murs et une couche d’isolant sur le plancher. 

En choisissant le tracé de là conduite, on cherche à réduire autant 
que possible sa longueur, ainsi que le nombre de cours d’eau, de 
voies ferroviaires et de chaussées rencontrés, vu que les traversées 
augmentent sensiblement le coût de la construction. 

Les galeries et les collecteurs sont dotés de joints de dilatation 
grâce auxquels les affaissements des différents tronçons de la conduite 
sont indépendants et la déformation thermique des structures est 
réduite. Les joints sont aménagés aux endroits où la galerie rencontre 
une chambre ou une niche, ainsi que dans les points où le sol devient 
nettement différent, mais ils ne seront jamais espacés de plus de 50 m 
en cas de pose souterraine et de plus de 30 m en cas de pose semi-en- 
terrée. 

Les structures des ouvrages souterrains et semi-enterrés sont faæ 
briquées en briques, béton et béton armé; dans les réseaux de surface, 
les briques et le béton sont employés pour les pylônes et le béton 
armé et le métal, pour les mâts et les rampes. 


21% 323 


$ XIII.2. CONCEPTION DES GALERIES ET DES COLLECTEURS 


Galeries surbaissées 


Le schéma le plus simple d’une galerie surbaissée est donné sur la 
figure XIII.1. Une couche de béton de classe M 75, épaisse de 100 mm, 
est posée sur la surface unie du sol. Après le montage et le calorifu- 
geage des tubes, on installe sur le fond les blocs des murs en béton et 
l’on recouvre la galerie avec des hourdis préfabriqués en béton armé. 


750-2000 
p—_—_— 


750-2000 


| ÎL | 50-1600 
| 120-250 — 10 199-250 


100 | 460-1060 


Maçonnerie de briques 
120 ou 250 


2 Suivant I 1 Suivant 4-A 


(pour murs en blocs) 


FIG. XIII.1. Galeries surbaissées aux murs en blocs de béton (ou en briques): 


a, à un compartiment ; b, à deux compartiments; 7, blocs des murs en béton ou maçonnerie 
de briques; 2, hourdis du plancher préfabriqué en béton armé; 3, couche de propreté en bé- 
ton; 4,-mortier de ciment de classe 30 


Les murs de la galerie peuvent aussi être réalisés en maçonnerie de 
briques rouges (bien cuites). La section d’une telle galerie peut varier 
largement en fonction du diamètre des conduites : elle peut avoir une 
hauteur de 460 à 1060 mm pour une largeur de 500 à 1800 mm. 

L'épaisseur des blocs des murs en béton, fonction de la hauteur de 
la galerie, varie entre 120 et 200 mm (120 et 250 mm pour la maçon- 
nerie de briques). Les parois ñè"résistent à la poussée latérale du sol 
que si elles sont entretoisées en haut; on attendra donc la pose du 
plancher avant de combler la fouille. S'il est nécessaire d'ouvrir 
une telle galerie pour visiter et réparer la conduite, on est obligé 
de mettre en place des entretoîses au niveau supérieur des parois. 

Les hourdis des planchers de couverture sont plats, épais de 
60 à 160 mm en fonction de la portée (largeur de la galerie). 

La figure XIII.2 montre une galerie longée par un tube de drai- 
nage destiné à abaisser le niveau des eaux souterraines. Le tube en 
amiante-ciment ou en céramique avec des trous d'admission d’eau 




de 150 à 200 mm de diamètre est disposé 400 mm plus bas que le fond 
de la galerie, à une distance de 700 mm de la paroi, dans un lit fil- 
trant de gravier et de sable. 

Comme nous l'avons déjà signalé dans le $ XIII.1, la galerie 
située dans un sol gonflé d’eau et démunie de drainage pour des rai- 
sons techniques est obligatoi- 
rement dotée d’une couche étan- 
che (fig. XIII.3). Le fond de la 
galerie doit alors être en béton 
armé, Car il encaisse la pression 
ascendante des eaux souterrai- 
nes et travaille à la flexion entre 
les murs. Pour éviter la remon- 
tée de la galerie par flottation, 
il faut que son poids soit supé- 
rieur à la résultante des pres- 
sions ascendantes (voir $ XI.3, 


formule (XI.21)) FIG. Ps RU En longée par un 
NS tube de drainage: 
Dans la pratique de la cons- 1,1lit filtrant gravier-sable; 2, tule de 


truction, on utilise largement drainage 

pour les galeries surbaissées des 

éléments-types préfabriqués en béton armé qui facilitent le travail 
et diminuent la dépense des matériaux. 

Une galerie souterraine surbaissée à un compartiment est montrée 
sur la figure XIIT.4. Des caniveaux préfabriqués en béton larmé 
sont posés sur un lit de sable 
et recouverts de hourdis plats 
(fig. XIII.4, a). Une galerie à 
deux compartiments est une 
réunion de deux galeries à un 
compartiment divisées par un 
S R | espace de 100 mm rempli de sable 
M PS 3 ES CNE RL Eee (fig. XIII.4, b). Quelquefois les 

| caniveaux sont employés comme 


É plancher de couverture de la con- 
FIG. XIIL.3. Galerie avec couche {iite montée sur une couche de 


étanche collée: ; 
1, murs, 2, hourdis du plancher :préfahri- béton (fig. XIIL.4, c). : 
qués en bhéton armé; 3, couche étanche La hauteur des caniveaux est 


protection a aeninedes 0 onde Léon 300, 450 et 600 mm, la largeur 
ie are. Fe bs ad reondé de 600 à 2100 mm, la longueur 
en béton; 10, lit de pierres cassées nominale 3 m (longueur de projet 
2,97 m). « 

Pour pouvoir varier la longueur du tronçon droit de la galerie 
entre chambres ou entre niches, on prévoit pour tous types de cani- 
veaux des éléments complémentaires de longueur 0,6 m (longueur de 
projet 570 mm). Les parois des caniveaux résistent à la poussée 
latérale du sol à la façon des consoles encastrées dans le fond, ce qui 
détermine leur épaisseur variable : 80 à 140 mm en bas et 50 à 100 mm 




Suivant I-I 
Détail À 




LN J000 4 


Suivant TI 
30 3 
1 ea 
|] 30 


FIG. XIII.4. Galerie surbaissée construite en caniveaux préfabriqués en béton 
armé et dalles plates: 
1, caniveau; 2, hourdis du plancher; ee de. ciment: 4, lit de sable; 5, radier en 
Jéton È 


(ARBSO.HABRGAS EX EME MR :0 RAA) 


94-58] 98-104-IT 
Esp -200 Esp 150-200 


FIG. XIII.5. Ferraillage des caniveaux et dalles du plancher préfabriqués en 
béton armé: 
1, armatures principales; 2, armatures de répartition 




en haut. S'il est nécessaire d'ouvrir la galerie, on dépose les hourdis 
en laissant en place le sol autour des parois. 
Les caniveaux sont fabriqués en béton de classe M 300 et armés 
de treillis soudés en acier des classes A-III et B-I (fig. XIII.5, a). 
Les hourdis sont plats. Leur portée nominale (en travers du cani- 
veau) est 0,85 à 2,4 m, la longueur nominale 3 m (0,6 m pour les 


FIG. XIII.6. Galerie surbaissée en deux caniveaux accolés 


hourdis complémentaires), l'épaisseur 70 à 160 mm. Béton de classe 
M 200, armatures principales en acier de classe A-IIT, armatures de 
répartition en acier de classe B-I (fig. XIII, b). 

Une autre solution retenue pour les galeries surbaïissées préfa- 
briquées en béton armé consiste à superposer deux caniveaux dont 


FIG. XIII.7. Galeries surbaissées en dalles plates: 


1, lit de sable; 2, béton coulé en place 


l’un fait office de fond et l’autre de plancher. Le caniveau supérieur 
est mis en place après avoir posé et calorifugé les tubes (fig. XIIL5). 
La hauteur d’une telle galerie est égale à la somme des hauteurs des 
parois des deux caniveaux augmentée d’un espace d'environ 20 mm 
rempli de mortier de ciment de classe 50. Afin de positionner correc- 
tement les caniveaux l’un par rapport à l’autre, on interpose dans 
le joint une garniture d'acier formée de deux fers U (n° 12 et 16) 
réunis par soudure en forme de double T. Les parois de chacun des 




caniveaux résistent à la poussée latérale du sol à la façon d’une con- 
sole encastrée dans le fond du caniveau. 
Une troisième solution pour les galeries de même type utilise 
des dalles plates préfabriquées en béton armé (fig. XIII.7). Les dalles 
c) du fond, posées sur un lit 
100. 150 100 de sable, présentent des 
rainures de 200 mm de 
profondeur qui reçoivent 
les dalles des murs. Le jeu 
est rempli de béton de clas- 
se 300 aux pierres cassées 
de faible granulométrie. 
Les hourdis du plancher 


En Ze sont posés sur les dalles des 


murs (fig. XIII. 7, a). Une 


b Ë 6) 20, 2380 galerie à deux comparti- 
64-581 ments est aménagée en 
Esp.200 LS T-5 25 installant une cloison sur 

le fond (fig. XIII.7, b), 
do dé Etrier 66 et une galerie à comparti- 
Esp. 400 en guënconce ments multiples, en juxta- 


posant des galeries à un 
et à deux compartiments 


FIG. XIII.8. Ferraillage des dalles plates: (ig- ei 4 ne 
a, dalle du fond; b, dalle du mur; c, joint des e ferraillage des dalles 


dalles des murs est montré sur la figu- 
re XIII.8. 

Une galerie fabriquée à partir de caniveaux et de dalles plates 
peut être semi-enterrée, auquel cas elle sera recouverte de hourdis 
calorifugés à trois couches (fig. XIITI.9). 

Les éléments-types pour galeries sont calculés pour une profon- 
deur de 700 à 2000 mm à partir de la surface du sol, compte tenu de la 
surcharge en surface provenant des véhicules automobiles. 


Galeries semi-passantes 


Les galeries semi-passantes sont destinées à la pose des lignes de 
transport de la chaleur à deux tubes; elles peuvent abriter aussi des 
tuyauteries diverses, des câbles et d’autres canalisations. 

Une variante de galerie semi-passante aux murs en maçonnerie de 
briques est montrée sur la figure XIII.10. Grâce à l'emploi des élé- 
ments préfabriqués en béton armé, on réalise des galeries semi-pas- 
santes de 1500, 1800 et 2100 mm de haut, larges de 1200 à 4200 mm, 
pour y poser des tubes de 900 à 1200 mm de diamètre. Une galerie 
fabriquée à partir de caniveaux (fig. XIII.6) a deux compartiments. 
Chaque compartiment est formé de deux caniveaux larges de 1500 
ou de 1800 mm et hauts de 900 !) + 600 mm ou de 900 + 900 mm 


1) Le caniveau de 900 mm de haut est un élément complémentaire. 




| f DOLILIILLI I LIT II LIT ESS 


RC LR PRIT AR 




FIG. XIII.9. Galeries semi-enterrées : 


a, en caniveaux,; b, en dalles plates; ce, hourdis du plancher calorifugé; 1, caniveau; 2, 

hourdis du plancher calorifugé ; 3, asphalte ; 4, laitier; 5, couche étanche; 6, dalle du mur; 

7, lit de sable; 8, dalle du fond; 9, pousse HE 10, pièces de remplissage en béton 
cellulaire 




1150-2500 


100. 200 


{00 00 (1600) 




FIG. XIII.10. Galerie semi-passante aux murs en briques (les cotes entre paren- 
thèses se rapportent à un dnt — 600 à 700 mm): 
1, mur; 2, hourdis du plancher en béton armé; 8, fond en béton 




E a X| 
1280 -2500 


1400-1600 




| LE 


1500 -1740 






Béton coulé 
en place 


FIG. XIII.{4. Galerie semi-passante en blocs préfabriqués en béton armé: 


1, bloc du plancher; 2, bloc du mur; 3, bloc du fond; 4, boucles d’armatures en attente; 
5, béton coulé en place; 6, couche de propreté en béton; 7, lit de sable et de pierres cassées 




respectivement. Construite en dalles planes, la galerie peut être à 
un compartiment, large de 1200 à 4200 mm et haute de 14500 à 2100 mm 
(fig. XIII.7, a), ou à deux compartiments, large de 2 x 2100 mm 
et haute de 1500 ou 1800 mm (fig. XIII.7, b). 

Dans la pratique de construction des lignes de transport de la 
chaleur, on utilise des galeries semi-passantes en blocs préfabriqués 
en béton armé (fig. XIII.11). Le bloc du fond est plat. Celui du mur 
a une forme en L dont une aile est le mur de la galerie et l’autre, 
une partie de son fond. L’assemblage avec le bloc du fond est obtenu 
grâce aux aciers en attente sous forme de boucles. Le bloc du mur a 
une stabilité suffisante au cours du montage, ce qui permet de sup- 
primer toute fixation provisoire. 

Les blocs des murs et le bloc du fond ont même épaisseur. Sur ses 
tranches orientées vers les murs, le bloc du fond possède des aciers 
en attente sous forme de boucles. 

Après avoir enfilé des barres longitudinales dans les boucles de 
manière à assembler les blocs, on remplit le joint avec du béton de 
classe M 300. Le bloc du plancher de couverture est bordé de nervu- 
res disposées en travers de la galerie et munies de saillies qui s’op- 
posent au déplacement des blocs des murs sous la pression latérale 
du sol. 


Galeries passantes ou tunnels (collecteurs) 


Ün tunnel est réalisé selon un schéma analogue aux galeries semi- 
passantes, avec des murs en maçonnerie (fig. XII1.10), en blocs pré- 
fabriqués en béton armé (fig. XIII.11), et‘aussi, quand ses dimen- 
sions ne sont pas trop importantes, en 
blocs-caissons (fig. XIII.12). La dernière 
solution minimise la dépense des maté- 
riaux;, par contre, le bloc unique est 
difficile à fabriquer en usine et sa lon- 
gueur est limitée par les considérations 
du poids, ce qui fait qu’on a un grand 
nombre de joints à sceller dans le tunnel, 
opération toujours délicate. Des tunnels 
de ce type pourront avantageusement 
être exécutés à partir du béton coulé en 
place, dans un coffrage mobile mécanisé. 

Le plus souvent, les tunnels (collec- | 
teurs) sont réalisés en structures-types FIG: an Sn 
préfabriquées en béton armé (fig. XIII.13). Ha 
Jusqu'à 2400 mm, la largeur du tunnel | 
est choisie multiple de 300 mm (1500, 1800, 2100, 2400 mm), et 
au-delà, multiple de 600 mm (3000, 3600, 4200 mm). La hauteur du 
tunnel est égale à 2100, à 2400 ou à 3000 mm. 

Si le tunnel est à un compartiment, on utilise des éléments pré- 
fabriqués en béton armé de trois types: dalles du fond, dalles des 




murs, hourdis du plancher. Pour un tunnel à deux compartiments, 
qui possède un fond coulé en place en raison de sa grande largeur, 
on emploie les mêmes dalles des murs et hourdis du plancher, et aussi 
des panneaux préfabriqués et des pannes qui soutiennent les hour- 
dis du plancher à la jonction des deux compartiments. Les poteaux 
sont espacés de 3 m dans le sens de la longueur du tunnel. 

La dalle du mur est engagée dans la rainure du fond et le jeu 
est rempli de béton à base de pierres cassées de faible granulométrie. 




A Ùf 
ER CR ES 






nr: NT MÉRITE 240 /a a YLL' AT AD SL AN A0 


ZA A: €, 
re E 




É ee ae) [Erebrol el | 




FIG. XII1.13. Schémas de réalisation des tunnels préfabriqués en béton armé: 


a, à un compartiment ; b, à deux compartiments; 1, dalle du fond; 2, panneau du mur; 
83, hourdis du plancher; 4, fond coulé en pres ; poteau : 6, panne; 7, couche de propreté 
en on 


Le bord supérieur de la dalle s'engage derrière un épaulement ap- 
proprié du hourdis du plancher. De cette façon le panneau du mur 
résiste à la poussée latérale du sol comme une pièce encastrée dans 
le fond et articulée sur le plancher. Le poteau préfabriqué est engagé 
dans un logement prévu dans le fond coulé en place. Toutes les struc- 
tures sont calculées pour une profondeur de 0,7 à 2 m (entre la tran- 
che supérieure du tunnel et.Ja surface du sol), compte tenu de la sur- 
charge provenant des véhicules automobiles. 

Les tunnels de tous les types décrits sont exécutés à découvert, 
c’est-à-dire en creusant une tranchée ouverte. On peut aussi procéder 
par percement. Par exemple, le procédé de percement au bouclier con- 
vient aux tunnels de section circulaire, revêtus extérieurement de 
blocs de béton mis en place au fur et à mesure de l’avancement du 
bouclier métallique, et intérieurement de segments préfabriqués en 
béton armé. 




$ XIIIS3. CONCEPTION DES CHAMBRES, NICHES, 
APPUIS DES CONDUITES DE CHALEUR 


Chambres 


Les chambres, qui sont destinées à abriter les accessoires des condui- 
tes de chaleur, peuvent avoir une forme rectangulaire ou circulaire 
en plan. Elles sont construites en briques, en béton armé coulé en 
place et en éléments préfabriqués de béton armé. Les cotes d'implan- 
tation d’ure chambre peuvent être très variées, de 1,8 x 1,8 à9 x 
X 7,2 m. Les chambres sont enterrées à une profondeur non infé- 
rieure à 0,3-0,5 m à partir de la surface du sol. Les parois de la cham- 
bre sont percées de trous de passage des conduites. Le plancher de 
couverture de la chambre présente un trou d’accès de 650 à 700 mm 
de diamètre communiquant avec la surface. La descente et la remon- 


Suivant I-I 


ads la SEE SEE 4 


. D RAA 




3 M, 
Vue en plan 
1500 - 6400 250 + 640 


1500 - 4000 




TOITDL 


FIG. XIII.14 Chambre: 


1, maconnerie de hriques hourdées au mortier de ciment; 2, hourdis préfabriqué en béton 

armé; 3, noutie préfabriquée en béton armé; 4, trous d’accès. de 650 mm de diamètre; 5, 

trous d’entrée des conduites; 6, crampons de descente; 7, fosse; 8, revêtement en béton; 
10, lit de pierres cassées damées 






tée du personnel sont facilitées par des crampons d’acier encastrés 
dans le mur à l’intervalle de 300 mm ou une échelle métallique ver- 
ticale. Une fosse pour la collecte de l’eau est prévue dans le fond. 

La figure XIIT.14 représente une chambre aux murs en briques, 
au fond en béton coulé en place et au plancher préfabriqué en béton 
armé. Les hourdis du plancher de couverture sont posés directement 


ti Fa 


FIG. XI11.15. Chambres en éléments préfabriqués 


sur les murs, et si la chambre est grande, aussi sur des poutres inter- 
médiaires préfabriquées (voir fig. XIII.14). 

L'utilisation des structures préfabriquées dans l’enceinte de la 
chambre facilite beaucoup les travaux et réduit les délais de la cons- 
truction. Les chambres de forme rectangulaire en plan peuvent être 
assemblées à partir des blocs de -kétan préfabriqués (fig. XIII.15, a, 
b), de dalles nervurées ou plates (fig. XIII.15, c), des blocs en forme 
de L analogues à ceux de la figure XIII.11, des blocs tridimension- 
nels (fig. XIII.15, d), etc. Les chambres circulaires peuvent être 
construites en utilisant des tuyaux en béton armé de 2,5 m de dia- 
mètre (fig. XIII.16, a) ou des dalles plates mises verticalement et 
assemblées sur chantier (fig. XIII.16, b). 

À cause de la grande diversité des solutions adoptées pour les 
murs des chambres, les éléments types en béton armé ne sont utilisés 
que dans le plancher de couverture. Le matériau et le système des 




murs sont indiqués dans le projet conformément aux possibilités 
techniques de l’entreprise de construction. Les cotes d'implantation 
intérieures sont prises multiples de 0,6 m entre 1,8 et 9 m. Les plan- 


FIG. XIII.16. Chambres cireulaires- 


chers sont réalisés avec les mêmes types de hourdis que les galeries 
et les tunnels. A titre complémentaire, on utilise pour les planchers 
des dalles avec un trou de 700 mm de diamètre, des poutres de sec-’ 


1500 


tion rectangulaire 500 X 250 mm longues de 3,2 à 5,2,4% aijtsi que 
des anneaux en béton armé pour regards. Dans une ch# : 


a); si la largeur est plus grande, on pose des poutres intermédiaires 
en direction longitudinale (fig. XIII.17, b). Dans les chambres 
spacieuses on place des poteaux intermédiaires qui supportent les 


FIG. XII1.18. Niches pour lyres de dilatation: 


1, conduites de chaleur ; 2, galerie; 8, Joint de dilatation; 4, niche; 5, poutre d’appui en 
cornières d’acier soutenant les hourdis 


poutres (fig. XIII.17, c). Les poteaux sont en briques, béton ou 
béton armé; leur système, ainsi que celui des murs, est précisé dans 
le projet. 


Niches 


Le système de compensation de la déformation thermique de la con- 
duite de chaleur entre deux appuis fixes, affectant la forme d’un U 
et appelé lyre de dilatation, est réalisé par un cintrage particulier des 
tubes. 

Les lyres de dilatation disposées le long du tracé de la conduite 
sont abritées dans de petites chambres appelées niches (fig. XIII.18). 
La forme de la niche en plan reproduit celle des tubes. Un joint de 
dilatation sépare la niche de la portion droite de la galerie. Les di- 
mensions de la lyre, donc aussi celles de la niche, dépendent du dia- 
mètre de la conduite. Si le tube de la conduite a un diamètre non 
supérieur à 150 mm, la niche pour lyre a la forme d'une galerie à 
deux compartiments (fig. XIII.18, a); pour les diamètres plus im- 
portants, la niche a la forme de deux galeries séparées de 1,2 à 1,8 m 
(fig. XIII.18, b). T 

Les murs de la niche peuvent être en briques, en blocs préfabri- 
qués en béton armé ou en béton coulé sur place. Le fond est en béton 
armé ou non. Le plancher est toujours constitué par des hourdis pré- 
fabriqués en béton armé, comme pour la couverture des tronçons 
droits de la galerie. Dans les coudes de la galerie, une poutre d’ap- 
pui spéciale est prévue pour soutenir les hourdis. On utilise à cet effet 
une poutre d'acier formée de cornières accolées, afin de ne pas ré- 
duire la dimension intérieure de la galerie. Les hourdis sont posés 




sur les ailes horizontales des cornières, tandis que les ailes verticales 
sont logées dans les joints entre les hourdis. 


Hourdis enlevés 
Axe de 


symétrie | 


FIG. XIII.19. Détails d’une niche: 


1, galerie, 2, joint de dilatation; 3, fond coulé en place; 4, murs de la niche (briques, 
blocs de béton, béton armé coulé en place); 5, hourdis du plancher de couverture ; 6, poutres 
en cornières d'acier 


La figure XIII.19 montre quelques détails de réalisation d’une 
niche pour lyre de dilatation. 


Appuis fixes et mobiles des conduites de chaleur 




Les appuis fixes sont destinés à encaisser les efforts longitudinaux 
provenant de la pression intérieure non équilibrée dans les tubes 
ainsi que les forces de frottement qui se développent au droit des 
appuis mobiles (glissants) pendant les déplacements des tubes consé- 
cutifs aux dilatations et contractions thermiques. L’effort longitudi- 
nal, fonction du diamètre du tube, de la distance entre deux lyres 
de dilatation, du type de la lyre, du type de l'appui mobile, peut 
varier largement: de 1-5 tf (10-50 kKN) à 50-70 tf (500-700 KN) et 
plus. L’appui fixe dans la galerie (fig. XIII.20) représente générale- 
ment une cloison transversale en béton armé préfabriqué ou coulé 
en place percée de trous pour les tubes. L’effort est transmis sur l’ap- 


22-0948 337 


pui par des brides d’acier renforcées par des goussets longitudinaux. 
Puisque les efforts peuvent être exercés dans les deux sens. on prévoit 
les brides des deux côtés de l’appui et l’on place les armatures contre 
les deux faces de la cloison. Si le diamètre des tubes ne dépasse pas 
50 mm, la cloison a une épaisseur égale à 100 mm ; entre 80 et 150 mm 
de diamètre, à 150 mm; entre 200 et 400 mm de diamètre, l’épaisseur 


100 = 400 


4) b) 1 es TE 


LP 5 


DUR MIUM/ARNE EE ; | 


FIG. XI11.20. Appui fixe du type bouclier: 


a, vue latérale (avec schéma de ferraillage); b, vue en coupe, 1, conduites de chaleur ; 2, 
bride: 3, gousset; 4, fond de la galerie; 5, héton; 6, armatures principales: 7, trou de 
passage de l’eau; 8, trous d’entrée des conduites; 9, armatures de répartition 


de la cloison est égale au diamètre du tube. En calculant un tel appui, 
on admet que tous les efforts reportés par ce dernier sont transmis sur 
les murs longitudinaux de la galerie uniquement. 

Pour les tubes de gros diamètre, on utilise des appuis fixes en T 
(fig. XIIT. 21). C'est une portion de la galerie longue de 4 ou 5 m, aux 


FIG. XIII.21. Appui fixe en T 
coulé en place: 


1, galerie: 2, fond de l’appui fixe: #, 
parois de l'appui; 4. cloison 


murs et au fond en béton armé coulé en place. Dans sa partie médiane 
est placée une cloison transversale de 500 à 600 mm d'épaisseur qui 
encaisse les efforts. Le fond est muni de saillies à ses bords. afin 
d'augmenter la résistance de la structure au glissement. Un appui 
de ce type peut également être assemblé à partir d'éléments préfa- 
briqués en soudant les aciers en attente et en remplissant Îles joints 
de béton. 




Une chambre peut aussi faire office d'appui (fig. XIII.22). La 
paroi traversée par les tubes est renforcée et munie d'une « dent » 
qui s'oppose au déplacement de la chambre. Si le diamètre de la 
conduite n'est pas grand, l’appui fixe 
est aménagé dans le mur en briques 
ou en béton de la chambre: à cet effet 
on installe deux profilés d'acier en U 
au niveau des tubes, on soude les 
goussets de butée des tubes sur ces 
profilés et on coule le béton (fig. 
XIII.23). On peut aussi installer des 
1ppuis fixes de profilés en U directe- 
ment dans les chambres (fig. XIII.24): 
chaque tube passe entre deux mon- 
tants verticaux encastrés dans la pou- 
tre inférieure en béton armé et fixés 
en haut par des poutrelles d'acier ju- 


FIG. XIII.22. Chambre en béton armé FIG. XIII.23. Appui fixe aména 
coulé en place faisant office d’appui gé sur le mur en briques de la 


fixe pour les conduites de gros dia- chambre: 
metre 1, galerie; 2, chambre: 8, profilés en 
U; 4, béton 


melées. Les efforts exercés font travailler les montants et les pou- 
tres à la flexion, aussi ces éléments doivent-ils avoir une épaisseur 


FIG. XII1.24. Appuis fixes en acier installés dans les chambres des galeries: 


1, montants (profilés en U); 2, poutre en béton armé: 3, poutrelles; 4, entretoises des 
montants 


29% 339 


considérable quand les efforts sont élevés. Les réactions d'appui 
sont reportées par les murs de la chambre. 

Les appuis mobiles (glissants) des conduites de chaleur ont la 
forme de patins métalliques 
soudés sur le tube et prenant 
appui sur des tôles d'acier 
fixées dans des semelles en 
béton armé. Pour les tubes 
de 25 à 80 mm de diamètre, 
le patin est une simple plaque 
mince pliée (fig. XIII.25, a); 
pour les tubes d’un plus 
grand diamètre, il est cons- 
titué de tôles d'acier soudées 
entre elles (fig. XIII.25, b). 
On interpose quelquefois des 
rouleaux afin de diminuer le 
frottement entre le patin d’ap- 
pui du tube et la semelle 
(fig. XIII.25, c). 

La distance entre deux 
appuis voisins est fonction 
du diamètre des tubes: en 
effet, le tube travaille à la 
flexion comme une poutre 
continue sollicitée par son 
poids propre et par le poids 
de l'agent caloporteur. Les 
semelles en béton armé ré- 
partissent la pression trans- 
mise par les tubes sur le fond 
de la galerie, ce qui fait 
qu’elles sont dimensionnées 
FIG. XIII. 25. Variantes des appuis aussi en fonction du diamè- 


mobiles : tre des tubes. 
1, tube d'acier; 2, couche d’isolant:; 3, patin : = 
d'appui; 4, tôle d’appui; 5, semelle en béton Il est possible de construi 
armé; 6, rouleau re les appuis mobiles sous 


forme d'une poutre d'acier 
assemblée à partir de cornières ou de profilés en U; disposée en 
travers de la galerie, la poutré"ét soudée sur les pièces scellées dans 
les parois (fig. XIII.25, d). 


Joints de dilatation 


Nous avons déjà dit dans le $ XIII.1 que les joints de dilatation 
ont pour but d'assurer un affaissement indépendant de chaque tron- 
çon de la conduite de chaleur et de réduire les déformations des struc- 




tures provoquées par les variations de la température. Dans un point 
approprié du tracé ou devant une chambre ou une niche, on laisse 
un espace de 30 mm entre les éléments des structures qu'on remplit 




Suivant I-T 
(vue en plan) 


FIG. XIII.26. Détails des joints de dilatation: 


a, dans un tronçon droit de la galerie: b, devant une chambre; J, bitume; 2, rubéroïde: 
3, muret de protection en briques 


ensuite de bitume. En haut et latéralement, les joints sont recouverts 
de deux couches de rubéroïde et protégés par un muret de briques 
(fig. ?XII1.26). 


$ XIIL.4. CONDUITES DE CHALEUR POSÉES EN TRANCHÉE 


Les conduites de chaleur peuvent être posées directement dans le 
sol, sans aménager une galerie. Un tel mode de pose des conduites 
s'avère très économique, mais en revanche on est obligé de mettre 
en place une isolation thermique suffisamment efficace tout en assuæ 
rant la liberté du déplacement des tubes. 

Les conduites sont posées en tranchée et protégées par une gaine 
constituée par des tuyaux en béton armé. La position correcte de la 
conduite dans son enveloppe est garantie par des étriers en acier 
rond soudés sur les tubes (fig. XIII.27, a). La gaine protectrice peut 
aussi être constituée par des tuyaux en amiante-ciment, et en cas de 
pose sans tranchée (par exemple sous la chaussée), également par des 




tubes d'acier. Dans une autre variante la conduite est protégée par 
des segments en béton armé avec une couche d’'isolant fixée à la 
colle (fig. XIII.27, b). On creuse la tranchée, on met en place un 
lit de pierres cassées, on pose les segments inférieurs (munis de se- 
melles cylindriques), on installe les tubes d'acier et enfin on place 
les segments supérieurs et on remplit les joints entre segments avec 
du mortier de ciment. 

Un procédé remarquablement économique et simple consiste à 
appliquer la gaine protectrice en béton mousse armé sur le tube en 






FIG. XI11.27. Conduites de chaleur posées en tranchée: 


1, conduite (tuhe d'acier); 2, isolant : 3, gaine (tube): 4, appuis de la conduite (étriers en 
acier); 5, segment sunérieur; 6, segment inférieur 


usine et à munir celui-ci d’une couche étanche solide. Pendant les 
déplacements de la conduite causés par les dilatations, une adhé- 
rence parfaite est garantie entre la gaine et le tube d’acier. Toutes les 
charges provenant de la pression du sol et du frottement de la gaine 
sur le sol sont reportées par le tube d'acier qui doit être calculé en 
conséquence. On utilise les conduites de ce type dans un sol de densité 
suffisante. TT: 

Les conduites de chaleur peuvent être protégées par un remblai 
(par exemple en isol à base d’asphalte) qui possède des qualités 
hydrophobes (c'est-à-dire ne s’imbibe pas d’eau du sol). Sous l’action 
de la chaleur provenant de l’agent caloporteur, le matériau du rem- 
blai s’agglomère en formant une couche dense aux propriétés anti- 
corrosives autour du tube d’acier. Le remblai entourant la couche ag- 
glomérée reste très poreux et assure un calorifugeage efficace sans 
gêner les déplacements de la conduite. Toutes les charges exercées sont 
reportées par le tube d'acier. 




$ XIIL.5. POSE AÉRIENNE DES CONDUITES DE CHALEUR 


Les conduites de chaleur sont montées sur des pylônes isolés ou sur 
des rampes. Une conduite qui longe un bâtiment peut être posée 
sur des supports encastrés dans le mur. Elle est placée à une hauteur 
de 5 ou 6 m, afin de permettre une circulation aisée sous les tubes. 

En cas de pose aérienne sur pylônes isolés (fig. XIII.28, a) on met 
à profit la capacité portante des tubes d'acier; de ce fait la distance 
entre pylônes est d’autant plus grande que le diamètre du tube est 


FIG. XII1.28. Conduites de chaleur aériennes posées sur pylônes: 


1, conduites; 2, traverses métalliques; 3, poteaux en béton armé; 4, haubans; 5, poutre 
longitudinale; 6, contre-fiches 


élevé. Ce mode de pose procure l’économie maximale si le tube a un 
diamètre élevé !) (300 mm et plus). L’écartement des pylônes est 
dicté non seulement par la résistance mécanique des tubes mais aussi 
par leur flèche laquelle ne doit pas gêner l'écoulement libre de l’eau 
ou du condensat compte tenu de la pente longitudinale adoptée. 
L'écartement entre pylônes étant / (en cm) et la pente longitudinale i, 
la flèche maximale admissible f (en cm) est déterminée par la for- 
mule 


f < 0,25il. 


Parallèlement aux tubes de gros diamètre, on peut poser des 
tubes de petit diamètre qui seront suspendus ou appuyés tous ls 
2 à 4 m aux gros tubes. Le poids des petits tubes doit être pris en 
compte lors du calcul de la conduite principale. 

Pour pouvoir augmenter la distance entre les pylônes isolés, 
on peut soit renforcer les conduites portantes par des haubans en 


1) La température de l’agent caloporteur n'étant pas supérieure à 300 °C. 




câbles ou barres (fig. XIII.28, b), soit écarter les traverses de sou- 
tien sur les pylônes en plaçant dans la partie supérieure du pylône 
des poutres longitudinales métalliques avec des contre-fiches 
(fig. XIII.28, c). 

Les pylônes types chargés jusqu’à 3 tf (30 KkN) sont constitués 
par des poteaux de section rectangulaire en béton armé (fig. XIII.29,a) 


100-120 


9 ) Lee 




LR S a a 140 pour L:1800 
> ss he 2400 
S LÉ 


6 =300 ou $00 


FIG. XIII.29. Poteaux en béton armé et traverses métalliques des pylônes des 
conduites aériennes 


et des traverses métalliques longues de 0,6 à 2,4 m (fig. XIII.29, b), 
ou bien par des poteaux, des traverses et des poutres longitudinales 
de 6 m de long munies de contre-fiches (fig. XII1.28, c). La hauteur 


À 1900 1300 ; 
2400,3000.4200 L) 
. 4800, 6000 


Na S 



FIG. XII1.30. Eléments en béton armé des pylônes (charge supérieure. à]3 tf): 
a, poteaux en T; b, poteaux en IT; c, traverses; d, poteau en II avec traverse 


d’un pylône À varie entre 2,4 et 7,8 m, échelonnée de 0,6 m. Si la 
charge sur le pylône est plus grande que 38 tf (30 kN) et sa hauteur est 
H = 5,4 à 7,8 m, on utilise des poteaux en T ou en II en béton armé 


et des traverses (fig. XIII.30). 
Les conduites sont posées soit directement sur la face supérieure 


du poteau, soit sur la traverse placée en tête du poteau. 




Une rampe est une espèce de pont, constituée par des poteaux sup- 
portant des poutres en béton armé ou des fermes d'acier (fig. XIII.31). 
Les conduites de chaleur sont soutenues par des traverses dont l’écarte- 
ment dépend du diamètre des tubes; un platelage de service peut 
être prévu sur toute la longueur de la rampe. Les rampes sont assez 


12000 7 | {2000 
_1 12000 


ee. à 



FIG. XIII.31. Rampes pour conduites aériennes: 


1, poteaux en béton armé; 2, fermes métalliques; 3, traverses métalliques; 4, conduites : 
5, poutres en béton armé; 6, traverses en béton armé 


onéreuses, mais leur emploi est justifié quand il s’agit de poser en- 
semble un grand nombre de tubes de petit diamètre qu’on doit visiter 
fréquemment. 

Les rampes types à un niveau chargées jusqu'à 0,5 tf/m (5 kN/m) 
sont constituées par des poteaux en béton armé et des fermes mé- 
talliques de 12 ou de 18 m de portéc. Les traverses posées sur les. 
fermes sont métalliques elles aussi (voir fig. XIII.31, a). Si la charge 
est de 0,5 à 4 tf/m (de 5 à 40 KN/m) et la hauteur Æ de 6 à 8,4 n° 
tous les éléments de la rampe à un niveau sont préfabriqués en béton 
armé. Les pylônes peuvent être simples (poteau simple, poteau en 
T, poteau en Il) ou doubles (poteaux simples). Sur les poteaux sont 
mises des poutres longitudinales en béton précontraint de section en 
T, longues de 12 m, qui supportent des traverses longues de 3 à 
7,8 m posées sous les tubes (voir fig. XIII.31, b). 


345- 


Les pylônes des rampes à deux niveaux en béton armé (voir 
fig. XIIT.31, c) sont écartés de 12 m, eux aussi. Les poutres longi- 
tudinales peuvent être prévues dans les deux niveaux ou seulement 
en bas, quand les tubes du niveau supérieur ne peuvent reposer sur 
les traverses qu'à l’aplomb des pylônes. 

Les pylônes disposés suivant la longueur de la conduite de cha- 
leur sont classés en pylônes intermédiaires et pylônes d'ancrage. 

Les pylônes intermédiaires supportent 


1 F des appuis mobiles, et les pylônes d'an- 
CNT  crage, des appuis fixes de la conduite. 
cu: Un pylône d'ancrage est disposé généra- 


lement à mi-distance entre deux joints de 
dilatation (dont l'écartement ne doit pas 
être supérieur à 72 m). Il est constitué de 
poteaux isolés reliés par des barres de con- 
treventement métalliques (fig. XIII.32). 
7 Les pylônes d'ancrage assurent la rigi- 
an dité spatiale du système dans son ensem- 
II ble. 


F1G. XII1.32. Pylône d’an- FIG. XIII.33. Disposition des lyres de dilata- 


crage: tion d’une conduite aérienne sur rampe: 
1, appui fixe des conduites de 1, pylône intermédiaire ; 2, pylône d’ancrage: 3, ferines 
chaleur # ou poutres; 4, ronduite; 5, lyre; 6,poutre intercalaire 


Les lyres de dilatation flexibles des conduites de chaleur placées 
sur rampes sont disposées aux droits des joints de dilatation, dans 
les intervalles longs de 3 ou de 6 m (fig. XIII.33). Dans les limites 
de la rampe, cet intervalle est recouvert par des poutres intercalaires 
à simple travée qui peuvent se déplacer librement sans gêner les dé- 
formations de la conduite lors.des variations de température. 

Les supports muraux sont faits en cornières ou en profilés en U 
(fig. XIII.34). Ils sont disposés conformément au schéma du mur, 
de façon à ne pas compromettre la stabilité et la résistance méca- 
nique de celui-ci. Dans un bâtiment à ossature, les supports sont 
fixéssur les pièces scellées dans les poteaux en béton armé (fig. 
XIIIL.35, a) ou sur des colliers mis autour du poteau (fig. XII1.35, b). 

Les appuis mobiles des conduites de chaleur aériennes sont réa- 
lisés à l’aide de patins, de rouleaux (voir fig. XIII.25) ou de suspen- 
sions (fig. XII1.36). Les appuis fixes des conduites de chaleur sont 




disposés sur les pylônes d'ancrage, par analogie au cas illustré sur 
Ja figure XIII1.20. Pour installer un appui fixe sur un support mural, 


FIG. XI1II.34 Supports muraux: 


1, support; 2, mur; 8, béton; 4, pièce de répartition 


on soude des butoirs en cornières sur le tube, de part et d’autre du 
support, et l’on fixe le tube sur le support à l’aide d’un collier 


FIG. XI11.35. Supports fixés sur poteaux en béton armé: 
1, poteau: 2, support: 3, pièce scellée; 4, collier 


(fig. XIII.37, a). Si le diamètre du tube est d>100 mm, le support 
doit être mieux ancré dans le mur ou muni d'une contre-fiche 
(fig. XIII.37, b). 






LETTRE à 


FIG. XIII1.36. Systèmes de suspension des conduites aériennes: 


a, b, sous une poutrelle ; ce, sous une poutre en béton armé: d, sous un hourdis; 7, conduite; 
2, collier; à, tirant de suspension; 4, trier; 5, profilé en U 


Suivant I-T 


RAC RS € (é N 




FIG. XIII.87. Détails des appuis fixes des conduites posées sur supports muraux : 


1, collier; 8, butoirs (cornières); 3, support mural; #, butoirs (plats d’acier); 5, contre- 
fiches du support 




$ XIII.6. PRINCIPES DE CALCUL DES STRUCTURES 
RELATIVES AUX CONDUITES DE CHALEUR 


Conduites de chaleur souterraines. Tous les ouvrages relatifs aux 
conduites souterraines — galeries, chambres, niches — sont exposés 
aux charges suivantes: 

— charges permanentes 
dues à la pression verticale 
et horizontale du sol; 

— surcharge en surface 
due aux véhicules; 

— poids des conduites de 
chaleur ; 

— efforts horizontaux cau- 
sés par la pression intérieure 
non équilibrée dans les con- 
duites et le déplacement de 
ces dernières lors des varia- 
tions de température. 

Les ouvrages étant cons- 
truits à ciel ouvert, les pres- 
sions verticale et horizontale 
du sol croissent de façon liné- 
aire en fonction de la profon- 
deur (fig. XI11.38, a). La char- 
ge verticale de calcul due à la 
pression du sol à l’unité de 
la surface est 


Qv = ÿhn, tf/m? (N/m°), 


où À est la distance de la 
surface, m,; y, la masse volu- 
mique du sol, t/m° (en moyen- 
ne y — 1,8 t/m°); n, le coef- 
ficient de surcharge égal à 1,2. 


Pa °P,k 


La charge horizontale de P; 
calcul provenant de la pression 
du sol est 
Qh — Qv tg* (45 — FIG. XIII.38. Efforts exercés sur une 
— p/2) — qvk tf /m° (N/m?), galerie souterraine " 


où v est l'angle de frottement intérieur du sol (en moyenne @ — 30°). 

En calculant la surcharge en surface due à la pression des roues 
du véhicule, on admet qu'elle est distribuée dans le sol sous un angle 
de 30° sur la verticale (45° dans le revêtement de route). Par consé- 
quent, les pressions verticale et horizontale correspondantes à l’unité 
de la surface diminuent avec la profondeur (fig. XIII.38, b). Les 




Normes de calcul des ponts et des tuyaux imposent pour la surcharge 
en surface due aux véhicules un coefficient de surcharge n = 1,4. 

Si la tranche supérieure de l’ouvrage se trouve à une profondeur 
égale ou supérieure à 1,2 m (fig. XIII.38, c), on admet que la sur- 
charge caractéristique verticale due aux véhicules est répartie uni- 
formément et égale à 2 tf/m°? (20 kN/m°) à toute profondeur =. La 
surcharge de calcul est p, = 1,4 x 2 — 2,8 tf/m° (28 kN/m°). 
La surcharge horizontale due aux véhicules est déterminée de la 
même façon que la charge provenant de la pression du sol 


Pn = Pv tg? (45° — 9/2) = pk. 


Dans les ouvrages enterrés (galeries, chambres, niches) la chaige 
verticale due au poids du sol au-dessus du plancher, la surcharge 
due aux véhicules et le poids propre des structures (y compris le 


FIG. XI11.39. Pressions sur le sol sous les murs et le fond des galeries 


poids propre des conduites de chaleur) sont transmis sur le sol sous- 
jacent et équilibrés par la réaction de ce dernier. La pression à l’unité 
de surface du sol de fondation provenant de la charge caractéristique 
totale ne doit pas être supérieure à la pression de calcul sur le sol R.. 

Si l'ouvrage a les murs en briques ou en béton et le fond en béton, 
l'épaisseur du mur en bas étant égale à b et le mur reposant sur une 
couche de propreté en béton d'épaisseur k,, (dont la fonction est de 
distribuer la pression sous un angle de 45°), la charge °C est transmise 
sur le sol de fondation par une bande de largeur by — b + 2h,, 
(fig. XIII.39, a). 

On calcule généralement VC pour un mèêtre de longueur de la 
paroi, c’est pourquoi on prend la surface du sol de fondation égale à 
bt x 100 cm’. La formule de calcul devient donc 


Si le fond est en béton armé, la pression est distribuée sur le sol 
suivant le schéma de la figure XIII.39, b. On admet qu'elle est 
uniformément répartie suivant la surface du fond (fig. XIII.39, c). 
Le fond est calculé pour résister à la réaction du sol déterminée par 
les charges de calcul. Le schéma des efforts de calcul est montré sur 
la figure XI11.40. Pour la charge horizontale due à la pression du sol, 
on admet qu'elle est exercée simultanément des deux côtés de l’ouvra- 




ge, car le remblai est fait des deux côtés et le sol est compacté couche 
par couche. Quant à la surcharge horizontale provenant des véhicules, 
elle peut être exercée des deux côtés ou d’un seul : on distingue donc 
deux cas particuliers dans le calcul. 
Le cas de charge des différents éléments de l’ouvrage dépend de 
la solution technique adoptée. 
‘ Les hourdis du plancher de couverture étant dans la plupart des 
cas articulés sur les murs et les poutres, on assimile le hourdis à 


FIG. XIII.40. Schémas des efforts de calcul appliqués aux galeries, tunnels, 
: chambres au fond en béton armé: 
a, profondeur inférieure à 1,2 m; b, profondeur égale ou supérieure à 1,2 m 


une poutre à simple travée sollicitée par la charge q,, la surcharge p, 
et le poids propre q,p. 

En fonction des ‘Charges exercées sur le hourdis, on calcule le 
moment fléchissant maximal, puis, compte tenu de la résistance du 
hourdis en section normale, on détermine la section à donner aux 
armatures principales longitudinales. 

Les murs en maçonnerie de briques et en blocs de béton sont arti- 
culés au niveau du plancher de couverture et du fond. Le mur subit 
la charge verticale déterminée par les hourdis et par son poids propre, 
ainsi que les charges horizontales gg», pn. Le mur ayant une longueur 
considérable (cas des galeries), on l’assimile à une poutre verticale à 
simple travée de 1 m de large articulée sur le plancher et le fond. 
On calcule le moment fléchissant dû à gn et Pn, puis on détermine. 
l'effort normal dû à q;, pv, qnp et au poids du mur au droit du moment 
maximal et l’on vérifie la résistance de la maçonnerie (ou des blocs. 
de béton) d’après les formules de calcul des structures sollicitées en, 
flexion avec compression (voir chapitre VIIT). 

Si le rapport de la longueur du mur ! à sa hauteur À est égal ou 
inférieur à 2 (on rencontre fréquemment ce cas dans les chambres), 
le mur est assimilé à une dalle appuyée sur les parois transversales, 
le fond et le plancher de couverture. Les moments fléchissants sont 


déterminés à l’aide des tables pour les dalles isotropes rectangulaires. 
(voir Annexe XX). 




On doit également prévoir le cas de travail des murs sans les 
hourdis du plancher. Dans ce cas, comme nous l'avons signalé dans 
le $ XIII.2, on met en place des entretoises afin de créer l'appui supé- 
rieur des murs, si bien que le cas de charge reste inchangé; or, en 
calculant le moment fléchissant, on ne considère que la pression laté- 
rale du sol (q.), et en déterminant l'effort normal, seul est pris en 
considération le poids propre du mur. On ne tient pas compte de la 
surcharge due aux véhicules. 

Dans les galeries et les tunnels en éléments préfabriqués en béton 
armé, les murs sont encastrés dans le fond et les hourdis du plancher 


oO CN y, y 4 great 


FIG. XIII.41. Pour le calcul des 


galeries et tunnels préfabriqués en 
béton armé: 


a, Schéma des efforts; b, système fon- 
M W, damental; oc, diagramme des moments 
A [4 fléchissants 


de couverture sont articulés sur les murs. Dans les calculs, la galerie 
(le tunnel) est assimilée à un portique en U muni d’une entretoise ri- 
gide articulée (hourdis du plancher de couverture) (fig. XIII.41). 
On cherche d’abord la poussée latérale X, et ensuite les moments flé- 
chissants en une section quelconque des murs et du fond comme la 
somme des moments de tous les efforts (la poussée À y comprise) 
agissant du même côté de la section considérée (voir fig. XITIT.41, b, c). 

La charge exercée sur le plancher (et la réaction correspondante 
du fond) fait naître un effort de éompression dans les murs, tandis 
que la charge latérale exercée sur les murs provoque une compres- 
sion dans le fond. On considère donc que les murs et le fond sont sol- 
licités en flexion avec compression. Puisque l'épaisseur des murs et 
du fond n'est pas grande, l’excentricité de la force longitudinale 
e — MIN dépasse largement la section ; pour cette raison la section à 
donner aux armatures est déterminée de façon approchée en fonction 
du moment , comme pour les pièces travaillant en flexion simple. 
Dans le cas où la galerie constituée par un caniveau en béton se trouve 




démunie de ses hourdis de couverture, ses parois résistent aux pres- 
sions latérales à la façon des consoles encastrées dans le fond 
(fig. XIITI.42). C’est d’après ce cas de charge qu’on détermine souvent 
la section à donner aux armatures principales du caniveau. En cal- 
culant un tunnel, quel que soit le cas de charge (voir fig. XIIT.40), 
on admet toujours que les hourdis du plancher de couverture sont en 
place. 


FIG. XII11.42. Schéma des efforts et diagramme des moments dans le caniveau 
préfabriqué en béton armé, le hourdis du plancher de couverture étant enlevé 


Conduites de chaleur aériennes. Le tube d'acier reposant sur 
pylônes doit être calculé à la résistance mécanique; sa flèche ne doit 
pas dépasser la valeur obtenue d’après la formule citée dans le 
$S XIII.5. 

Le tube est assimilé à une poutre continue à travées multiples 
sollicitée par une charge verticale uniformément répartie due au 
poids propre, au poids de l’isolant et au poids de l’agent caloporteur, 
affectée d’un coefficient de surcharge 1,2. La charge due à la neige 
et au givre n’est pas prise en compte. Le même cas de charge est adopté 
en calculant la charge horizontale due au vent : rapportée à 1 m de 
longueur du tube, elle est égale à 


{vent — 1,2 X 1,4Dq, 


où 1,2 est le coefficient de surcharge ; 1,4, le coefficient aérodynam- 
que ; D, le diamètre extérieur du tube avec la couche d’isolant, cm; 
Go, la pression dynamique caractéristique du vent, kgf/m? (N/m°), 
qui dépend de la zone géographique et de l’altitude (voir Annexe IT). 

Si le tube à calculer supporte d’autres tubes suspendus, on admet 
que les charges correspondantes agissent comme des efforts concentrés. 
En calculant la résistance mécanique du tube, on doit se rappeler qu’en 


23—0948 353 


plus des charges énumérées, les parois du tube subissent des contrain- 
tes dues à la pression intérieure de l'agent caloporteur, aux efforts 
axiaux provenant des déformations gênées (à cause du frottement 
dans les appuis et les lyres de dilatation), etc. Les méthodes de calcul 
des conduites font l’objet de normes particulières. 


( 3 Suivant l-[ 
Ta Le! 
FIG. XI1I1.43. Renforcement du tube: 


1, pylône: 2, tube; 2, nervure de renforcement 


Toutes les charges signalées (sauf l'effet du vent) sont prises en 
considération en calculant les conduites souterraines et les condui- 
tes posées sur rampes. 

Afin de pouvoir écarter davantage les pylônes, on peut renforcer 
les portions les plus sollicitées du tube (à l’aplomb des pvlônes) 
par des nervures longitudinales soudées (fig. XIT1.43). 


ü) b) c) N, NW 
N=M nee 
TE nn MN, ÿ, 


1, Fr 


«DACl*PasS 
P ent 


FIG. XII1.44. Pour le calcul des pylônes des conduites aériennes 


Les pylônes supportant les appuis mobiles des conduites sont 
calculés comme des poutres consoles verticales encastrées dans le sol 
(fig. XIII.44, a). La charge verticale comprend la réaction de l’ap- 




pui due au poids de la conduite V,, ainsi que le poids propre W, 
(on admet conventionnellement qu'il est appliqué en haut). Dans le 
plan perpendiculaire à l’axe de la conduite, le pylône se trouve exposé 
à l’action du vent Vent. C’est la résultante des pressions du vent 
exercées sur la portion du tube comprise entre deux pylônes, tandis 
que Pvent St la pression du vent exercée directement sur le pylône. 
Dans la direction de la conduite agit la charge horizontale W,;.: 
c’est la force de frottement dans les appuis des tubes. Les charges 
horizontales dues au vent et au frottement peuvent être orientées dans 
les deux sens. 

La longueur de flambement du pylône est prise égale au double 
de la hauteur. 

La semelle de chaque pylône est calculée en chaque direction 
comme une fondation excentrée. 

Dans un pylône à deux montants, les efforts exercés sont les 
mêmes (fig. XIII.44, b). La traverse étant généralement articulée 
sur les montants, on l'assimile à une poutre à simple travée sollicitée 
par les charges indiquées, tandis que les montants sont calculés 
comme des consoles verticales subissant la réaction de la traverse 
et l’action du vent. 

Le calcul des pylônes intermédiaires d’une rampe s'opère de la 
même façon, à cette différence qu’en calculant la charge verticale, 
on prend en considération le poids de la structure qui recouvre la 
travée (la ferme ou la poutre). Quant aux pylônes d'ancrage, ils 
subissent les charges verticales dues au poids propre et au poids des 
conduites, les charges horizontales transmises par la conduite et l’ac- 
tion du vent (fig. XIII.44, c). 

Afin de faciliter le calcul du système tridimensionnel composé 
de montants, de poutres et de barres de contreventement croisées, 
on le divise en éléments. Les poutres transversales sont calculées 
comme des poutres à simple travée soumises aux charges indiquées. 
Puis on considère un système de barres plan constitué par deux mon- 
tants reliés par les barres de contreventement croisées (fig. XII1.44, d) 
et on le calcule en tenant compte de la charge horizontale en chaque 


direction. Dans un tel système, la force SN fait naître dans les 
montants des efforts 


Ni N nor 11/0 ; 


il est à noter qu’un montant sera comprimé et l’autre tendu. Ces 
efforts se superposent aux compressions qui proviennent des charges 


verticales. Quand la force horizontale D W,,, est élevée, la compræ 
sion due à la charge verticale risque d’être moins grande que la trac- 
tion : il est nécessaire d’en tenir compte en dimensionnant les mon- 
tants. Plus les montants sont écartés, moins l'effort V,, est grand. 
Pour calculer l'effort dans la barre de contreventement, on admet 
(avec une certaine approximation) qu’au moment où l’une des barres 
commence à travailler à la compression, elle cesse de contribuer à la 


23* 355 


résistance du système (en raison de son grand élancement), tandis 
que l’autre barre travaille à la traction avec l'effort 


D Nhor/Sin a. 


C'est pour cet effort que seront calculées les attaches des barres de 
contreventement aux montants. 

Les structures des travées des rampes sont calculées comme des 
poutres ou fermes à simple travée qui subissent une charge verticale 
due au poids propre et au poids des conduites et des charges hori- 
zontales dues au vent. | 


ANNEXES 


ANNEXE 1 


Systèmes d'unités des grandeurs physiques et leurs rapports 


Unité, son symbole 


Grandeur système adopté dans Rapport des unités 
les Normes soviéti- système SI 
ques 
Force, charge, | kilogramme-force | newton (N) 1 kgf=9,8 N£&=10N 
poids (kgf), tonne-force |kilonewton (kN) |1 tf = 10 000 N — 
(t£) (4 tf — 1000kgf)| (1 kN = 1000 N) = 40 kN 


Charge linéi- | kilogramme-force | newton par mètre | 1 kgf/m = 10 N/m 


que, charge | par mètre (kgf/m) | (N/m) 4 tf/m = 10 kN/m 
surfacique tonne-force par |kilonewton par | 1 kgf/m? = 10 N/m2 
mètre (tf/m) mêtre (kN/m) 1 tf/m? = 10 kN/m2 
kilogramme-force | newton par mètre 
par mètre carré | carré (N/m°?) 


(kgf/m?) 
tonne-force par 
mètre carré (tf/m?) 


kilonewton par 
mètre carré 
(kN/m°?) 




pascal (Pa) (1 Pa = | 1 kgf/mm? = 107 Pa = 

Æ 0,1 millimètre | — 10 MPa 

de colonne d'eau) | 1 kgf/em? Æ 10° Pa = 

mégapascal (MPa) | —0,1 MPa 

(4 MPa—105 Pa) |1 tf/m? = 105 Pa — 
—1 MPa 


Contrainte, kilogramme-force 

pression, mo- {par millimètre 

dules de défor- | carré (kgf/mm!?) 

mations kilogramme-force 
par centimètre 
carré  (kgf/cm?) 
tonne-force par 
mètre carré 
(tf/m?2) (1 tf/m?— 
= 0,1 kgf/cm?) 


newton-mètre 1 kgf-m = 10 N':m 
(N-m) 1 t£-m = 10 KN:m 
kilonewton-mètre 

(kN :m) 


Moment d'une |kilogramme-for- 
force, d'un |ce-mètre (kgf-m) 
couple de for- | tonne-force:mètre 
ces (tf-m) 






ANNEXE II 


Charges normatives et coefficients de surcharge 


Charge 


Poids des structures en béton (avec y> 
> 1800 kg/mi), en béton armé, en pierres, en 
métal, en bois 
Idem, en béton avec y < 1800 kg/m3 
Poids des couches d'’isolant, d'égalisation, de 
parachèvement appliquées : 
en usine 
sur chantier 
Sols intacts 
Sols de remblai 
Poids propre et poids de l'isolant de l’équipe- 
ment à poste fixe 
Poids des matières remplissant l'équipement : 
liquides 
matières en suspension, boues, matières pul- 
vérulentes 
Charges dues aux ponts roulants, ponts roulants 
suspendus, chariots 
Charge uniformément répartie sur le plancher: 
appartements des immeubles d'habitation, 
150 kgf/m? (1,5 kN/m?) ; bureaux, locaux du per- 
sonnel, salles de lecture, 200 kgf/m? (2 KN/m°?): 
laboratoires, étages techniques, etc., en fonction 
de la charge réelle mais non inférieure à 
200 kgf/m? (2 kN/m?); cantines, 300 kgf/m2 
(3 KN/m?), salles de conférences, salles de spec- 
tacles, salles de sport, balcons, 400 kgf/m2 
(4 KN/m?); entrepôts de livres, archives, en fonc- 
tion de la charge réelle mais non inférieure 
à 9500 kgf/m? (5 kN/m?); greniers, 75 kgf/m2 
(0,75 KN/m?) en plus du poids de l'équipement ; 
halls, couloirs, escaliers, 300 à 409+kgf/m°? (3 à 
4 kN/m?) 




Coefficients de surcharge 


1,1 ({ pour conduites) 
1,2 (1,1 pour conduites) 




1,2 pour pC > 500 kgf/m? 
(50 KN/m°) 

1,3 pour pc—200 à 
900 kgf/m? (2 à 5 kN/m?) 
1,4 pour pC << 200 kgf/m°? 
(2 kN/m?°) 


Suite 


Charge Coefficients de surcharge 


Charge de neige: en fonction de la zone géo- 

graphique, poids de la neige p,— 50 à 250 kgf/m? 

(0,5 à 2,5 kN/m°?); Pésige 

profil de la toiture De 1,4 à 1,6, en fonction 
du rapport du poids pro- 
pre de la toiture au 
poids de la neige 


= poc, Où c dépend du 


Charge due à l'effet du vent : ‘en fonction de la 

zone géographique, pression dynamique go —=27 à 

100 kgf/m? (0,27 à 1,0 KN/m?), qéent = doc 

où k est un coefficient dépendant de la hauteur 

de l'ouvrage et du tvpe du terrain et c, le coef- 

ficient aérodynamique dépendant du profil de 

l'ouvrage 1,2 (1,3 pour les ouvra- 

ges de grande hauteur) 

Nota. Dans les Cas où toute diminution de la charge permanente est défavorable 


pour le comportement de l'ouvrage (par exemple, lors de 1a vérification à la stabilité 
au basculement), on prend le coefficient de surcharge égal à 0,9. 


ANNEXE III 
Résistances caractéristiques du béton lourd R;r et R\,, résistances 
de calcul du béton pour les états-limites d'utilisation R,, 11 et R4, 11 


kgf/cm? (MPa) 


Classe de résistance du béton 


Sollicitation 
Mi00 | M150 | M200 | M300 | M400 | M500 | M600 
Compression axiale 60 85 115 170 225 280 | 340 
(résistance sur pris- 6) (8,5) | (11,5) | (17) | (22,5) | (28) | (34) 
me) À; et Rat æ 
Traction axiale R°, 7,5 9,5 11,5 415 18 20 22 
et Risrr (0,75) | (0,95) | (1,15) | (1,5) | (1,8) | (2) | (2,2) 


Nota. Pour les bétons hourdés au ciment fondu, les valeurs de Rf_etde Rtr II 
sont à multiplier par 0,7. 




ANNEXE IV 


Résistances de calcul du béton lourd pour les états-limites ultimes 
Ror €t Rirs kgf/em? (MPa) 


Classe de résistance du béton 


Sollicitation 


M100 M150 M200 M300 M400 M500 M600 


Compression axia- 

le (résistance sur 

prisme) Rpr 45 70 90 135 175 215 245 
(4,9) (9) (9) | (13,5) | (17,5) | (21,5) | (24,5) 

Traction axiale 

Rtr 4,8 6,3 7,5 10 12 13,5 14,5 
(0,48) | (0,63) | (0,75) (4) | (4,2) | (1,35) | (1,45) 


Nota. Pour les bétons hourdés au ciment fondu, les valeurs de Rtr sont à multi- 
plier par 0,7. 


ANNEXE V 


Modules d’élasticité initiaux du béton lourd (non traité) 
en compression et en traction E:-10-3, kgf/cm? (MPa) 


CHA Qc PÉSIERNEE M100 | M150 | M200 | M300 | M400 | M500 | M600 


Module d'’élasticité initial 470 210 240 | 290 330 360 380 
(17) | (21) | (24) | (29) | (33) | (36) | (38) 


Nota. Pour les bétons traités par la chaleur à l’air libre les valeurs de E} sont à 
multiplier par 0,9, et pour les bétons autoclavés, par 0,75. 







( « 0€7) « 0065 e . . CE] e . Q . . 0 e e . UIUI 0 (4 OI (42) 
(CAN 0Y8) 319/J94 00 "ww Ee)9 


: a1peo ne qjuouguiojuoo “+ Ey pusrd uo ‘saqeurpn)13 
UOL S9118q Sup d1JueIp NP S101} NE INOHYJUI 359 1JQUICIP 01 JUOP III-V 9SSU19 2P 2118 U2 S01PU9 SOI INO ‘S9PNOS SOSSBIIEO SOL SUEC « 


(007) 000% (079) 0079 (008) 0008 (0007) 000 0H IA-LV 
a. (007) 0007 (0ÿG) 00FG (079) 0079 (008) 000 8 AV 
(007) 0007 (007) 0007 (00S) 0006 (009) 000 9 AI-LV 
(00%) 0007 (07G) 00FG (0#9) 0079 (008) 000 8 A-V 
(00%) 0007 (00%) 000$ (00G) 000€ (009) 000 9 AI-V 
ré (09€) 009€ (062) x 0062 (09€) 009€ ne 0-01 
(0ÿ£) 007£ (0L2) » 00LZ (0ÿ£) 007€ 8-9 III-V 
7. (042) 0012 (12) OSre (0L&) 0OLZ (00€) 000 £ IT-V 
(OZ) 007Z (0ZF) 001 (072) O0FZ (072) 00% x I-V 
ee — D 
JJ°e Eu 
: #4 jUeu) ; 
ta en 0er Anodson inod Sonbi1QO SUO1)905 ILE uoresipr 
01" ARS MOLEO ne Sepaos | AL QUEANS note ne | Ep sn EGE1D S91 mod 
_ ! YTY ‘SD9ANIDI ‘SUIPSIN ? . ; » 
mr NEA ‘SO[CSIVASUBIY SOC TE UIDN SUOI pepe UONOUIY UT E [NO189 9P S99 | synuurre s0p sossu]9 


-UUJSISD1 30 SH VOICI) EI P 
UOISSHIduI09 EI p uotJ984) v[ E Sonbrist19)98189 suourisis9ux 


SOIN SoJTWII-S30)9 Sul INOd SHINJUUHE SP [N90189 9P S99UVISIS9M 


————— "tt 
(8aN) sw9/754 ‘omjeuwuie p soueq SP 911918819,P 9[NpOu 39 [no[89 9p 32 sonbrisrigpouieo sooue)sIs9y 
IA AXANNV 


(0G8) 006 8 (O90F) 009 07 (0G9r) 006 97 G 
(088) 008 8 (00F+) 000 FH (0021) 000 LI 4’ 
(006) 000 6 (ETF) 00€ FT (OSLF) 006 LY 6 
(06) 00€ 6 (09FF) 009 FF (008r) 000 87 G'°L 
(0G6) 006 6 (065+) 006 Fr (GG8F) 066 87 9 
(8r‘0)8°r (00%) 000 % (086) 008 6 (O£GE) OO€ GI (0065) 000 67 c'y LM 
(029) 004 9 (078) 007 8 (00£E) 000 £7 8 
(0ZL) 008 L (006) 000 6 (007+) 000 77 L 
(OLL) 00L L (0ZL6) 004 6 (00SF) 000 GT 9 
(0£8) 00€ 8 (0£OF) 00€ 0} (0097) 000 97 G 
| (088) 008 8 (0077) 000 F7 (O0LF) 000 LT y 
(z‘o) x (00%) 000 (0£6) 00€ 6 (O9FE) 009 FI (008r) 000 8F € 11-dg 
(0GL) 008 L (006) 000 6 (00Y+) 000 7T 8 
(0L2) 00 Z (026) 002 6 (00GT) 000 87 L 
(08) 00€ 8 (0£0+) 00€ O7 (0097) 000 9F 9 
(088) 008 8 (00FF) 000 FF (0021) 000 LE G 
| (0£6) 00€ 6 (0975) 009 Fr (0087) 000 87 y 
(c‘0) x (007) 000 x (086) 008 6 (0£GE) 00€ GE (0067) 000 6} £ II-4 
a. (0€) 007 € (02) 006 z (07€) 00 € (G26) Sc ç G 
(L+‘O) L‘} (0S£) 008 £ (092) 009 x (0G£) 006 £ (0GG) 006 & y-C 1-dg 
(z'‘o)z (gr£) OST £ (023) 00 2 (Gr£) OST £ (0GG) 006 ç G-£ | I-g 
11e & : dr JUUS 
_ uopjuel anod son | *LMOQIS JUATOU o 1nod a 
H “1140 SUO1192S SOL JULCA | juvains [no[vI ne S29A ET Ode Le 
9-0F-°4 9110 US TNOIEO NE SPAM | 1 ‘sopessaASUC ‘Sol | nore9 ap OUEST 19 UIUI soinqeurte 
-1} U[9,P V[NPON SO[PSIDASUEI] SOINEUNC| stnpnyguor songer | | LEO PP OUEST D Li Lomerq | 50p sasse19 


où uOlj901) EI e onb 
-1)S119)00IP9 DOUCJSISYIT 


UOISS)J1d(U09 EI EL UOIJOU41) EI RP 




SOIN SJUUI[-S3079 Su NO SUINJUULIRE SP [NO ED 0P VOULISISON 


(C4) :&9/15% ‘oinjewav,p SIt] S9P 9)191)SUIY,p 9INpOU 39 [N9[P9 9p 39 SonbristiaJou1P9 S9UEJSISIY 
TIA AXAINNV 




————————————————————pLELELZLZLZLZEL 


‘Sd quos of ou inb Xno9 LE‘ — ouBis 6 10 ‘juoWioflotijsnput syinpoid quos nb sorjauelp xnv PACE QUBIS YT *DJON 

= L OIZDIDILILILIXIX] 07] 486] 9 cerfro erri8r 001) 6 ‘28 9e GL| 8‘cg|ve oc |89'Le | cr cz | 9c'z1| 0 
= TOUT IX IX] 9% | 66 2! 8 70rc9 76 |#7 ‘18 |9c ‘72 | 80 19! G'‘0c | 2107 |vc ‘08 | 9€ ‘oz | 87‘ OT] 9% 
Sn TO) |X IX] ce |ere'oley' og (s‘ez (re'‘r9 | e‘oc|cz'er | 1c'ov | LT ‘ce [er ‘ve | 80‘9r cr0 8 | CE 
Le — [—|—|—-|-|—-|x 88 [768 v|SG'T9 [er GG 190 ‘6% | r'er | 6° 96 | 62°08 | €9 ‘#2 | LF‘8T ce cr |8SY 9 | 8 
= L IXIXITIXICIXIX] Se esse lo 6v (er vr |La'ée | 96've | Gr'oc | vo ‘ve | 9‘ 67 |e1‘vr | 78 ‘6 606% | Se 
= — OIXIXIXIX|XIX IX | 22 |rs6‘elro se |1z're [1708 | 1992 | 18‘zz 6+| a Sr] Er] 9°Z |r08‘€ | cc 
= TO [XX [XX IX |X IX) 02 [997 als 1e l8c'sc (sr ce |66 ‘re lcs‘gr |rz' gr oc'cr|rr'6 |gc'g [ev1'g | oc 
— OIXIXIX[X|X|X IX] 8, |866 Fr 1676 | 6‘ec [96‘oc | 18271 gr |eL er |8r or |£9‘z |[60'‘c lesc'z | 81 
= — OIXIX [XX IX |X IX! 97 1826 F|rr 08 | 187 (80° 97 | 20‘ #7 | 90°3r | GO‘ 07 | #0°‘8 09 [20 Y |FI0 c | 91 
= T'IXIXIXIXIX|X|X]| Yr 807 F6 cr 18 er te cr |LL'07|ec'6 |69'2 |[97°9 |29'7 |80'e |6eS‘r | #1 
_ — [XIXIXIX IX IX |X | 3r |888 011€" Fr (8707 |co‘6e |c6°z |621‘9 |ça'‘a lac'r |6c'e |9c'a rer‘ | 21 
= 'IXIXIXIX|X|X|X} OF LOGS L Loz geo | Ge |rL'y |go‘e |vr'e [9g‘e |26‘y |G82‘o | or 
= OI |—-|—-IX|—| 6 |667 019‘9 [22° l6o's |cv'r [cs‘e [8r'e |#c'e |16°+ |zc‘r ([99‘0 | 6 
X X [—|—{—|—|—|X|—| 8 |cée'olkgos fec'v [cor |cc'e |co‘e |rc‘a |ro‘a |rc‘r |10‘r |goc‘o | 8 
X X [—|—|—|—|-|X  4 |co'‘olss'e |97'e leo'e |oo'a |re‘e [c6‘r |vc'‘r |[ar‘r |z2‘o |g8e‘o | L 
X X |—|—|—|—|—|X|—| 9 |ccc ofeg'a (ss'e gcc [ser | L‘r [avr |er‘r |cs‘o |1c‘o |g8z‘o | 9 
_— X [——|—|—|—]—|—1s's |88rois'e (yr'a |6°r 199°r lev‘r |61°r |c6‘o |r2‘0 |8v‘o l8gz'o le‘c 
X X [TITI TITI! S [roy LV S'y |Le'r |8r'r |86‘0 |6L‘0 |65'0 |68‘o |967‘o | s 
OX Il |—IS % [Ser'ol6S'r (ev r ze‘r |vr‘r |G6‘o | 8‘o |#9‘o |8v‘o |ze‘o legr‘o le‘r 
X X [TT IT ) % [860 0/9 7 [ferry or |880 |9'0 |e9'o | S'o |8€'o |cz‘o [970 | 
L X [—|—|—|—|—|—]—1)5'€ [620 0196 0 1980 1z‘o |19‘o |8c'o |sz‘o |8£‘o [620 161‘0 |960‘0 lc'‘£ 
X X [—{—|—|—|—|—|—] € so 0 0 (#9'o l1S'o |67‘o [ego [ge‘o |8z'‘o |rz‘o [yr‘o |720‘0 | € 
as | 30 J>l>ls >> |s >| tv Es = 
or | va [an |L|s I LILILlI Es | 5 = = 
RE 5 |<|< 2l<ialTiz & O1 6 ù L 9 G y E re L 3 
ae T : mr 3 
5 * LES : 
| 5 B 5 

Jol9B,P SoSSerI) = 3 


SIM EUNEP | -pnuyo v SoguIWeI vousJaupe 
STI] Sop ane  oANJeUIC,P SOJIVE 9P HIQUOU NP UOTJOUOZ Us ‘eu ‘SHNDIIOPU} SUOTJ90S 


MIIETOUUMON À OSarIPq SoP HINCIOUAUON 


2U8SIS91 97n4 L J9 SOIIBUIPIO 91NJ}UWAL, D SIT, SOP 19 pneyo e soaultuel 


JOUSIHUPE 91NEU L 9INJUULIL,p S9IIUQ SOP 91NJU[OUOUION "9INJULUAIL,| 9p 2SSEW )9 onbriooy) uor)20S 
[ITA AX4NNV 




*SIN9119)X9 S[IJ SOP IVUIWIOU 1}QWPIP NP ofdii} NC PUUVdSH1109 o[{R9 NP [CUIWOU 91]QUPIP J'] ‘LION 


EH (492 G GE 
€0L‘0 8060 y A’ 
LGE‘ 0 60G‘0 € 5 
922 ‘0 yGc'0 c'e G°L 
AL 0 92 0 a * : 9 
660'0 LG‘ 0 c°T c‘y 
u } RE Re so ‘o[QpO NP UO1J20S uuI ‘SAN91197X0 SIIF SP 21JQWv1Œ uWU ‘2[{r9 NP IBUIWOU 217981 


=" qq 


L-M 9SSEI9 9p S2pPSI0] S9inJeuIIE p S2]qR2 SP 91N)P[DUAWION 
XI TXINNV 




9°0? co'£ r ‘98 L99 &'9} 6G6 c90 6} LG L'CL £T c'e GGF 007 07 
ÿ'L 69° 6° 67 LEE £'ar CLY 080 Z G°9€ G‘9r &' O1 ‘9 GET 00€ 0€ 
09'8 La T 9"8c LGE er‘ 6 GG 0GG & VLA 9° 0€ L'8 g'G (012 06G 44 
v6 L c'e z'8t GGT 1£'8 £0c 0£0 & L'at 6°88 9'8 SG (112 00 e0G 
C6 9 L0'T L'ec (42 88 8 y8} 08} IG 8° 92 v'8 c'S 007 00 0c 
9y7°‘y L'T G'Y] 9'8ç 16°9 607 CLS 6'GF z'0c 8'L G 18 09F 9F 
ae | pe Lu ee, | ee | [our] eus |! pre] Nu 


UUI ‘SUOISUYUII( 


Sa[1jOid suie)199 op sonbrist1930e81e87 


| "09 ‘66 ‘os ‘Gr ‘Or ‘9€ ‘EE 
‘e06 ‘O8 ele ‘Le ‘ue ‘ve ‘vec ‘Ce ‘OZ “O8 ‘ut ‘8Y ‘OF ‘VE ‘SE ‘OV : SolIJoid sep soxæunn 


+ GL-6608 LSO9D UO[SS S9[[917n04 


mens + 


X AXAINNV 




GL'Z ET'e | v'eL 59 L'GT 191 | 0ccS} €'sy G°r9 | c'er 8 | S+r | 00 0Y 
(AA v8 a | 9‘£y LCE a’ LS£ 08 8°I£ G‘07 hr | G'9 00 | O0E 0€ 
cy'e 9° | 9°J€ 808 €L'6 cye 006 & ve 9°0€ OF | 9°c 06 072 ve 

8c'c c'e | c'yc GET Gr'8 LT 029 F 8°GI «Ge L'6 |2'S 08 008 0 

L0‘& ca | S'‘02 CF L0'8 GT OCG I y 8} y'£c 6 |S'S 9L 008 0G 

8°} L8"y | 8'€r | £'e9 cy'9 y'€6 LYyL CV} l°8r VA: G 9 097 97 
td 1 

l D Q y 

OU LR louo tie | moe |ouo #4 | moe | 3% ssselg | “ado |— + 1 | so v 


uIU ‘SUOfSUAUI(I 


S9[1Jo1d sure)199 9p Sonbt}S11939810) ‘ 




 . O7 “9€ ‘RE “0€ 
e7C VC CC Ce re0c ‘OC ‘e8l ‘81 ‘e9l ‘OL ‘epl ‘PE ‘CE ‘OI ‘8 ‘GG ‘G : so[1Jo1d sep sorswunn 


GL-0ÿc8 LSO9 uo[es NA usa sa[rjo1q 




IX AXINNV 




6‘ y LSS & VAE GGHIF]  GU'L 9002 PEL 6 L'GF ya GG X UGS 
£6 € d12 aL'L 096 c'9 L8c L'S +‘ 09 G'9z 8r 08 X 008 
gc'£ 07G ÿO'L €60 & 66° LIST 68°% T'££ c'Cy 9} GI X08F 
9F'€ Ey c'9 99 6‘? 9Y0T Ly'‘Y y £'ey | 97 ÿr X 091 
9L°2 gyc €v'G LGG 1£‘Y t09 6'€ ‘cz G'z€ ÿt GI X OI 
Ly'C 6} 78 y YLG Gg'€ 09€ cy'€ ‘61 £'ye y} OFXGGE 
96°F p'yL yS'e y8c GU'E 61] €g't Fc & GI c} OX 00} 
LS'Y £'o€ 80'£ 97} yy'e y'eL La‘ G9°6 ‘cr 6 8X08 
2 8°Yc 18" |6'Y6 8e | S'66 Gr'c c0‘6 G°Yr 6 8XGL 
8£°} G'Gr L'& | 9°6c GT'e 9°LE ÿ6'} 6£°9 cr'8 8 9X0L 
Ye} a 1’ eva |6'cy 6‘} F'LC 8L‘y L'G 8c'L L 9XE9 
860 |£c9'? 6 + | 8'LT €c'r A 2’ 4/2’ LL'E 8'y G'G GX0G 
EE — 
wo A, | jo Ap | wo «0%, Qu y | wo wo “r u p q 
_— _ L SO tes 


WU ‘SUOISUYUI( 
SoXU Xne J1oddui Jed Sonbrs1199980109 




(3L-G068 LSO9 np 11v49X9) soeño sa[ie v soigru107 
IIX IXANNV 


0S'E SL | 8ç°Y €eer| c0'8 7607 | 6°67 9°e9 69°€ A2: 87 | 97 097 | OGC | 9F*<X09F*X 062 


EL'T Lee | c'e GG | 79 | 087] v‘#e 6‘ F6‘2 99 PT | Yr | Sr | 00 |7rXGzrX008 
81‘ vtr | cg‘ 6€c | Fr'G | Y81 | 9'‘ex 0€ 9€°z ce's €r | + | 007 | 097 |zrX00FX097 
yL'‘r | £'66 | 92‘2 007 | 86 € | are | cg'er L‘61 26°} vr'Y FF | O7 | 08 | Scr | OF XO8XG2 
L£'T | 8'OZ | SL°T GE |67'€ | £yrr L°8 V'Yr 9ÿ'°T 8t € OF | L €9 | 007] ZX£9X007 
act] L'er | 8ç'r | z‘re | 88‘ | 9‘04 L'9 c'e 8°} G6‘7 6 | 9 9G | 06 9X 96 X06 
80°r [888 |O07'r | 8‘#r | GS | 6 | 26‘S GG°L LY'T co‘z 8 | 9 06 | 08 9X06X08 
80‘r 1878 |cv'r| 9'vr | 8e‘e | 607 | 69'c Gc'L Fa‘ vv'e 8 | 9 06 | cz 9X0SXGL 
86 0 #2" G |24c 7 1G0'6 |£sz'a | 81e | 6‘? 66°G GO‘F 88e |S'L | S d OL GXGyXOL 
a8‘o |eL'e |cr'r |92'‘9 | 6‘6r | 76‘€ 86‘? G6‘0 80tz L IS 6 €9 GX07XE9 
8L‘O |6r"e |co'‘r|0L‘e |gL‘r|%"rr | y8‘2 8ç°£ 80 81 9 | g€ | 96 yX9E X 96 
a : “hi, me e . 0x of y p Qq g 

— | — |} 202 PE | nn 


W9 ‘9J1APIT 0P | 
21JU99 Np 99UPSIQ uIU SUOISUPUI(T 


SoXe Xnv 310ddvi Jed Sonbristi$19r1e9 


(ZL-01G8 LSO9 np 11e13X9) So[esoaut so[Ie vu Soiatu10o) 


IIIX AX4NNV 




ANNEXE XIV 


Détermination du coefficient q, pour la vérification au flambement 
-des poutres 


Pour les poutres de section symétrique en double T 
= Jy fh\2 
Lun 5: us (0 


où h est la hauteur de la poutre, /, la distance entre les points de fixa- 
tion de la membrure comprimée, J', et J,,, les moments d'inertie de 
la section, 1, un coeïfficient qu'on trouve dans le tableau ci-après 
en fonction du paramètre «@. 

Pour les poutres laminées en double T (poutrelles) on a 


QG — 1,54 DE 


OÙ J'tors est le moment d'inertie à la torsion, voir Annexe X. 
Pour les poutres en double T formées de trois tôles soudées on a 


a=8(%) (1+2%e) : 


où = est la hauteur totale de la section de la poutre, b et 6, la largeur 
et l'épaisseur de la membrure, Ô l’épaisseur de l’âme. 


Coefficients 4 pour les poutres en double T en acier de classe C38/23 


Coefficients 14 


Poutre sans fixations en travée ; HSE 
ee SÉÉSR RS 
œ charge concentrée Fe tie ment Hasgsve 
appliquée à appliquée à | appliquée à | appliquée à EME 
a membrure la  membrure la membrure la membrure 3 SE ES 29 & 
supérieure inférieure supérieure inférieure ROSE TRS 
0,4 1,77 5,03 4,60 3,85 2,20 
| 4,85 5,11 1,67 3,90 2,27 
8 2,63 5,94 2,35 4,59 2,90 +» 
24 4,03 7,31 3,99 5,79 4,00 
48 5,60 8,88 4,90 7,13 0,23 
80 7,31 40,59 6,30 8,58 6,51 
160 10,59 13,83 9,04 11,30 8,95 
240 13,21 16,36 11,21 13,48 10,86 
400 17,24 20,48 14,57 16,80 13,91. 


24—0948 369 


Si la valeur de D calculée selon la formule (1) est supérieure à 0,85, 
on la prend égale à ®;, conformément au tableau suivant : 


0,85 | 0,90 11 1,2 




0,95 | 1 


1,3 14 1,58 


Pp | 0,85 | 0,87 | 0,89 | 0,904 


0,927 | 0,948 | 0,964 | 0,98 | 1,0 


ANNEXE XV 


Détermination du coefficient og‘ pour la vérification des pièces d’a- 
cier comprimées et fléchies au flambement dans le plan du moment 


1-4 L: me; M, =, 


où À — L/r est l'élancement de la pièce; À, l’élancement fictif; À, 
la résistance de calcul de l’acier ; Æ, le module d'élasticité de l'acier; 
e — MIN, l'excentricité de la force; F, la section de la pièce; W, 
le module de résistance de la section (pour la fibre la plus comprimée); 
n, le coefficient d'influence de la forme de section (pour les pièces 
à âme pleine); mn, l’excentricité relative. 


Valeurs de n 


Type de la section pour 0S1< 5 pour À >5 


0,1<m<515<m<2010,1 << mL 0,2 


175 à | 15 à 
0,43X | 0,087 1,1 




&0‘0 co‘0 #0 0 #0 0 70‘0 700 GO‘0 GO‘ 0 C0‘ 0 0‘Y} 
£o‘0 #0 ‘0 90 ‘0 L0‘0 L0‘0 L0‘0 60° 0 60°0 07‘0 0‘07 
70 ‘0 10‘0 }r‘0 Gr‘ 0 8r'‘0 08‘0 €z 0 8z' 0 G£‘0 0°‘G 
70‘ 0 80‘0 Pr 0 (dt) Gz'0 0€‘0 9£ ‘0 9ÿ'0 79° 0 0'‘£ 
70‘ 0 60‘0 97‘ 0 cz 0 6c' 0 G£‘0 cy' 0 9G‘0 LL‘O 0‘ 
G0‘0 60° 0 90 Yc 0 €c‘0 6£°0 8z 0 #9°0 180 0‘T 
G0‘0 60°0 LE'0 Gz Q ££‘O 07'‘0 0G‘0 190 16‘0 G‘0 
2 ——— — 
n‘0S | 0‘0} | o‘c | 0‘E 0‘c + | 0‘F | c‘0 | Lr‘0 . 


WU YP UOIJOUOJ U2 ]J90 YP SMOIEA 
—_—_—_—_—_—_—_—_————— ————  …—————— 
SI[[T913 uo owe e Sooaid 591 anod j9D SJU919117909 


€0‘0 #0‘ 0 #0‘ 0 70‘ 0 #0‘ 0 70‘ 0 F0‘ 0 #0‘ 0 GO‘ 0 C0‘0 G0‘0 G0‘0 0'‘YI 
£o'0 G0‘0 c0‘0 90‘0 90 ‘0 L0‘0 L0‘0 800 80‘ 0 60°0 60‘0 0T‘0 0‘0T 
ÿ0'0 900 10°0 800 80'‘0 60°0 0F‘0 [A 2) At €r‘0 ÿr 0 GF‘0 0‘8 
GO‘ 0 80‘ 0 60‘0 0F‘0 pr'0 €F'0 #1 0 Lr'0 8r‘0 02'0 cc 0 92°0 0‘9 
C0‘ 0 60°0 OF 0 At €r 0 GF'0 Ly'0 02'°0 ca 0 GO 6&°0 G£‘0 0‘G 
90‘0 OF‘0 cr'0 ÿ1'0 9F'0 8r'‘0 Fz‘0 92‘0 6 0 €£‘0 6£ ‘0 0S‘0 0‘Y 
90‘0 Fr'U €r'0 LY'0 6+'0 ca 0 92‘0 tE‘0 9£‘0 cy‘0 &g'0 L9'0 0'£ 
90‘0 gr 0 cF'0 6+‘0 Adi 92‘0 € 0 07‘0 97° 0 ÿG‘0 G9‘0 18‘0 0'‘Z 
LO‘0 £r'0 970 08 ‘0 ÿc 0 8c 0 G£'O #ÿ7'0 GO 6G‘0 &L‘0 L8‘0 G‘T 
L0‘0 AA Ly'0 cc 0 90 1€ ‘0 8£'0 87'0 9G‘0 G9‘0 8L'‘0 &6 0 0'‘F 
L0°‘0 GF'0 8r'0 ÿt 0 82‘ 0 yCc'0 '0 ÿG'0 29'0 &L'0 cg'0 16‘0 G‘0 


0° 08 | 0‘07 | 0°8 | 0'9 | ( | (1 


Tw 9P UOIJOUOJ Ua 19Ÿ YP SINd2ILA 


——_—_—_—_—_—_—_—_— ————————— 
auroqd owue ve sa9g1d soj anod 390 SJu91917[909 






ANNEXE XVI 


Détermination du coefficient c pour la vérification des pièces d'acier 
comprimées et fléchies au flambement dans le plan perpendiculaire à 
celui du moment 


Pour les pièces en acier de classe C 38/23, pour À, << 100, on a 




Ce rase 
+ am, 


Dans cette formule #», est l’excentricité relative dans le plan du 
moment, 

Mx F 
TN W: 


où .1/, est le moment maximal dans le tiers moyen de la pièce qui 
est fixée à ses extrémités (il n’est jamais inférieur à la moitié de 
Mmas pour la pièce tout entière), V, le moment d'encastrement pour 
une pièce console; F, la section de la pièce; W, le module de ré- 
sistance de la section (pour la face la plus comprimée). 


Valeurs du coefficient « 


Type de la section 


e=M/N À p=M/N 
Excentricité | - | 
relative y Y— 1. ——. — y 


mx <1 0,7” 0,6 
1<m,<5 0,7+0,05 (m;—1) 0,6-1-0,05 (mx — 
mx > 9 0,9 0,8 


£90°0 £90‘0 €9G‘0— LEy'‘0 €90‘0— GT 0 — 9600 
K, g 4 
‘ (4) j (1) (f 
GLE'O— G29°0 GG9 0 — GL£‘O GGE 0 L0‘0 10‘0 HT 
29 HD do Vo dy SW [W 
indde ms 991U49 9p Se) 
JUHIUON 
siurouei} S)IOJJA 299481} UO SJUNUON 


S99AU1) XN9P E Sa1}n04 


1(d9+)=0 ‘a (dd+3v)= 
Sa[eS9 So3AUI} e Sonulju09 so13nod s2p [n2]29 9p S2[qUL 


ITIAX AXAINNV 




cgo‘o | £go‘o |zr#‘o—| gec'‘o |219‘o—|£8€"o |€£go0‘o—|Lrr 0— 
Go‘o | go‘o | g'‘o—| g‘o | so‘o—| co‘o— | So‘o—| So‘o—-|620'0 |S20'0— mm” 


Gy'O—| çcc'o 0 n | gG‘o—| Gz'0 G0‘0—| Go‘o--| S0o‘0—|+07‘0 


v‘o—| g9‘'o | g'o—| çg'‘o | 9‘o—| %‘0 v‘o—| 1‘o—|szo‘o | 80‘0 OT ANNE 


A  —  —_—_—_—_—_—_—]_—]_—…”…"”"—"—"—’…"—"”…"—"”"—" _—"—…—…—…—…—…"”"”—"—"—”—”"”—"—"—"—"—"—"—"—"—"”…>"—"—"—"—"—"—"—"—"—"—"—"—"—"—"—"—"—"———— 
d 1p0 30 1pÔ 40 Vo On | °W W 
a ———_—_— 99I10U9 vP SCI 


sindde 09A04) 
syuvuouva} S}I0JJ4 Ans SJUYUION U) SJUWON 


0 00 
S39ALI) SI013 E S91]n04 






150 0— | 020 0— | FFF O— | SE0'0— TN 
1G0‘0— | #50‘0— | 2c0‘0— | 6r+°0— 

€c0‘0— | 0ÿ0‘0— | 0%0‘0— | 80°0— | 070‘0— | 6L0°0 920 ‘0— 

€G0‘0— | 0Y0‘0— | 070‘0— | £S0‘0— | 980°0 9ÿ0‘0— | 00F'0 

GOF 0— | 6L0‘0— | 6L0‘0— | Or 0— | 950°0 €£0‘0 8L0'‘0 

Ty Cyy 9 y Ty CS 24 SW TM 


sindde 4ns SJuowuon 


291649 9p SP9 


09ACI19 U) SJUOUON 


(ssuouour sop [no[e9 8[ anod s)u919117909) 
So94v1) bur9 u s91)n0q4 


ANNEXE XVIII 


Pressions de calcul conventionnelles À, sur les sols de fondation 


Type du sol Ro, kgf/cm? 




Détritique à gros morceaux 


En pierres cassées mêlées au sable 6 
Graveleux, roches cristallines 5 
Idem, roches sédimentaires 3 


Forte densité | Hôvenre 


Sablonneux 


Gros sables, humidité quelconque 
Sables moyens, humidité quelconque 
Sables fins, peu humides 

Idem, humides et imbibés d'eau 
Sables poussiéreux, peu humides 
Idem, humides 

Idem, imbibés d’eau 


2 NN © CO EE O1 © 
= 2 ND ND © & 




Consistance O0|Consistance 1 


Argileux (non compressibles) 


Limons sableux, porosité 0,5 3 3 
Idem, porosité 0,7 2,5 2 
Limons argileux, porosité 0,5 3 2,5 
Idem, porosité 0,7 ''.— . 2,5 1,8 
Idem, porosité 1,0 2 1 
‘Argiles, porosité 0,5 6 4 
Idem, porosité 0,6 5] 3 
Idem, porosité 0,8 3 2 
Idem, porosité 1,1 2,9 1 




ANNEXE XIX 


Réaction d'appui dans des poteaux à bord encastré des portiques 
transversaux des bâtiments industriels sans étages 


Poteau simple 


Poteau double 


Pour un simple poteau k, —0 


Système de la 


Système de la 


Charge Réaction d'appui Charge Réaction d'appui 
Da = "nr | gp 3Mn mn 
B(+k+k) 21(1+—k+k:) 


_ SM (+kja) ie T (1—a+k:) 
PITENES AI (+k+k:) 


__ 3 SM (1— a?) ) 
AA +k+H) 


P B = 
8pl [{+ak+ 
___ +1,33: (1+a) ki] 
8 (1+k+k1) 




ANNEXE XX 
Tables de calcul des dalles appuyées sur les quatre côtés 


Schémas des dalles 


DR Bord encas tré 


SES Bord articulé 
CCC Bora libre 


: Ha 2 


_ Bi) 
Mans gs Pa 


des efforts qui proviennent des charges 


Les efforts provenant de La charge 
trapézoidale sont obtenus en faisant la somme 
uniformément répartie et triangulaire 


Charge uniformément répartie 
Cas I Cas II Cas III Cas IV 


a/b | B5 


b/a = _— 
le , = 0 — pl 2 
Y5 B6 | Vs | —B3 L- Bs | V5 |-B31-v2|-v1|i-Vve| 85 | Vs | _B3 | -v 


0,5 [17/96/0,5| 3141] 56 | 84 
0,6 [2418210,6| 61381 56 | 81 
0,7 |30/6810,7| 9135] 56 | 77 
0,8 |33156|10,8|12|31| 56 | 72 
0,9 |3614610,9/15127| 55 | 66 
1,0 |37/3711,0/17]23| 54 | 60 




90 | 34 | 27 | 71 | 4140| 56 | 82 
17] 53 | 42 | 33 | 80 | 8137| 56 | 78 
211 54 | 49 | 38 | 84 |12132| 56 | 72 
241 55 | 56 | 41 | 85 |14127] 55 | 65 
96 | 62 | 43 | 85 116122] 53 | 58 
28| 56 | 66 | 44 | 85 [18118] 51 | 51 


©) O1 OO © 10 Où à NN 
[ep] 


1,2 32 | 56 | 73 | 44 | 85 
1,5 36| 56 | 79 | 45 | 85 
2,0 401 56 | 83 | 45 | 84 





LT — ca | 81 | £€ 6 01 6 6 0'F 
9€ — £e LY 8€ v} OF ÿ} L g'0 
97— 6€ y} €Yy 0C 6 87 y 9'0 
0G— 77 12 cy GG 6 0c G G'0 

L-9A xvm | 54a— Tg— | cg— IE-FA xewu |£-Fd xewm | A 9ÿ q/v DA — TA SA — eg JA sd 
a — —_—_— v/q 
AI SU9 JII SUD 


6&— 62 ve 12, OF } 6 8r ce 8} 8} 0‘? 
LE— G£ 8€ Gy 6 G} L 8c €c 88 LV 8'0 
9ÿ— 07 y 07 6 6} € y 44 Fy 4! 9°0 
0G— F7 Gy (TA 6 06 ré yG T4 0G 6 G‘0 
ER  — 
L-94 xewu GA cg— CFA xewu €-Fg xewu SA 9g CFA xeu €-Tg xewu 4 qd 
II SU) I SE) 


9118[NSuvr1] 95109 
XX 2Ta2uuF,1 9P 9110S 


TABLE DES MATIÈRES 


Préface 9 ee ee ee ee + + ee ee + ee ee C2 e ° e e e. e e. ° e. ° ° e 


Chapitre premier 
PRINCIPES DE CALCUL DES STRUCTURES ....,..... 


8 1.1. Etats-limites des structures . . . . . . . . . . . . . 
8 I.2. Coefficients forfaitaires . . . . . . . . . . . . . . . 
$ 1.3. Valeurs caractéristiques et de calcul des charges et des 

TÉSISTANCES sn 0 2 D ue Don 4 dd de dre te ds eh 
$ 1.4. Calcul des structures aux états-limites . . . . . . . . . 
8 I.5. Systèmes d’unités ............... .. 


Chapitre II 


NOTIONS SUR LE BÉTON ARMÉE . ee ee ee 0 ee ee ee ee ee ee ee «s 


& II.1. Principes du béton armé .............. 
SIl.2:- Delon en En SN ere SR Ro. 
STÉ9: Atmiatures 2 2 28 0m a rade de à pe core 
& II.4. Principales propriétés du béton armé. . . . . . . . . . 


Chapitre II 


PARTICULARITÉS DE CAMCUL ET DE CONCEPTION DES PIE- 
CES EN BÉTON ARMÉE . . . .. CE 
8 III.1. Généralités sur le caleu . . . . . . . . . . . . .. 

$ III.2. Particularités de calcul des pièces en béton précontraint 

II1.3. Généralités sur la conception de Ar ri ue A 


$ III.4. Particularités de conception; des pièces en béton précon- 
LED 5 Es ed he be sue . 


Chapitre IV 


PIÈCES EN BÉTON ARMÉ -GHARGÉES EN COMPRESSION SIMPLE 
$ IV.1. Dispositions constructives , . .« . 
& IV.2. Calcul des pièces présentant une excentricité accidentelle 


Chapitre V 


PIÈCES EN BÉTON ARMÉ CHARGÉES EN TRACTION SIMPLE 
$ V.1. Dispositions constructives ........... D 
$ V.2. Etat de contrainte et calcul d’une pièce tendue . . 
$8 V.3. Particularités du comportement et calcul d’une pièce en bé- 
ton: -PrécontraAint 5: 4 26e 6-40 nie NO Lis DR ar nt 




Chapitre VI 
PIÈCES EN BÉTON ARMÉ CHARGÉES EN FLEXION SIMPLE 


& VI.{. Dispositions constructives . .. . . . . . . . . . . 

& VI.2. Etat de contrainte et de déformation d’une pièce chargée 
en flexion simple . . . . . . . . . . . . . . . . . . 

VI.3. Calcul de résistance suivant les sections normales 

VI.4. Calcul de résistance suivant les sections obliques 

VI.5. Calcul à la fissuration des pièces précontraintes . . . . 

VI.6. Calcul des flèches ................. 

& VI.7. Calcul de l'ouverture des fissures . . . . . . . . .. 




Chapitre VII 
PIÈCES EN BÉTON ARMÉE CHARGÉES EN FLEXION COMPOSÉE 


$ VII.1. Dispositions constructives des pièces chargées en flexion- 
COMPTESSION à 4 ne He ne à + 6e à 0 à à à 

& VII.2. Calcul d’une pièce chargée en flexion-compression 

$ VII.3. Pièces chargées ‘en flexion avec traction . . . . . . . 


Chapitre VIII 


STRUCTURES EN MAÇONNERIE . ...... MODES re 
$ VIII.1. Matériaux utilisés en maçonnerie, leur résistance et 
défofMaAtiOn 5 2 à 2-0 ere. à die à 4 Lie sm 

& VIII.2. Calcul des pièces comprimées . .. . .. . . . . .. 

$ VIII.3. Maçonnerie armée . . . . . . . . . . . . . . . 


$ VIII.4. Les structures en maçonnerie dans le bâtiment 
$ VIII.5. Exemples de calcul des pièces en maçonnerie 


Chapitre IX 
STRUCTURES MÉTALLIQUES _...... 


$ IX.1. Matériaux des structures métalliques . . . . . . . . 
2. Assemblage des pièces dans la structure métallique . . 
X.3. Conception et calcul des poutres . . . . . . . . . . . 
X.4. Conception et calcul des poteaux .... . . . . . .. 
X.5. Conception et principes de calcul des fermes . . . . . 
X.6. Structures métalliques précontraintes ,. . . . . . . . 


Chapitre X 
LES STRUCTURES DANS LES BÂTIMENTS . .. se. 


$ X.1. Principes de conception des structures du Bâtiment . . . 
$ X.2. Planchers en béton armé ............,.. 
$& X.3. Fondations de poteaux en béton armé . . . . . . . . 
$ X.4. Bâtiments industriels sans étages composés de structures 

préfabriquées en béton armé . . . . . . . . . . . . . 
$& X.5. Bâtiments des réseaux de distribution et d'évacuation des 

eaux et bâtiments des chaudières ,. . . . . . . . . : 


Chapitre XI 


OUVRAGES SPÉCIAUX DANS LES RÉSEAUX DE DISTRIBUTION 
ET D'ÉVACUATION DES EAUX . e. 0 ee + 0 ee ee ee 8 ee 0e © ee oe 


8 XI.1. Généralités ..... .......... — 
$& XI.2. Conception des réservoirs cylindriques en béton armé 








CON CAN ANS CON AN 
DAPDE 




$ XI. 


Chapi 


Calcul des réservoirs cylindriques  . . . . . . . . . 
Conception des réservoirs rectangulaires en béton armé 
Calcul des réservoirs rectangulaires . . . . . . . .. 
Conception et calcul des réservoirs cylindriques en acier 
Tuyaux et puits en béton armé utilisés dans les réseaux 
de distribution et d'évacuation des eaux 
Conception et calcul des châteaux d’eau 


tre XII 


QUELQUES EXEMPLES DE PROJETS DE STRUCTURES EN 


BÉTON ARMÉ e e [] (] ° ° ° e e ° e 
. Généralités 
. Panneau de toiture nervuré sans précontrainte 
. Panneau de toiture nervuré précontraint 
. Panneau de toiture carré 
. Poutre de toiture 
. Poteau et semelle 


Chapi 


tre XIII 


OUVRAGES DES SYSTÈMES DE TRANSPORT DE LA CHALEUR 


XIII.5. Pose aérienne des conduites de chaleur 


s GÉNÉTANLES . 2 ds LU L ES LS SE dE 
. Conception des galeries et des collecteurs . . . . . . 
. Conception des chambres, niches, appuis des conduites 

dé-Chaleur LS A sn dE St ra re 
. Conduites de chaleur posées en tranchée 


. Principes de calcul des structures relatives aux conduites 
de chaleur 


À NOS LECTEURS 


Les Editions Mir vous seraient très reconnais- 
santes de bien vouloir leur communiquer votre opinion 
sur le contenu de ce livre, sa traduction et sa présen- 
tation ainsi que toute autre suggestion. 

Ecrire à l’adresse : Pervi Rijski péréoulok, 2, 
Moscou, 1I-110, GSP, U.R.S.S. 


META CA DE MEDIOS C( 
ESTRUCTURES E INGEù 


Imprimé en UNION SOVIÉTIQUE 


HYDRAULIQUE 


par N. KRÉMENETSKI, D. SCHTÉRENLIHT, 
V. ALYCHEV, L. YAKOVLEVA 


Le manuel soumet à l'étude les propriétés principales des liqui- 
des, les questions relatives à l’hydrostatique, la cinématique du 
liquide, les questions fondamentales de l’hydrodynamique, l'équa- 
tion de Bernoulli pour un liquide non visqueux et visqueux, la 
résistance hydraulique sous des régimes laminaire et turbulent, 
l'écoulement à partir des trous, ajutages, tubes courts et 
vannes. 

On y trouve l'exposé des questions sur le mouvement uniforme 
et non permanent (coup de bélier) dans les conduites, du mou- 
vement uniforme et non permanent de l'eau dans des lits ou- 
verts : calcul des canaux et des courbes de la surface libre dans 
des lits prismatiques. 

Il contient également la description des travaux de laboratoire 
essentiels, des problèmes et des tables nécessaires pour la réali- 
sation des calculs.