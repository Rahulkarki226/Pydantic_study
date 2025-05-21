from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title='Name of the patient',description='Give the name of the patient in less than 50 chars', examples=['Rahul','Rohit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: Annotated[float,Field(gt=0,strict=True)]
    married :Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies : Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated')

patient_info ={'name':'Rahul','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':'30','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'123132123'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)