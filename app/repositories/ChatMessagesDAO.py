from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMessagesModel import ChatMessagesModel
from app.schemas.ChatMessagesSchemas import ChatMessagesSchema



class ChatMessagesDAO(BaseDAO):
    model = ChatMessagesModel
    schema = ChatMessagesSchema


chat_messages_dao = ChatMessagesDAO()
