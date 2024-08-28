from pydantic import BaseModel


class UpdateUser(BaseModel):
    cNombre:srt
    cApellido:str
    cEmail:str
