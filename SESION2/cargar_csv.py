import streamlit as st
import pandas as pd

st.title("Cargar un archivo CSV")

archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    st.write("Vista previa de los datos:")
    st.dataframe(df)

    st.subheader("Estadisticas basicas")
    st.write(df.describe())
