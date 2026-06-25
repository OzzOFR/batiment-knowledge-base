#!/usr/bin/env python3
"""
Conversion et indexation des volumes Viollet-le-Duc depuis Archive.org
"""

import os
import re
import requests

CORPUS_DIR = "/home/ubuntu/batiment-knowledge-base/corpus"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SUPABASE_URL = "https://humvcalhznukzdbkninw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1bXZjYWxoem51a3pkYmtuaW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTM3NjIsImV4cCI6MjA5Nzg4OTc2Mn0.XzRg8FMGz3J6vakkxHP8JsUOFMUH57ats3Yg9vQKV2o"

VIOLLET_VOLUMES = [
    {"id": "dictionnairerai01viol", "vol": 1, "sujet": "Architecture (A-B) : Abside, Arc, Arcade, Bois"},
    {"id": "dictionnairerais05viol", "vol": 5, "sujet": "Architecture (F-M) : Fondation, Maçonnerie, Menuiserie"},
    {"id": "dictionnairerais07violuoft", "vol": 7, "sujet": "Architecture (P-R) : Pierre, Plâtre, Porte, Poutre"},
    {"id": "dictionnairerais08viol_0", "vol": 8, "sujet": "Architecture (S-T) : Serrurerie, Toit, Tuile, Voûte"},
    {"id": "dictionnaireraison09viol", "vol": 9, "sujet": "Architecture (V-Z) : Vitrail, Voûte, Zinguerie"},
]

def get_embedding(text):
    url = "https://openrouter.ai/api/v1/embeddings"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "text-embedding-3-small", "input": text}
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()['data'][0]['embedding']
        return None
    except:
        return None

def insert_chunk(content, embedding, corps_etat, source):
    url = f"{SUPABASE_URL}/rest/v1/batiment_chunks"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    data = {"content": content, "embedding": embedding, "corps_etat": corps_etat, "source": source}
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        return response.status_code in (200, 201)
    except:
        return False

def chunk_text(text, max_chars=1500, overlap=200):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\x0c', '\n\n', text)  # Supprimer les form feeds (saut de page DjVu)
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = start + max_chars
        if end < text_len:
            last_para = text.rfind('\n\n', start, end)
            if last_para != -1 and last_para > start + max_chars/2:
                end = last_para + 2
            else:
                last_dot = text.rfind('. ', start, end)
                if last_dot != -1 and last_dot > start + max_chars/2:
                    end = last_dot + 2
        chunk = text[start:end].strip()
        if len(chunk) > 100:
            chunks.append(chunk)
        start = end - overlap
    return chunks

total_indexed = 0

for vol in VIOLLET_VOLUMES:
    txt_path = f"{CORPUS_DIR}/encyclopedie-generale/viollet/{vol['id']}.txt"
    if not os.path.exists(txt_path):
        print(f"Fichier manquant: {txt_path}")
        continue
    
    print(f"\nTraitement Vol. {vol['vol']} - {vol['sujet'][:50]}...")
    
    with open(txt_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Limiter à 200 000 caractères pour éviter trop de chunks
    content = content[:200000]
    chunks = chunk_text(content)
    print(f"  -> {len(chunks)} chunks")
    
    source = f"Viollet-le-Duc - Dictionnaire raisonné de l'architecture française (Vol. {vol['vol']})"
    success = 0
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        if embedding and insert_chunk(chunk, embedding, "encyclopedie-generale", source):
            success += 1
            total_indexed += 1
            if (i+1) % 10 == 0:
                print(f"  [{i+1}/{len(chunks)}] OK")
    
    print(f"  -> {success}/{len(chunks)} chunks indexés")

print(f"\nTotal indexé: {total_indexed} chunks")
