# Wine Classification App
Overview
This simple machine learning app uses Streamlit to classify wine varieties based on their chemical properties. Built as a demonstration for educational purposes, it showcases how to implement a classification model with a user-friendly web interface.

# Features
Interactive sliders to input wine chemical properties
Real-time prediction of wine variety
Visualization of prediction probabilities
Multi-page interface with About section

# Installation
Requirements
Python 3.8 or later

# Setup

# Clone this repository:
git clone https://github.com/yourusername/wine-classification-app.git
cd wine-classification-app

# Install dependencies:
pip install -r requirements.txt

# Run the app:
streamlit run app.py


# Project Structure
app.py: Main application entrypoint
pages/classifier.py: Wine variety classifier interface
pages/about.py: Information about the dataset and model
wine_classifier.pkl: Pre-trained RandomForest model

#  Dataset
The application uses the Wine dataset from scikit-learn, which contains chemical analyses of wines from three different cultivars.
Technologies Used: 

- Streamlit
- scikit-learn
- pandas
- NumPy

# For Educational Purposes
This application was created as a demonstration for a class project to showcase machine learning concepts and interactive web development.
License
MIT
