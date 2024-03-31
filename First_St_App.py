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

st.write("My CheckBox Experience")

if st.checkbox("Main Checkbox"):
    st.text("Check Box Active")

st.write("Display Dataframe, after Checking Box")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    #chart_data
    st.write(chart_data)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

st.write("Display Dataframe, after Checking Box")

if st.checkbox('First Column'):
    st.write(df['first column']
elif st.checkbox('Secon Column'):
    st.write(df['second column']

st.write("Select Box")

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

'''
option = st.selectbox(
    'Which number do you like best?',
     'first_column', 
     'second_column'
)
if option = "first_column":
    st.write(df['first column']
else:
    st.write(df['second column']

'''
