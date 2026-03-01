from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.prediction import Prediction
from app.schemas.request import PredictionRequest
from app.schemas.response import PredictionResponse
from app.services.inference_service import predict
from app.core.config import settings 

router = APIRouter()

@router.post("/", response_model=PredictionResponse)
def run_inference(
    request: PredictionRequest,
    db: Session = Depends(get_db)
):
    result = predict(request.features)

    if settings.record_on_db == 'true':

        db_prediction = Prediction(
            username=request.username,
            prediction=str(result[0])
        )

        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)

    return {"prediction": result}