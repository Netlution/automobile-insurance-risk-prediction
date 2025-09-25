import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from style import set_black_background
 
set_black_background()


st.title("📊 The Visualization Charts")

# Define column names
columns = [ 
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration",
    "num_doors", "body_style", "drive_wheels", "engine_location", "wheel_base",
    "length", "width", "height", "curb_weight", "engine_type", "num_cylinders",
    "engine_size", "fuel_system", "bore", "stroke", "compression_ratio",
    "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"
]


# Load dataset
with st.expander("See explanation"):
    # Load dataset with headers
    df = pd.read_csv(
        r"C:\Users\user\Downloads\AutombileC\imports-85.data", 
        header=None, 
        names=columns
    )

    df.index = df.index + 1

    st.dataframe(df.head(20))
                 

# Example column names (replace with correct ones if needed)
df.columns = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_doors",
    "body_style", "drive_wheels", "engine_location", "wheel_base", "length", "width",
    "height", "curb_weight", "engine_type", "num_cylinders", "engine_size",
    "fuel_system", "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
    "city_mpg", "highway_mpg", "price"
]

# Convert numeric columns
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["engine_size"] = pd.to_numeric(df["engine_size"], errors="coerce")

# Intro explanation with bullet list
st.write("This section provides insights into automobile prices using different visualizations:")

st.markdown("""
- ⛽ **Average Car Price by Fuel Type** → Compare how fuel type affects average selling price.  
- 🔧 **Engine Size vs Price** → See how engine capacity correlates with car price.  
- 🚘 **Price by Body Style** → Understand price variations across different car body styles.  
""")

# Tabs for charts
tab1, tab2, tab3 = st.tabs([
    "Average cars sale by fuel type",
    "Engine size by price",
    "Price distribution"
])

with tab1:
    avg_price = df.groupby("fuel_type", as_index=False)["price"].mean()
    fig_fuel_price = px.bar(
        avg_price,
        x="fuel_type",
        y="price",
        title="Average Car Price by Fuel Type",
        labels={"fuel_type": "Fuel Type", "price": "Average Price"},
        color="fuel_type"
    )
    st.plotly_chart(fig_fuel_price, use_container_width=True)

with tab2:
    fig_engine_size = px.scatter(
        df,
        x="engine_size",
        y="price",
        color="fuel_type",
        trendline="ols",
        title="Engine Size vs Price",
        labels={"engine_size": "Engine Size", "price": "Car Price"}
    )
    st.plotly_chart(fig_engine_size, use_container_width=True)

with tab3:
    fig_body = px.box(
        df,
        x="body_style",
        y="price",
        title="Price by Body Style",
        labels={"body_style": "Body Style", "price": "Car Price"}
    )
    st.plotly_chart(fig_body, use_container_width=True)

