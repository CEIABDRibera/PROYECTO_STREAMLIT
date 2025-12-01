import streamlit as st
import pandas as pd

st.title("Exploracion de Datos")

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    st.write("Columnas del dataset:")
    st.write(df.columns.tolist())

    st.subheader("Estadisticas basicas")
    st.write(df.describe())

    st.subheader("Primeras filas")
    st.dataframe(df.head())
