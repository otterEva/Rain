from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.Services.ChatsService import chats_service


ChatsRouter = APIRouter(tags=["privat"])


@ChatsRouter.post("/new-chat")
async def create_private_chat(request: Request,
    chat_name: str = None, session: AsyncSession = Depends(get_session),
    
):
    await chats_service.create_new_chat(chat_name = chat_name, session = session,
                                        request = request)
