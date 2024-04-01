from datetime import datetime

from pydantic import BaseModel
from pydantic import NonNegativeInt
from pydantic import PositiveInt


class CreateNoteSchema(BaseModel):
    text: str
    board_id: PositiveInt | None


class UpdateNoteSchema(BaseModel):
    text: str | None


class NoteSchema(CreateNoteSchema):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    views: NonNegativeInt

    class Config:
        orm_mode = True
