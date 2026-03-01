from app.models.model_loader import load_model

def predict(data):
    model = load_model()
    prediction = model.predict([data])
    return prediction.tolist()