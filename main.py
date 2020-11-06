from typing import List
from sqlalchemy.orm import Session
from fastapi import FastAPI

from schema import job_create ,_job_c
from database import *
from models import *

app = FastAPI()

@app.get('/')
def job():
	return {'hello':'Helloworld'}

@app.post('/jobs/create/' ,response_model = _job_c)
async def createjob(jc:job_create):
    query = Create_job.insert().values(Company_name=jc.Company_name,Job_title=jc.Job_title,Qualification=jc.Qualification,Email_No=jc.Email_No,Description=jc.Description,Experience=jc.Experience,Salary=jc.Salary)
    last = await data_base.execute(query)
    return {**jc.dict(),'id':last}

@app.delete('/jobs/delete/{id}')
async def del_job(id:int):
    query = Create_job.delete().where(Create_job.c.id == id)
    await data_base.execute(query)
    return 

@app.get('/jobs/getalljobs/',response_model=List[_job_c])
async def get_jobs(skip:int=0,take:int=20):
    query = Create_job.select().offset(skip).limit(take)
    return await data_base.fetch_all(query)    

@app.get('/jobs/getjobs/{id}',response_model=_job_c)
async def get_jobs(id:int):
    query = Create_job.select().where(Create_job.c.id == id)
    return await data_base.fetch_one(query)



@app.post('/jobs/update/{id}',response_model=_job_c)
async def update_jobs(id:int,jc:job_create):
    query = Create_job.update().where(Create_job.c.id == id).values(Company_name=jc.Company_name,Job_title=jc.Job_title,Qualification=jc.Qualification,Email_No=jc.Email_No,Description=jc.Description,Experience=jc.Experience,Salary=jc.Salary)
    await data_base.execute(query)
    return {**jc.dict(),'id':id}


