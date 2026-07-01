import logging
import os

from config import LOG_FOLDER

# ==========================================
# Log File
# ==========================================

log_file = os.path.join(LOG_FOLDER, "toolkit.log")

# ==========================================
# Logger Configuration
# ==========================================

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

# ==========================================
# Functions
# ==========================================

def log_info(message):
    """
    Write an INFO message to the log file.
    """
    logging.info(message)


def log_warning(message):
    """
    Write a WARNING message to the log file.
    """
    logging.warning(message)


def log_error(message):
    """
    Write an ERROR message to the log file.
    """
    logging.error(message)