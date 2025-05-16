import streamlit as st

st.title("📊 Acerca del Conjunto de Datos de Vino y el Modelo")

st.markdown("""
El **conjunto de datos de Vino** es un conjunto de datos clásico en aprendizaje automático y estadística. Contiene:

- 178 muestras
- 3 variedades de vino diferentes
- 13 características químicas por muestra (alcohol, ácido málico, ceniza, etc.)

Este conjunto de datos contiene los resultados de un análisis químico de vinos cultivados en la misma región de Italia pero derivados de tres diferentes cultivares.

El modelo utilizado aquí es un clasificador previamente entrenado (Random Forest) guardado en `wine_classifier.pkl`.

Construido usando [Streamlit](https://streamlit.io).
""")
