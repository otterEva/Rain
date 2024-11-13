from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.AuthUserSchemas import SAuthUser
from app.repositories.UsersDAO import UsersDAO
from app.api.utils.auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
    get_current_user,
)
from app.db import get_session
from app.models import UsersModel

UsersRouter = APIRouter(tags=["Authentification"])


@UsersRouter.post("/register")
async def register_user(
    user_data: SAuthUser, session: AsyncSession = Depends(get_session)
):
    existing_user = None

    existing_user = await UsersDAO.find_one_or_none(
        email=user_data.email, session=session
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        email=user_data.email, hashed_password=hashed_password, session=session
    )


@UsersRouter.post("/login")
async def login_user(
    response: Response,
    user_data: SAuthUser,
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(user_data.email, user_data.password, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="Rain_login_token", value=access_token, httponly=True)
    return access_token


@UsersRouter.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("Rain_login_token")


@UsersRouter.get("/me")
async def read_users_me(current_user: UsersModel = Depends(get_current_user)):
    return current_user
