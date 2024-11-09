from fastapi import APIRouter, HTTPException

from app.shcemas.register_schemas import SUserData
from app.schemas.users_dao import Users_DAO
from app.api.utils.auth import get_password_hash, verify_password

router = APIRouter(prefix = '/register',
				tags = ['Registration'])

@router.post("")
async def register_user(user_data : SUserData):
    existing_user = await Users_DAO.find_one_or_none(email = user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await Users_DAO.add(email = user_data.email, hashed_password = hashed_password)
	
