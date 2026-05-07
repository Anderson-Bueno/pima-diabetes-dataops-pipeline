FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código da API + treinamento
COPY deploy/api ./deploy/api

# Dataset para demo (mantém simples; em produção viria de S3/DB/feature store)
COPY data ./data

# Treina o modelo no build para facilitar demo local
# (Em produção: treinar no CI e copiar o artifact versionado)
RUN python deploy/api/train.py

EXPOSE 8000
CMD ["uvicorn", "deploy.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
