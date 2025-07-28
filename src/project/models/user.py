from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String, select
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column, relationship
from fastapi import Depends, HTTPException
from starlette import status
from ..database import Base


class User(MappedAsDataclass, Base, unsafe_hash=True):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, init=False, primary_key=True)
    name: Mapped[str | None] = mapped_column(String, nullable=True, default=None)