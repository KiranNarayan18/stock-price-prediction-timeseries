import sys
from stockPrediction.logger import event_logger


try:
    2 / 0

except Exception as e:
    event_logger.error('hello')