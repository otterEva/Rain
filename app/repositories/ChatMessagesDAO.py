from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMessagesModel import ChatMessagesModel


class ChatMessagesDAO(BaseDAO):
    model = ChatMessagesModel
