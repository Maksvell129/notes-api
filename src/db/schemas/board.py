from datetime import datetime

from pydantic import BaseModel
from pydantic import PositiveInt

from src.db.schemas.note import NoteSchema


class UpdateBoardSchema(BaseModel):
    name: str | None


class CreateBoardSchema(BaseModel):
    name: str


class BoardSchema(CreateBoardSchema):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    notes: list[NoteSchema] = []

    class Config:
        orm_mode = True
