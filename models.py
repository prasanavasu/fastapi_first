from database import engine
from sqlalchemy import Column,String,Integer,Numeric ,MetaData ,Table

import models


metadata = MetaData()

Create_job = Table(
	'job',
	metadata,
	Column("id",Integer,primary_key=True, index=True),
	Column("Company_name",String, index=True),
	Column("Job_title",String,index=True),
	Column("Qualification",String,index=True),
	Column("Email_No",String,index=True),
	Column("Description",String,index=True),
	Column("Experience",Integer,index=True),
	Column("Salary",Integer, index=True),

)

	
metadata.create_all(engine)

