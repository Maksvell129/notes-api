import fastapi
from fastapi import status
from pydantic import NonNegativeInt
from pydantic import PositiveInt

from src.db.schemas.note import CreateNoteSchema
from src.db.schemas.note import NoteSchema
from src.db.schemas.note import UpdateNoteSchema
from src.services.note import NoteService

router = fastapi.APIRouter()


@router.post(
    "/",
    response_model=NoteSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_note(note: CreateNoteSchema):
    return await NoteService().create_note(note=note)


@router.get(
    "/{note_id}",
    response_model=NoteSchema,
    status_code=status.HTTP_200_OK,
)
async def read_note(note_id: PositiveInt):
    return await NoteService().get_note(note_id=note_id)


@router.get(
    "/",
    response_model=list[NoteSchema],
    status_code=status.HTTP_200_OK,
)
async def get_notes(skip: NonNegativeInt = 0, limit: NonNegativeInt = 100):
    return await NoteService().get_all_notes(skip=skip, limit=limit)


@router.put(
    "/{note_id}",
    response_model=NoteSchema,
    status_code=status.HTTP_200_OK,
)
async def update_existing_note(note_id: PositiveInt, note: UpdateNoteSchema):
    return await NoteService().update_note(note_id=note_id, note=note)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_note(note_id: PositiveInt):
    await NoteService().delete_note(note_id=note_id)