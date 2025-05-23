import logging
import sys
import os

def get_logger(name: str = "diabetes_logger", log_to_file: bool = False, log_file_path: str = "logs/app.log") -> logging.Logger:
    """
    Configure and return a logger instance.
    
    Args:
        name (str): Name of the logger.
        log_to_file (bool): If True, log messages will also be saved to a file.
        log_file_path (str): Path to the log file if file logging is enabled.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Console handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Optional file handler
        if log_to_file:
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
