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
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    isWarning = st.button("Feedback")
    if (isWarning):
        # st.warning('This is a warning', icon="⚠️")
        st.balloons()
        # st.write(isWarning, fail)
