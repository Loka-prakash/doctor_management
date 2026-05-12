from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate
from fastapi import HTTPException
def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor_data: DoctorCreate):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        return {"error": "Doctor not found"}

    doctor.name = doctor_data.name
    doctor.specialization = doctor_data.specialization
    doctor.phone = doctor_data.phone
    doctor.experience = doctor_data.experience
    doctor.email = doctor_data.email
    doctor.is_active = doctor_data.is_active

    db.commit()
    db.refresh(doctor)
    return doctor


def delete_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(
    status_code=404,
    detail="Doctor not found"
)
 
    db.delete(doctor)
    db.commit()

    return doctor