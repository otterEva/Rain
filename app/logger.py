from loguru import logger

logger.add("logs.txt",
		    level = "INFO",
		    serialize = True,  colorize = True, 
		    backtrace = True, diagnose = True,
			format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>\n"
                  "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>\n"
                  "- <level>{message}</level> {exception}",
		   )