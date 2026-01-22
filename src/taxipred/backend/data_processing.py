from pydantic import field_validator
import json

@field_validator(mode="before")
def dummies_stings_input(str, mode="before"):
    