import streamlit as st
import httpx


pages =[st.Page("", title="Home"),
        st.Page("", titel = "Pred"),
        st.Page("", titel = "Metrics")
        ]

steam = st.navigation(pages)