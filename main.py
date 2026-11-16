
from fastapi import FastAPI
import pandas as pd
from pathlib import Path

app = FastAPI(title="Pakistan Cricket API")

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "pakistan_all_matches.csv"

@app.get("/")
def home():
    return {"message": "Pakistan Cricket API is running!"}

@app.get("/matches")
def get_matches():
    df = pd.read_csv(CSV_FILE)

    # Replace missing values (NaN) with None
    df = df.astype(object).where(pd.notna(df), None)

    return df.to_dict(orient="records")
