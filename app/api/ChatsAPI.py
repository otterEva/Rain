from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.utils.auth import get_current_user, get_user_by_email
from app.db import get_session
from app.models.UsersModel import UsersModel
from app.repositories.ChatMembersDAO import ChatMembersDAO
from app.repositories.ChatsDAO import ChatsDAO

ChatsRouter = APIRouter(tags=["privat"])


@ChatsRouter.post("/new-chat")
async def create_private_chat(
    chat_name: str = None,
    session: AsyncSession = Depends(get_session),
    current_user: UsersModel = Depends(get_current_user),
    partner: UsersModel = Depends(get_user_by_email),
):
    chat = await ChatsDAO.add(chat_name=chat_name, session=session)
    await ChatMembersDAO.add(
        chat_id=chat.id, chat_user_id=current_user.id, session=session
    )
    await ChatMembersDAO.add(chat_id=chat.id, chat_user_id=partner.id, session=session)
    session.commit()
