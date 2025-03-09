import os

files = {
    "backend/Dockerfile": "FROM python:3.10-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY ./app ./app\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n",
    "backend/requirements.txt": "fastapi\nuvicorn[standard]\nrequests\npython-dotenv\nredis\nSQLAlchemy\npsycopg2-binary",
    "backend/.env": "AI_SERVICE_URL=http://ai_service:5000/predict\nREDIS_URL=redis://redis:6379\nDATABASE_URL=postgresql://postgres:postgres@postgres:5432/qcdb\n",
    "backend/app/main.py": "from fastapi import FastAPI\nfrom .routers import ai\n\napp = FastAPI()\napp.include_router(ai.router, prefix=\"/ai\")\n",
    "backend/app/routers/ai.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.post('/predict')\nasync def predict():\n    return {\"message\": \"AI endpoint connected.\"}\n",

    "frontend/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package.json package-lock.json ./\nRUN npm install\nCOPY . .\nCMD [\"npm\", \"run\", \"dev\"]\n",
    "frontend/package.json": '{"name":"qc-frontend","scripts":{"dev":"vite"},"dependencies":{"axios":"latest","react":"latest","react-dom":"latest"},"devDependencies":{"vite":"latest"}}',
    "frontend/.env": "VITE_BACKEND_URL=http://localhost:8000\n",
    "frontend/src/App.jsx": "import React from 'react';\nexport default function App(){ return <div>QC Frontend Running</div>; }\n",

    "ai_service/Dockerfile": "FROM python:3.10-slim\nWORKDIR /app\nCOPY requirements.txt ./\nRUN pip install -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"service:app\", \"--host\", \"0.0.0.0\", \"--port\", \"5000\"]\n",
    "ai_service/requirements.txt": "fastapi\nuvicorn[standard]\ntorch\nnumpy\npillow\n",
    "ai_service/service.py": "from fastapi import FastAPI, UploadFile\nfrom model.inference import predict\n\napp = FastAPI()\n\n@app.post('/predict')\nasync def prediction(file: UploadFile):\n    result = predict(await file.read())\n    return {\"prediction\": result}\n",
    "ai_service/model/inference.py": "def predict(image_bytes):\n    return \"ok\"\n",

    "docker-compose.yaml": "version: '3.8'\n\nnetworks:\n  qc-network:\n    driver: bridge\n\nservices:\n  backend:\n    build: ./backend\n    ports:\n      - \"8000:8000\"\n    networks:\n      - qc-network\n    depends_on:\n      - redis\n      - postgres\n      - ai_service\n\n  frontend:\n    build: ./frontend\n    ports:\n      - \"3000:3000\"\n    networks:\n      - qc-network\n\n  ai_service:\n    build: ./ai_service\n    networks:\n      - qc-network\n    ports:\n      - \"5000:5000\"\n\n  redis:\n    image: redis:latest\n    ports:\n      - \"6379:6379\"\n    volumes:\n      - ./redis_data:/data\n    networks:\n      - qc-network\n\n  postgres:\n    image: postgres:latest\n    ports:\n      - \"5432:5432\"\n    environment:\n      POSTGRES_USER: postgres\n      POSTGRES_PASSWORD: postgres\n      POSTGRES_DB: qcdb\n    volumes:\n      - ./database/postgres_data:/var/lib/postgresql/data\n    networks:\n      - qc-network\n"
}


def create_structure(files_dict):
    for path, content in files_dict.items():
        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(path, 'w') as file:
            file.write(content)


if __name__ == '__main__':
    create_structure(files)
    print("✅ QC project structure created successfully.")
