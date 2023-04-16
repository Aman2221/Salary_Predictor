import streamlit as st
import pickle
import numpy as np


# @st.cache

# uploaded_file = st.file_uploader(
#     "Choose your database", accept_multiple_files=False)

# if uploaded_file is not None:
#     file_name = uploaded_file
# else:
#     file_name = "saved_steps.pkl"

def load_model():
    #with open('saved_steps.pkl', 'rb') as file:
    #    data = pickle.load(file)
    data = pickle.load(open('saved_steps.pkl', 'rb'))
    return data


data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

currency = ""
salaryConverted = 0

# @st.cache


def show_predict_page():
    st.write("""## Software Developer Salary Prediction""")

    st.write("""#### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries, key=3)
    education = st.selectbox("Education Level", education, key=4)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    inputs = {
        "Country": country,
        "Education": education,
        "Experience": experience
    }
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)
        salary = regressor.predict(X)
        if country == "India":
            currency = "₹"
            # salary[0]: .2f
            salaryConverted = int(81.98*salary[0])
        else:
            currency = "$"
            salaryConverted = int(salary[0])
        st.balloons()
        st.subheader(
            f"The estimated salary is {currency} {salaryConverted}")
        st.write("Inputs :", inputs)
        st.success('Are you satisfied with the results ?', icon="😃")
        successButton = st.button("Yes ✅")
        fail = st.button("No 😳")
        if successButton :
            st.balloons()
