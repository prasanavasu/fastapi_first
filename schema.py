from pydantic import BaseModel,EmailStr
from typing import Optional

class job_create(BaseModel):
    	
    id:int
    Job_title: str
    Company_name:str
    Salary : Optional[int] = None
    Qualification:str
    Experience:int
    Email_No:Optional[EmailStr] = None
    Description:str 

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Cand_create(BaseModel):
	id:int
	Name:str
	Mobile_No:str
	Email_No: EmailStr
	Qualification:str
	Experience:str 

	class Config:
		orm_mode = True
		arbitrary_types_allowed = True      
        
class Application(BaseModel):
	id:int

	class Config:
		orm_mode = True
		arbitrary_types_allowed = True