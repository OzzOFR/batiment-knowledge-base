# Batiment Knowledge Base

Base de connaissances structurée sur les métiers du bâtiment, conçue pour être interrogée par une IA via le protocole MCP (Model Context Protocol).

## Architecture

```
batiment-knowledge-base/
├── corpus/                  # Textes structurés par corps d'état (Markdown)
│   ├── maconnerie/
│   ├── charpente-couverture/
│   ├── plomberie-chauffage/
│   ├── electricite/
│   ├── menuiserie/
│   ├── platrerie-peinture/
│   ├── isolation-etancheite/
│   ├── gros-oeuvre/
│   ├── gestion-chantier/
│   ├── normes-reglements/
│   └── pathologies/
├── sources/                 # Sources brutes téléchargées
│   ├── gallica/             # Ouvrages BNF libres de droits
│   ├── aqc/                 # Fiches AQC (Agence Qualité Construction)
│   └── capeb-ffb/           # Guides CAPEB et FFB
├── chunks/                  # Fragments découpés avec métadonnées (JSON)
├── scripts/                 # Pipeline Python (collecte, chunking, indexation)
├── mcp_server/              # Serveur MCP FastAPI
└── docs/                    # Documentation du projet
```

## Stack technique

| Composant | Outil |
|---|---|
| Stockage documents | Google Drive + GitHub |
| Base vectorielle | Supabase + pgvector |
| Embeddings | OpenAI text-embedding-3-small |
| Serveur MCP | FastAPI (Python) |
| Déploiement | Railway |
| LLM | GPT-4o / Mistral / Claude (au choix) |

## Sources indexées

- **Gallica (BNF)** : Nouvelle Encyclopédie Pratique du Bâtiment (René Champly, ~1920)
- **AQC** : Fiches pathologies et désordres courants
- **CAPEB / FFB** : Guides pratiques des fédérations professionnelles

## Outils MCP exposés

| Outil | Description |
|---|---|
| `search_batiment` | Recherche sémantique dans toute la base |
| `get_fiche_pathologie` | Retrouve les fiches AQC par symptôme |
| `get_norme` | Retrouve les règles de l'art et DTU applicables |
| `list_sources` | Liste toutes les sources indexées |

## Installation

```bash
pip install -r scripts/requirements.txt
cp .env.example .env  # Renseigner les clés API
python scripts/index_corpus.py  # Indexer le corpus
python mcp_server/main.py       # Lancer le serveur MCP
```
