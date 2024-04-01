import fastapi
from fastapi import status
from pydantic import NonNegativeInt
from pydantic import PositiveInt

from src.db.schemas.board import BoardSchema
from src.db.schemas.board import CreateBoardSchema
from src.db.schemas.board import UpdateBoardSchema
from src.services.board import BoardService

router = fastapi.APIRouter()


@router.post(
    "/",
    response_model=BoardSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_board(board: CreateBoardSchema):
    return await BoardService().create_board(board=board)


@router.get(
    "/{board_id}",
    response_model=BoardSchema,
    status_code=status.HTTP_200_OK,
)
async def read_board(board_id: PositiveInt):
    return await BoardService().get_board(board_id=board_id)


@router.get(
    "/",
    response_model=list[BoardSchema],
    status_code=status.HTTP_200_OK,
)
async def get_boards(skip: NonNegativeInt = 0, limit: NonNegativeInt = 100):
    return await BoardService().get_all_boards(skip=skip, limit=limit)


@router.put(
    "/{board_id}",
    response_model=BoardSchema,
    status_code=status.HTTP_200_OK,
)
async def update_existing_board(board_id: PositiveInt, board: UpdateBoardSchema):
    return await BoardService().update_board(board_id=board_id, board=board)


@router.delete(
    "/{board_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_existing_board(board_id: PositiveInt):
    return await BoardService().delete_board(board_id=board_id)


@router.post("{board_id}/add_note/{note_id}", response_model=BoardSchema)
async def add_note_to_board(board_id: PositiveInt, note_id: PositiveInt):
    return await BoardService().add_note_to_board(board_id, note_id)


@router.post("{board_id}/remove_note/{note_id}", response_model=BoardSchema)
async def remove_note_from_board(board_id: PositiveInt, note_id: PositiveInt):
    return await BoardService().remove_note_from_board(board_id, note_id)
