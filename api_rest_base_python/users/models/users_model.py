from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from config.db_config import engine
import datetime, uuid

Base = declarative_base()


class Users(Base):
    __tablename__ = 'catUsers'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cNombre = Column(String(150))
    cApellido = Column(String(150))
    cEmail = Column(String(250), unique=True)
    cPassword = Column(String(50))
    dAlta = Column(DateTime, default=datetime.datetime.now)
    bIsActive = Column(Boolean, default=True)

Base.metadata.create_all(engine)

