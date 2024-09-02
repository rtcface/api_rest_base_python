from typing import List, Optional

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from users.repository.user_repository import UserRepository
from users.schemas.users_schema import AddUserInput, UserOutput, UpdateUserInput, DeleteUserInput
from auth.services.validate_password import ValidatePassword
from auth.services.email_validator import EmailValidator
from auth.services.security import get_password_hash



class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def create(self, user: AddUserInput) -> UserOutput:
        """
        Create a new user
        """
        if self.repository.user_exists_by_email(user.cEmail):
            raise HTTPException(status_code=400, detail="User already exists") 

        ValidatePassword(user.cPassword)
        EmailValidator().validate(user.cEmail)
        hashed_password = get_password_hash(user.cPassword)
        user.cPassword = hashed_password
        return self.repository.create(user)
    
    def get(self, uuid: UUID4) -> UserOutput:
        return self.repository.get(uuid)
    
    def update(self, user: UpdateUserInput) -> UserOutput:
        return self.repository.update(user)
    
    def disable(self, user: DeleteUserInput) -> None:
        self.repository.disable(user)

    def enable(self, user: DeleteUserInput) -> UserOutput:
        return self.repository.enable(user)
    
    def get_all(self) -> List[UserOutput]:
        return self.repository.get_all()
