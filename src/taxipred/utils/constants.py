from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"
MODEL_PATH = DATA_PATH / "taxi_price_random_forest.joblib"
TAXI_DATA =  DATA_PATH / "taxi_trip_pricing.csv"
TAXI_REMOVED_NA = DATA_PATH / "removed_na_lin_reg"
TAXI_FILLED_NA = DATA_PATH / "remove_na_log_reg.csv"
LINJER_FILLED_NA = DATA_PATH / "filled_na_lin_reg.csv"
LOG_REG_FILLED_NA = DATA_PATH / "filled_na_log_reg.csv"
RANDOM_FOREST = DATA_PATH / "random_forest.csv"