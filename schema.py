from pydantic import BaseModel,EmailStr
from typing import Optional

class job_create(BaseModel):
    
	Company_name:str
	Salary : Optional[int] = None
	Job_title: str
	Qualification:str
	Experience:int
	Email_No:Optional[EmailStr] = None
	Description:str 

class _job_c(job_create):
    id:int
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

        
        