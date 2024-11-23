from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatMembersDAO import chat_members_dao
from app.schemas.ChatMembersSchemas import ChatsMembersSchema
class ChatMembersService:

	def __init__(self):
		self.repo = chat_members_dao

	async def get_all(self, session: AsyncSession) -> list[ChatsMembersSchema]:
		chats = await self.repo.find_all(session=session)
		return chats

	async def get_by_id(self, session: AsyncSession) -> ChatsMembersSchema:
		chats = await self.repo.find_by_id(session=session)
		return chats
	
	async def add(self, session: AsyncSession, **data) -> list[ChatsMembersSchema]:
		chats = await self.repo.add(session=session, **data)
		return chats
	
chat_members_service = ChatMembersService()
