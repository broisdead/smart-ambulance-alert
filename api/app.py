from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.anomaly_detection import compute_anomaly_score
from src.risk_scoring import compute_risk_score

app = FastAPI(title="Smart Ambulance Alert API")

# ---------- Input Schema ----------
class VitalsInput(BaseModel):
    heart_rate: float
    spo2: float
    bp_sys: float
    bp_dia: float
    motion: float


# ---------- API Endpoint ----------
@app.post("/predict")
def predict(vitals: VitalsInput):
    # Convert input to DataFrame
    df = pd.DataFrame([vitals.dict()])

    # Anomaly detection
    df = compute_anomaly_score(df)

    # Risk scoring
    df = compute_risk_score(df)

    response = {
        "anomaly_score": round(float(df["anomaly_score"].iloc[0]), 3),
        "risk_score": round(float(df["risk_score"].iloc[0]), 3),
        "alert": int(df["alert"].iloc[0]),
        "confidence": round(float(1 - df["motion"] / 3), 2)
    }

    return response


@app.get("/")
def health_check():
    return {"status": "Smart Ambulance API running"}
