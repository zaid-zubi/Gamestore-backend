from typing import Annotated

from fastapi import APIRouter, Depends, status, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.settings.database import get_db
from app.core.settings.dependencies import get_current_active_user
from app.core.settings.response import http_response
from app.core.settings.constants import ResponseMessages
from app.enums.language import Language
from app.models import User
from app.schemas.auth import (
    UserResponse,
    RegisterRequest
)
from app.services.auth import (
    register_user,
    login_user,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(
        data: RegisterRequest,
        language: Language = Query(default=Language.EN),
        db: Session = Depends(get_db),
):
    user = register_user(data, db)

    return http_response(
        status=status.HTTP_201_CREATED,
        message=ResponseMessages.GENERAL.CREATE.get(language),
        data=user
    )


@router.post("/login")
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
        language: Annotated[Language, Query()] = Language.EN,
):
    data = login_user(form_data, db)
    return data


@router.get("/me", response_model=UserResponse)
def read_current_user(
        current_user: Annotated[User, Depends(get_current_active_user)],
) -> UserResponse:
    return current_user


@router.post("/logout")
def logout(language: Language = Query(default=Language.EN)):
    return http_response(status=status.HTTP_200_OK,
                         message=ResponseMessages.AUTH.LOGOUT_SUCCESS.get(language))
