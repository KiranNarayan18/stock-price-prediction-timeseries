import os
import sys

from stockPrediction.utils import (load_object, plot_predictions)
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging

class ForecastPipeline:
    def __init__(self) -> None:
        pass

    def initiate_forecast(self, number_of_days:int):
        try:
            
            model_path = os.path.join('artifacts', 'model.pkl')
            model = load_object(model_path)

            forecasted_values = model.forecast(steps=number_of_days)
            
            plot_predictions(forecasted_values, number_of_days)

            return forecasted_values

        except Exception as e:
            logging.info('error occured in prediction')
            raise CustomException(e, sys)
        


# if __name__ == '__main__':
#     obj = ForecastPipeline()
    
#     num_of_days = int(input('Enter the number of days to forecast'))

#     result = obj.initiate_forecaste(num_of_days)

#     plot_predictions(result, num_of_days)

#     logging.info(f'the closing share value after {num_of_days} is {result[-1]}')