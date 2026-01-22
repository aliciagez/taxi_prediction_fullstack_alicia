from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from taxipred.utils.constants import RANDOM_FOREST, MODEL_PATH
from pydantic import BaseModel, Field, field_validator


df = pd.read_csv(RANDOM_FOREST)
app = FastAPI()
router = APIRouter(prefix="/api/data")


class must_input(BaseModel):
    Trip_Distance_km: float = Field(gt=0, lt=600) 
    Passenger_Count: int = Field(gt=1, lt=10)
    Base_Fare: float = Field(...)
    Per_Km_Rate: float = Field(...)
    Per_Minute_Rate: float = Field()
    Trip_Duration_Minutes: float = Field(...)
    Day_of_Week_Weekend: int = Field(default=0, ge=0, le=1)
    Time_of_Day_Evening: int = Field(ge=0, le=1)
    Time_of_Day_Morning: int = Field(ge=0, le=1)
    Time_of_Day_Night: int = Field(ge=0, le=1)

    @field_validator(
        "Day_of_Week_Weekend",
        "Time_of_Day_Evening",
        "Time_of_Day_Morning",
        "Time_of_Day_Night",
        mode="before"
)
    def dummies_stings_input(cls, I):
        if isinstance(I, str): 
            if I == "yes":
                return True
        if I == "no":
         return False
        return I
    

class pred_output(BaseModel):
   pred_taxi_price: float

@router.get("")
def get_data():
    return df.to_dict(orient="records")


@router.post("/taxi_pred")
def random_forset_ml(priceload: must_input):
    forest_data = pd.DataFrame(priceload.model_dump(), index=[0])
    reg = joblib.load(MODEL_PATH) 
    pred_price = reg.predict(forest_data) 
    print(pred_price)
    return{"price_prediction": float(pred_price[0])}

app.include_router(router=router)