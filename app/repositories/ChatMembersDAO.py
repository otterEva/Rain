from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMembersModel import ChatMembersModel


class ChatMembersDAO(BaseDAO):
    model = ChatMembersModel
