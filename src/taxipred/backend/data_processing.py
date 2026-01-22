from pydantic import field_validator
import json

@field_validator(
"Day_of_Week_Weekend",
"Time_of_Day_Evening",
 "Time_of_Day_Morning",
"Time_of_Day_Night",
mode="before")
def dummies_stings_input(cls, I):
    if isinstance(I, str): 
        if I == "yes":
            return True
        if I == "no":
            return False
    return I

