import streamlit as st
import httpx
import pandas as pd
from taxipred.utils.constants import RANDOM_FOREST

all_taxi_data = httpx.get("http://127.0.0.1:8000/api/data").json()

df = pd.read_csv(RANDOM_FOREST)

st.markdown("# Here you can checkout some of the data")

st.dataframe(df)

