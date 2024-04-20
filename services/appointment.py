from fastapi import HTTPException
from schemas.doctors import  Doctor, doctors
from schemas.patient import patients, Patient
from schemas.appointment import Appointment, AppointmentCreate, appointments, Status



class AppointmentService:


    @staticmethod
    def create_appointment(payload:AppointmentCreate):
        """
        TO create an appointment
        The doctors must be availabe 

        The appointment must be completed
        The appointent must be cancelled

        if an appointment exists with a doctor, mark the doctor unavailable 

        """
        #appointment id
        appointment_id = len(appointments) + 1


        #checking if doctor is available
        available_doctor_id = None
        for doctor_id, doctor in doctors.items():
            if doctor.is_available:
                available_doctor_id = doctor_id
                break

        #when doctor is unavailable raise an error 
        if available_doctor_id is None:
            raise HTTPException(status_code=404, detail="No available doctors at this time")

        #checking if patient is in the database and raising error id not
        if payload.patient not in patients: 
            raise HTTPException(status_code=404, detail="Patient ID is not in our database please register")
                        
        #creating new appointment 
        new_appointment = Appointment(
            id=appointment_id,
            doctor=doctors[available_doctor_id],
            patient=patients[payload.patient],
            date=payload.date
        )
        
        appointments[appointment_id] = new_appointment

        #marking doctor on an appointment unavailable
        doctors[available_doctor_id].is_available = False

        return new_appointment
    

    """
        complete the appointment:
        1. Check if appointment is exist
        2. raise exception if not 
        3. change appointment status to completed
    """

    @staticmethod
    def complete_appointments(appointment_id:int, payload:Status):
        completed_appoint = None
      
        for appointment_id_ in appointments:
            if appointment_id_ == appointment_id: 
                completed_appoint = appointments[appointment_id]
                break
        

        if not completed_appoint:
            raise HTTPException(status_code=404, detail="Appointment with id above was not creatted")

        completed_appoint.status = payload
      


        completed_appoint.doctor.is_available = True

        return completed_appoint
        


    """
    Cancel_appointment:
    1: check if appointment exists
    2. if appointment does not exist, raise an exception
    3. change the doctor status attached to appointment to available
    
    """
    @staticmethod
    def cancel_appointment(appointment_id:int):
        target_appointment = None
        for appointment_id_ in appointments:
            if appointment_id_ == appointment_id:
                target_appointment = appointments[appointment_id_]
                break

        if not target_appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        
        target_appointment.doctor.is_available = True

        del appointments[appointment_id]
        
        return {
            "Message": "Appointment cancelled Successfully"
        }
    
appointment_service = AppointmentService()
        
