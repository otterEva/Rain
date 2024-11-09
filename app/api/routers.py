from fastapi import APIRouter
from app.shcemas.register_schemas import SUserData

router = APIRouter(prefix = '/register',
				tags = ['Registration'])

@router.post("")
def register(userdata: SUserData):
	pass
	
