import streamlit as st
import numpy as np
import pandas as pd


def show_data():
    data = pd.read_csv("./survey_results_public.csv")
    st.write("""## Data used by the model for prediction""")
    st.dataframe(data)
