from pydantic import BaseModel

class DeleteUser(BaseModel):
    nId: int
