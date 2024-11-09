from fastapi import APIRouter, HTTPException, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.register_schemas import SUserData
from app.repositories.users_dao import Users_DAO
from app.api.utils.auth import get_password_hash, verify_password
from app.db import get_session

router = APIRouter(prefix = '/register',
				tags = ['Registration'])

@router.post("")
async def register_user(user_data: SUserData, session: AsyncSession = Depends(get_session)):
    existing_user = None

    existing_user = await Users_DAO.find_one_or_none(email = user_data.email, session = session)


    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await Users_DAO.add(email = user_data.email, hashed_password = hashed_password, session = session)