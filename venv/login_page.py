import streamlit as st
import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials

cred = credentials.Certificate("./firebase-adminsdk.json")

firebase_admin.initialize_app(cred, {
   "databaseURL": "https://msc-it-python-default-rtdb.firebaseio.com"
})

def login():

    tab1, tab2 = st.tabs(["LOGIN", "SIGNUP", ])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        isLogin = st.button("Login", type="primary")
        if isLogin == True:
            if len(email) == 0 or len(password) == 0:
                st.warning('Please fill all fields properly', icon="⚠️")
            else:
                try:
                    user = auth.get_user_by_email(email)
                    st.write("user :", user)
                    auth.sign_in_with_email_and_password(email, password)
                    st.success('User logged in successfully',icon="✅")
                except Exception as e:
                    st.warning('Error while logging in user'.format(e))
                    st.write("Error :",e)

    with tab2:
        name = st.text_input("Name")
        new_email = st.text_input("Email", key="Your email")
        new_password = st.text_input(
            "Password", key="Your password",  type="password")
        isSignup = st.button("Sign up", type="primary")
        if isSignup == True:
            if len(name) == 0 or len(new_email) == 0 or len(new_password) == 0:
                st.warning('Please fill all fields properly', icon="⚠️")
            else :
                try:
                    user = auth.create_user(
                        email=new_email,
                        password=new_password
                    )
                    st.success('User created successfully',icon="✅")
                except Exception as e:
                    st.warning('Error creating user:'.format(e))

    # with col1:
    #     isLogin = st.button("Login")

    # with col2:
    #     isSignup = st.button("Sign up")

    # if (isWarning):
    # st.warning('This is a warning', icon="⚠️")
    # st.balloons()
    # st.write(isWarning, fail)
