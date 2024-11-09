from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, Table
from app.db import get_session
from fastapi import Depends

class baseDAO:

    model = None

    @classmethod
    async def find_by_id(cls, model_id : int,
						session : AsyncSession = Depends(get_session)):

        query = select(cls.model).filter_by(id = model_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls,
					session : AsyncSession = Depends(get_session), **filter_by):

        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    
    @classmethod
    async def find_all(cls,
					session : AsyncSession = Depends(get_session), **filter_by):

        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()
        
    @classmethod
    async def add(cls,
				session : AsyncSession = Depends(get_session), **data):
       
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()