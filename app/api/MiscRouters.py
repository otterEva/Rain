from fastapi import APIRouter, Request
from app.schemas.MiscSchemas import HealthcheckSchema
from app.config import settings
from app.logger import logger

router = APIRouter()


@router.get("/healthcheck")
def healthcheck(request: Request) -> HealthcheckSchema:
    logger.info("я живой")
    return HealthcheckSchema(status="OK", version=settings.app.app_version)
