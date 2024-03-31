import pandas as pd
import streamlit as st
import numpy as np

st.title("Hi This is my First Streamlit App!")

st.write("My first DataFrame")

st.write(
pd.DataFrame({
    'A': [1, 5, 9, 7],
    'B': [3, 2, 4, 8],
    'C': [3, 2, 4, 8],
    'D': [3, 2, 4, 8],
  })
)
