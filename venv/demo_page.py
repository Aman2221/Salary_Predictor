# Modules
import pyrebase
import streamlit as st
from datetime import datetime

# Configuration Key
firebaseConfig = {
    "apiKey": "AIzaSyAUA8KxjPCcgmyc5Q2_eo2bQ9jn5UZIjcY",
    "authDomain": "msc-it-python.firebaseapp.com",
    "databaseURL": "https://msc-it-python-default-rtdb.firebaseio.com",
    "projectId": "msc-it-python",
    "storageBucket": "msc-it-python.appspot.com",
    "messagingSenderId": "106638161647",
    "appId": "1:106638161647:web:1c23d156468c7f04de0d1a",
    "measurementId": "G-GTMC3296PB"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

# App 

# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Please input your app handle name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()

# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('Jump to',['Home','Workplace Feeds', 'Settings'])
    
            