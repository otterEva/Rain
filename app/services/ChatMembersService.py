from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatMembersDAO import chat_members_dao
from app.schemas.ChatMembersSchemas import ChatsMembersSchema

class ChatMembersService:
    def __init__(self):
        self.repo = chat_members_dao


chat_members_service = ChatMembersService()
