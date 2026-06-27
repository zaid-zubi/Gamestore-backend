from typing import Any

from pydantic import BaseModel, EmailStr

from app.enums.user_role import UserRole


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: str = UserRole.USER


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int | Any
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"