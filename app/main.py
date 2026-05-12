from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import doctor
from app.routers import doctor
from app.routers import patient
from app.routers import auth

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# router
app.include_router(doctor.router)
app.include_router(auth.router)
app.include_router(patient.router)
app.include_router(doctor.router)

@app.get("/")
def home():
    return {"message": "Doctor API Running"}