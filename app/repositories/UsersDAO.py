from app.repositories.BaseDAO import BaseDAO
from app.models.UsersModel import UsersModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.UserSchemas import UsersSchema


class UsersDAO(BaseDAO):
    model = UsersModel

    async def find_by_id(self, id: int, session: AsyncSession) -> UsersSchema:
        query = select(self.model).filter_by(id=id)
        result = await session.execute(query)
        user = result.scalars().one()
        return UsersSchema.model_validate(user)

    async def find_all(self, session: AsyncSession, **filter_by) -> list[UsersSchema]:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return [UsersSchema.model_validate(user) for user in result.scalars().all()]

    async def add(self, session: AsyncSession, **data) -> list[UsersSchema]:
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        await session.commit()
        return [UsersSchema.model_validate(user) for user in result.scalars().all()]

    async def find_one_or_none(self, session: AsyncSession, **filter_by) -> UsersSchema:
        query = select(self.model).filter_by(**filter_by)
        result = await session.execute(query)
        return UsersSchema.model_validate(result.scalar_one_or_none())


users_dao = UsersDAO()
