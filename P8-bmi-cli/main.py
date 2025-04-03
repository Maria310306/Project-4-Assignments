import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height =st.slider("Adjust your height accordingly(in cm)", 100, 250,175)
mass =st.slider("Adjust your mass accordingly(in kg)", 20, 200,70)

bmi= mass/((height/100)**2)

st.write(f"Your Body Mass Index is: {bmi:.2f}")

st.write("|||| BMI Categories ||||")
st.write("BMI < 18.5 - Underweight")
st.write("18.6 < BMI < 25 - Normal Weight")
st.write("25.1 < BMI < 30 - Overweight")
st.write("30.1 < BMI < greater - Obesity")

