import streamlit as st
import pandas as pd

st.title("Filtro numerico sobre un dataset")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    columnas_numericas = df.select_dtypes("number").columns

    if len(columnas_numericas) == 0:
        st.error("No hay columnas numericas en este dataset.")
    else:
        columna = st.selectbox("Selecciona columna numerica:", columnas_numericas)

        minimo = float(df[columna].min())
        maximo = float(df[columna].max())

        rango = st.slider("Selecciona rango:", minimo, maximo, (minimo, maximo))

        df_filtrado = df[(df[columna] >= rango[0]) & (df[columna] <= rango[1])]

        st.subheader("Datos filtrados")
        st.dataframe(df_filtrado)
