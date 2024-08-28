from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker 
from decouple import config


#nurl = "postgresql+psycopg://postgres:postgres@localhost:5432/postgres"

url = URL.create(config("DB_DRIVER"), config("POSTGRES_USER"), config("POSTGRES_PASSWORD"), config("POSTGRES_HOST"), config("POSTGRES_PORT"), config("POSTGRES_DB"))
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()




