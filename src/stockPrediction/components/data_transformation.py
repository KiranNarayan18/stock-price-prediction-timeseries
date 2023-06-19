import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd


from stockPrediction.exception import CustomException
from stockPrediction.logger import logging


class DataTransformation:
    def __init__(self) -> None:
        pass


    def  initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            train_df = train_df[['Date', 'Close']]
            test_df = test_df[['Date', 'Close']]

            train_df = train_df.dropna()
            test_df = test_df.dropna()
            logging.info("dropping nan values")

            train_df['Date'] = pd.to_datetime(train_df['Date'])
            test_df['Date'] = pd.to_datetime(test_df['Date'])
            logging.info("converting date to datetime")

            train_df = train_df.set_index('Date')
            test_df = test_df.set_index('Date')
            logging.info("setting index")

 
            return(
                train_df,
                test_df                
            )


        except Exception as e:
            logging.error(f'error in inittiate data transformation function {e}')
            raise CustomException(e, sys)