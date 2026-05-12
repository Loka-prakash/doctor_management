from pydantic import BaseModel, Field

class PatientBase(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str = Field(min_length=10, max_length=15)

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True