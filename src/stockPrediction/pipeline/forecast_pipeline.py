import os
import sys

from stockPrediction.utils import load_object
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def initiate_forecaste(self, number_of_days:int):
        try:
            
            model_path = os.path.join('artifacts', 'model.pkl')
            model = load_object(model_path)

            forecasted_values = model.forecast(steps=number_of_days)

            return round(forecasted_values[-1], 2)

        except Exception as e:
            logging.info('error occured in prediction')
            raise CustomException(e, sys)
        


if __name__ == '__main__':
    obj = PredictPipeline()
    num_of_days = int(input('Enter the number of days to forecast'))
    result = obj.initiate_forecaste(num_of_days)

    logging.info(f'the closing share value after {num_of_days} is {result}')