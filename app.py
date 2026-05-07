from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path


MODEL_PATH = Path("deploy/api/model.joblib")

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model artifact not found at {MODEL_PATH}. "
        "Run `python deploy/api/train.py` or build the Docker image which trains during build."
    )

model = joblib.load(MODEL_PATH)

app = FastAPI(title="Pima Diabetes Predictor", version="1.0")


class Patient(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(p: Patient):
    X = [[
        p.Pregnancies,
        p.Glucose,
        p.BloodPressure,
        p.SkinThickness,
        p.Insulin,
        p.BMI,
        p.DiabetesPedigreeFunction,
        p.Age,
    ]]

    proba = float(model.predict_proba(X)[0][1])
    pred = int(proba >= 0.5)

    return {"prediction": pred, "probability": round(proba, 6)}
