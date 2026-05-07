## 🚀 Deploy (MLOps) — API de predição com FastAPI + Docker

### Estrutura adicionada
```
deploy/api/
  train.py
  app.py
  Dockerfile
deploy/api/model.joblib   # gerado no build
```

### Build + Run
```bash
docker build -t pima-api -f deploy/api/Dockerfile .
docker run -p 8000:8000 pima-api
```

### Teste rápido
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"Pregnancies":2,"Glucose":130,"BloodPressure":70,"SkinThickness":20,"Insulin":80,"BMI":33.2,"DiabetesPedigreeFunction":0.5,"Age":55}'
```

### Endpoints
- `GET /health` → healthcheck
- `POST /predict` → retorna `prediction` (0/1) e `probability` (classe 1)
