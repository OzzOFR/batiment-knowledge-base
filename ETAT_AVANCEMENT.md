# État d'avancement — Base de connaissances bâtiment
## Date : 2 août 2026

## Infrastructure
- **VPS** : 213.32.71.18 (Hozzo LaForge)
- **PostgreSQL** : container `forge-postgres`, IP interne 172.20.0.6:5432
- **Credentials** : user=createk, password=Forge2026Hozzo!, db=batiment_knowledge
- **MCP container** : `batiment-mcp`, port 8100
- **URL publique** : https://knowledge.ozzo.fr
- **OAuth** : login=ozzo, password=Batiment2026!
- **Token service** : t-63pCvruQiQGxX8d3qQnqjVB-RwT7FEQth0jmFBrj8
- **GitHub** : OzzOFR/batiment-knowledge-base

## Base de données (PostgreSQL VPS)
- **Total chunks** : ~10 808
- **Auteurs** : 27 uniques
- **Modèle embedding** : paraphrase-multilingual-mpnet-base-v2 (768 dims)
- **Chunking** : sémantique par section logique

### Tables
- `batiment_chunks` : chunks vectorisés (id, content, embedding, corps_etat, source, auteur, titre_ouvrage, annee_publication, fiabilite, figure_ids)
- `batiment_figures` : 35 figures SVG générées (id, titre, description, corps_etat, categorie, url_svg, url_png, mots_cles, source)
- `batiment_figures_gallica` : 322 références figures Gallica avec URLs (id, chunk_id, vol_num, figure_num, legende, url_gallica, url_image, ark, gallica_page, note_precision)

## Version MCP : 7.3.0
### Outils disponibles
- `search_batiment` : recherche sémantique avec scoring pondéré
- `ask_batiment` : réponse synthétisée par LLM avec sources
- `list_sources` : liste des auteurs indexés
- `get_figure` : récupérer une figure SVG par ID

### À faire dans le MCP
- Ajouter les références Gallica dans les résultats de search_batiment
  (quand un chunk a des figures dans batiment_figures_gallica, afficher les URLs)

## Lacunes résolues
1. ✅ Hiérarchie de confiance (scoring pondéré fiabilité × récence)
2. ✅ Chunking sémantique (découpage par section logique)
3. ✅ Figures SVG (7 figures générées + catalogue 35)
4. ✅ Figures Gallica (322 références avec URLs estimées ±3 pages)
5. ✅ Fiches OzzO marquées "synthèse IA"
6. ✅ 15 volumes Champly complets indexés (1227 chunks sémantiques)
7. ✅ Migration Supabase → VPS PostgreSQL
8. ✅ Claude.ai connecté via OAuth 2.1

## Lacunes en attente
- Pathologies (fissures, humidité, corrosion) → accès CSTB/AQC requis
- Normes/DTU → accès CSTB requis

## ARKs Gallica Champly
- Vol.1 Arpentage : bpt6k9774323q
- Vol.2 Maçonnerie : bpt6k97743229
- Vol.3 Béton armé : bpt6k9774321w
- Vol.4 Charpente bois : bpt6k97744269
- Vol.5 Charpentes métalliques : bpt6k97744284
- Vol.6 Couvertures : bpt6k9774427q
- Vol.7 Menuiserie : bpt6k65806792
- Vol.8 Serrurerie : bpt6k6580680q
- Vol.9 Pavages/Peintures : bpt6k65806814
- Vol.10 Vitrerie/Chauffage : bpt6k6580763j
- Vol.11 Plomberie/Chauffage : bpt6k6580764z
- Vol.12 Plomberie/Eau : bpt6k6580765c
- Vol.13 Salubrité : bpt6k65807550
- Vol.14 Escaliers/Ascenseurs : bpt6k6580756d
- Vol.15 Architecture/Plans : bpt6k6580757t

## Tunnel SSH
```bash
ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519_vps -N -L 5433:172.20.0.6:5432 ubuntu@213.32.71.18 &
```
