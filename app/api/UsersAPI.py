from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.Services.UsersService import users_service
from app.db import get_session
from app.schemas.UserSchemas import UsersSchema
from app.exceptions import ServiceException, DAOException
UsersRouter = APIRouter(tags=["Authentification"])


@UsersRouter.post("/register")
async def register_user(email, password, session: AsyncSession = Depends(get_session)):
    try:
        await users_service.register_new_user(
            email=email, password=password, session=session
    )
    except DAOException:
        return Response(status_code=status.HTTP_418_IM_A_TEAPOT)
    except ServiceException
        return Response

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
    except DAOException as e:
        return Response(status_code=status.HTTP_418_IM_A_TEAPOT)
    except ServiceException as e:
        return e
    except Exception as e:
        pass


@UsersRouter.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("Rain_login_token")


@UsersRouter.get("/me")
async def read_users_me(request: Request, session: AsyncSession = Depends(get_session)):
    current_user: UsersSchema = await users_service.get_current_user(
        session=session, request=request
    )
    return current_user
