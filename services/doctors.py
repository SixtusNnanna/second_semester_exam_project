from fastapi import HTTPException

from schemas.doctors import DoctorCreate, doctors, Doctor

class DoctorService:
    

    
    @staticmethod
    def doctor_create(payload:DoctorCreate):
        doctor_id = len(doctors)  + 1
        new_doctor = Doctor(id=doctor_id,
                            **payload.model_dump())
        
        doctors[doctor_id] = new_doctor
    
        return new_doctor
    



    @staticmethod
    def update_doctor(doctor_id:int, payload:DoctorCreate):
        target_doctor = None
        for doctor_id_ in doctors:
            if doctor_id_ == doctor_id:
                target_doctor = doctors[doctor_id_]
                break

        if not target_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        
        target_doctor.name = payload.name
        target_doctor.specialization = payload.specialization
        target_doctor.phone = payload.phone
        target_doctor.is_available = payload.is_available


        return target_doctor


    @staticmethod
    def delete_doctors(doctor_id):
        target_doctor = None
        for doctor_id_ in doctors:
            if doctor_id_ == doctor_id:
                target_doctor = doctors[doctor_id_]
                break
        if not target_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        
        del doctors[doctor_id_]

        return target_doctor


  
    @staticmethod
    def change_status(doctor_id:int, payload:bool):
        target_doctor = None
        for doctor_id_ in doctors:
            if doctor_id_ == doctor_id:
                target_doctor = doctors[doctor_id_]
                break

        if not target_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        
        target_doctor.is_available = payload

        return target_doctor



doctor_service = DoctorService()
