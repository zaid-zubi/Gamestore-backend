from fastapi import status

from app.core.settings.base_exception import AppException
from app.core.settings.constants import ResponseMessages


class UserNotFound(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(
            message or ResponseMessages.Error.USER_NOT_FOUND,
            status.HTTP_404_NOT_FOUND,
        )


class IncorrectEmailOrPassword(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(
            message or ResponseMessages.Error.INCORRECT_EMAIL_OR_PASSWORD,
            status.HTTP_401_UNAUTHORIZED,
        )


class UserAlreadyExists(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(
            message or "Email already registered",
            status.HTTP_409_CONFLICT,
        )


class InactiveUser(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(
            message or "User is inactive",
            status.HTTP_403_FORBIDDEN,
        )
