import pandas as pd
import streamlit as st
import numpy as np
import time

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

st.write("My second DataFrame - Display using table") 

df_city = pd.DataFrame({
    'Karnataka Districts': ['Bagalkot','Bengaluru','Belagavi','Ballari','Bidar','Raichur'],
    'Colleges': ["BIT", "RV", "GIT", "BEIT", "APPA", "GEC"]
    })

st.table(df_city)

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
    st.write(df['first column'])
elif st.checkbox('Second Column'):
    st.write(df['second column'])

st.write("Select Box")

df = pd.DataFrame({
    'Karnataka Districts': ['Bagalkot','Bengaluru','Belagavi','Ballari','Bidar','Raichur'],
    'Colleges': ["BIT", "RV", "GIT", "BEIT", "APPA", "GEC"]
    })

option = st.selectbox(
    'Which City you do you like best?',
     df['Karnataka Districts'])

'You selected: ', option

option1 = st.selectbox(
    'Which College you do you like best?',
     df['Colleges'])

'You selected: ', option1


st.subheader("Basic Widgets of Streamlit")

st.write("My first Slider")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write("Slide with Min and Max")

slider_value = st.slider("Slider", min_value=0.5, max_value=9.5)
st.text(f"Slider value is {slider_value} and its double is {slider_value*slider_value}" )


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write("Completed")

# Usage of multiselect widget

options_1 = st.multiselect(
    'What are your favorite colors and citys',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red', 'Green'])
    #['Yellow', 'Red'])
    #)

st.write('You selected:', options_1)

st.sidebar.text("Please Enter Your name")
name = st.sidebar.text_input("Your name", key="name")
st.sidebar.write("your name is", name)

st.sidebar.checkbox("Side Panel Checkbox")
