from src.db.models.board import Board
from src.db.repository.base import BaseRepository
from src.db.repository.note import NoteRepository


class BoardRepository(BaseRepository):
    model = Board

    async def add_note_to_board(self, board_id: int, note_id: int):
        board = await self.get_by_id(board_id)
        note = await NoteRepository().get_by_id(note_id)

        await NoteRepository().update(note.id, {"board_id": board.id})
        return await self.get_by_id(board_id)

    async def remove_note_from_board(self, board_id: int, note_id: int):
        note = await NoteRepository().get_by_id(note_id)

        await NoteRepository().update(note.id, {"board_id": None})
        return await self.get_by_id(board_id)
