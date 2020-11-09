from typing import List
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import *
from database import *
from models import *

app = FastAPI()

# origins = [
#    "http://192.168.1.19:8080/"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get('/')
def job():
	return {'hello':'Helloworld'}

@app.post('/jobs/create/' ,response_model = job_create)
async def createjob(jc:job_create):
    query = Create_job.insert().values(Company_name=jc.Company_name,Job_title=jc.Job_title,Qualification=jc.Qualification,Email_No=jc.Email_No,Description=jc.Description,Experience=jc.Experience,Salary=jc.Salary)
    last = await data_base.execute(query)
    return {**jc.dict(),'id':last}

@app.delete('/jobs/delete/{id}')
async def del_job(id:int):
    query = Create_job.delete().where(Create_job.c.id == id)
    await data_base.execute(query)
    return 

@app.get('/jobs/getalljobs/',response_model=List[job_create])
async def get_jobs(skip:int=0,take:int=20):
    query = Create_job.select().offset(skip).limit(take)
    return await data_base.fetch_all(query)    

@app.get('/jobs/getjobs/{id}',response_model=job_create)
async def get_jobs(id:int):
    query = Create_job.select().where(Create_job.c.id == id)
    return await data_base.fetch_one(query)

@app.patch('/jobs/update/{id}',response_model=job_create)
async def update_jobs(id:int,jc:job_create):
    query = Create_job.update().where(Create_job.c.id == id).values(Company_name=jc.Company_name,Job_title=jc.Job_title,Qualification=jc.Qualification,Email_No=jc.Email_No,Description=jc.Description,Experience=jc.Experience,Salary=jc.Salary)
    await data_base.execute(query)
    return {**jc.dict(),'id':id}

@app.post('/jobs/candidates/' ,response_model = Cand_create)
async def cand_reg(jc:Cand_create):
    query = Create_Cand.insert().values(Name=jc.Name,Mobile_No=jc.Mobile_No,Qualification=jc.Qualification,Email_No=jc.Email_No,Experience=jc.Experience)
    last = await data_base.execute(query)
    return {**jc.dict(),'id':last}





