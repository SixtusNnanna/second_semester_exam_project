from fastapi import FastAPI
from routers.patient import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router


app = FastAPI()


app.include_router(router=patient_router, prefix="/patient", tags=["Patient"])
app.include_router(router=doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(router=appointment_router, prefix="/appointments", tags=["Appointment"])


@app.get("/")
def index():
    return{
        "message": "Welcome to Backend Second Semester Exams"
    }