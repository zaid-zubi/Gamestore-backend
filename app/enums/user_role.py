from enum import StrEnum


class UserRole(StrEnum):
    ADMIN = "admin"
    USER = "user"

    @classmethod
    def list(cls):
        return [role.value for role in cls]