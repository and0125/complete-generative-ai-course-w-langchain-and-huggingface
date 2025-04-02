import streamlit as st 
import pandas as pd

st.title("Text Input Demo")

name = st.text_input("enter your name: ")

# check if name exists
if name:
    st.write(f"Hello, {name}")

# using a slider

age = st.slider("Select your age:", 0,100, 25)
# sets the min, max, and sets the starting value as 25

st.write("your age is: ", age)

# using a select box

options = ["python", "Java", "C"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"You selected {choice}")

# Upload button for files

uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

df.to_csv("sampledata.csv")