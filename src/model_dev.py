import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression


class Model(ABC):
    """
    Abstract class for All Models
    """
    
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Trains the model
        Args:
            X_train: Training data
            y_train: Training Labels
        Returns:
            None 
        """
        pass
    
class LinearRegressionModel(Model):
    """
    Linear Regression model
    """
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, X_train, y_train, **kwargs):
        """
        Trains the model
        Args:
            X_train: Training data
            y_train: Training labels 
        Returns: 
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training Completed")
            return reg
        except Exception as e:
            logging.error("Error in Training model: {}".format(e))
            raise e
        

