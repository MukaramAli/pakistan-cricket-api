
from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Pakistan Cricket API")

@app.get("/")
def home():
    return {"message": "Pakistan Cricket API is running!"}

@app.get("/matches")
def get_matches():
    df = pd.read_csv("pakistan_all_matches.csv")
    return df.to_dict(orient="records")
