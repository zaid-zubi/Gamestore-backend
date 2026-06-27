from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.enums.locations import LocationEnum
from app.models.product import Product
from app.schemas.product import ProductResponse
from app.services.crud import crud


def get_products(db: Session, skip: int, limit: int, location: LocationEnum | None) -> list[ProductResponse]:
    filters = {}

    if location is not None:
        filters["location"] = location

    return crud.get_all(
        db,
        Product,
        skip=skip,
        limit=limit,
        **filters,
    )


def get_product_by_id(db: Session, product_id: int):
    product = crud.get_one(db, Product, id=product_id)
    return product


def get_product(db: Session, product_id: int) -> ProductResponse:
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
