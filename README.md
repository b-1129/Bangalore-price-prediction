# Bangalore-price-prediction
Regression on Bangalore House Prediction Dataset.

![Screenshot 2024-08-31 201440](https://github.com/user-attachments/assets/d52a5957-9347-429d-a647-2c145e54753c)
![Screenshot 2024-08-31 201524](https://github.com/user-attachments/assets/90a83f9a-e420-486c-b856-d2474c62d707)

# Bangalore Housing Price Prediction
This project aims to predict housing prices in Bangalore, India, using machine learning techniques. The model predicts prices based on key features such as location, BHK (number of bedrooms, hall, and kitchen), number of bathrooms, and total square feet area.

# Overview
Housing prices in Bangalore can vary significantly depending on several factors like location, the size of the property, and the number of rooms. This project utilizes a machine learning model to predict housing prices based on these features, helping potential buyers, sellers, and real estate professionals make informed decisions.

# Features
The model uses the following features to predict the price:

- **Location** : The area or locality within Bangalore.
- **BHK** : The number of bedrooms, hall, and kitchen in the property.
- **Bathroom** : The number of bathrooms in the property.
- **Total Square Feet** : The total area of the property in square feet.
# Data Preprocessing
- **One-Hot Encoding** : Location data is categorical and is converted into numerical format using One-Hot Encoding.
- **Standard Scaler** : The features are scaled using StandardScaler to ensure that all features contribute equally to the model.

# Models Used
Several machine learning models were tested to find the best fit for predicting housing prices:

- **Linear Regression** : Provided good results but similar to Ridge Regression.
- **Lasso Regression** : Did not perform as well as Linear or Ridge Regression.
- **Ridge Regression** : Chosen as the final model due to its ability to handle multicollinearity and prevent overfitting, providing the most reliable predictions.
# Final Model
The Ridge Regression model was selected as the final model for this project because it produced similar results to Linear Regression but with better regularization, which helps in managing bias-variance trade-offs effectively.

# Web Application
The project includes a web application built with Streamlit to provide an interactive user interface where users can input their property details and get a predicted price for a house in Bangalore.

# How to Run the Application

1. Clone the repository
2. Install the required dependencies
3. Run the Streamlit application

# Conclusion
This project provides a practical solution for predicting housing prices in Bangalore based on various features. By leveraging Ridge Regression, StandardScaler for scaling, and a user-friendly web interface, users can easily input their property details and obtain a price prediction.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request to contribute to this project.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contact
- **email** : brijesh29.it11@gmail.com
- **GitHub** : https://github.com/b-1129
