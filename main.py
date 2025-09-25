import streamlit as st
import pandas as pd
import joblib
# from style import set_black_background

# set_black_background()

st.set_page_config(page_title="Automobile Insurance Risk Prediction App", layout="wide")

# ✅ Custom CSS for dropdowns, sliders, and buttons
st.markdown("""
    <style>
    /* Dropdown (selectbox) main box */
    div[data-baseweb="select"] > div {
        background-color: #001f3f !important; /* Deep blue background */
        color: white !important;              /* White text */
        border-radius: 8px;
    }

    /* Selected text inside dropdown */
    div[data-baseweb="select"] span {
        color: white !important; 
        font-weight: bold;
    }

    /* Dropdown arrow */
    div[data-baseweb="select"] svg {
        fill: white !important;
    }

    /* Dropdown menu (when opened) */
    ul[role="listbox"] {
        background-color: #001f3f !important; 
        color: white !important;
    }

    /* Dropdown options text */
    ul[role="listbox"] li {
        color: white !important; 
        font-weight: normal;
    }

    /* Hover effect for dropdown options */
    ul[role="listbox"] li:hover {
        background-color: #004080 !important; 
        color: white !important;
    }

    /* Slider track */
    .stSlider > div[data-baseweb="slider"] > div > div {
        background: #001f3f !important; 
    }

    /* Slider thumb (circle) */
    .stSlider > div[data-baseweb="slider"] > div > div > div {
        background-color: #001f3f !important;
        border: 2px solid white !important;
    }

    /* Style for Streamlit button */
    div.stButton > button:first-child {
        background-color: #001f3f; 
        color: white;              
        border-radius: 8px;        
        height: 3em;
        width: 100%;
        border: none;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #004080; 
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)


# ---------------------------
# 🚘 App Title & Description
# ---------------------------
st.title("🚘 Automobile Insurance Risk Prediction App")
st.write("This app predicts the **insurance risk rating (symboling)** of a car based on its features.")

# Sidebar Inputs
st.sidebar.header("User Input Features")

Make = st.sidebar.selectbox("Make", options=[
    'toyota', 'nissan', 'mazda', 'mitsubishi',
    'honda', 'subaru', 'volkswagen', 'volvo',
    'peugot', 'dodge', 'mercedes-benz', 'bmw',
    'audi', 'plymouth', 'saab', 'porsche',
    'isuzu', 'alfa-romero', 'chevrolet', 'jaguar',
    'renault', 'mercury'
])

Fuel_type = st.sidebar.selectbox("Fuel Type", options=["gas", "diesel"])
Aspiration = st.sidebar.selectbox("Aspiration", options=['std', 'turbo'])
Body_style = st.sidebar.selectbox("Body Style", options=[
    "sedan", "hatchback", "wagon", "hardtop", "convertible"
])
Drive_wheels = st.sidebar.selectbox("Drive Wheels", options=["fwd", "rwd", "4wd"])
Engine_location = st.sidebar.selectbox("Engine Location", options=["front", "rear"])

Wheel_base = st.sidebar.number_input("Wheel Base", min_value=85.0, max_value=130.0, value=95.0)
Length = st.sidebar.number_input("Length", min_value=140.0, max_value=210.0, value=170.0)
Width = st.sidebar.number_input("Width", min_value=60.0, max_value=75.0, value=65.0)
Height = st.sidebar.number_input("Height", min_value=47.0, max_value=60.0, value=54.0)
Curb_weight = st.sidebar.number_input("Curb Weight", min_value=1500, max_value=4000, value=2500)

Engine_type = st.sidebar.selectbox("Engine Type", options=[
    "ohc", "ohcf", "ohcv", "dohc", "l", "rotor", "dohcv"
])
Num_cylinders = st.sidebar.selectbox("Number of Cylinders", options=[
    "four", "six", "five", "eight", "two", "twelve", "three"
])
Engine_size = st.sidebar.slider("Engine Size", 60, 350, 120)

Fuel_system = st.sidebar.selectbox("Fuel System", options=[
    "mpfi", "2bbl", "idi", "1bbl", "spdi", "4bbl", "mfi", "spfi"
])
Compression_ratio = st.sidebar.number_input("Compression Ratio", min_value=7.0, max_value=23.0, value=9.0)
City_mpg = st.sidebar.slider("City mpg", 10, 55, 25)
Highway_mpg = st.sidebar.slider("Highway mpg", 15, 55, 30)

# Collect Data
input_data = {
    "make": Make,
    "fuel_type": Fuel_type,
    "aspiration": Aspiration,
    "body_style": Body_style,
    "drive_wheels": Drive_wheels,
    "engine_location": Engine_location,
    "wheel_base": Wheel_base,
    "length": Length,
    "width": Width,
    "height": Height,
    "curb_weight": Curb_weight,
    "engine_type": Engine_type,
    "num_cylinders": Num_cylinders,
    "engine_size": Engine_size,
    "fuel_system": Fuel_system,
    "compression_ratio": Compression_ratio,
    "city_mpg": City_mpg,
    "highway_mpg": Highway_mpg
}

df_input = pd.DataFrame([input_data])

st.subheader("User Input Summary")
st.dataframe(df_input)

# Prediction
if st.button("Predict"):
    rf = joblib.load("automobile_model.pkl")  # Load trained model
    prediction = rf.predict(df_input)  # Predict symboling
    
    st.subheader("Prediction Result")
    st.write(f"Predicted Symboling: **{prediction[0]}**")

    if prediction[0] == 3:
        st.error("The car is **risky** (symboling = +3).")
    elif prediction[0] == -3:
        st.success("The car is **very safe** (symboling = -3).")
    elif prediction[0] > 0:
        st.warning("The car has **above average risk**.")
    elif prediction[0] < 0:
        st.info("The car is **safer than average**.")
    else:
        st.write("The car has **average risk**.")


st.header("💻 Streamlit Application", anchor=False)

st.write("""
The project includes an interactive web application built with **Streamlit**.

👉 Users can input car features (e.g., make, fuel type, dimensions, mpg).  
👉 The model predicts the **symboling (risk rating)**.  
👉 Results are explained clearly with categories:
""")

st.markdown("""
- ✅ **Very Safe**
- ℹ️ **Safer than Average**
- ⚠️ **Above Average Risk**
- ❌ **Risky**
""")

st.image("././static/Streamlit application.png", caption="Streamlit App Example")

st.header("📌 Conclusion", anchor=False)

st.write("""
This project demonstrates how **machine learning** can enhance insurance decision-making by predicting automobile risk ratings based on specifications.
""")

st.subheader("🔑 Practical Use Cases")

st.markdown("""
- 🏦 **Insurance companies** → Adjust policies and premiums.  
- 🚘 **Car buyers** → Make safer purchase decisions.  
- 🏭 **Manufacturers** → Evaluate risk trends across models.  
""")

st.write("""
✨ This project combines **data science, machine learning, and web deployment** to create a real-world application for automobile insurance risk analysis.
""")
