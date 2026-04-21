### 🚀 Load Test FastAPI

A FastAPI application for serving predictions and storing them in a PostgreSQL database. The project is containerized with Docker and orchestrated using Docker Compose.

### 📦 Tech Stack

- FastAPI

- Uvicorn

- PostgreSQL

- Docker & Docker Compose

- uv (Python package manager)

### ▶️ Running the Application Locally

Make sure you have uv installed.

Start the FastAPI development server with auto-reload:

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```bash
http://127.0.0.1:8000
```
Swagger docs:

```bash
http://127.0.0.1:8000/docs
```

### 🐳 Running with Docker

1️⃣ Build the Docker image

```bash
docker build -f Dockerfile -t load_test_fast_api .
```

2️⃣ Start services with Docker Compose

```bash
docker-compose up
```

### This will start:

- FastAPI application

### Database Setup

If you need to manually create the table, connect to PostgreSQL:

```bash
psql -h localhost -p 5432 -U fastapi_user -d fastapi_db
```

Create the predictions table:

```bash
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    prediction TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 📡 Example Prediction Request

Example JSON payload for a prediction request:

```bash
{
  "username": "victory",
  "features": [13.28, 1.64, 2.84, 15.5, 110, 2.6, 2.68, 0.34, 1.36, 4.6, 1.09, 2.78, 880.0]
}
```

You can send this payload to your prediction endpoint using:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "username": "victory",
    "features": [13.28, 1.64, 2.84, 15.5, 110, 2.6, 2.68, 0.34, 1.36, 4.6, 1.09, 2.78, 880.0]
  }'
```

📁 Project Structure
```bash
.
├── app/
├── artifacts/
├── load_tests/
├── postgresql/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

### 🧪 Load Testing

Load tests can be placed and executed from the load_tests/ directory depending on your setup.

### 📝 Notes

Ensure PostgreSQL is running before sending prediction requests.

Environment variables should be configured in a .env file if required.

For production, disable --reload and configure proper logging and security settings.


openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/key.pem \
  -out certs/cert.pem