from typing import Sequence
from typing import Union

from pydantic import NonNegativeInt
from pydantic import PositiveInt
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.sql.expression import and_

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

    async def get_one(self, **kwargs) -> Union[model, None]:
        async with self.session() as session:
            stmt = select(self.model).where(
                and_(
                    *(
                        getattr(self.model, key) == value
                        for key, value in kwargs.items()
                    )
                )
            )
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def get_all(
        self, skip: NonNegativeInt = 0, limit: NonNegativeInt = 100
    ) -> Sequence[model]:
        async with self.session() as session:
            stmt = select(self.model).offset(skip).limit(limit)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def update(self, entity_id: PositiveInt, data: dict) -> model:
        async with self.session() as session:
            query = update(self.model).where(self.model.id == entity_id).values(**data)
            await session.execute(query)
            await session.commit()
            return await self.get_one(id=entity_id)

    async def delete(self, entity_id: PositiveInt) -> None:
        async with self.session() as session:
            db_object = await self.get_one(id=entity_id)
            await session.delete(db_object)
            await session.commit()

    async def exists(self, **kwargs) -> bool:
        return bool(await self.get_one(**kwargs))
