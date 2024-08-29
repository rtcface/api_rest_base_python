from pydantic import BaseModel, Field, UUID4, EmailStr


class AddUserInput(BaseModel):
    cNombre: str = Field(min_length=2, max_length=150)
    cApellido: str = Field(min_length=2, max_length=150)
    cEmail: EmailStr = Field(min_length=2, max_length=254)
    cPassword: str = Field(min_length=6, max_length=254)

class UserOutput(BaseModel):
    uuid: UUID4
    cNombre: str
    cApellido: str
    cEmail: EmailStr

class UpdateUserInput(BaseModel):
    uuid: UUID4 = Field(..., alias="uuid")
    cNombre:str = Field(None, alias="cNombre")
    cApellido:str = Field(None, alias="cAapellido")
    cEmail:EmailStr = Field(None, alias="cEmail")

class DeleteUserInput(BaseModel):
    uuid: UUID4 = Field(..., description="The user's UUID")



