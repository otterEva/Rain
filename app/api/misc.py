# тут живут вспомогательные ручки, не учавствующие в бизнесовом коде. нужен для технической части

from fastapi import APIRouter, Request
from app.chema.misc_chemas import HealthcheckSchema
from app.config import settings
router = APIRouter()

@router.get("/healthcheck")
def healthcheck(request: Request) -> HealthcheckSchema:
	return HealthcheckSchema(status = "OK", version = settings.app.app_version)