from sqladmin import ModelView
from app.models.ChatMembersModel import ChatMembersModel
from app.models.ChatMessagesModel import ChatMessagesModel
from app.models.ChatsModel import ChatsModel
from app.models.UsersModel import UsersModel
from app.db import engine
from sqladmin import Admin


class UsersAdmin(ModelView, model=UsersModel):
    column_exclude_list = [UsersModel.hashed_password]
    column_details_exclude_list = [UsersModel.hashed_password]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class ChatMembersAdmin(ModelView, model=ChatMembersModel):
    column_list = [c.name for c in ChatMembersModel.__table__.c] + [
        ChatMembersModel.ChatMembers_Users,
        ChatMembersModel.ChatMembers_Chats,
    ]
    name = "Chat member"
    name_plural = "Chat members"
    icon = "fa-solid fa-people-group"


class ChatMessagesAdmin(ModelView, model=ChatMessagesModel):
    column_list = [c.name for c in ChatMessagesModel.__table__.c] + [
        ChatMessagesModel.ChatMessages_Users,
        ChatMessagesModel.ChatMessages_Chats,
    ]
    name = "Chat message"
    name_plural = "Chat messages"
    icon = "fa-regular fa-message"


class ChatsAdmin(ModelView, model=ChatsModel):
    column_list = [c.name for c in ChatsModel.__table__.c]
    name = "Chats"
    name_plural = "Chats"
    icon = "fa-brands fa-rocketchat"


def get_admin(app):
    admin = Admin(app, engine)
    admin.add_view(UsersAdmin)
    admin.add_view(ChatMembersAdmin)
    admin.add_view(ChatMessagesAdmin)
    admin.add_view(ChatsAdmin)
