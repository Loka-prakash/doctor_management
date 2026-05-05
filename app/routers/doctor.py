from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorResponse
from app.services import doctor_service

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=DoctorResponse)
def create(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return doctor_service.create_doctor(db, doctor)


@router.get("/", response_model=list[DoctorResponse])
def get_all(db: Session = Depends(get_db)):
   return doctor_service.get_all_doctors(db)


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update(doctor_id: int, doctor: DoctorCreate, db: Session = Depends(get_db)):
    return doctor_service.update_doctor(db, doctor_id, doctor)

@router.delete("/{doctor_id}")
def delete(doctor_id: int, db: Session = Depends(get_db)):
    return doctor_service.delete_doctor(db, doctor_id)


 