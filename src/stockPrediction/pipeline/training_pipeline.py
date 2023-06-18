
import sys
import os
import pandas as pd

from dataclasses import dataclass

from stockPrediction.components.data_ingestion import DataIngestion
from stockPrediction.components.data_transformation import DataTransformation
from stockPrediction.components.model_trainer import ModelTrainer
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_training(train_arr,test_arr))