from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from taxipred.utils.constants import RANDOM_FOREST, MODEL_PATH
from pydantic import BaseModel, Field

df = pd.read_csv(RANDOM_FOREST)
app = FastAPI()
router = APIRouter(prefix="/api/data")


class optional_input1(str):
  Morning ="Morning"
  Afternoon ="Afternoon"
  Evening = "Evening"


class optional_input2(str):
  Weekend ="Weekend"
  Weekday ="Weekday"

#used LLM for how to get a specif sting and how to make them into a default 

class must_input(BaseModel):
    km_lengt: float = Field()
    passangers: int = Field(gt=1, lt=10)
    time_of_day: optional_input1 = optional_input1.Morning
    time_of_week: optional_input2 = optional_input2.Weekday

class pred_output(BaseExceptionGroup):
   pred_taxi_price: float

@router.get("")
def get_data():
    return df.to_dict(orient="records")


@router.post("/taxi_pred")
def random_forset_ml(priceload: must_input):
    forest_data = pd.DataFrame(priceload.model_dump(), index=[0])
    reg = joblib.load(MODEL_PATH /  "")