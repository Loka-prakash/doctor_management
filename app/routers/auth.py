from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import RegisterSchema, LoginSchema
from app.services import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    return auth_service.register_user(db, data)

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return auth_service.login_user(db, data)