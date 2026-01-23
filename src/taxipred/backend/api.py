from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from taxipred.utils.constants import RANDOM_FOREST, MODEL_PATH
from taxipred.backend.data_processing import OutputClass, InputClass

df = pd.read_csv(RANDOM_FOREST)
app = FastAPI()
router = APIRouter(prefix="/api/data")
reg = joblib.load(MODEL_PATH) 

@router.get("")
def get_data():
    return df.to_dict(orient="records")


@router.post("/apri/taxi_pred", response_model=OutputClass)
async def random_forset_ml(priceload:InputClass = None):
    forest_data = pd.DataFrame([priceload.model_dump()], index=[0])
    pred_price = reg.predict(forest_data) 
    print(pred_price)
    return{"pred_taxi_price": float(pred_price[0])}

app.include_router(router=router)