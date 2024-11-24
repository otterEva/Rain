from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.models.UsersModel import UsersModel
from app.Services.UsersService import users_service
from app.Services.ChatsService import chats_service
from app.repositories.ChatMembersDAO import chat_members_dao

ChatsRouter = APIRouter(tags=["privat"])


@ChatsRouter.post("/new-chat")
async def create_private_chat(
    chat_name: str = None, session: AsyncSession = Depends(get_session)
):
    current_user: UsersModel = (users_service.get_current_user(session=session),)
    partner: UsersModel = users_service.get_user_by_email(session=session)

    chat = await chats_service.add(chat_name=chat_name, session=session)
    await chat_members_dao.add(
        chat_id=chat.id, chat_user_id=current_user.id, session=session
    )
    await chat_members_dao.add(
        chat_id=chat.id, chat_user_id=partner.id, session=session
    )
    session.commit()
