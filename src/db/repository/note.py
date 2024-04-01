from src.db.models.note import Note
from src.db.repository.base import BaseRepository


class NoteRepository(BaseRepository):
    model = Note
