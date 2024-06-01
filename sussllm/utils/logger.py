import logging
import os
from datetime import datetime

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """
    Sets up and returns a logger with the given name and log file.

    Args:
    name (str): The name of the logger.
    log_file (str): Path to the log file where logs will be written.
    level (logging.Level): The logging level, defaults to logging.INFO.

    Returns:
    logging.Logger: Configured logger.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = logging.FileHandler(f'logs/{log_file}')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    
    logger = setup_logger('example_logger', f'example_log_{datetime.now().strftime("%Y%m%d")}.log')
    logger.info('This is an informational message')
    logger.error('This is an error message')
