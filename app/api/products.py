from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.settings.database import get_db
from app.core.settings.dependencies import get_current_user
from app.core.settings.response import http_response
from app.core.settings.constants import ResponseMessages
from app.enums.language import Language
from app.enums.locations import LocationEnum
from app.services.product import get_products, get_product

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("")
def list_products(
        skip: int = 0,
        limit: int = 10,
        location: LocationEnum | None = Query(default=None),
        language: Language = Query(default=Language.EN),
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
):
    data = get_products(db, skip, limit, location)
    return http_response(status=status.HTTP_200_OK,
                         message=ResponseMessages.GENERAL.READ.get(language),
                         data=data)


@router.get("/{product_id}")
def product_details(
        product_id: int,
        db: Session = Depends(get_db),
        language: Language = Query(default=Language.EN),
        user=Depends(get_current_user),
):
    product = get_product(db, product_id)
    return http_response(status=status.HTTP_200_OK,
                         message=ResponseMessages.GENERAL.READ.get(language),
                         data=product)
