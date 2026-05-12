from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.services import patient_service

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.post("/", response_model=PatientResponse)
def create(data: PatientCreate, db: Session = Depends(get_db)):
    return patient_service.create_patient(db, data)

@router.get("/", response_model=list[PatientResponse])
def get_all(db: Session = Depends(get_db)):
    return patient_service.get_all_patients(db)

@router.get("/{patient_id}", response_model=PatientResponse)
def get_one(patient_id: int, db: Session = Depends(get_db)):
    return patient_service.get_patient(db, patient_id)