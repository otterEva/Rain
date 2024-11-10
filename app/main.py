from fastapi import FastAPI
from app.api.MiscRouters import router as router_health
from app.api.AuthUserRouters import (
    register_router,
    login_router,
    logout_router,
    myself_router,
)
from app.api.ChatCreatingRouters import privat_chat_router
from app.api.SendMessageRouter import send_message_router, get_chat_messages_router
import uvicorn

app = FastAPI()

# app health
app.include_router(router_health)

# authentification
app.include_router(register_router)
app.include_router(login_router)
app.include_router(logout_router)
app.include_router(myself_router)

# chat_creating
app.include_router(privat_chat_router)

# messaging
app.include_router(send_message_router)
app.include_router(get_chat_messages_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)