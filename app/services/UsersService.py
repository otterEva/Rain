from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.UsersDAO import users_dao
from app.schemas.UserSchemas import UsersSchema
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import EmailStr
from app.config import settings
from fastapi import Request, HTTPException, status


class UsersService:
    pwd_context = CryptContext("bcrypt", deprecated="auto")

    def __init__(self):
        self.repo = users_dao

    async def get_user_by_email(self, email: EmailStr, session: AsyncSession):
        partner = await users_dao.find_all(email=email, session=session)
        if partner:
            return partner
        else:
            return None

    async def authenticate_user(
        self, email: EmailStr, password: str, session: AsyncSession
    ) -> UsersSchema:
        user = await users_dao.find_one_or_none(email=email, session=session)
        if not user and not self._verify_password(password, user.hashed_password):
            return None
        return UsersSchema.model_validate(user)

    async def get_current_user(
        self, session: AsyncSession, request: Request
    ) -> UsersSchema:
        try:
            token = self._get_token(request=request)
            payload = jwt.decode(token, settings.db.db_key, settings.db.db_algorythm)
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        expire: str = payload.get("exp")
        if not expire or int(expire) < datetime.utcnow().timestamp():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        user_id: str = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        user = await users_dao.find_by_id(id=int(user_id), session=session)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return UsersSchema.model_validate(user)

    async def register_new_user(
        self, email: EmailStr, password: str, session: AsyncSession
    ):
        existing_user: UsersSchema = (
            await self.get_user_by_email(email=email, session=session),
        )

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = self._get_password_hash(password)
        await users_dao.add(
            email=email, hashed_password=hashed_password, session=session
        )
        session.commit()

    async def login_user(
        self, email: EmailStr, password: str, session: AsyncSession, response
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

    ###################################################################

    def _get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def _verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def _create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jst = jwt.encode(
            to_encode, settings.db.db_key, settings.db.db_algorythm
        )
        return encoded_jst

    def _get_token(self, request: Request):
        token = request.cookies.get("Rain_login_token")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return token


users_service = UsersService()
