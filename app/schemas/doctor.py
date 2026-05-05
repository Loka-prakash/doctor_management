from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str
    experience: int
    email: str
    is_active: bool = True
   

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True