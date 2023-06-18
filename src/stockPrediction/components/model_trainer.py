import os
import sys
import numpy as np
from dataclasses import dataclass

from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, mean_absolute_error

from stockPrediction.exception import CustomException
from stockPrediction.logger import logging
from stockPrediction.utils import save_object

import warnings
warnings.filterwarnings('ignore')

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def train_arima_model(self, X, y, arima_order):
        history = [x for x in X]
        predictions = list()
        for t in range(len(y)):
            model = ARIMA(history, order=arima_order)
            model_fit = model.fit()
            yhat = model_fit.forecast()[0]
            predictions.append(yhat)
            history.append(y[t])
        
        rmse = np.sqrt(mean_squared_error(y, predictions))
        return (rmse, model_fit)
    

    def evaluate_models(self, dataset, test, p_values, d_values, q_values):
        dataset = dataset.astype('float32')
        best_score, best_cfg = float("inf"), None
        for p in p_values:
            for d in d_values:
                for q in q_values:
                    order = (p,d,q)
                    try:
                        rmse, model_obj = self.train_arima_model(dataset, test, order)
                        if rmse < best_score:
                            best_score, best_cfg = rmse, order

                            best_model = model_obj
                            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                                        obj=best_model)

                        logging.info('ARIMA%s RMSE=%.3f' % (order,rmse))
                    except Exception as e:
                        logging.info(f'error while training model {e}')
                        continue

        logging.info('Best ARIMA%s RMSE=%.3f' % (best_cfg, best_score))



    def initiate_model_training(self, train_df, test_df):

        p_values = range(0, 3)
        d_values = range(0, 3)
        q_values = range(0, 3)

        self.evaluate_models(train_df, test_df, p_values, d_values, q_values)

