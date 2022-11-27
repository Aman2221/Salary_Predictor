import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from view_data import show_data
# st.set_page_config(
#     page_title='Salary Predictor',
#     page_icon='asset/logo.png'
# )

page = st.sidebar.selectbox(
    "Explore Or Predict", ("Predict", "Explore", "View Data"))

if page == "Predict":
    show_predict_page()
elif page == "View Data":
    show_data()
else:
    show_explore_page()
