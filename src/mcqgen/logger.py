import logging
import os
from datetime import datetime

FILE_NAME = f"{datetime.now().strftime('%d -%m-%y_%H-%M-%S')}.log"

log_path = os.path.join("../", "logs")

os.makedirs(log_path, exist_ok=True)  # Create logs

FILE_PATH = os.path.join(log_path, FILE_NAME)

logging.basicConfig(
    level=logging.INFO,
    filename=FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)
