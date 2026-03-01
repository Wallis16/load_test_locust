from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    username: str
    features: List[float]