from src.db.models.note import Note
from src.db.repository.base import BaseRepository


class NoteRepository(BaseRepository):
    model = Note

    async def add_views(self, note_id: int, views: int):
        note = await self.get_by_id(note_id)

        await self.update(note.id, {"views": note.views + views})
        return await self.get_by_id(note_id)
