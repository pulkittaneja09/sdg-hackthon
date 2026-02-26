from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from feature_engineering import extract_features
from model_loader import load_model
from scoring import calculate_scores
from schemas import PredictionResponse

app = FastAPI(title="SecondSpark AI Battery Evaluation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SecondSpark Backend Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        if df.empty:
            return {"error": "Empty CSV file"}

        battery_id = (
            str(df["battery_id"].iloc[0])
            if "battery_id" in df.columns
            else "Unknown"
        )

        # Trend data for frontend charts
        capacity_trend = []
        temperature_trend = []

        if "cycle" in df.columns and "capacity" in df.columns:
            capacity_trend = [
                {"cycle": int(c), "capacity": float(cap)}
                for c, cap in zip(df["cycle"], df["capacity"])
            ]

        if "cycle" in df.columns and "temperature" in df.columns:
            temperature_trend = [
                {"cycle": int(c), "temperature": float(t)}
                for c, t in zip(df["cycle"], df["temperature"])
            ]

        # Feature extraction
        features = extract_features(df)

        # Load model & predict
        model = load_model()
        rul = model.predict([features])[0]

        # Scoring
        result = calculate_scores(rul, features)

        return {
            "battery_id": battery_id,
            "summary": result,
            "trends": {
                "capacity_trend": capacity_trend,
                "temperature_trend": temperature_trend
            }
        }

    except Exception as e:
        return {"error": str(e)}