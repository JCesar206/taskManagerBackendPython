from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models import User
from app.schemas import TaskCreate, TaskUpdate, TaskOut, Status
from app.services import task_service as service

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("", response_model=list[TaskOut])
def list_tasks(
    status: Status | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    return service.list_tasks(db, user.id, status)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    return service.get_task(db, task_id, user.id)

@router.post("", response_model=TaskOut, status_code=201)
def create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    return service.create_task(db, user.id, data)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    return service.update_task(db, task_id, user.id, data)

@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    service.delete_task(db, task_id, user.id)