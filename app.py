import streamlit as st
import pandas as pd
import numpy as np
import time

# Initialize web app with simple table and comment
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Create text and table in streamlit web app
st.write("This is my first streamlit web application. Here's a sample dataframe:")

st.write(df)

# Line charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

# Widgets
x = st.slider('x')
st.write(x, 'Squared is', x * x)

# Text input
st.text_input("Your name", key='name')


# Check box (text input)
if st.checkbox("Output session name"):
    st.session_state.name

# Check box (line chart)
if st.checkbox("Output line chart"):
    st.line_chart(chart_data)    


# Selectbox
option = st.selectbox("Which option do you want", df['first column'])

# Sidebar
option_sidebar = st.sidebar.selectbox("How would you like to be contacted?", ('Email', 'Messenger', 'Telegram'))
add_slider = st.sidebar.slider("Select a range of values", 0, 100, (25, 75))


# progress bar


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    # Update the progress bar with each iteration
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

