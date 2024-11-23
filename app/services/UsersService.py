from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.UsersDAO import users_dao
from app.schemas.UserSchemas import UsersSchema
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import EmailStr
from app.repositories.UsersDAO import UsersDAO
from app.config import settings
from fastapi import Request, HTTPException, Depends, status
from app.db import get_session

class UsersService:

	pwd_context = CryptContext("bcrypt", deprecated="auto")

	def __init__(self):
		self.repo = users_dao

	async def  get_all(self, session: AsyncSession) -> list[UsersSchema]:
		users = await self.repo.find_all(session=session)
		return users

	async def get_by_id(self, session: AsyncSession) -> UsersSchema:
		users = await self.repo.find_by_id(session=session)
		return users
	
	async def add(self, session: AsyncSession, **data) -> list[UsersSchema]:
		users = await self.repo.add(session=session, **data)
		return users
	
################################################################################

	def _get_password_hash(self, password: str) -> str:
		return self.pwd_context.hash(password)

	def _verify_password(self, password: str, hashed_password: str) -> bool:
		return self.pwd_context.verify(password, hashed_password)

	def _create_access_token(data: dict) -> str:
		to_encode = data.copy()
		expire = datetime.utcnow() + timedelta(minutes=30)
		to_encode.update({"exp": expire})
		encoded_jst = jwt.encode(to_encode, settings.db.db_key, settings.db.db_algorythm)
		return encoded_jst

	async def authenticate_user(self, email: EmailStr, password: str, session: AsyncSession):
		user = await UsersDAO.find_all(email=email, session=session)
		if not user and not self._verify_password(password, user.hashed_password):
			return None
		return user

	def _get_token(self, request: Request):
		token = request.cookies.get("Rain_login_token")
		if not token:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		return token

	async def get_current_user(self, session: AsyncSession):
		try:
			token = self._get_token()
			payload = jwt.decode(token, settings.db.db_key, settings.db.db_algorythm)
		except JWTError:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		expire: str = payload.get("exp")
		if not expire or int(expire) < datetime.utcnow().timestamp():
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		user_id: str = payload.get("sub")
		if not user_id:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		user = await UsersDAO.find_by_id(int(user_id), session=session)
		if not user:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		return user

	async def get_user_by_email(self, 
		email: EmailStr, session: AsyncSession = Depends(get_session)
	):
		partner = await UsersDAO.find_all(email=email, session=session)
		if partner:
			return partner
		else:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

users_service = UsersService()
