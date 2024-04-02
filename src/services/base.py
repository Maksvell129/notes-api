from typing import Sequence

from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel
from pydantic import NonNegativeInt
from pydantic import PositiveInt

from src.db.models import Base


class BaseService:
    repository_class = None

    def __init__(self):
        self.repository = self.repository_class()

    async def get_one(self, entity_id: PositiveInt) -> Base:
        if await self.exists(entity_id=entity_id):
            return await self.repository.get_one(id=entity_id)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
        )

    async def get_all(
        self, skip: NonNegativeInt = 0, limit: NonNegativeInt = 100
    ) -> Sequence[Base]:
        return await self.repository.get_all(skip, limit)

    async def create(self, entity: BaseModel) -> Base:
        return await self.repository.create(entity.model_dump())

    async def update_one(self, entity_id: PositiveInt, entity: BaseModel) -> Base:
        if not await self.exists(entity_id=entity_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Board not found"
            )

        return await self.repository.update(
            entity_id=entity_id, data=entity.model_dump()
        )

    async def delete(self, entity_id: PositiveInt) -> None:
        if not await self.exists(entity_id=entity_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Entity not found"
            )

        return await self.repository.delete(entity_id=entity_id)

    async def exists(self, entity_id: PositiveInt) -> bool:
        return await self.repository.exists(id=entity_id)
