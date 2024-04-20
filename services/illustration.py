
# from datetime import datetime
# from fastapi import HTTPException, Depends
# from schemas.doctors import  Doctor, doctors
# from schemas.patient import patients, Patient
# from schemas.appointment import Appointment, AppointmentCreate, appointments, Status




# # def doctor_availabilty(payload:AppointmentCreate):

    
# def check_available_doctor():
#     for doctor_id, doctor in doctors.items():
#         if doctor.is_available.available:
#             return doctor_id
#     return None
        
    
# class AppointmentService:


# #    @ staticmethod
# #    def create_appointment(payload: Appointment):

# #     appointment_id = len(appointments)+ 1

# #     #check doctor availability
# #     if appointment_id > len(doctors) or  doctors[appointment_id].is_available.unavailable:
# #         raise HTTPException(status_code=404, detail="Doctor not available")
    
# #     new_appointment = Appointment(
# #         id=appointment_id,
# #         doctor=doctors[appointment_id],
# #         patient=patients[payload.patient],
# #        date=payload.date
# #        )
# #     appointments[appointment_id] = new_appointment


# #     return new_appointment
        
       
#     @staticmethod
#     def create_appointment(payload:AppointmentCreate):
#         """
#         TO create an appointment
#         The doctors must be availabe 
#         The appointment must be completed
#         The appointent must be cancelled

#         """

#         for doctor_id_, doctor in doctors:
#             if doctor.is_available.unavailable:
#                 raise HTTPException(status_code=404, detail="No available doctor found")
            
            
#         appointment_id = len(appointments) + 1
#         new_appointment = Appointment(
#             id=appointment_id,
#             doctor=doctor_id_,
#             patient=patients[payload.patient],
#             date=payload.date
#         )

#         appointments[appointment_id] = new_appointment
          
#     # @staticmethod
#     # def create_appointment(payload:AppointmentCreate):
#     #     appt_id = len(appointments) + 1
#     #     doctor_id = check_available_doctor()
        
#     #     if appt_id > len(doctors):
#     #         raise HTTPException(status_code=404, detail="No available doctor found")
        
        
#     #     new_appointment = Appointment(
#     #     id=appt_id,
#     #     doctor=doctors[check_available_doctor()],
#     #     patient=patients[payload.patient],
#     #     date=payload.date)
#     #     appointments[appt_id] = new_appointment
        
#     #     return new_appointment
    

    
    
#     # @staticmethod
#     # def create_appointment(payload:AppointmentCreate):
        
#     #     appointment_id = str(uuid.uuid4())
#     #     if appointment_id > len(appointments):
#     #         raise HTTPException(status_code=404, detail="Appointment can no longer be booked")


#     #     #if the number of doctors available are all booked
#     #     if  doctors[appointment_id].is_available:
            

#     #         new_appointment = Appointment(
#     #         id=appointment_id,
#     #         doctor=doctors[appointment_id],
#     #         patient=patients[payload.patient],
#     #         date=payload.date) 
#     #         appointments[appointment_id] = new_appointment

#     #         #if appointment is booked doctor becomes unavailable
#     #         new_appointment.doctor.is_available.unavailable 

#     #         #as the doctor is booked he is unavailable
            
#     #         return new_appointment
        
#     #     else:
#     #         raise HTTPException(status_code=404, detail="No available doctor found")
            

#     @staticmethod
#     def complete_appointments(appointment_id:int, payload:Status):
#         completed_appoint = None
#         for appointment_id_ in appointments:
#             if appointment_id_ == appointment_id: 
#                 completed_appoint = appointments[appointment_id]
#                 break
        

#         if not completed_appoint:
#             raise HTTPException(status_code=404, detail="Appointment with id above was not creatted")

#         completed_appoint.status = payload
#         #doctors becomes available
#         completed_appoint.doctor.is_available = True

#         return completed_appoint

#     """
#     Condittions for doctors avalaibilty 
#     1. there must be doctors in the dictionary
#     2. the available status of a doctor must be true 
#     3. the appointment must be completed 
#     4. the appointent must be cancelled 

#     """

   
    @staticmethod
    def cancel_appointment(appointment_id:int):
        target_appointment = None
        for appointment_id_ in appointments:
            if appointment_id_ == appointment_id:
                target_appointment = appointments[appointment_id_]
                break

        if not target_appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        
        del appointments[appointment_id_]
        return target_appointment
    

   
    
    
# appointment_service = AppointmentService()
            