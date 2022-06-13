from fastapi import APIRouter, Request
from typing import Optional
from app.models.MLR_PredictingHousePrices.predict import PredictHousePrice
from pydantic import BaseModel

ph = PredictHousePrice()
router = APIRouter()

@router.post("/predicthouseprice")
async def getInformation(info : Request):
    req_info = await info.json()
    res = ph.getPrice([req_info["data"]])
    return {
        "status" : "SUCCESS",
        "prediction" : res[0]
    }
