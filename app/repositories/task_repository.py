from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Task

def get_all(db: Session, user_id: int, status: str | None = None) -> list[Task]:
    query = select(Task).where(Task.user_id == user_id).order_by(Task.id.desc())
    if status:
        query = query.where(Task.status == status)
    return list(db.scalars(query))

def get_by_id(db: Session, task_id: int, user_id: int) -> Task | None:
    return db.scalar(select(Task).where(Task.id == task_id, Task.user_id == user_id))

def create(db: Session, user_id: int, data: dict) -> Task:
    task = Task(**data, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update(db: Session, task: Task, data: dict) -> Task:
    for key, value in data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()