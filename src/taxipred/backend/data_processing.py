import json
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class InputClass(BaseModel):
    Trip_Distance_km: float = Field(gt=0, lt=600) 
    Passenger_Count: int = Field(gt=1, lt=10)
    Base_Fare: float = Field(...)
    Per_Km_Rate: float = Field(...)
    Per_Minute_Rate: float = Field(...)
    Trip_Duration_Minutes: float = Field(...)
    Day_of_Week_Weekend: Optional[bool] = None
    Time_of_Day_Evening: Optional[bool] = None
    Time_of_Day_Morning: Optional[bool] = None
    Time_of_Day_Night: Optional[bool] = None

    @field_validator(mode="after")
    def dummies_stings_input(self):
       check = [self.Time_of_Day_Evening, self.Time_of_Day_Morning, self.Time_of_Day_Night]

       if all(I is None for I in check):
          return self
       if all(I is True for I in check) != 1:
          raise ValueError ("only check one of the boxes")
        

class OutputClass(BaseModel):
   pred_taxi_price: float
