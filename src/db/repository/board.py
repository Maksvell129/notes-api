from pydantic import PositiveInt

from src.db.models.board import Board
from src.db.repository.base import BaseRepository
from src.db.repository.note import NoteRepository


class BoardRepository(BaseRepository):
    model = Board

    async def add_note_to_board(
        self, board_id: PositiveInt, note_id: PositiveInt
    ) -> Board:
        await NoteRepository().update(note_id, {"board_id": board_id})
        return await self.get_one(id=board_id)

    async def remove_note_from_board(
        self, board_id: PositiveInt, note_id: PositiveInt
    ) -> Board:
        await NoteRepository().update(note_id, {"board_id": None})
        return await self.get_one(id=board_id)
