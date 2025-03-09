from fastapi import APIRouter
import requests, os

router = APIRouter()

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL")

@router.post('/predict')
async def predict():
    return {"message": "AI endpoint connected."}

@router.post('/train')
async def train():
    ai_train_url = f"{AI_SERVICE_URL}/train"
    response = requests.post(ai_train_url)
    return response.json()
