import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(lineno)d: %(message)s]"

log_dir = "logs"
#To gemerate a new log file each day
log_file_name =f"running_logs_{datetime.now().strftime('%Y_%m_%d')}.log"
log_filepath = os.path.join(log_dir,log_file_name)
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logging = logging.getLogger("cnnClassifierLogger")
