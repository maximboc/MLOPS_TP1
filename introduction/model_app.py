import streamlit as st
import joblib
import pandas as pd

model = joblib.load('regression.joblib')

size = st.number_input(label = 'size', min_value = 0)
bedrooms = st.number_input(label = 'number of bedrooms', min_value=0, step=1)
garden = st.number_input(label = 'Does the house have a garden ?', min_value=0, max_value = 1, step=1)

if st.button("Predict"):
    elements = pd.DataFrame([[size, bedrooms, garden]], columns=["size", "nb_rooms", "garden"])
    pred = model.predict(elements)
    st.write(f"Predicted price: {pred[0]:,.2f}€")
