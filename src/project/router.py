from typing import Annotated, List, Optional
from fastapi import Query
from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Body, Path
from starlette import status
from src.project.models import Order
from src.project.dependencies import get_db_session
from src.project.models import User
from src.project.schemas import OrderSchema


router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=List[OrderSchema], status_code=status.HTTP_200_OK)
async def get_orders(
    user_id: int,
    session: Session = Depends(get_db_session)
):
    try:
        db_user = session.scalar(select(User).where(User.id == user_id))
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        orders = session.execute(
            select(Order).where(Order.user_id == user_id)
        ).scalars().all()

        return orders

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )