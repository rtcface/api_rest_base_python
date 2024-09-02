from datetime import timedelta

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import UUID4
from sqlalchemy.orm import Session

from security import get_password_hash, pwd_context, create_access_token
from config.settings import settings
from users.repository.user_repository import UserRepository
