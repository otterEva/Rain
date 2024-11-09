from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.AuthUserSchemas import SAuthUser
from app.repositories.UsersDAO import UsersDAO
from app.api.utils.auth import get_password_hash, authenticate_user, create_access_token
from app.db import get_session

privat_router = APIRouter(prefix="/private", tags=["privat"])
group_router = APIRouter(prefix="/groups", tags=["privat"])

# @privat_router.post("/new-chat")
#     async def create_private_chat():
# 		pass