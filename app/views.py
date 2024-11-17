from sqladmin import ModelView
from app.models.ChatMembersModel import ChatMembersModel
from app.models.ChatMessagesModel import ChatMessagesModel
from app.models.ChatsModel import ChatsModel
from app.models.UsersModel import UsersModel
from app.db import engine
from sqladmin import Admin

class UsersAdmin(ModelView, model = UsersModel):
	column_list = [UsersModel.id, UsersModel.email]

class ChatMembersAdmin(ModelView, model = ChatMembersModel):
	column_list = [ChatMembersModel.chat_user_id, ChatMembersModel.chat_id]

class ChatMessagesAdmin(ModelView, model = ChatMessagesModel):
	column_list = [ChatMessagesModel.chat_user_id, ChatMessagesModel.chat_id]

class ChatsAdmin(ModelView, model = ChatsModel):
	column_list = [ChatsModel.id]

def get_admin(app):
	admin = Admin(app, engine)
	admin.add_view(UsersAdmin)
	admin.add_view(ChatMembersAdmin)
	admin.add_view(ChatMessagesAdmin)
	admin.add_view(ChatsAdmin)