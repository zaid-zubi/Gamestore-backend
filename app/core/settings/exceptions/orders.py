from fastapi import status

from app.core.settings.base_exception import AppException
from app.core.settings.constants import ResponseMessages


class OrderNotFound(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(
            message or ResponseMessages.Error.ORDER_NOT_FOUND,
            status.HTTP_404_NOT_FOUND,
        )