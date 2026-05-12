from pydantic import BaseModel
from pydantic import Field

class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str = Field(..., pattern="^[0-9]{10,15}$")
    experience: int
    email: str
    is_active: bool = True
   

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True