from sqlalchemy import String, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.enums.locations import LocationEnum
from app.models.base import Base, IntIDMixin, TimestampMixin


class Product(Base, IntIDMixin, TimestampMixin):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String, nullable=False)

    price: Mapped[float] = mapped_column(Float, nullable=False)

    location: Mapped[LocationEnum] = mapped_column(
        Enum(LocationEnum),
        nullable=False,
        index=True
    )