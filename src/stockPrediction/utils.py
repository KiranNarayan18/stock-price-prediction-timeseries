
import os
import sys
import dill
import pickle
import pandas as pd
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging

from stockPrediction.components.data_transformation import DataTransformation


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('error occured while loading the model')
        raise CustomException(e, sys)
    

def plot_predictions(predictions, forecast_steps):
    try:
        train_data_path: str = os.path.join('artifacts', 'train.csv')
        test_data_path: str = os.path.join('artifacts', 'test.csv')

        data_transformation=DataTransformation()
        train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        data = pd.concat([train_arr, test_arr], axis=0)

        import matplotlib.pyplot as plt
        plt.figure(figsize=(18,8))
        plt.plot(data, label='Original')
        
        forecast_dates = pd.date_range(start=data.index[-1] + pd.DateOffset(days=1), periods=forecast_steps, freq='D')

        plt.plot(forecast_dates, predictions, label='Forecast')

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('ARIMA Forecast')

        

        plt.legend()
        plt.savefig('static/plot.jpg')
        plt.show()


    except Exception as e:
        logging.info(f"error occured while plotting the predictions {e}")