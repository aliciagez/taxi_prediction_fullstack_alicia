import streamlit as st
import httpx

url_pred = "http://127.0.0.1:8000/api/data/apri/taxi_pred"

st.markdown("Here you can predict taxi prices")

with st.form("data_pred"):
    Trip_Distance_km = st.number_input("Trip_Distance_km")
    Passenger_Count= st.number_input("Passenger_Count", min_value=1, max_value =9, step=1, value=1, format="%d")
    Base_Fare  = st.number_input("Base_Fare", min_value=0.0, max_value=100.0, value=3.502989)
    Per_Km_Rate = st.number_input("Per_Km_Rate", min_value=0.0, max_value=300.0, value=1.233316)
    Per_Minute_Rate = st.number_input("Per_Minute_Rate", min_value=0.0, max_value=300.0, value=0.292916)
    Trip_Duration_Minutes  = st.number_input("Trip_Duration_Minute", min_value=0.0, max_value=300.0, value=62.118116)

    Day_of_Week_Weekend = st.checkbox("Weekend?")
    Time_of_Day = st.selectbox("Time of day (Optional)", ["None", "Evening", "Morning", "Night"])
    
    user_input = st.form_submit_button("Get Prediction")

    if user_input:
        priceload = {
                "Trip_Distance_km": Trip_Distance_km, 
                "Passenger_Count": int(Passenger_Count),
                "Base_Fare": Base_Fare,
                "Per_Km_Rate": Per_Km_Rate,
                "Per_Minute_Rate": Per_Minute_Rate,
                "Trip_Duration_Minutes": Trip_Duration_Minutes,

        }

        user_respose = httpx.post(f"{url_pred}",json=priceload)
        price_prediction = user_respose.json().get("pred_taxi_price")
        st.markdown(f"Predicted taxi price:{price_prediction}")
        st.write("staus", user_respose.status_code)
     