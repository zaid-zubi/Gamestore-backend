import getpass
import re

from sqlalchemy import select

from app.core.settings.database import SessionLocal
from app.core.settings.security import hash_password
from app.enums.user_role import UserRole
from app.models.user import User

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def validate_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email) is not None


def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if len(password) > 128:
        return False, "Password must be less than 128 characters"
    return True, ""


def create_admin():
    print("\n**** Create your default Admin account ****\n")

    email = input("Enter admin email: ").strip()

    if not validate_email(email):
        print("❌ Invalid email format")
        return

    password = getpass.getpass("Enter admin password: ").strip()
    confirm_password = getpass.getpass("Confirm admin password: ").strip()

    if password != confirm_password:
        print("❌ Passwords do not match")
        return

    is_valid, msg = validate_password(password)
    if not is_valid:
        print(f"❌ {msg}")
        return

    with SessionLocal() as db:
        existing = db.scalar(
            select(User).where(User.email == email)
        )

        if existing:
            print("⚠️ Admin already exists with this email")
            return

        admin = User(
            email=email,
            hashed_password=hash_password(password),
            role=UserRole.ADMIN,
            is_active=True,
        )

        db.add(admin)
        db.commit()

        print("✅ Admin created successfully")


if __name__ == "__main__":
    create_admin()