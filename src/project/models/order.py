from __future__ import annotations
import datetime
from typing import List

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
from ..utils.enum import OrderStatus
from ..models import User

class Order(MappedAsDataclass, Base, unsafe_hash=True):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, init=False, primary_key=True)

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User", backref=backref("orders", passive_deletes=True)
    )

    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False
    )
    total_price: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False, init=False
    )

    @staticmethod
    def get_all(session: Session, user_id: int) -> List["Order"]:
        stmt = select(Order).where(Order.user_id == user_id)
        result = session.execute(stmt)
        return result.scalars().all()
