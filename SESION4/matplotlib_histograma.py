import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Histograma con Matplotlib")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    columnas = df.select_dtypes("number").columns.tolist()

    columna = st.selectbox("Selecciona columna numerica:", columnas)

    fig, ax = plt.subplots()
    ax.hist(df[columna], bins=20)
    ax.set_title(f"Histograma de {columna}")

    st.pyplot(fig)
