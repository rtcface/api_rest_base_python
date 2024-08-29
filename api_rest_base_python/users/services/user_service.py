from typing import List, Optional

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from users.repository.user_repository import UserRepository
from users.schemas.users_schema import AddUserInput, UserOutput, UpdateUserInput, DeleteUserInput

class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def create(self, user: AddUserInput) -> UserOutput:
        return self.repository.create(user)
    
    def get(self, uuid: UUID4) -> UserOutput:
        return self.repository.get(uuid)
    
    def update(self, user: UpdateUserInput) -> UserOutput:
        return self.repository.update(user)
    
    def delete(self, user: DeleteUserInput) -> None:
        self.repository.delete(user)
    
    def get_all(self) -> List[UserOutput]:
        return self.repository.get_all()
