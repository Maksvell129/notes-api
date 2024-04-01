from typing import Sequence

from fastapi import HTTPException
from fastapi import status
from pydantic import NonNegativeInt
from pydantic import PositiveInt

from src.db.models.note import Note
from src.db.repository.note import NoteRepository
from src.db.schemas.note import CreateNoteSchema
from src.db.schemas.note import UpdateNoteSchema
from src.services.board import BoardService


class NoteService:
    def __init__(self):
        self.repository = NoteRepository()

    async def get_note(self, note_id: PositiveInt) -> Note:
        if await self.exists_by_id(note_id=note_id):
            return await self.repository.get_by_id(entity_id=note_id)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )

    async def create_note(self, note: CreateNoteSchema) -> Note:
        if not await BoardService().exists_by_id(board_id=note.board_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.create(note.model_dump())

    async def update_note(self, note_id: PositiveInt, note: UpdateNoteSchema) -> Note:
        if not await self.repository.exists_by_id(entity_id=note_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
            )

        return await self.repository.update(entity_id=note_id, data=note.model_dump())

    async def delete_note(self, note_id: PositiveInt):
        if not await self.repository.exists_by_id(entity_id=note_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
            )

        return await self.repository.delete(entity_id=note_id)

    async def get_all_notes(
        self, skip: NonNegativeInt = 0, limit: NonNegativeInt = 100
    ) -> Sequence[Note]:
        return await self.repository.get_all(skip, limit)

    async def exists_by_id(self, note_id):
        return await self.repository.exists_by_id(entity_id=note_id)
