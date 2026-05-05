from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import doctor

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# router
app.include_router(doctor.router)

@app.get("/")
def home():
    return {"message": "Doctor API Running"}