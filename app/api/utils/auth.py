from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import EmailStr
from app.repositories.UsersDAO import UsersDAO
from app.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request, HTTPException, Depends, status
from app.db import get_session

pwd_context = CryptContext("bcrypt", deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jst = jwt.encode(to_encode, settings.db.db_key, settings.db.db_algorythm)
    return encoded_jst

async def authenticate_user(email: EmailStr, password: str, session: AsyncSession):
    user = await UsersDAO.find_one_or_none(email=email, session=session)
    if not user and not verify_password(password, user.hashed_password):
        return None
    return user

##########################################################################################

def get_token(request: Request):
    token = request.cookies.get("Rain_login_token")
    if not token:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    return token

async def get_current_user(token: str = Depends(get_token), session: AsyncSession = Depends(get_session)):
    try:
        payload = jwt.decode(
            token,
            settings.db.db_key, settings.db.db_algorythm
        )
    except JWTError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    user_id : str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(int(user_id), session = session)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    return user