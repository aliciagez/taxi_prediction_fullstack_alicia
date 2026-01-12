from taxipred.utils.constants import TAXI_DATA
import pandas as pd

df = pd.read_csv(TAXI_DATA)

print(df.head(5))
