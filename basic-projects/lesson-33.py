import streamlit as st
import pandas as pd
import numpy as np 

## starting with a streamlit application

# Title of Application
st.title("Hello Steamlit")

# Simple Text
st.write("this is simple text to write on the page of the webapp for streamlit")

# create a dataframe

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

## Display the dataframe

st.write("here is the dataframe")
st.write(df)

## Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b','c'] # creates 3 columns of random data
)
st.line_chart(chart_data)