from app.repositories.BaseDAO import BaseDAO
from app.models.ChatsModel import ChatsModel
from app.schemas.ChatsSchema import ChatsSchema


class ChatsDAO(BaseDAO):
    model = ChatsModel
    schema = ChatsSchema


chats_dao = ChatsDAO()
