import numpy as np

class FCM(BaseClustering):

    def __init__(self,):
        
        ...

    def fit(self,X):
        """Assign clusters to all data points in X and set self.labels_"""

    
    def predict(self,X):
        """Assign new data points X to the self.k clusters after being fit."""

    def fit_predict(self,X):
        """Fit the model to X and return the cluster labels for all data points."""
    
    def init_centroids(self, X: np.ndarray) -> np.ndarray:
        """Randomly select k points which will represent the k centroids."""
