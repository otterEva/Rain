from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMessagesModel import ChatMessagesModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.UserSchemas import UsersSchema


class ChatMessagesDAO(BaseDAO):
    model = ChatMessagesModel

    async def find_by_id(self, chat_id: int, session: AsyncSession) -> UsersSchema:
        query = select(self.model).filter_by(id=chat_id)
        result = await session.execute(query)
        return UsersSchema.model_validate(result.scalars().all())

    async def find_all(self, session: AsyncSession, **filter_by) -> list[UsersSchema]:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return [UsersSchema.model_validate(user) for user in result.scalars().all()]

    async def add(self, session: AsyncSession, **data) -> list[UsersSchema]:
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        await session.commit()
        return [UsersSchema.model_validate(user) for user in result.scalars().all()]


chat_messages_dao = ChatMessagesDAO()
