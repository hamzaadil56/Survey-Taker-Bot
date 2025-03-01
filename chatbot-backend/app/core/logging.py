import logging
import sys
from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration"""
    LOGGER_NAME: str = "survey_chatbot"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": sys.stderr,
        },
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


def get_logger(name: str = "survey_chatbot") -> logging.Logger:
    """Get logger instance"""
    return logging.getLogger(name)
