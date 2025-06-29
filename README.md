

# 🧩 Task Tracker - Backend

This is the **FastAPI-based backend** for the Task Tracker application. It provides a RESTful API for managing tasks and communicates with a SQLite database.

---

## 📁 Project Structure

```

task-tracker-backend/
├── .github/
│   └── workflows/
│       └── deploy.yml           # GitHub Actions CI/CD pipeline
├── app/
│   ├── **pycache**/
│   ├── database.py              # Database connection logic
│   ├── main.py                  # Entry point for FastAPI app
│   ├── models.py                # SQLAlchemy models
│   └── schemas.py               # Pydantic schemas for request/response
├── venv/                        # Python virtual environment (local only)
├── .dockerignore               # Docker ignore rules
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Dockerfile for containerization
├── requirements.txt            # Python dependencies
└── tasks.db                    # SQLite database file

````

---

## 🧪 Local Development

To run the backend locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/task-tracker-backend.git
cd task-tracker-backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI app
uvicorn app.main:app --reload
````

API will be available at:
👉 [http://localhost:8000](http://localhost:8000)
Interactive docs:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Instructions

### 🔧 1. Build Docker Image

```bash
docker build -t yourdockerhubuser/task-tracker-backend:latest .
```

### ▶️ 2. Run Container

```bash
docker run -d -p 8000:8000 yourdockerhubuser/task-tracker-backend:latest
```

---

## ⚙️ GitHub Actions - CI/CD Pipeline

This project includes a **CI/CD pipeline** using GitHub Actions. When changes are pushed to the `main` branch, a new Docker image is automatically built and pushed to Docker Hub.


### 🔐 Required GitHub Secrets

Go to your repo → **Settings** → **Secrets** → **Actions**, and add:

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

---

## 🚀 FastAPI + Docker

The backend is containerized using Docker and serves via **Uvicorn**.

### Dockerfile Overview

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

> 💡 Make sure to use this backend with the [Task Tracker Frontend](https://github.com/your-username/task-tracker-frontend)


