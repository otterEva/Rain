from app.repositories.ChatMembersDAO import chat_members_dao


class ChatMembersService:
    def __init__(self):
        self.repo = chat_members_dao


chat_members_service = ChatMembersService()