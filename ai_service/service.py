from fastapi import FastAPI
from model.inference import predict, train_model

app = FastAPI()

@app.post('/predict')
async def prediction():
    return {"prediction": "placeholder"}

@app.post('/train')
async def training():
    result = train_model()
    return {"message": result}
