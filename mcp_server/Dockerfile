FROM python:3.11-slim

WORKDIR /app

# Dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code source
COPY main.py .

# Variables d'environnement par défaut (surchargées par docker-compose)
ENV PORT=8100
ENV PYTHONUNBUFFERED=1

EXPOSE 8100

CMD ["python", "main.py"]
