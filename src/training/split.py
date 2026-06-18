import numpy as np
import pandas as pd


def temporal_split(
    data: pd.DataFrame,
    date_column: str,
    train_end: str,
    val_end: str,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split data into train, validation, and test sets using temporal cutoffs."""
    print(
        f"Splitting data with temporal split "
        f"(train until {train_end}, validation until {val_end})..."
    )
    pass


def split_features_target(
    data: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
) -> tuple[np.ndarray, np.ndarray]:
    """Extract feature matrix and target vector from a tabular dataset."""
    print(f"Splitting features ({feature_columns}) and target ({target_column})...")
    pass
