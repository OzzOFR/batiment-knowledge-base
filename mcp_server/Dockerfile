FROM python:3.11-slim

WORKDIR /app

# Dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Dépendances Python (torch CPU pour réduire la taille de l'image)
COPY requirements.txt .
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Code source
COPY main.py .

# Pré-télécharger le modèle d'embedding au build (évite le téléchargement au runtime)
RUN python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')" || true

# Variables d'environnement par défaut (surchargées par docker-compose)
ENV PORT=8100
ENV PYTHONUNBUFFERED=1

EXPOSE 8100

CMD ["python", "main.py"]
