# Doctor's Appointment API

This API provides endpoints for managing doctor's appointments with their patients. 
Patients can create appointments
doctors can set their availability and appointments can be completed or canceled.


## ENDPOINTS
## PATIENTS
### get all the patients 
`GET /patient GET Patients`

### Create Patient
`POST /patient Create Patient`

### Update Patient information
`PUT /patient/{patient_id } Update Patient`

### Delete patient

`DELETE /patient/{patient_id/ Delete Patient`

## DOCTORS
### get all the doctors 
`GET /doctors Get Doctors`

### Create Doctor
`POST /doctors Create Doctor`

### Update Doctor's information
`PUT /doctors/{doctor_id } Update Doctor`

### Delete Doctor

`DELETE /doctors{doctor_id/ Delete Doctor`


### Change Doctor Availabilty status
`PUT /doctors/{doctor_id }/status Change Doctor's Status`



## APPOINTMENTS
### get all the appointments 
`GET /appointments Get Appointments`

### Create Appointment
`POST /appointments  Create Appointment `

### Complete Appointment
`PUT /appointments/{appointment_id }/status Complete Appointment`


### Cancel Appoint

`DELETE /appointments{appointments_id/ Cancel Appointment`



# Models

## Patient
- id (integer): ID of the patient.
- name (string): Name of the patient.
- age (int): Age of the patient
- sex(string): Sex of the patient
- weight(float): Weight of the patient
- height(float): Height of the patient
- phone(int): Phone of the patient

## Doctor
- id (integer): ID of the doctor.
- name (string): Name of the doctor.
- specialization(string): Doctor's specialization
- phone(string): Doctors phone
- is_available (boolean): Availability status of the doctor.


## Appointment
- id (integer): ID of the appointment.
- patient_id (integer): ID of the patient.
- doctor_id (integer): ID of the assigned doctor.
- date (date): Date of the appointment.
- status (string): Status of the appointment (pending/completed).


# Usage
- Start the server.
- Use the provided endpoints to manage patients, appointments, doctors and doctor availability.
- Ensure proper authentication and authorization mechanisms are in place.
