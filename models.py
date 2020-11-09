from database import engine
from sqlalchemy import ForeignKey,Column,String,Integer,Numeric ,MetaData ,Table

import models


metadata = MetaData()

Create_job = Table(
	'jobs',
	metadata,
	Column("id",Integer,primary_key=True, index=True),
	Column("Job_title",String,index=True),
	Column("Company_name",String, index=True),
	Column("Qualification",String,index=True),
	Column("Email_No",String,index=True),
	Column("Description",String,index=True),
	Column("Experience",Integer,index=True),
	Column("Salary",Integer, index=True),

)


Create_Cand = Table(
    'candidates',
	metadata,
	Column("id",Integer,primary_key=True, index=True),
	Column("Name",String,index=True),
	Column("Mobile_No",String,index=True),
	Column("Email_No",String,index=True),
	Column("Qualification",String,index=True),
	Column("Experience",Integer,index=True),

)

Create_job_app = Table(
	'Job_applications',
	metadata,
	Column("id",Integer,primary_key = True , index = True),
	Column("jobs_apply",Integer,ForeignKey("jobs.id",ondelete="CASCADE")),
	Column("Candidates_apply",Integer,ForeignKey("candidates.id",ondelete="CASCADE")),

)


	
metadata.create_all(engine)
