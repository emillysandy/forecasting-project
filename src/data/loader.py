import pandas as pd

REQUIRED_COLUMNS = {"date", "item_id", "sales"}
OPTIONAL_COLUMNS = {"store_id"}


def load_sales_data(path: str) -> pd.DataFrame:
    """Load raw sales data from a CSV file."""
    print(f"Loading sales data: {path}")
    pass


def validate_sales_schema(data: pd.DataFrame) -> pd.DataFrame:
    """Validate that the raw sales data contains the required columns."""
    print("Validating sales data schema...")
    pass
