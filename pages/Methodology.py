import streamlit as st
import pandas as pd
from style import set_black_background

set_black_background()


st.title("📂 Data Preparation")

st.set_page_config(page_title="Automobile Insurance Risk Prediction App", layout="wide")


# Define column names
columns = [ 
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration",
    "num_doors", "body_style", "drive_wheels", "engine_location", "wheel_base",
    "length", "width", "height", "curb_weight", "engine_type", "num_cylinders",
    "engine_size", "fuel_system", "bore", "stroke", "compression_ratio",
    "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"
]

with st.expander("See explanation"):
    # Load dataset with headers
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    df = pd.read_csv(url, header=None, names=columns)


    df.index = df.index + 1

    st.dataframe(df.head(20))

st.write("""
The raw dataset (df) contained many features, some of which were dropped due to redundancy or missing values.
         
✅ **Features Removed:**
""")

# Bullet list for removed features
st.markdown("""
- 🔥 normalized_losses  
- 🔥 num_doors  
- 🔥 bore  
- 🔥 stroke  
- 🔥 horsepower  
- 🔥 peak_rpm  
- 🔥 price  
""")

st.write("""
This resulted in the cleaned dataset (df_drop) containing **symboling** as the target, and both categorical and numerical features as inputs.
""")

st.header("🛠️ Methodology", anchor=False)

st.write("✅ **Preprocessing**")
st.markdown("""
- ✔️ Categorical features encoded using OneHotEncoder  
- ✔️ Numerical features kept as continuous inputs  
""")

st.write("✅ **Modeling**")
st.markdown("""
- ✔️ RandomForestRegressor was chosen for its robustness and ability to capture non-linear feature relationships.  
- ✔️ Evaluation done using MSE, MAE, and R² score.  
""")

st.write("✅ **Deployment**")
st.markdown("""
- ✔️ The trained model was saved as `automobile_model.pkl`.  
- ✔️ A Streamlit web app was built for interactive predictions.  
""")

st.image("././static/Pipeline.png", caption="Pipeline")
