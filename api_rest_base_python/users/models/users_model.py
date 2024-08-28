from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from config.db_config import engine
import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'catUsers'

    nId = Column(Integer, primary_key=True)
    cNombre = Column(String(150))
    cApellido = Column(String(150))
    cEmail = Column(String(250), unique=True)
    cPassword = Column(String(50))
    dAlta = Column(DateTime, default=datetime.datetime.now)
    bIsActive = Column(Boolean, default=True)

Base.metadata.create_all(engine)

