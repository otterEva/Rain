from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatsDAO import chats_dao
from app.Services.UsersService import users_service
from app.schemas.UserSchemas import UsersSchema
from app.repositories.ChatMembersDAO import chat_members_dao


class ChatsService:
    def __init__(self):
        self.repo = chats_dao

    async def create_new_chat(
        self, request: Request, chat_name: str, session: AsyncSession
    ):
        current_user: UsersSchema = await users_service.get_current_user(
            session=session, request=request
        )

        chat = (await self.repo.add(chat_name=chat_name, session=session))[0]
        await chat_members_dao.add(
            chat_id=chat.id, chat_user_id=current_user.id, session=session
        )
        session.commit()


chats_service = ChatsService()
