import streamlit as st
import numpy as np
import pandas as pd
# from firebase_admin import firestore

# firebase_config = {
#     "apiKey": "AIzaSyAUA8KxjPCcgmyc5Q2_eo2bQ9jn5UZIjcY",
#     "authDomain": "msc-it-python.firebaseapp.com",
#     "projectId": "msc-it-python",
#     "storageBucket": "msc-it-python.appspot.com",
#     "messagingSenderId": "106638161647",
#     "appId": "1:106638161647:web:1c23d156468c7f04de0d1a",
#     "measurementId": "G-GTMC3296PB"
# }

# auth.initialize_app(firebase_config)


def login():

    tab1, tab2 = st.tabs(["LOGIN", "SIGNUP", ])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        isLogin = st.button("Login", type="primary")
        if isLogin == True:
            if len(email) == 0 or len(password) == 0:
                st.warning('Please fill all fields properly', icon="⚠️")
    with tab2:
        name = st.text_input("Name")
        new_email = st.text_input("Email", key="Your email")
        new_password = st.text_input(
            "Password", key="Your password",  type="password")
        isSignup = st.button("Sign up", type="primary")
        if isSignup == True:
            if len(name) == 0 or len(new_email) == 0 or len(new_password):
                st.warning('Please fill all fields properly', icon="⚠️")
    # with col1:
    #     isLogin = st.button("Login")

    # with col2:
    #     isSignup = st.button("Sign up")

    # if (isWarning):
    # st.warning('This is a warning', icon="⚠️")
    # st.balloons()
    # st.write(isWarning, fail)
