from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from taxipred.utils.constants import RANDOM_FOREST, MODEL_PATH
from pydantic import BaseModel, Field
from typing import Literal

df = pd.read_csv(RANDOM_FOREST)
app = FastAPI()
router = APIRouter(prefix="/api/data")


class must_input(BaseModel):
    km_lengt: float = Field()
    passangers: int = Field(gt=1, lt=10)
    time_of_day: Literal["Moring", "Afternoon", "Evening"] = "Afternoon" # check if this i mean
    time_of_week: Literal["Weekday", "Weekday"] = "Weekday"

class pred_output(BaseModel):
   pred_taxi_price: float

@router.get("")
def get_data():
    return df.to_dict(orient="records")


@router.post("/taxi_pred")
def random_forset_ml(priceload: must_input):
    forest_data = pd.DataFrame(priceload.model_dump(), index=[0])
    reg = joblib.load(MODEL_PATH /  "taxi_price_random.joblib") 
    pred_price = reg.predict(forest_data) 
    print(pred_price)
    return{random_forset_ml: float(pred_price[0])}

app.include_router(router=router)