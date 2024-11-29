from __future__ import annotations
from typing import Any, Type, TypeVar
from fastapi import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.BaseSchemas import BaseSchema
from app.exceptions import DAOException
from app.logger import logger

T = TypeVar("T", bound=BaseSchema)


class BaseDAO:
    schema: Type[T] = None
    model: Any = None

    async def find_by_id(self, id: int, session: AsyncSession) -> T:
        try:
            query = select(self.model).filter_by(id=id)
            result = await session.execute(query)
            item = result.scalar_one_or_none()
            if item is None:
                HTTPException(status_code=404, detail=f"Item with ID {id} not found")
            return self.schema.model_validate(result.scalar_one_or_none())
        except SQLAlchemyError as exc:
            logger.bind(id=id).error(500, exc)
            raise DAOException(exc=exc, data=id)

    async def find_all(self, session: AsyncSession, **filter_by) -> list[T]:
        try:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return [self.schema.model_validate(user) for user in result.scalars().all()]
        except SQLAlchemyError as exc:
            logger.bind(filter_by=filter_by).error(500, exc)
            raise DAOException(exc=exc, data=filter_by)

    async def add(self, session: AsyncSession, **data) -> list[T]:
        try:
            query = insert(self.model).values(**data).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            return [self.schema.model_validate(user) for user in result.scalars().all()]
        except SQLAlchemyError as exc:
            await session.rollback()
            logger.bind(data=data).error(500, exc)
            raise DAOException(exc=exc, data=data)

    async def find_one_or_none(self, session: AsyncSession, **filter_by) -> T:
        try:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return self.schema.model_validate(result.scalar_one_or_none())
        except SQLAlchemyError as exc:
            logger.bind(filter_by=filter_by).error(500, exc)
            raise DAOException(exc=exc, data=filter_by)
