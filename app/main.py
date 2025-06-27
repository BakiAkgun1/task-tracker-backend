from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=database.engine)

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme için * kullanılabilir; üretimde kısıtla
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veritabanı oturumu alma fonksiyonu
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Görev oluşturma (POST)
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Tüm görevleri listeleme (GET)
@app.get("/tasks/", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# Görev silme (DELETE)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
