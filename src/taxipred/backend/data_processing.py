import json
from pydantic import BaseModel, Field, model_validator
from typing import Optional

class InputClass(BaseModel):
    Trip_Distance_km: float = Field(gt=0, lt=600) 
    Passenger_Count: int = Field(ge=1, lt=10)
    Base_Fare: float = Field(gt=0, lt=100)
    Per_Km_Rate: float = Field(gt=0, lt=300)
    Per_Minute_Rate: float = Field(gt=0, lt=50)
    Trip_Duration_Minutes: float = Field(gt=0, lt=600)
    Day_of_Week_Weekend: Optional[bool] = None
    Time_of_Day_Evening: Optional[bool] = None
    Time_of_Day_Morning: Optional[bool] = None
    Time_of_Day_Night: Optional[bool] = None

    @model_validator(mode="after")
    def dummies_stings_input(self):
       check = [self.Time_of_Day_Evening, self.Time_of_Day_Morning, self.Time_of_Day_Night]

       if all(I in (None, False) for I in check):
          return self
       if sum(I is True for I in check) != 1:
          raise ValueError ("only check one of the boxes")
       return self 
    


class OutputClass(BaseModel):
   pred_taxi_price: float
