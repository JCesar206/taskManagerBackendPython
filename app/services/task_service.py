from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import task_repository as repo
from app.schemas import TaskCreate, TaskUpdate

def list_tasks(db: Session, user_id: int, status: str | None = None):
    return repo.get_all(db, user_id, status)

def get_task(db: Session, task_id: int, user_id: int):
    task = repo.get_by_id(db, task_id, user_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

def create_task(db: Session, user_id: int, data: TaskCreate):
    return repo.create(db, user_id, data.model_dump())

def update_task(db: Session, task_id: int, user_id: int, data: TaskUpdate):
    task = get_task(db, task_id, user_id)
    return repo.update(db, task, data.model_dump(exclude_unset=True))

def delete_task(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id, user_id)
    repo.delete(db, task)