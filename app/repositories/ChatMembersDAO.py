from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMembersModel import ChatMembersModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.ChatMembersSchemas import ChatsMembersSchema


class ChatMembersDAO(BaseDAO):
    model = ChatMembersModel
    
    async def find_by_id(
        self, chat_id: int, session: AsyncSession
    ) -> ChatsMembersSchema:
        query = select(self.model).filter_by(id=chat_id)
        result = await session.execute(query)
        return ChatsMembersSchema.model_validate(result.scalars().all())

    async def find_all(
        self, session: AsyncSession, **filter_by
    ) -> list[ChatsMembersSchema]:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return [
            ChatsMembersSchema.model_validate(user) for user in result.scalars().all()
        ]

    async def add(self, session: AsyncSession, **data) -> list[ChatsMembersSchema]:
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        await session.commit()
        return [
            ChatsMembersSchema.model_validate(user) for user in result.scalars().all()
        ]

    async def find_one_or_none(
        self, session: AsyncSession, **filter_by
    ) -> ChatsMembersSchema:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return ChatsMembersSchema.model_validate(result.scalar_one_or_none())


chat_members_dao = ChatMembersDAO()
