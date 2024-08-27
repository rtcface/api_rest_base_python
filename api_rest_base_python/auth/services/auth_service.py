from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi import HTTPException, status
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from decouple import config

SCRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES")

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    cName: str
    cEmail: str
    bIsActive: bool

class UserInDB(User):
    id: int
    password: str
