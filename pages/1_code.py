import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn import datasets

wine = datasets.load_wine()
target_names = wine.target_names

with open("wine_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title("Clasificador de Variedades de Vino")
st.write("Ingrese las propiedades químicas para clasificar la variedad de vino.")

alcohol = st.slider("Alcohol", min_value=11.0, max_value=15.0, step=0.1, value=13.0)
malic_acid = st.slider("Ácido Málico", min_value=0.5, max_value=6.0, step=0.1, value=2.0)
color_intensity = st.slider("Intensidad de Color", min_value=1.0, max_value=13.0, step=0.1, value=5.0)
hue = st.slider("Tonalidad", min_value=0.4, max_value=1.8, step=0.05, value=1.0)
proline = st.slider("Prolina", min_value=200, max_value=1600, step=50, value=700)

with st.expander("Propiedades Avanzadas"):
    ash = st.slider("Ceniza", min_value=1.0, max_value=4.0, step=0.1, value=2.3)
    alcalinity = st.slider("Alcalinidad de la Ceniza", min_value=10.0, max_value=30.0, step=0.5, value=19.0)
    magnesium = st.slider("Magnesio", min_value=70, max_value=170, step=5, value=100)
    phenols = st.slider("Fenoles Totales", min_value=0.5, max_value=4.0, step=0.1, value=2.0)
    flavanoids = st.slider("Flavonoides", min_value=0.0, max_value=6.0, step=0.1, value=2.0)
    nonflavanoids = st.slider("Fenoles No Flavonoides", min_value=0.0, max_value=1.0, step=0.05, value=0.4)
    proanthocyanins = st.slider("Proantocianinas", min_value=0.0, max_value=4.0, step=0.1, value=1.5)
    od_ratio = st.slider("Ratio OD280/OD315", min_value=1.0, max_value=4.0, step=0.1, value=2.5)

if st.button("Predecir Variedad de Vino"):
    features = np.array([[
        alcohol, malic_acid, ash, alcalinity, magnesium, 
        phenols, flavanoids, nonflavanoids, proanthocyanins, 
        color_intensity, hue, od_ratio, proline
    ]])
    
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)
    
    st.success(f"Variedad de Vino Predicha: **{target_names[prediction[0]]}**")
    st.subheader("Probabilidades de Predicción")
    
    proba_df = pd.DataFrame({
        'Variedad': target_names,
        'Probabilidad': prediction_proba[0]
    })
    
    st.bar_chart(proba_df.set_index('Variedad'))
    