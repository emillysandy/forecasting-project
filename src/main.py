import numpy as np

from src.data.loader import load_sales_data, validate_sales_schema
from src.evaluation.metrics import evaluate
from src.models.linear import LinearRegressionModel
from src.preprocessing.transform import (
    MONTH_COLUMN,
    TARGET_AHEAD_COLUMN,
    aggregate_monthly_by_sku,
    build_supervised_dataset,
    lag_column_names,
    to_numpy,
)
from src.training.split import split_features_target, temporal_split
from src.utils.config import default_config


def main() -> None:
    """Run the monthly SKU demand forecasting pipeline.

    Functions are called in pipeline order, but most are still stubs and do
    not return real values yet. Placeholders (None, empty arrays) are used
    until each step is implemented.
    """
    print("Starting monthly SKU demand forecasting pipeline\n")

    config = default_config()
    raw_data = load_sales_data(str(config.data_path))
    data = validate_sales_schema(raw_data)
    monthly = aggregate_monthly_by_sku(data)

    build_supervised_dataset(
        monthly,
        lags=config.lags,
        horizon=config.forecast_horizon,
    )
    lag_columns = lag_column_names(config.lags)
    to_numpy(None, None, config.lags)

    temporal_split(
        None,
        date_column=MONTH_COLUMN,
        train_end=config.train_end,
        val_end=config.val_end,
    )

    split_features_target(None, lag_columns, TARGET_AHEAD_COLUMN)
    split_features_target(None, lag_columns, TARGET_AHEAD_COLUMN)
    split_features_target(None, lag_columns, TARGET_AHEAD_COLUMN)

    model = LinearRegressionModel()
    model.fit(np.array([]), np.array([]))

    val_predictions = model.predict(np.array([]))
    evaluate(np.array([]), val_predictions)

    test_predictions = model.predict(np.array([]))
    evaluate(np.array([]), test_predictions)

    print("\nPipeline finished.")


if __name__ == "__main__":
    main()
