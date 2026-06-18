from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_DATA_PATH = PROJECT_ROOT / "data" / "sample" / "fake_sales.csv"

DEFAULT_LAGS = (1, 2, 3, 6, 12)
DEFAULT_FORECAST_HORIZON = 1
DEFAULT_TRAIN_END = "2015-06"
DEFAULT_VAL_END = "2015-09"


@dataclass(frozen=True)
class ProjectConfig:
    lags: tuple[int, ...]
    forecast_horizon: int
    train_end: str
    val_end: str
    target_column: str
    sku_column: str
    date_column: str
    data_path: Path


def default_config() -> ProjectConfig:
    """Return the default project configuration."""
    print("Loading default project configuration...")
    return ProjectConfig(
        lags=DEFAULT_LAGS,
        forecast_horizon=DEFAULT_FORECAST_HORIZON,
        train_end=DEFAULT_TRAIN_END,
        val_end=DEFAULT_VAL_END,
        target_column="sales",
        sku_column="item_id",
        date_column="date",
        data_path=SAMPLE_DATA_PATH,
    )
