import logging
from consts.paths import LOG_FILE_PATH
from pathlib import Path

# Configure logger and logs formats
def setup_logger():
    log_file_path = Path(LOG_FILE_PATH)
    
    # Create logs folder if does not exist
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file_path, mode="w", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger()
    logger.info("Logger initialized successfully")

    return logger
