from sqlalchemy.orm import Session
from app.models.patient import Patient

def create_patient(db: Session, data):

    patient = Patient(**data.model_dump())

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient

def get_all_patients(db: Session):

    return db.query(Patient).all()

def get_patient(db: Session, patient_id: int):

    return db.query(Patient).filter(Patient.id == patient_id).first()