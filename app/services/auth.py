from sqlalchemy.orm import Session

from app.core.settings.security import hash_password, verify_password, create_access_token
from app.core.settings.exceptions.auth import UserAlreadyExists, IncorrectEmailOrPassword, InactiveUser
from app.core.settings.logging import logger
from app.models.user import User
from app.schemas.auth import TokenResponse, LoginRequest, RegisterRequest, UserResponse


def get_user_by_email(db: Session, email: str) -> User | None:
    logger.info(f"Fetching user by email: {email}")
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, body: RegisterRequest) -> User:
    logger.info(f"Creating user in DB: {body.email}")

    user = User(
        email=body.email,
        hashed_password=hash_password(body.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"User persisted in DB: id={user.id}, emails={user.email}")

    return user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    logger.info(f"Authenticating user: {email}")
    user = get_user_by_email(db, email)

    if user is None:
        logger.warning(f"Authentication failed: user not found ({email})")
        return None

    if not verify_password(password, user.hashed_password):
        logger.warning(f"Authentication failed: wrong password ({email})")
        return None

    logger.info(f"User authenticated successfully: {email}")
    return user


def register_user(body, db):
    logger.info(f"Registering new user with emails: {body.email}")

    existing = get_user_by_email(db, body.email)
    if existing is not None:
        logger.error(f"User already exists: {body.email}")
        raise UserAlreadyExists()

    new_user = create_user(db, body)

    logger.info(f"User created successfully: id={new_user.id}, emails={new_user.email}")

    return UserResponse.model_validate(new_user)


def login_user(data, db: Session) -> TokenResponse:
    logger.info(f"Login attempt: {data.username}")
    user = authenticate_user(db, data.username, data.password)
    if user is None:
        logger.warning(f"Login failed: invalid credentials {data.username}")
        raise IncorrectEmailOrPassword()
    if not user.is_active:
        logger.warning(f"Login blocked (inactive): {user.email}")
        raise InactiveUser()
    access_token = create_access_token(
        subject=str(user.id),
        role=user.role.value,
        email=user.email,
    )

    logger.info(f"Login successful: {user.email} (id={user.id})")

    return TokenResponse(access_token=access_token)
