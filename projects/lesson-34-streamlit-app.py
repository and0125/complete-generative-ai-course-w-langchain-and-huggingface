import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

"""
Creating an ML application with Streamlit and a Random ForestClassifier
"""

@st.cache_data # loads the dataset into the cache, so its not loaded from the library every time
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# applying model
model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species']) # x axis is first, y or dependent feature is second

st.sidebar.title('input features')

# setting up the four features that are needed as input (independent variables) for determining the species
sepal_length  = st.sidebar.slider("sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max())) 
sepal_width   = st.sidebar.slider("sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max())) 
petal_length  = st.sidebar.slider("petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max())) 
petal_width   = st.sidebar.slider("petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max())) 

# Prediction
input_data = [ [sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]] # looking at the prediction from the first record input 


# outputting all predictions and species
st.write('Prediction')
st.write(f"The predicted species is: {predicted_species}")