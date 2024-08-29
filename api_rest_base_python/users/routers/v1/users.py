from typing import List

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.db_config import get_db
from users.schemas.users_schema import AddUserInput, UserOutput, UpdateUserInput, DeleteUserInput
from users.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)]
)

@router.post("/", response_model=UserOutput)
def create_user(user: AddUserInput, db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.create(user)

@router.get("/{uuid}", response_model=UserOutput)
def get_user(uuid: UUID4, db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.get(uuid)

@router.put("/", response_model=UserOutput)
def update_user(user: UpdateUserInput, db: Session = Depends(get_db)):
    _service = UserService(db)
    print(user)
    return _service.update(user)

@router.delete("/{uuid}", response_model=None)
def delete_user(user: DeleteUserInput, db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.delete(user)

@router.get("/", response_model=List[UserOutput])
def get_all_users(db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.get_all()



