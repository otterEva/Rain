from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatsDAO import chats_dao
from app.schemas.ChatsSchema import ChatsSchema
class ChatsService:

	def __init__(self):
		self.repo = chats_dao

	async def  get_all(self, session: AsyncSession) -> list[ChatsSchema]:
		chats = await self.repo.find_all(session=session)
		return chats

	async def get_by_id(self, session: AsyncSession) -> ChatsSchema:
		chats = await self.repo.find_by_id(session=session)
		return chats
	
	async def add(self, session: AsyncSession, **data) -> list[ChatsSchema]:
		chats = await self.repo.add(session=session, **data)
		return chats
	
chats_service = ChatsService()