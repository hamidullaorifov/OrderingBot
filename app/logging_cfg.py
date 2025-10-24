from loguru import logger
import sys

def configure_logging():
    logger.remove()
    logger.add(sys.stdout, level="INFO", backtrace=True, diagnose=True,
               format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <lvl>{level}</lvl> | {message}")
    return logger

logger = configure_logging()
