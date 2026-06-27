from datetime import datetime, timezone

from sqlalchemy import ForeignKey, Numeric, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, UUIDIDMixin, TimestampMixin


class Order(Base, UUIDIDMixin, TimestampMixin):
    __tablename__ = "orders"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        index=True,
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        index=True,
        nullable=False
    )

    product_title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    product_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    product_location: Mapped[str] = mapped_column(
        String(2),
        nullable=False
    )

    user = relationship("User", lazy="joined")
    product = relationship("Product", lazy="joined")