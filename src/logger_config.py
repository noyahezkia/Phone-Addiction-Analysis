import logging
from pathlib import Path

# Set the path for the log file
log_file_path = Path("logs") / "analysis.log"

# Configure logger and logs formats
def setup_logger():
    
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
