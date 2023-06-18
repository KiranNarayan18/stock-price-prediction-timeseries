import sys
import os
import pandas as pd

from dataclasses import dataclass

from stockPrediction.components.data_transformation import DataTransformation
from stockPrediction.components.model_trainer import ModelTrainer
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_csv: str = os.path.join('artifacts', 'raw_data.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('enterede the data ingestion method or config')
        try:
            df = pd.read_csv('notebooks\data\TSLA.csv')
            logging.info('read data as dataframe')

            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)


            df = df[['Date', 'Close']]
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.set_index('Date')

            df.to_csv(self.ingestion_config.raw_data_csv,
                      index=False, header=True)

            logging.info('train test split initiated')

            train_set, test_set = df[0:-60], df[-60:]

            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)

            logging.info('data ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(f'error in data ingestion function')
            CustomException(e, sys)


