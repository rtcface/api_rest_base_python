from pydantic import BaseModel, Field, UUID4, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    cNombre: str = Field(min_length=2, max_length=150)
    cApellido: str = Field(min_length=2, max_length=150)
    cEmail: EmailStr = Field(min_length=2, max_length=254)


class AddUserInput(UserBase):
    cPassword: str = Field(min_length=8, max_length=120)

class UserOutput(UserBase):
    uuid: UUID4 = Field(..., alias="id")
    bIsActive: bool
    dFechaRegistro: datetime
    dFechaModificacion: datetime
    dFechaBaja: Optional[datetime]=None


class UpdateUserInput(UserBase):
    uuid: UUID4 = Field(..., alias="uuid")

class DeleteUserInput(BaseModel):
    uuid: UUID4 = Field(..., description="The user's UUID")

class TokenData(BaseModel):
    username: Optional[str] = None

class TokenOutput(BaseModel):
    access_token: str
    token_type: str

