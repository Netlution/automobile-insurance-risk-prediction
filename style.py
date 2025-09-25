import streamlit as st

def set_black_background():
    st.markdown(
        """
        <style>
        /* Main app background */
        [data-testid="stAppViewContainer"] {
            background-color: black;
        }

        /* Header (top bar) */
        [data-testid="stHeader"] {
            background-color: black;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: black;
        }

        /* Text color (so it’s visible) */
        .stMarkdown, .stText, .stDataFrame, .stTable, div, span, p {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
