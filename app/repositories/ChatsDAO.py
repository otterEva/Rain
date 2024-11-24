from app.repositories.BaseDAO import BaseDAO
from app.models.ChatsModel import ChatsModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.ChatsSchema import ChatsSchema


class ChatsDAO(BaseDAO):
    model = ChatsModel

    async def find_by_id(self, chat_id: int, session: AsyncSession) -> ChatsSchema:
        query = select(self.model).filter_by(id=chat_id)
        result = await session.execute(query)
        return ChatsSchema.model_validate(result.scalars().all())

    async def find_all(self, session: AsyncSession, **filter_by) -> list[ChatsSchema]:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return [ChatsSchema.model_validate(user) for user in result.scalars().all()]

    async def add(self, session: AsyncSession, **data) -> list[ChatsSchema]:
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        await session.commit()
        return [ChatsSchema.model_validate(chat) for chat in result.scalars().all()]

    async def find_one_or_none(self, session: AsyncSession, **filter_by) -> ChatsSchema:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return ChatsSchema.model_validate(result.scalar_one_or_none())


chats_dao = ChatsDAO()
