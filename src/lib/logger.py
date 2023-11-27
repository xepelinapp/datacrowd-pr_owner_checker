import logging
import os

from dataclasses import dataclass
from datetime import datetime
from config.config import LOGGING_FMT, DATE_FMT, LOGGING_LEVEL_CONSOLE, LOGGING_LEVEL_FILE, LOGGING_LEVEL_LOGGER


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Logger(metaclass=Singleton):
    def __init__(self, console_output: bool = True, file_output: bool = False):
        ## logger
        date = datetime.strftime(datetime.now(), DATE_FMT)
        self.logger = logging.getLogger("output_logger")
        ## console logger
        console_log = logging.StreamHandler()
        ## file logger
        log_path = os.path.join(os.getcwd(), f"{date}-execution.log")
        file_log = logging.FileHandler(filename=log_path, mode="a", encoding="latin-1", delay=False)
        ## set levels
        self.logger.setLevel(LOGGING_LEVEL_LOGGER)
        console_log.setLevel(LOGGING_LEVEL_CONSOLE)
        file_log.setLevel(LOGGING_LEVEL_FILE)
        ## set up formatter
        formatter = logging.Formatter(LOGGING_FMT)
        console_log.setFormatter(formatter)
        file_log.setFormatter(formatter)
        ## add console log to handler
        if console_output:
            self.logger.addHandler(console_log)
        if file_output:
            self.logger.addHandler(file_log)
        return None
    
    def debug(self, msg: str) -> None:
        self.logger.debug(msg=msg)
        return None

    def info(self, msg: str) -> None:
        self.logger.info(msg=msg)
        return None

    def warning(self, msg: str) -> None:
        self.logger.warning(msg=msg)
        return None

    def error(self, msg: str) -> None:
        self.logger.error(msg=msg)
        return None

    def critical(self, msg: str) -> None:
        self.logger.critical(msg=msg)
        return None

    def exception(self, msg: str, exception: Exception) -> None:
        self.logger.exception(msg=msg, stack_info=True, exc_info=exception)
        return None
