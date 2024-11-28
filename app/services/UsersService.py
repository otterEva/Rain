from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions import DAOException
from app.repositories.UsersDAO import users_dao
from app.schemas.UserSchemas import UsersSchema
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import EmailStr
from app.config import settings
from fastapi import HTTPException, Request, status


class UsersService:
    pwd_context = CryptContext("bcrypt", deprecated="auto")

    def __init__(self):
        self.repo = users_dao

    async def register_new_user(
        self, email: EmailStr, password: str, session: AsyncSession
    ):
        try:
            existing_user: UsersSchema = (
                await self._get_user_by_email(email=email, session=session),
            )

            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"User with email {email} already exists",
                )

            hashed_password = self._get_password_hash(password)
            await self.repo.add(
                email=email, hashed_password=hashed_password, session=session
            )
            session.commit()

        except DAOException as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(str(e), "register error"),
            )

    async def login_user(
        self, email: EmailStr, password: str, session: AsyncSession, response
    ):
        try:
            user = await self.authenticate_user(
                email=email, password=password, session=session
            )
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                )

            access_token = self._create_access_token({"sub": str(user.id)})
            response.set_cookie(
                key="Rain_login_token", value=access_token, httponly=True
            )
            return access_token

        except DAOException as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(str(e), "login error"),
            )

    async def authenticate_user(
        self, email: EmailStr, password: str, session: AsyncSession
    ) -> UsersSchema:
        try:
            user = await self.repo.find_one_or_none(email=email, session=session)
            if not user or not self._verify_password(password, user.hashed_password):
                return None
            return UsersSchema.model_validate(user)

        except DAOException as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(str(e), "authenticate error"),
            )

    async def get_current_user(
        self, session: AsyncSession, request: Request
    ) -> UsersSchema:
        try:
            try:
                token = self._get_token(request=request)
                payload = jwt.decode(
                    token, settings.db.db_key, settings.db.db_algorythm
                )
            except JWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
                )
            expire: str = payload.get("exp")
            if not expire or int(expire) < datetime.utcnow().timestamp():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
                )
            user_id: str = payload.get("sub")
            if not user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="User ID not found"
                )
            user = await self.repo.find_by_id(id=int(user_id), session=session)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
                )
            return UsersSchema.model_validate(user)

        except DAOException as e:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(str(e), "get_current_user_error"),
            )

    #########################################################################################

    def _get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def _verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def _create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=120)
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

    async def _get_user_by_email(self, email: EmailStr, session: AsyncSession):
        partner = await self.repo.find_all(email=email, session=session)
        if partner:
            return partner
        else:
            return None


users_service = UsersService()
