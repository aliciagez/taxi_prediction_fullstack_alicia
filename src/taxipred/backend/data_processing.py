import json
from pydantic import BaseModel, Field, field_validator

class InputClass(BaseModel):
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

class OutputClass(BaseModel):
   pred_taxi_price: float
