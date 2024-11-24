from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from sqlalchemy import NullPool

engine = create_async_engine(
    url=settings.db.db_url,
    echo=True,
    poolclass=NullPool,
)

async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
