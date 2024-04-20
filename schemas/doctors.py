from enum import Enum
from pydantic import BaseModel

#Doctors: id, name, specialization, phone, is_available (defaults to True)



class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: int
    is_available: bool = True



class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: int
    is_available:bool = True



doctors:dict[int, Doctor] = {
    1:Doctor(id=1, name="Jude", specialization="Cardiologist", phone=9087966723, is_available=True),
    2:Doctor(id=2, name="Nnanna", specialization="Dermatologist", phone=8121654321, is_available=True),
    3:Doctor(id=3, name="Chinedu", specialization="Opthamologist", phone=8086543219, is_available=True),
    4:Doctor(id=4, name="Jerome", specialization="Neurologist", phone=9166543200, is_available=True),
}

