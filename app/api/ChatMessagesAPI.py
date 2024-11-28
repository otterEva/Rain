from fastapi import APIRouter, Depends, Request, status, Response, HTTPException
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.Services.ChatMessagesService import chat_messages_service

ChatMessagesRouter = APIRouter(tags=["messages"])


@ChatMessagesRouter.post("/send_message")
async def send_messages(
    chat_id: int,
    message: str,
    request: Request,
    session: AsyncSession = Depends(get_session),
):
    try:
        await chat_messages_service.send_new_message(
            chat_id=chat_id, message=message, session=session, request=request
        )
        return Response(status_code=status.HTTP_200_OK)

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ChatMessagesRouter.get("/get_chat_messages")
async def get_chat_message(
    chat_id: int, request: Request, session: AsyncSession = Depends(get_session)
):
    try:
        return await chat_messages_service.get_message(
            chat_id=chat_id, session=session, request=request
        )

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
