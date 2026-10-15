from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import user_repository as repo
from app.schemas import UserCreate
from app.security import hash_password, verify_password, create_access_token

def register(db: Session, data: UserCreate):
    email = data.email.lower()
    if repo.get_by_email(db, email):
        raise HTTPException(status_code=409, detail="El email ya está registrado")
    return repo.create(db, email, hash_password(data.password))

def login(db: Session, email: str, password: str) -> str:
    user = repo.get_by_email(db, email.lower())
    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
				)
    return create_access_token(user.id)