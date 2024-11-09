from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.AuthUserSchemas import SAuthUser
from app.repositories.UsersDAO import UsersDAO
from app.api.utils.auth import get_password_hash
from app.db import get_session

router = APIRouter(prefix="/register", tags=["Registration"])


@router.post("")
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
