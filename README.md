# 🚀 QC Application

This is a Quality Control (QC) AI application built with a modular, Docker-based architecture. The setup includes a frontend UI, a backend server, an AI microservice, Redis for caching, and PostgreSQL for database storage.

## 📦 Project Structure

```plaintext
qc_application/
├── backend/         # FastAPI backend
├── frontend/        # React frontend
├── ai_service      # AI service container
├── redis_data      # Redis storage
├── database
│   └── postgres_data/
├── docker-compose.yaml
├── .gitignore
└── README.md
```

## 🛠 Technologies & Containers Used

| Container       | Technology                | Port             | Purpose                  |
|-----------------|---------------------------|------------------|--------------------------|
| **Frontend**    | React.js (Vite)           | `3000`           | User Interface           |
| **Backend**     | FastAPI                   | `8000`           | Backend API              |
| **AI Service**  | FastAPI & Python          | `5001`           | AI Model Training/Inference |
| **Redis**       | Redis (latest)            | `6379`           | Caching & Queuing        |
| **Postgres**    | PostgreSQL (latest)       | `5432`           | Database storage         |

---

## ✅ How to Run the Project (Clearly Documented)

### **1. Build & Run Docker Containers:**

Run from the project root directory:

```bash
docker-compose down
docker-compose build
docker-compose up -d
```

### Check Running Containers:
```bash
docker-compose ps
```

---

## 🌐 Service URLs

- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **AI Service API Docs**: [http://localhost:5001/docs](http://localhost:5001/docs)
- **Redis**: `redis://localhost:6379`
- **PostgreSQL**: `postgres://postgres:postgres@localhost:5432/qcdb`

---

## 🚨 Important Commands

### 🔄 Rebuilding Containers

To rebuild all containers explicitly:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

To rebuild specific container explicitly (frontend example):
```bash
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

### 🐞 Debugging Containers
Check container logs explicitly:
```bash
docker-compose logs frontend
docker-compose logs backend
docker-compose logs ai_service
```

---

## ⚙️ Git Setup

Your git user details:

```bash
git config --global user.name "mohithhp"
git config --global user.email "mohithhp@example.com"
```

## 📌 Development Workflow

- Start by developing frontend UI components and integration with backend APIs.
- Implement backend logic clearly to communicate with the AI microservice.
- Implement your AI inference/training logic in the AI microservice container.
- Use Redis for caching intermediate data.
- Store structured data in PostgreSQL database.

---

## 📝 Notes

- Ensure to keep your `.env` files updated clearly with the correct container URLs and credentials.
- Regularly clear and rebuild your Docker containers if you're making major configuration changes.

## 🚀 Next Steps

- Implement actual AI logic.
- Add comprehensive frontend features, including image upload and display.
- Enhance backend and AI integration clearly for robust communication.

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React.js](https://react.dev)
- [Docker](https://docs.docker.com)
- [Vite Documentation](https://vitejs.dev)

---

Happy coding! 🎉

