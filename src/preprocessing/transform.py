import numpy as np
import pandas as pd

SKU_COLUMN = "item_id"
DATE_COLUMN = "date"
TARGET_COLUMN = "sales"
MONTH_COLUMN = "month"
TARGET_AHEAD_COLUMN = "target"


def aggregate_monthly_by_sku(data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate daily sales into monthly totals per SKU across all stores."""
    print("Aggregating daily sales into monthly totals per SKU...")
    pass


def lag_column_names(lags: tuple[int, ...]) -> list[str]:
    """Return lag feature column names for the given lag values."""
    print(f"Defining lag columns: {lags}")
    return [f"lag_{lag}" for lag in lags]


def add_lag_features(
    monthly: pd.DataFrame,
    lags: tuple[int, ...],
) -> pd.DataFrame:
    """Add lag columns for each SKU time series."""
    print(f"Creating lag features: {lags}")
    pass


def build_supervised_dataset(
    monthly: pd.DataFrame,
    lags: tuple[int, ...],
    horizon: int = 1,
) -> tuple[pd.DataFrame, pd.Series]:
    """Build tabular features (X) and one-step-ahead target (y)."""
    print(f"Building supervised dataset (X, y) with horizon={horizon}...")
    add_lag_features(monthly, lags)
    pass


def to_numpy(
    features: pd.DataFrame,
    target: pd.Series,
    lags: tuple[int, ...],
) -> tuple[np.ndarray, np.ndarray]:
    """Convert feature matrix and target vector to NumPy arrays."""
    print("Converting features and target to NumPy arrays...")
    pass
