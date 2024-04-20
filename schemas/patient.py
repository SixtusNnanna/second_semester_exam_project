from pydantic import BaseModel


#Patient: id, name, age, sex, weight, height, phone

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int


class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str



patients:dict[int, Patient] = {
    1:Patient(id=1, name="Theresa", age=22, sex="Female", weight=70, height=1.80, phone="7035466723"),
    2:Patient(id=2, name="James", age=25, sex="Male", weight=90, height=1.97, phone="8076543210"),
    3:Patient(id=3, name="Munachiso", age=24, sex="Male", weight=87, height=1.86, phone="8176543210"),
    4:Patient(id=4, name="Mmesomma", age=21, sex="Female", weight=65, height=1.65, phone="9176543210"),
}