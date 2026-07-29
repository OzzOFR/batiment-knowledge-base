#!/usr/bin/env python3
import os
import json
import requests
import re

# Configuration
CORPUS_DIR = "/home/ubuntu/batiment-knowledge-base/corpus"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

# Vérifier que les clés sont présentes
if not OPENROUTER_API_KEY:
    print("ERREUR: OPENROUTER_API_KEY non définie")
    exit(1)
if not SUPABASE_KEY:
    print("ERREUR: Clé Supabase non définie")
    exit(1)

def get_embedding(text):
    """Génère un embedding via OpenRouter (text-embedding-3-small)"""
    url = "https://openrouter.ai/api/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-embedding-3-small",
        "input": text
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['data'][0]['embedding']
        else:
            print(f"Erreur API: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Erreur requête: {e}")
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
        
        # Si on n'est pas à la fin, chercher un point ou un saut de ligne pour couper proprement
        if end < text_len:
            # Chercher le dernier double saut de ligne (paragraphe)
            last_para = text.rfind('\n\n', start, end)
            if last_para != -1 and last_para > start + max_chars/2:
                end = last_para + 2
            else:
                # Sinon chercher le dernier point
                last_dot = text.rfind('. ', start, end)
                if last_dot != -1 and last_dot > start + max_chars/2:
                    end = last_dot + 2
        
        chunk = text[start:end].strip()
        if len(chunk) > 100:  # Ignorer les micro-chunks
            chunks.append(chunk)
            
        start = end - overlap
        
    return chunks

def insert_chunk(chunk_text, embedding, corps_etat, source):
    """Insère un chunk dans Supabase via l'API REST"""
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    data = {
        "content": chunk_text,
        "embedding": embedding,
        "corps_etat": corps_etat,
        "source": source
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code not in (200, 201):
            print(f"Erreur API Supabase: {response.status_code} - {response.text}")
        return response.status_code in (200, 201)
    except Exception as e:
        print(f"Erreur insertion Supabase: {e}")
        return False

# Fichiers à indexer (les fiches synthétiques et les dossiers manquants)
files_to_index = [
    "isolation-etancheite/guide_technique_isolation-etancheite.md",
    "pathologies/guide_pathologies_batiment.md",
    "normes-reglements/guide_normes_reglements.md",
    "electricite/guide_technique_electricite.md",
    "electricite/installations-hydroel-trabeka_electricite.md",
    "menuiserie/guide_technique_menuiserie.md",
    "plomberie-chauffage/guide_technique_plomberie-chauffage.md",
    "champly/champly_vol11_plomberie-chauffage.md"
]

total_chunks = 0
for rel_path in files_to_index:
    file_path = os.path.join(CORPUS_DIR, rel_path)
    if not os.path.exists(file_path):
        print(f"Fichier introuvable: {file_path}")
        continue
        
    print(f"\nTraitement de {rel_path}...")
    
    # Extraire les métadonnées
    corps_etat = rel_path.split('/')[0]
    source = "Synthèse technique"
    if "champly" in rel_path:
        source = "Archive.org / Gallica BnF"
    elif "trabeka" in rel_path:
        source = "Archive.org"
        
    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Découper en chunks
    chunks = chunk_text(content)
    print(f"  -> {len(chunks)} chunks générés")
    
    # Indexer chaque chunk
    success_count = 0
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        if embedding:
            if insert_chunk(chunk, embedding, corps_etat, source):
                success_count += 1
                total_chunks += 1
                print(f"  [{i+1}/{len(chunks)}] Inséré")
            else:
                print(f"  [{i+1}/{len(chunks)}] Échec insertion")
        else:
            print(f"  [{i+1}/{len(chunks)}] Échec embedding")
            
    print(f"  -> {success_count}/{len(chunks)} chunks indexés avec succès")

print(f"\nTerminé ! {total_chunks} nouveaux chunks indexés.")
