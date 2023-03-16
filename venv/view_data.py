import streamlit as st
import numpy as np
import pandas as pd
import pickle
from st_aggrid import AgGrid, GridOptionsBuilder

def show_data():
    data = pd.read_csv("./survey_results_public.csv")
    st.write("""## Data used by the model for prediction""")
    st.write("""### You can filter and sort data by selecting column header""")
    AgGrid(data.head(50),gridOptions=GridOptionsBuilder.from_dataframe(data).build(),)
