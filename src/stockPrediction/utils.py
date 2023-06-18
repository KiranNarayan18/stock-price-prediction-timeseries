
import os
import sys
import dill
import pickle
from stockPrediction.exception import CustomException
from stockPrediction.logger import logging


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