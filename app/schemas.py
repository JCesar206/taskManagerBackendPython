from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, EmailStr

Status = Literal["pending", "in_progress", "done"]
Priority = Literal["low", "medium", "high"]

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str | None = None
    status: Status = "pending"
    priority: Priority = "medium"
    due_date: date | None = None

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = None
    status: Status | None = None
    priority: Priority | None = None
    due_date: date | None = None

class TaskOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: Status
    priority: Priority
    due_date: date | None
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"