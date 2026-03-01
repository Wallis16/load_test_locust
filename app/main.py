from fastapi import FastAPI
from app.api.endpoints.predict import router as predict_router

app = FastAPI(title="ML Inference API")

app.include_router(predict_router, prefix="/predict", tags=["Inference"])