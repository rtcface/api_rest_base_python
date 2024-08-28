from pydantic import BaseModel


class AddUser(BaseModel):
    cNombre: str
    cApellido: str
    cEmail: str
    cPassword: str
