from fastapi import APIRouter, HTTPException, Depends, Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.Services.UsersService import users_service
from app.db import get_session
from app.schemas.UserSchemas import UsersSchema

UsersRouter = APIRouter(tags=["Authentification"])


@UsersRouter.post("/register")
async def register_user(email, password, session: AsyncSession = Depends(get_session)):

    existing_user : UsersSchema = (
        await users_service.get_user_by_email(email=email, session=session),
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = users_service.get_password_hash(password)
    await users_service.add(
        email=email, hashed_password=hashed_password, session=session
    )


@UsersRouter.post("/login")
async def login_user(
    response: Response,
    email: str,
    password: str,
    session: AsyncSession = Depends(get_session),
):
    user = await users_service.authenticate_user(
        email=email, password=password, session=session
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    print(user.id)
    access_token = users_service._create_access_token({"sub": str(user.id)})
    response.set_cookie(key="Rain_login_token", value=access_token, httponly=True)
    return access_token


@UsersRouter.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("Rain_login_token")


@UsersRouter.get("/me")
async def read_users_me(request: Request, session: AsyncSession = Depends(get_session)):
    current_user: UsersSchema = await users_service.get_current_user(
        session=session, request=request
    )
    return current_user
