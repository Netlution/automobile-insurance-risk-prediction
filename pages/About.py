import streamlit as st
from style import set_black_background

set_black_background()

st.set_page_config(page_title="Automobile Insurance Risk Prediction App", layout="wide")

st.title("🚗 About the Project – Automobile Insurance Risk Prediction")

st.header("📖 Project Overview", anchor=False)

st.write("""
The Automobile Insurance Risk Prediction Project is designed to predict the insurance risk rating (symboling) of cars using a machine learning model trained on the well-known Automobile Dataset (imports-85).

✅ Symboling is an insurance risk indicator:
""")
st.markdown("""
- 🔥 **+3 → Highly risky vehicle**
- 🔥 **0 → Average risk**
- 🔥 **-3 → Very safe**
""")

st.write("""
This project helps insurance companies, car buyers, and auto manufacturers assess the safety/risk level of a vehicle based on its technical and categorical attributes.
""")

st.image("././static/Car_insurance_themed.png", caption="Car_insurance_themed")


st.header("📊 Dataset Information", anchor=False)
st.write("""
The dataset contains 205 instances of automobile specifications and insurance ratings.

It includes:
""")

# Bullet list with emojis
st.markdown("""
- 🚗 **Car specifications**: make, fuel type, aspiration, body style, drive type, engine details, mpg, and more.
- ⚠️ **Insurance risk rating (symboling)**: reflects how risky the car is compared to its price.
- 📉 **Normalized losses**: relative average loss payment per insured vehicle per year.
""")

st.image("././static/Car Insurance Infographic.png", caption="Car Insurance Infographic")


