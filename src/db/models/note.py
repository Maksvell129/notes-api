from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship

from src.db.models.base import Base
from src.db.models.base import CreateMixin
from src.db.models.base import UpdateMixin
from src.db.models.board import Board


class Note(Base, CreateMixin, UpdateMixin):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    views = Column(Integer, default=0)

    board_id = Column(Integer, ForeignKey("boards.id"), nullable=True)
    board = relationship(Board, back_populates="notes")

    def __repr__(self) -> str:
        return f"Note(text={self.text}, board={self.board})"

    async def add_views(self, views: int, session: AsyncSession):
        self.views += views
        await session.commit()
        await session.refresh(self)
