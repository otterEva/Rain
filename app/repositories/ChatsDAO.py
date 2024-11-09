from app.repositories.BaseDAO import BaseDAO
from app.models.ChatsModel import ChatsModel


class ChatsDAO(BaseDAO):
    model = ChatsModel
