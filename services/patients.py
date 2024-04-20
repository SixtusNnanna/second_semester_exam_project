from fastapi import HTTPException
from schemas.patient import Patient, PatientCreate, patients

class PatientService:


    @staticmethod
    def create_patient(payload:PatientCreate):
        patient_id = len(patients) + 1
    
        patient = Patient(
            id=patient_id,
            **payload.model_dump(),)
        patients[patient_id] = patient

        return patient
    

    
    @staticmethod
    def update_patient(patient_id:int ,payload:Patient):
        target_patient = None
        for patient_id_ in patients:
            if patient_id_ == patient_id:
                target_patient = patients[patient_id_]
                break
        if not target_patient:
            raise HTTPException(status_code = 404, detail = "Patient not found")
        
        target_patient.name = payload.name
        target_patient.age = payload.age
        target_patient.sex = payload.sex
        target_patient.weight = payload.weight
        target_patient.height = payload.height
        target_patient.phone = payload.phone
    
        return target_patient
    

    @staticmethod
    def delete_patient(patient_id:int):
        target_patient = None
        for patient_id_ in patients:
            if patient_id_ == patient_id:
                target_patient = patients[patient_id_]
                break
        if not target_patient:
            raise HTTPException(status_code = 404, detail = "Patient not found")
        
        del patients[patient_id_]
        return target_patient



patient_services = PatientService()
            