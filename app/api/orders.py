from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.settings.database import get_db
from app.core.settings.dependencies import get_current_user
from app.core.settings.response import http_response
from app.core.settings.constants import ResponseMessages
from app.enums.language import Language
from app.schemas.order import OrderCreateRequest
from app.services.order import create_order, get_order_receipt

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("")
def create_new_order(
        payload: OrderCreateRequest,
        db: Session = Depends(get_db),
        language: Language = Query(default=Language.EN),
        user=Depends(get_current_user),
):
    order = create_order(db=db, user=user, product_id=payload.product_id)

    return http_response(
        status=status.HTTP_201_CREATED,
        message=ResponseMessages.GENERAL.CREATE.get(language),
        data=order
    )

@router.get("/{order_id}")
def order_receipt(
        order_id,
        db: Session = Depends(get_db),
        language: Language = Query(default=Language.EN),
        user=Depends(get_current_user),
):
    order = get_order_receipt(db=db, order_id=order_id, user=user)

    return http_response(
        status=status.HTTP_200_OK,
        message=ResponseMessages.GENERAL.READ.get(language),
        data=order
    )