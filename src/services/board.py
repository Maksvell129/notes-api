from typing import Sequence

from fastapi import HTTPException
from fastapi import status
from pydantic import NonNegativeInt
from pydantic import PositiveInt

from src.db.models.board import Board
from src.db.repository.board import BoardRepository
from src.db.schemas.board import CreateBoardSchema
from src.db.schemas.board import UpdateBoardSchema


class BoardService:
    def __init__(self):
        self.repository = BoardRepository()

    async def get_board(self, board_id: PositiveInt) -> Board:
        if await self.exists_by_id(board_id=board_id):
            return await self.repository.get_by_id(entity_id=board_id)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
        )

    async def create_board(self, board: CreateBoardSchema) -> Board:
        return await self.repository.create(board.model_dump())

    async def update_board(
        self, board_id: PositiveInt, board: UpdateBoardSchema
    ) -> Board:
        if not await self.repository.exists_by_id(entity_id=board_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.update(entity_id=board_id, data=board.model_dump())

    async def delete_board(self, board_id: PositiveInt):
        if not await self.repository.exists_by_id(entity_id=board_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.delete(entity_id=board_id)

    async def get_all_boards(
        self, skip: NonNegativeInt = 0, limit: NonNegativeInt = 100
    ) -> Sequence[Board]:
        return await self.repository.get_all(skip, limit)

    async def add_note_to_board(self, board_id: int, note_id: int):
        if not await self.repository.exists_by_id(entity_id=board_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.add_note_to_board(board_id, note_id)

    async def remove_note_from_board(self, board_id: int, note_id: int):
        if not await self.repository.exists_by_id(entity_id=board_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.remove_note_from_board(board_id, note_id)

    async def exists_by_id(self, board_id):
        return await self.repository.exists_by_id(entity_id=board_id)
