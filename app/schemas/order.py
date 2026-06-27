from pydantic import BaseModel


class OrderCreateRequest(BaseModel):
    product_id: int

