from fastapi import APIRouter, Depends
from sqlalchemy import select, and_
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.utils.auth import get_current_user
from app.models.UsersModel import UsersModel
from app.models.ChatMembersModel import ChatMembersModel
from app.repositories.ChatMessagesDAO import ChatMessagesDAO

ChatMessagesRouter = APIRouter(tags=["messages"])


@ChatMessagesRouter.post("/send_message")
async def send_messages(
    chat_id: int,
    message: str,
    session: AsyncSession = Depends(get_session),
    current_user: UsersModel = Depends(get_current_user),
):
    query = select(ChatMembersModel).where(
        and_(
            ChatMembersModel.chat_id == chat_id,
            current_user.id == ChatMembersModel.chat_user_id,
        )
    )

    result = await session.execute(query)
    if result:
        await ChatMessagesDAO.add(
            chat_id=chat_id,
            message=message,
            chat_user_id=current_user.id,
            session=session,
        )
        await session.commit()


@ChatMessagesRouter.get("/get_chat_messages")
async def get_chat_message(
    chat_id: int,
    session: AsyncSession = Depends(get_session),
    current_user: UsersModel = Depends(get_current_user),
):
    query = select(ChatMembersModel).where(
        and_(
            ChatMembersModel.chat_id == chat_id,
            current_user.id == ChatMembersModel.chat_user_id,
        )
    )

    result = await session.execute(query)
    if result:
        return await ChatMessagesDAO.find_all(chat_id=chat_id, session=session)
