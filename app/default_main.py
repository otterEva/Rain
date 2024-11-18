from fastapi import FastAPI
from app.api.ChatMessagesAPI import ChatMessagesRouter
from app.api.ChatsAPI import ChatsRouter
from app.api.MiscRouters import router
from app.api.UsersAPI import UsersRouter


app = FastAPI()

app.include_router(ChatMessagesRouter)
app.include_router(ChatMessagesRouter)
app.include_router(router)
app.include_router(UsersRouter)
