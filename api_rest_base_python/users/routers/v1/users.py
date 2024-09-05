from typing import List

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.db_config import get_db
from users.schemas.users_schema import AddUserInput, UserOutput, UpdateUserInput, DeleteUserInput, GetUserByUuid
from users.services.user_service import UserService

from auth.services.auth_service import AuthService
from auth.services.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)]
)

@router.post("/", response_model=UserOutput)
def register_user(user: AddUserInput, db: Session = Depends(get_db), auth_service: AuthService = Depends( get_current_user  )):
    _service = UserService(db)
    return _service.create(user)

@router.get("/{uuid}", response_model=UserOutput)
def get_user(uuid:UUID4 ,db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.get(uuid)

@router.put("/", response_model=UserOutput)
def update_user(user: UpdateUserInput, db: Session = Depends(get_db)):
    _service = UserService(db)
    print(user)
    return _service.update(user)

@router.delete("/{uuid}", response_model=None)
def delete_user(uuid: UUID4, db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.disable(uuid)
# Funcion para habilitar un usuario
@router.post("/enable/{uuid}", response_model=UserOutput)
def enable_user(uuid: UUID4, db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.enable(uuid)

@router.get("/", response_model=List[UserOutput])
def get_all_users(db: Session = Depends(get_db)):
    _service = UserService(db)
    return _service.get_all()



