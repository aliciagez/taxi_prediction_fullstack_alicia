import streamlit as st
import httpx
import json

url_pred = "http://127.0.0.1:8000/api/data/apri/taxi_pred"

st.markdown("Here you can predict taxi prices")

with st.form("data_pred"):
    Trip_Distance_km = st.number_input("Trip_Distance_km")
    Passenger_Count = st.number_input("Passenger_Count")
    Base_Fare  = st.number_input("Base_Fare")
    Per_Km_Rat = st.number_input("Per_Km_Rat ")
    Per_Minute_Rate = st.number_input("Per_Minute_Rate")
    Trip_Duration_Minutes  = st.number_input("Trip_Duration_Minute")
    Day_of_Week_Weekend = st.text_input("Day_of_Week_Weekend")
    Time_of_Day_Evening = st.text_input("Time_of_Day_Evening")
    Time_of_Day_Morning = st.text_input("Time_of_Day_Morning")
    Time_of_Day_Night = st.text_input("Time_of_Day_Night")

    user_input = st.form_submit_button("Get Prediction")

    if user_input:
        priceload = {
                "Trip_Distance_km": Trip_Distance_km, 
                "Passenger_Count": Passenger_Count,
                "Base_Fare": Base_Fare,
                "Per_Km_Rat": Per_Km_Rat,
                "Per_Minute_Rate": Per_Minute_Rate,
                "Trip_Duration_Minutes": Trip_Duration_Minutes,
                "Day_of_Week_Weekend": Day_of_Week_Weekend,
                "Time_of_Day_Evening": Time_of_Day_Evening,
                "Time_of_Day_Morning": Time_of_Day_Morning,
                "Time_of_Day_Night": Time_of_Day_Night

        }

        user_respose = httpx.post(f"{url_pred}",json=priceload)
        price_prediction = user_respose.json().get("pred_taxi_price")