from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

from src.db.session import async_session


class BaseRepository:
    model = None

    def __init__(self):
        self.session = async_session

    async def create(self, data: dict) -> model:
        async with self.session() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def get_by_id(self, entity_id: int):
        async with self.session() as session:
            stmt = select(self.model).where(self.model.id == entity_id)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100):
        async with self.session() as session:
            stmt = select(self.model).offset(skip).limit(limit)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def update(self, entity_id: int, data: dict):
        async with self.session() as session:
            query = update(self.model).where(self.model.id == entity_id).values(**data)
            await session.execute(query)
            await session.commit()
            return await self.get_by_id(entity_id)

    async def delete(self, entity_id: int) -> None:
        async with self.session() as session:
            query = delete(self.model).where(self.model.id == entity_id)
            await session.execute(query)
            await session.commit()

    async def exists_by_id(self, entity_id) -> bool:
        return bool(await self.get_by_id(entity_id))
