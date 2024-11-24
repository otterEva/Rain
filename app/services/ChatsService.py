from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatsDAO import chats_dao
from app.schemas.ChatsSchema import ChatsSchema


class ChatsService:
    def __init__(self):
        self.repo = chats_dao


chats_service = ChatsService()
