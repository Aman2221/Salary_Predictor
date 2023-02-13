import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from view_data import show_data
from login_page import login

# st.set_page_config(
#     page_title='Salary Predictor',
#     page_icon='asset/logo.png'
# )

isLogin = True
if (isLogin):
    page = st.sidebar.selectbox(
        "Explore Or Predict", ("Predict", "Explore", "View Data", "Login"))
else:
    page = st.sidebar.selectbox("Login page", ("Login",))

if (isLogin):
    if page == "Predict":
        show_predict_page()
    elif page == "View Data":
        show_data()
    elif page == "Login":
        login()
    else:
        show_explore_page()
else:
    login()


st.caption(
    "Support me by either reporting problem for bad formatting or buying a coffee, Aman Singh!")
