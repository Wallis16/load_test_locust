import joblib
from app.core.config import settings  

model = None

def load_model():
    global model
    if model is None:
        model = joblib.load(settings.model_path)
    return model