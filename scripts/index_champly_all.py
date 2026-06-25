#!/usr/bin/env python3
"""
Script d'indexation de tous les volumes Champly dans Supabase.
Vérifie les chunks déjà présents pour éviter les doublons.
"""
import os
import json
import requests
import re
import time

# Configuration
CORPUS_DIR = "/home/ubuntu/batiment-knowledge-base/corpus/champly"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

# Vérifier que les clés sont présentes
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


def get_existing_sources():
    """Récupère les sources déjà indexées dans Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    params = {
        "select": "source",
        "limit": 10000
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            sources = set()
            for row in data:
                if row.get('source'):
                    sources.add(row['source'])
            return sources
        else:
            print(f"Erreur récupération sources: {response.status_code}")
            return set()
    except Exception as e:
        print(f"Erreur: {e}")
        return set()


def get_embedding(text, retries=3):
    """Génère un embedding via OpenRouter (text-embedding-3-small)"""
    url = "https://openrouter.ai/api/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-embedding-3-small",
        "input": text[:8000]  # Limite de tokens
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
    # Nettoyage basique
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
    """Insère un chunk dans Supabase via l'API REST"""
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
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
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code not in (200, 201):
            print(f"  Erreur API Supabase: {response.status_code} - {response.text[:200]}")
        return response.status_code in (200, 201)
    except Exception as e:
        print(f"  Erreur insertion Supabase: {e}")
        return False


def main():
    print("=== Indexation des volumes Champly dans Supabase ===\n")
    
    # Récupérer les sources déjà indexées
    print("Récupération des sources déjà indexées...")
    existing_sources = get_existing_sources()
    print(f"Sources existantes: {len(existing_sources)}")
    
    total_chunks = 0
    total_skipped = 0
    
    for filename, meta in CHAMPLY_VOLUMES.items():
        file_path = os.path.join(CORPUS_DIR, filename)
        
        if not os.path.exists(file_path):
            print(f"\n[MANQUANT] {filename}")
            continue
        
        # Vérifier si déjà indexé
        source = meta["source"]
        if source in existing_sources:
            print(f"\n[DÉJÀ INDEXÉ] {filename}")
            total_skipped += 1
            continue
        
        print(f"\n[INDEXATION] {filename}")
        print(f"  Corps d'état: {meta['corps_etat']}")
        print(f"  Source: {source}")
        
        # Lire le fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Découper en chunks
        chunks = chunk_text(content)
        print(f"  -> {len(chunks)} chunks à indexer")
        
        # Indexer chaque chunk
        success_count = 0
        for i, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            if embedding:
                if insert_chunk(chunk, embedding, meta["corps_etat"], source, meta["titre"]):
                    success_count += 1
                    total_chunks += 1
                else:
                    print(f"  [{i+1}/{len(chunks)}] Échec insertion")
            else:
                print(f"  [{i+1}/{len(chunks)}] Échec embedding")
            
            # Pause légère pour éviter le rate limiting
            if (i + 1) % 10 == 0:
                time.sleep(0.5)
        
        print(f"  -> {success_count}/{len(chunks)} chunks indexés avec succès")
    
    print(f"\n=== Terminé ! ===")
    print(f"  Nouveaux chunks indexés: {total_chunks}")
    print(f"  Volumes déjà indexés (ignorés): {total_skipped}")


if __name__ == "__main__":
    main()
