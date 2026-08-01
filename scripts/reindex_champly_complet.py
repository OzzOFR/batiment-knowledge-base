#!/usr/bin/env python3
"""
Réindexation complète des 15 volumes Champly dans Supabase.
1. Supprime les anciens chunks Champly (incomplets)
2. Réindexe tous les volumes complets depuis le corpus
"""
import os
import requests
import re
import time

# Configuration
CORPUS_DIR = "/home/ubuntu/batiment-knowledge-base/corpus/champly"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

if not OPENROUTER_API_KEY:
    print("ERREUR: OPENROUTER_API_KEY non définie")
    exit(1)

# Mapping des volumes Champly avec leurs métadonnées
CHAMPLY_VOLUMES = {
    "champly_vol01_arpentage-fondations.md": {
        "corps_etat": "gros-oeuvre",
        "titre": "Champly Vol.1 - Arpentage, Nivellement, Terrassements, Fondations",
        "source": "Gallica BnF ark:/12148/bpt6k9774323q"
    },
    "champly_vol02_maconnerie-brique.md": {
        "corps_etat": "maconnerie",
        "titre": "Champly Vol.2 - Maçonnerie, Pierre, Brique, Mortiers",
        "source": "Gallica BnF ark:/12148/bpt6k97743229"
    },
    "champly_vol03_beton-arme.md": {
        "corps_etat": "gros-oeuvre",
        "titre": "Champly Vol.3 - Travaux en Ciment et Béton Armés",
        "source": "Gallica BnF ark:/12148/bpt6k9774321w"
    },
    "champly_vol04_charpente-bois.md": {
        "corps_etat": "charpente-couverture",
        "titre": "Champly Vol.4 - Charpentes en Bois et Échafaudages",
        "source": "Gallica BnF ark:/12148/bpt6k938852q"
    },
    "champly_vol05_charpentes-metalliques.md": {
        "corps_etat": "charpente-couverture",
        "titre": "Champly Vol.5 - Charpentes Métalliques",
        "source": "Gallica BnF ark:/12148/bpt6k97744284"
    },
    "champly_vol06_couvertures-toitures.md": {
        "corps_etat": "charpente-couverture",
        "titre": "Champly Vol.6 - Couvertures et Toitures",
        "source": "Gallica BnF ark:/12148/bpt6k9774427q"
    },
    "champly_vol07_menuiserie-parquets.md": {
        "corps_etat": "menuiserie",
        "titre": "Champly Vol.7 - Menuiserie et Parquets",
        "source": "Gallica BnF ark:/12148/bpt6k65806792"
    },
    "champly_vol08_serrurerie-fermetures.md": {
        "corps_etat": "menuiserie",
        "titre": "Champly Vol.8 - Serrurerie et Fermetures",
        "source": "Gallica BnF ark:/12148/bpt6k6580680q"
    },
    "champly_vol09_pavages-carrelages-peintures.md": {
        "corps_etat": "platrerie-peinture",
        "titre": "Champly Vol.9 - Pavages, Carrelages, Peintures",
        "source": "Gallica BnF ark:/12148/bpt6k65806814"
    },
    "champly_vol10_vitrerie-chauffage-ventilation.md": {
        "corps_etat": "plomberie-chauffage",
        "titre": "Champly Vol.10 - Vitrerie, Chauffage et Ventilation",
        "source": "Gallica BnF ark:/12148/bpt6k6580763j"
    },
    "champly_vol11_plomberie-chauffage.md": {
        "corps_etat": "plomberie-chauffage",
        "titre": "Champly Vol.11 - Plomberie et Chauffage",
        "source": "Gallica BnF ark:/12148/bpt6k6580764z"
    },
    "champly_vol12_plomberie-eau-assainissement.md": {
        "corps_etat": "plomberie-chauffage",
        "titre": "Champly Vol.12 - Plomberie, Eau et Assainissement",
        "source": "Gallica BnF ark:/12148/bpt6k6580765c"
    },
    "champly_vol13_salubrite-sonneries.md": {
        "corps_etat": "electricite",
        "titre": "Champly Vol.13 - Salubrité, Sonneries et Téléphonie",
        "source": "Gallica BnF ark:/12148/bpt6k65807550"
    },
    "champly_vol14_escaliers-ascenseurs.md": {
        "corps_etat": "menuiserie",
        "titre": "Champly Vol.14 - Escaliers et Ascenseurs",
        "source": "Gallica BnF ark:/12148/bpt6k6580756d"
    },
    "champly_vol15_architecture-plans.md": {
        "corps_etat": "encyclopedie-generale",
        "titre": "Champly Vol.15 - Architecture et Plans de Maisons",
        "source": "Gallica BnF ark:/12148/bpt6k6580757t"
    },
}

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
}


def delete_champly_chunks():
    """Supprime tous les chunks Champly existants dans Supabase"""
    print("Suppression des anciens chunks Champly...")
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    r = requests.delete(url, headers=HEADERS,
        params={"auteur": "eq.René Champly"})
    if r.status_code in (200, 204):
        print(f"  Suppression OK (status {r.status_code})")
    else:
        print(f"  Erreur suppression: {r.status_code} - {r.text[:300]}")
        # Essayer avec source like
        sources = [meta["source"] for meta in CHAMPLY_VOLUMES.values()]
        deleted = 0
        for source in sources:
            r2 = requests.delete(url, headers=HEADERS,
                params={"source": f"eq.{source}"})
            if r2.status_code in (200, 204):
                deleted += 1
        print(f"  Suppression par source: {deleted}/{len(sources)} OK")


def get_embedding(text, retries=3):
    """Génère un embedding via OpenRouter (text-embedding-3-small)"""
    url = "https://openrouter.ai/api/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-embedding-3-small",
        "input": text[:8000]
    }
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                return response.json()['data'][0]['embedding']
            elif response.status_code == 429:
                wait = 2 ** attempt
                print(f"  Rate limit, attente {wait}s...")
                time.sleep(wait)
            else:
                print(f"  Erreur API embedding: {response.status_code} - {response.text[:200]}")
                return None
        except Exception as e:
            print(f"  Erreur requête embedding: {e}")
            if attempt < retries - 1:
                time.sleep(2)
    return None


def chunk_text(text, max_chars=1500, overlap=200):
    """Découpe le texte en chunks avec chevauchement"""
    text = re.sub(r'\n{3,}', '\n\n', text)
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = start + max_chars
        if end < text_len:
            last_para = text.rfind('\n\n', start, end)
            if last_para != -1 and last_para > start + max_chars / 2:
                end = last_para + 2
            else:
                last_dot = text.rfind('. ', start, end)
                if last_dot != -1 and last_dot > start + max_chars / 2:
                    end = last_dot + 2
        chunk = text[start:end].strip()
        if len(chunk) > 100:
            chunks.append(chunk)
        start = end - overlap
    return chunks


def insert_chunk(chunk_content, embedding, corps_etat, source, titre):
    """Insère un chunk dans Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    data = {
        "content": chunk_content,
        "embedding": embedding,
        "corps_etat": corps_etat,
        "source": source,
        "titre_document": titre,
        "auteur": "René Champly",
        "date_document": "1910-1914",
        "type_contenu": "encyclopedie",
        "libre_droits": True
    }
    try:
        response = requests.post(url, headers=HEADERS, json=data, timeout=30)
        if response.status_code not in (200, 201):
            print(f"  Erreur Supabase: {response.status_code} - {response.text[:200]}")
        return response.status_code in (200, 201)
    except Exception as e:
        print(f"  Erreur insertion: {e}")
        return False


def main():
    print("=== Réindexation complète des 15 volumes Champly ===\n")

    # Étape 1: Supprimer les anciens chunks
    delete_champly_chunks()
    time.sleep(2)

    # Étape 2: Indexer tous les volumes
    total_chunks = 0
    total_errors = 0

    for filename, meta in CHAMPLY_VOLUMES.items():
        file_path = os.path.join(CORPUS_DIR, filename)
        if not os.path.exists(file_path):
            print(f"\n[MANQUANT] {filename}")
            continue

        print(f"\n[INDEXATION] {filename}")
        print(f"  Titre: {meta['titre']}")
        print(f"  Corps d'état: {meta['corps_etat']}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        file_size = len(content)
        chunks = chunk_text(content)
        print(f"  Taille: {file_size:,} chars -> {len(chunks)} chunks")

        success_count = 0
        for i, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            if embedding:
                if insert_chunk(chunk, embedding, meta["corps_etat"], meta["source"], meta["titre"]):
                    success_count += 1
                    total_chunks += 1
                else:
                    total_errors += 1
            else:
                print(f"  [{i+1}/{len(chunks)}] Échec embedding")
                total_errors += 1

            # Pause anti-rate-limit
            if (i + 1) % 10 == 0:
                time.sleep(0.5)
                print(f"  Progression: {i+1}/{len(chunks)} chunks...")

        print(f"  -> {success_count}/{len(chunks)} chunks indexés")

    print(f"\n=== TERMINÉ ===")
    print(f"  Total chunks indexés: {total_chunks}")
    print(f"  Erreurs: {total_errors}")


if __name__ == "__main__":
    main()
