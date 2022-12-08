from fastapi import FastAPI
import ktrain
import numpy as np
import pickle
import os

from typing import Union


class DistilbertContextClassifier():
    def __init__(self, model_dir:str):
        """Make predictions from the DistilBERT context classifier.

        Args:
            model_dir (str): The directory location of the DistilBERT model.
        """
        self.model_dir = model_dir
        self.predictor_fname = os.path.join(self.model_dir, "tf_model.preproc")
        
        self.preprocessor = self._get_preprocessor()
        self.predictor = self._get_predictor()
        self.model = self.predictor.model

        self.labels = self.predictor.get_classes()
        self.labels_mapper = {i: label for i, label in enumerate(self.labels)}
    
    def _get_preprocessor(self):
        with open(self.predictor_fname, "rb") as preproc:
            preprocessor = pickle.load(preproc)
        
        return preprocessor

    def _get_predictor(self):
        predictor = ktrain.load_predictor(self.model_dir)
        return predictor

    def map_label(self, index:int) -> str:
        """Map a label from its one-hot encoded integer index to its string
        representation.
        """
        label = self.labels_mapper[index]
        return label

    def predict_label(self, x_stream:list[str]) -> str:
        """Predict the most probable label from a stream of observations

        Args:
            x_stream (list[str]): A list of observations to make predictions on

        Returns:
            y_pred_labels (list[str]): The most probable label for each
                observation.
        """
        y_pred_labels = self.predictor.predict(x_stream)
        return y_pred_labels

    def predict_probabilities(
            self, x_stream:list[str]
        ) -> list[dict[str, float]]:
        """Predict the probability of each label occuring from each observation

        Args:
            x_stream (list[str]): A list of observations to make predictions on
        
        Returns:
            y_pred (list[dict[str, float]]): Each observation is a
                dictionary where the key corresponds to the label and the value
                corresponds to the probability of the label.
        """
        y_pred_probabilities = self.predictor.predict_proba(x_stream)

        y_pred = []
        for probabilities in y_pred_probabilities:
            y_pred_labels = {
                self.map_label(i): float(probability)
                for i, probability in enumerate(probabilities)
            }
            y_pred.append(y_pred_labels)

        return y_pred


MODEL_DIR = "distilbert"
classifier = DistilbertContextClassifier(MODEL_DIR)


# Instantiate app
app = FastAPI()


@app.get("/distilbert/{x_stream}")
async def make_prediction(
        x_stream:str, return_probabilities:bool=True
    ) -> Union[str, dict[str, float]]:
    """Predict the label of an incoming observation using the DistilBERT
    context classifier

    Args:
        
        x_stream (str): The incoming text to classify
       
        return_probabilities (bool): Whether to return the probabilities for
            each class
    
    Returns:
      
        predictions (str or dict[str, float]): The predictions by the model. If
            return_probabilities is True, we return a dictionary that
            corresponds to model probability. Otherwise, we simply return the
            most probable label.
    """
    # Coerce the observation into a single element list to feed the classifier
    x_stream = [x_stream]

    if return_probabilities:
        predictions = classifier.predict_probabilities(x_stream)
        return predictions
    
    predictions = classifier.predict_label(x_stream)
    return predictions
    