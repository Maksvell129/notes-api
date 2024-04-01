from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from src.db.models.base import Base
from src.db.models.base import CreateMixin
from src.db.models.base import UpdateMixin


class Board(Base, CreateMixin, UpdateMixin):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    notes = relationship(
        "Note", back_populates="board", cascade="all, delete", lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"Board(name={self.name})"
