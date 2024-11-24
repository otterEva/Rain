from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatMessagesDAO import chat_messages_dao
from app.schemas.ChatMessagesSchemas import ChatMessagesSchema


class ChatMessagesService:
    def __init__(self):
        self.repo = chat_messages_dao


chat_messages_service = ChatMessagesService()
