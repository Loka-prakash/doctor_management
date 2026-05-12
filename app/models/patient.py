from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    phone = Column(String(15))