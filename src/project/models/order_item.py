from __future__ import annotations
import datetime
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Enum,
    Text,
    func,
    select,
    desc,
)
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    Session,
    mapped_column,
    backref,
    relationship,
)

from ..database import Base
from ..models import Order


class OrderItem(MappedAsDataclass, Base, unsafe_hash=True):

    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, init=False, primary_key=True)

    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
    )

    order: Mapped["Order"] = relationship(
        "Order", backref=backref("items", passive_deletes=True)
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    unit_price: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False, init=False
    )
    product_name: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)