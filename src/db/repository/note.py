from pydantic import PositiveInt

from src.db.models.note import Note
from src.db.repository.base import BaseRepository


class NoteRepository(BaseRepository):
    model = Note

    async def add_views(self, note_id: PositiveInt, views: int) -> Note:
        note = await self.get_one(id=note_id)

        await self.update(note.id, {"views": note.views + views})
        return await self.get_one(id=note_id)
