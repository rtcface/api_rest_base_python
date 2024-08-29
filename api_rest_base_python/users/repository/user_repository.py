from sqlalchemy.orm import Session
from users.models.users_model import Users 
from users.schemas.users_schema import AddUserInput, UserOutput, UpdateUserInput, DeleteUserInput
from typing import List, Optional, Type
from pydantic import ValidationError, UUID4

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: AddUserInput) -> UserOutput:
        try:
            new_user = Users(
                cNombre=user.cNombre,
                cApellido=user.cApellido,
                cEmail=user.cEmail,
                cPassword=user.cPassword
            )
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return UserOutput(
                uuid=new_user.uuid,
                cNombre=new_user.cNombre,
                cApellido=new_user.cApellido,
                cEmail=new_user.cEmail
            )
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get(self, uuid: UUID4) -> UserOutput:
        try:
            user = self.session.query(Users).filter(Users.uuid == uuid).first()
            if user is None:
                raise ValueError(f"User with UUID {uuid} not found")
            return UserOutput(
                uuid=user.uuid,
                cNombre=user.cNombre,
                cApellido=user.cApellido,
                cEmail=user.cEmail
            )
        except Exception as e:
            raise e
    
    def update(self, user_input: UpdateUserInput) -> UserOutput:
        try:
            user = self.session.query(Users).filter(Users.uuid == user_input.uuid).first()
            if user is None:
                raise ValueError(f"User with UUID {user_input.uuid} not found")
            user.cNombre = user_input.cNombre if user_input.cNombre is not None else user.cNombre
            user.cApellido = user_input.cApellido if user_input.cApellido is not None else user.cApellido
            user.cEmail = user_input.cEmail if user_input.cEmail is not None else user.cEmail
            self.session.commit()
            self.session.refresh(user)
            return UserOutput(
                uuid=user.uuid,
                cNombre=user.cNombre,
                cApellido=user.cApellido,
                cEmail=user.cEmail
            )
        except Exception as e:
            self.session.rollback()
            raise e
    
    def delete(self, user: DeleteUserInput) -> None:
        try:
            user = self.session.query(Users).filter(Users.uuid == user.uuid).first()
            if user is None:
                raise ValueError(f"User with UUID {user.uuid} not found")
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_all(self) -> List[UserOutput]:
        try:
            users = self.session.query(Users).all()
            return [UserOutput(
                uuid=user.uuid,
                cNombre=user.cNombre,
                cApellido=user.cApellido,
                cEmail=user.cEmail
            ) for user in users]
        except Exception as e:
            raise e
