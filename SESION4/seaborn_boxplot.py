import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Boxplot con Seaborn")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    columnas = df.select_dtypes("number").columns.tolist()

    columna = st.selectbox("Selecciona columna numerica:", columnas)

    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=columna, ax=ax)

    st.pyplot(fig)
