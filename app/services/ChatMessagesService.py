from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatMessagesDAO import chat_messages_dao
from app.schemas.ChatMessagesSchemas import ChatMessagesSchema

class ChatMessagesService:

	def __init__(self):
		self.repo = chat_messages_dao

	async def  get_all(self, session: AsyncSession) -> list[ChatMessagesSchema]:
		messages = await self.repo.find_all(session=session)
		return messages

	async def get_by_id(self, session: AsyncSession) -> ChatMessagesSchema:
		messages = await self.repo.find_by_id(session=session)
		return messages
	
	async def add(self, session: AsyncSession, **data) -> list[ChatMessagesSchema]:
		messages = await self.repo.add(session=session, **data)
		return messages
	
chat_messages_service = ChatMessagesService()
