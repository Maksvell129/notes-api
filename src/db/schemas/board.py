from datetime import datetime

from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from src.db.schemas.note import NoteSchema


class CreateBoardSchema(BaseModel):
    name: str = Field(min_length=3, max_length=255)


class UpdateBoardSchema(CreateBoardSchema):
    pass


class BoardSchema(CreateBoardSchema):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    notes: list[NoteSchema] = []

    class Config:
        orm_mode = True
