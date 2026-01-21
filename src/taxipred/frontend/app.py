from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from constants import DATA_PATH, MODELS_PATH
from pydantic import BaseModel, Field

app = FastAPI()