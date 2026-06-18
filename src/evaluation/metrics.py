import numpy as np


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute mean absolute error."""
    print("Computing MAE...")
    pass


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute root mean squared error."""
    print("Computing RMSE...")
    pass


def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    """Compute a summary of evaluation metrics."""
    print("Evaluating model performance...")
    mae(y_true, y_pred)
    rmse(y_true, y_pred)
    pass
