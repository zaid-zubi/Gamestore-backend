from pydantic import BaseModel

from app.enums.locations import LocationEnum


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    location: LocationEnum

    class Config:
        from_attributes = True
