from fastapi import APIRouter
from schemas.doctors import DoctorCreate, doctors
from services.doctors import doctor_service


doctor_router = APIRouter()


@doctor_router.get("", status_code=200)
def get_doctors():
    return {
        "message": "Successful",
        "data": doctors
    }



@doctor_router.post("", status_code=201)
def create_doctor(payload:DoctorCreate):
    data = doctor_service.doctor_create(payload)
    return{
        "message": "Successful",
        "data": data
    }


@doctor_router.put("", status_code=200)
def update_doctor(doctor_id: int, payload:DoctorCreate):
    data = doctor_service.update_doctor(doctor_id, payload)
    return{
        "message": "Successful",
        "data": data
    }


@doctor_router.delete("", status_code=200)
def delete_doctor(doctor_id:int):
    data = doctor_service.delete_doctors(doctor_id)
    return{
        "message": "Successful",
    }

@doctor_router.put("{doctor_id}/status", status_code=200)
def change_doctor_status(doctor_id:int, payload:bool):
    data = doctor_service.change_status(doctor_id, payload)
    return{
        "message": "Successful",
        "data": data
    }