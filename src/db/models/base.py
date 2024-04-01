from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class CreateMixin:
    created_at = Column(DateTime, default=datetime.now)


class UpdateMixin:
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
