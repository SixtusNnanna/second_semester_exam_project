from fastapi import APIRouter
from schemas.patient import  PatientCreate, patients
from services.patients import patient_services




patient_router = APIRouter()


@patient_router.get("", status_code=200)
def get_patients():
    return {
        "message": "Successful",
        "data": patients
    }


@patient_router.post("", status_code=201)
def create_patient(payload: PatientCreate):
    data = patient_services.create_patient(payload)
    return {
        "message": "Successful",
        "data": data
    }


@patient_router.put("/{patient_id}", status_code=200)
def update_patient(patient_id: int, payload: PatientCreate):
    data = patient_services.update_patient(patient_id, payload)
    return {
        "message": "Successful",
        "data": data
    }


@patient_router.delete("/{patient_id}", status_code=200)
def delete_patient(patient_id: int):
    data = patient_services.delete_patient(patient_id)
    return {
        "message": "Successful",
    }