from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib

# Reemplace esto con su implementación:
class ApiInput(BaseModel):
    features: List[float]

# Reemplace esto con su implementación:
class ApiOutput(BaseModel):
    forecast: float

app = FastAPI()
model = joblib.load("model.joblib")

# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    predictions = model.predict(np.array(data.features).reshape(1, -1))
    prediction = ApiOutput(forecast=predictions)
    return prediction
