from sqlalchemy.orm import Session

from app.core.settings.exceptions.orders import OrderNotFound
from app.core.settings.exceptions.products import ProductNotFound
from app.models.order import Order
from app.models.product import Product
from app.services.crud import crud

def create_order(db: Session, user, product_id: int):
    product = crud.get_one(db, Product, id=product_id)

    if not product:
        raise ProductNotFound()

    order = Order(
        user_id=user.id,
        product_id=product.id,
        product_title=product.title,
        product_price=product.price,
        product_location=product.location,
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "id": order.id,
        "product_id": order.product_id,
        "user_id": order.user_id,
        "product_title": order.product_title,
        "product_price": order.product_price,
        "product_location": order.product_location,
        "created_at": order.created_at,
    }

def get_order_receipt(db: Session, order_id: int, user):
    order = crud.get_one(db, Order, id=order_id, user_id=user.id)

    if not order:
        raise OrderNotFound

    return {
        "id": order.id,
        "product_id": order.product_id,
        "product_title": order.product_title,
        "product_price": order.product_price,
        "product_location": order.product_location,
        "created_at": order.created_at,
    }