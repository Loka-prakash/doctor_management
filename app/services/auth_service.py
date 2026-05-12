from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def register_user(db: Session, data):

    user = User(
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, data):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        return {"error": "Invalid email"}

    if not verify_password(data.password, user.password):
        return {"error": "Invalid password"}

    token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }