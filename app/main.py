import uvicorn
from app.app import get_app
from app.config import settings
from app.logger import logger


def run_api_app() -> None:
    app = get_app()
    logger.info("Starting api app...")
    uvicorn.run(
        app, host=settings.app.app_host, port=settings.app.app_port, log_config=None
    )
