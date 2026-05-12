from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    specialization = Column(String(100))
    phone = Column(String(15))
    experience = Column(Integer)
    email = Column(String(100), unique=True, index=True)
    is_active = Column(Boolean, default=True)