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

st.subheader("Basic APP Components")

st.write("My first Radio Button")

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
elif genre == 'Drama':
    st.write('You selected Drama.')
elif genre == 'Documentary':
    st.write('You selected Documentary.')
else:
    st.write("You didn't select comedy.")
