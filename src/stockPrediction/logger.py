import logging 
import os
import sys
from datetime import datetime

format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    level= logging.INFO,
    format= format,

    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)


"""if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        a = 1/0
    except Exception as e:
        logging.info("zero division error")"""


