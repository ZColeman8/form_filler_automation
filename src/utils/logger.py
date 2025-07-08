import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("form_test_logger")
logger.setLevel(logging.DEBUG)

logging.getLogger("WDM").setLevel(logging.WARNING)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/form_test.log")

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)