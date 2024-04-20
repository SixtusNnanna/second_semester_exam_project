from enum import Enum
from datetime import date
from pydantic import BaseModel
from schemas.patient import Patient,patients
from schemas.doctors import Doctor, doctors


#Appointment: id, patient, doctor, date

class Status(Enum):
    completed = "COMPLETED"
    pending = "PENDING"


class Appointment(BaseModel):
    id: int
    patient: Patient | int
    doctor: Doctor | int
    date: date
    status:str = Status.pending


class AppointmentCreate(BaseModel):
    patient: int 
    date: date
    status: Status = Status.pending






appointments:dict[int, Appointment] = {
#     1:Appointment(id=1, patient=patients[1], doctor=doctors[1], date="2022-01-01"),
#     2:Appointment(id=2, patient=patients[2], doctor=doctors[2], date="2022-01-02"),
#    3: Appointment(id=3, patient=patients[3], doctor=doctors[3], date="2022-01-03"),

}