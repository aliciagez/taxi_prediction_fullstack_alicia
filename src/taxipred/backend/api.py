from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from taxipred.utils.constants import RANDOM_FOREST, MODEL_PATH
from pydantic import BaseModel, Field

df = pd.read_csv(RANDOM_FOREST)

app = FastAPI()

@app.get("/api/data")
def get_data():
    return df.to_dict(orient="records")


