from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ChatMessagesDAO import chat_messages_dao
from app.schemas.ChatMessagesSchemas import ChatMessagesSchema
from app.schemas.UserSchemas import UsersSchema
from app.Services.UsersService import users_service
from fastapi import Request
from sqlalchemy import select, and_
from app.models.ChatMembersModel import ChatMembersModel
from app.exceptions import ServiceException
from app.exceptions import DAOException

class ChatMessagesService:
    def __init__(self):
        self.repo = chat_messages_dao

    async def send_new_message(
        self, chat_id: int, message: str, session: AsyncSession, request: Request):
        current_user: UsersSchema = await users_service.get_current_user(
            session=session, request=request
        )

        try:
            query = select(ChatMembersModel).where(
                and_(
                    ChatMembersModel.chat_id == chat_id,
                    current_user.id == ChatMembersModel.chat_user_id,
                )
            )

            result = await session.execute(query)
            if result:
                await self.repo.add(
                    chat_id=chat_id,
                    message=message,
                    chat_user_id=current_user.id,
                    session=session,
                )
                await session.commit()

        except DAOException as e:
            session.rollback()
            raise e
        except Exception as e:
            session.rollback()
            raise ServiceException(message=str(e))

    async def get_message(self, chat_id: int, session: AsyncSession, request: Request) -> list[ChatMessagesSchema]:
        current_user: UsersSchema = await users_service.get_current_user(
            session=session, request=request
        )

        try:
            query = select(ChatMembersModel).where(
                and_(
                    ChatMembersModel.chat_id == chat_id,
                    current_user.id == ChatMembersModel.chat_user_id,
                )
            )
            result = await session.execute(query)
            if result:
                messages : list[ChatMessagesSchema] = await self.repo.find_all(session=session, chat_id=chat_id)
                return messages
        
        except DAOException as e:
            raise e
        except Exception as e:
            raise ServiceException(message=str(e))


chat_messages_service = ChatMessagesService()
