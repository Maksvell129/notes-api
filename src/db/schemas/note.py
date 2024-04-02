from datetime import datetime

from pydantic import BaseModel
from pydantic import Field
from pydantic import NonNegativeInt
from pydantic import PositiveInt


class CreateNoteSchema(BaseModel):
    text: str = Field(min_length=3, max_length=255)
    board_id: PositiveInt


class UpdateNoteSchema(BaseModel):
    text: str = Field(min_length=3, max_length=255)


class NoteSchema(CreateNoteSchema):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    views: NonNegativeInt

    class Config:
        orm_mode = True
