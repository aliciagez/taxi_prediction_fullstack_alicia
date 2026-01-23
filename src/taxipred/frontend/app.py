import streamlit as st


pages =[st.Page("stream_pages/Home.py", title="Home"),
        st.Page("stream_pages/Pred.py", title = "Pred"),
        st.Page("stream_pages/Raw_data.py", title = "Raw_data")
        ]

steam = st.navigation(pages)

steam.run()

