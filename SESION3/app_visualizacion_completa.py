import streamlit as st
import pandas as pd

st.title("App de visualizacion interactiva")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    columnas = df.select_dtypes("number").columns.tolist()

    seleccion = st.multiselect("Selecciona columnas numericas:", columnas)

    tipo = st.selectbox(
        "Selecciona tipo de grafico:",
        ["Lineas", "Barras", "Area"]
    )

    if seleccion:
        if tipo == "Lineas":
            st.line_chart(df[seleccion])
        elif tipo == "Barras":
            st.bar_chart(df[seleccion])
        elif tipo == "Area":
            st.area_chart(df[seleccion])
    else:
        st.warning("Selecciona columnas para visualizar.")
