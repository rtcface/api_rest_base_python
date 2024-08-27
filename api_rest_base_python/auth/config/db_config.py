from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker 
from decouple import config

url = URL(
    drivername=config("DB_DRIVER"),
    username=config("POSTGRES_USER"),
    password=config("POSTGRES_PASSWORD"),
    host=config("POSTGRES_HOST"),
    port=config("POSTGRES_PORT"),
    database=config("POSTGRES_DB"),
)

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()




