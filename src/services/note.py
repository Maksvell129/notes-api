from pydantic import PositiveInt

from src.db.models.note import Note
from src.db.repository.note import NoteRepository
from src.db.schemas.note import CreateNoteSchema
from src.exceptions import NotFoundException
from src.services import board
from src.services.base import BaseService


class NoteService(BaseService):
    repository_class = NoteRepository

    async def create(self, note: CreateNoteSchema) -> Note:
        if not await board.BoardService().exists(entity_id=note.board_id):
            raise NotFoundException(detail="Board not found")

        return await self.repository.create(note.model_dump())

    async def add_views(self, note_id: PositiveInt, views: int) -> Note:
        return await self.repository.add_views(note_id=note_id, views=views)
