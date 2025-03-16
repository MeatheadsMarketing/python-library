from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class InputData(BaseModel):
    input: list

@app.post("/predict")
def predict(data: InputData):
    """AI model API using FastAPI"""
    result = np.array(data.input) * 3
    return {"prediction": result.tolist()}
