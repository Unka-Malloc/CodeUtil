import logging
import os
import time


def logger_config(log_name, log_path=None):
    # Default Log File Path
    if log_path is None:
        log_path = os.getcwd() + fr'{os.sep}log'
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    # Default Log File Name
    file_name = f'{log_name}_{time.strftime("%Y%m%d_%H%M%S", time.localtime())}.log'
    file_path = log_path + os.sep + file_name

    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging.DEBUG)

    # %(asctime)s - time
    # %(name)s - name of logger
    # %(levelname)s - level of logging message [ERROR, WARN, DEBUG, INFO]
    # %(message)s - logging message
    # %(lineno)d - line number
    msg_formatter = logging.Formatter('[%(levelname)s]: %(asctime)s | Line:%(lineno)d | %(message)s')

    # File Handler
    file_handler = logging.FileHandler(file_path, encoding='UTF-8')
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(msg_formatter)  # Log File Message Formatter

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=logging.INFO)
    console_handler.setFormatter(msg_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
