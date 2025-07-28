from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class OrderItemSchema(BaseModel):
    product_name: str = Field(min_length=3, max_length=100)
    unit_price: str = Field(min_length=3, max_length=100)
    quantity: int = Field(gt=0)

    class Config:
        from_attributes = True


class OrderSchema(BaseModel):
    id: int
    created_at: datetime
    total_price: float = Field(ge=0)
    status: str = Field(min_length=3, max_length=20)
    items: List[OrderItemSchema]

    class Config:
        from_attributes = True




