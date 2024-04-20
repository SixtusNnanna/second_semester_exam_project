from fastapi import APIRouter, Depends
from schemas.appointment import Appointment, AppointmentCreate, appointments, Status
from services.appointment import appointment_service 



appointment_router  = APIRouter()


@appointment_router.get("", status_code=200)
def get_appointments():
    return {
        "message": "Successful",
        "data": appointments
    }


@appointment_router.post("", status_code=201)
def create_appointment(payload: AppointmentCreate ):
    data = appointment_service.create_appointment(payload)
    return {
        "message": "Successful",
        "data": data
    }


@appointment_router.put("/{appointment_id}/status", status_code=200)
def complete_appointment(appointment_id:int, payload: Status):
    data = appointment_service.complete_appointments(appointment_id, payload)
    return{
        "message": "Successful",
        "data": data
    }



@appointment_router.delete("/{appointment_id}/cancel", status_code=204)
def cancel_appointment(appointment_id:int):
    data = appointment_service.cancel_appointment(appointment_id)
    return {
        "Message": "Appointment has be successfully cancelled",
    }