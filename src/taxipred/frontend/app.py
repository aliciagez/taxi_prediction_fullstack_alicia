import streamlit as st
import httpx


pages =[st.Page("stream_pages/Home.py", title="Home"),
        st.Page("stream_pages/Pred.py", title = "Pred"),
        st.Page("stream_pages/Metrics.py", title = "Metrics")
        ]

steam = st.navigation(pages)

steam.run()

