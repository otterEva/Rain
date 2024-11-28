from fastapi import HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions import DAOException
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
        try:
            current_user: UsersSchema = await users_service.get_current_user(
                session=session, request=request
            )

            if current_user:
                chat = (await self.repo.add(chat_name=chat_name, session=session))[0]
                await chat_members_dao.add(
                    chat_id=chat.id, chat_user_id=current_user.id, session=session
                )
                session.commit()
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        except DAOException as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(str(e), "create new chat error"),
            )


chats_service = ChatsService()
