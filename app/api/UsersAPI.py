from fastapi import APIRouter, Depends, Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.Services.UsersService import users_service
from app.db import get_session
from app.schemas.UserSchemas import UsersSchema
from fastapi import HTTPException
from logger import logger

UsersRouter = APIRouter(tags=["Authentification"])


@UsersRouter.post("/register")
async def register_user(email, password, session: AsyncSession = Depends(get_session)):
    await users_service.register_new_user(
        email=email, password=password, session=session
    )


@UsersRouter.post("/login")
async def Login_user(
    response: Response,
    email: str,
    password: str,
    session: AsyncSession = Depends(get_session),
) -> None:
    
    try:
        await users_service.login_user(
            email=email, password=password, session=session, response=response
        )
        return Response(status_code=status.HTTP_200_OK)

    except HTTPException as e:
        raise e
    except Exception as exc:
        logger.bind({'email': email, 'password': password}).critical('500 ', exc)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@UsersRouter.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("Rain_login_token")


@UsersRouter.get("/me")
async def read_users_me(request: Request, session: AsyncSession = Depends(get_session)):
    try:
        current_user: UsersSchema = await users_service.get_current_user(
            session=session, request=request
        )
        return current_user

    except HTTPException as e:
        raise e
    except Exception as exc:
        logger.critical('500', str(exc))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
