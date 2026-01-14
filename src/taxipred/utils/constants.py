from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"
TAXI_DATA =  DATA_PATH / "taxi_trip_pricing.csv"
TAXI_REMOVED_NA = DATA_PATH / "removedna.csv"
TAXI_FILLED_NA = DATA_PATH / "fillna.csv"