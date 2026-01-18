import logging

# Set the path for the log file
log_file_path = "logs/analysis.log"

# Configure logger and logs formats
def setup_logger():
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
