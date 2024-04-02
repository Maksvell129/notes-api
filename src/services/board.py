from pydantic import PositiveInt

from src.db.models import Board
from src.db.repository.board import BoardRepository
from src.exceptions import NotFoundException
from src.services.base import BaseService
from src.services.note import NoteService


class BoardService(BaseService):
    repository_class = BoardRepository

    async def add_note_to_board(
        self, board_id: PositiveInt, note_id: PositiveInt
    ) -> Board:
        if not await self.exists(entity_id=board_id):
            raise NotFoundException(detail="Board not found")

        if not await NoteService().exists(entity_id=note_id):
            raise NotFoundException(detail="Note not found")

        return await self.repository.add_note_to_board(board_id, note_id)

    async def remove_note_from_board(
        self, board_id: PositiveInt, note_id: PositiveInt
    ) -> Board:
        if not await self.exists(entity_id=board_id):
            raise NotFoundException(detail="Board not found")

        if not await NoteService().exists(entity_id=note_id):
            raise NotFoundException(detail="Note not found")

        return await self.repository.remove_note_from_board(board_id, note_id)
