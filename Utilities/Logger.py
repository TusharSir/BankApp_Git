import inspect
import logging


class Log_Class:

    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file = logging.FileHandler(".\\Logs\\BankApp.log")
        log_format = logging.Formatter(" %(asctime)s : %(levelname)s : %(funcName)s  : %(message)s  ")
        file.setFormatter(log_format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
