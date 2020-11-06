from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databases
from fastapi import FastAPI

''' FastAPI CONFIGURATION '''
app = FastAPI()
SQLALCHEMY_DATABASE_URL = "sqlite:///./jobs.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
data_base = databases.Database(SQLALCHEMY_DATABASE_URL)




''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
    await data_base.connect()


@app.on_event("shutdown")
async def shutdown():
    await data_base.disconnect()
