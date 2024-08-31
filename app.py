import streamlit as st
import pandas as pd
import pickle

# Load the dataset
data_path = 'clean_data.csv'
df = pd.read_csv(data_path)

# Extract unique values
unique_locations = df['location'].unique()
unique_bhk = sorted(df['bhk'].unique())
unique_bathroom = sorted(df['bath'].unique())

# Load the trained pipeline model
model_path = 'RidgeModel.pkl'
with open(model_path, 'rb') as file:
    model_pipeline = pickle.load(file)

# Streamlit app layout
st.title("Bangalore House Price Prediction")

st.header("Enter the property details:")

# Input fields for user input using extracted data
location = st.selectbox('Location', unique_locations)
bhk = st.selectbox('BHK', unique_bhk)
bath = st.selectbox('Bathroom', unique_bathroom)
total_sqft = st.number_input('Total Square Feet')

# Prepare the input data in the format expected by the model pipeline
input_data = pd.DataFrame([[location, bhk, bath, total_sqft]], 
                          columns=['location', 'bhk', 'bath', 'total_sqft'])

# Button for prediction
if st.button('Predict Price'):
    # Make prediction using the trained model pipeline
    price = model_pipeline.predict(input_data)[0] * 1e5
    st.success(f"The predicted price of the property is ₹{price:,.2f}")
