from app.repositories.BaseDAO import BaseDAO
from app.models.ChatMembersModel import ChatMembersModel
from app.schemas.ChatMembersSchemas import ChatsMembersSchema


class ChatMembersDAO(BaseDAO):
    model = ChatMembersModel
    schema = ChatsMembersSchema


chat_members_dao = ChatMembersDAO()
