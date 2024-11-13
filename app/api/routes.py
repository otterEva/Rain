from app.api.ChatMessagesAPI import ChatMessagesRouter
from app.api.ChatsAPI import ChatsRouter
from app.api.UsersAPI import UsersRouter
from app.api.MiscRouters import router as router_health

ROUTES = {
	"/health" : router_health,
	"/chats" : ChatsRouter,
	"/users" : UsersRouter,
	"/messages" : ChatMessagesRouter
}