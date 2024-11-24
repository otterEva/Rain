from fastapi import APIRouter, Depends, Request
from sqlalchemy import select, and_
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.Services.UsersService import users_service
from app.Services.ChatMessagesService import chat_messages_service
from app.models.UsersModel import UsersModel
from app.models.ChatMembersModel import ChatMembersModel

ChatMessagesRouter = APIRouter(tags=["messages"])


@ChatMessagesRouter.post("/send_message")
async def send_messages(
    chat_id: int,
    message: str,
    request : Request,
    session: AsyncSession = Depends(get_session)):

    current_user: UsersModel = await users_service.get_current_user(session = session, request = request)
    query = select(ChatMembersModel).where(
        and_(
            ChatMembersModel.chat_id == chat_id,
            current_user.id == ChatMembersModel.chat_user_id,
        )
    )

    result = await session.execute(query)
    if result:
        await chat_messages_service.add(
            chat_id=chat_id,
            message=message,
            chat_user_id=current_user.id,
            session=session,
        )
        await session.commit()


@ChatMessagesRouter.get("/get_chat_messages")
async def get_chat_message(
    chat_id: int,
    request : Request,
    session: AsyncSession = Depends(get_session)
):
    current_user: UsersModel = await users_service.get_current_user(session = session, request = request)
    query = select(ChatMembersModel).where(
        and_(
            ChatMembersModel.chat_id == chat_id,
            current_user.id == ChatMembersModel.chat_user_id,
        )
    )

    result = await session.execute(query)
    if result:
        return await chat_messages_service.find_all(session=session, chat_id = chat_id)
