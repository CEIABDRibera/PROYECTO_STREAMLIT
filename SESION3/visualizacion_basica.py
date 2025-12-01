import streamlit as st
import pandas as pd

st.title("Visualizacion basica con Streamlit")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    st.write("Datos cargados:")
    st.dataframe(df)

    st.subheader("Grafico de lineas")
    st.line_chart(df)

    st.subheader("Grafico de barras")
    st.bar_chart(df)

    st.subheader("Grafico de area")
    st.area_chart(df)
