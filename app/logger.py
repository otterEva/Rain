from loguru import logger

logger.remove()
logger.add(
    "logs.txt",
    level="INFO",
    serialize=True,
    format="{time:YYYY-MM-DD HH:mm:ss} {level} {message} {exception}",
    encoding="utf-8",
)
