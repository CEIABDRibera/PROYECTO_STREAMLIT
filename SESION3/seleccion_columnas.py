import streamlit as st
import pandas as pd

st.title("Seleccion de columnas para graficar")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    columnas = df.select_dtypes("number").columns.tolist()
    seleccion = st.multiselect("Selecciona columnas numericas:", columnas)

    if seleccion:
        st.line_chart(df[seleccion])
    else:
        st.info("Selecciona al menos una columna para visualizar.")
