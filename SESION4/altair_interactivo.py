import streamlit as st
import pandas as pd
import altair as alt

st.title("Grafico interactivo con Altair")

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    columnas = df.select_dtypes("number").columns.tolist()

    if columnas:
        x = st.selectbox("Columna para eje X:", columnas)
        y = st.selectbox("Columna para eje Y:", columnas)

        grafico = alt.Chart(df).mark_circle(size=60).encode(
            x=x,
            y=y,
            tooltip=list(df.columns)
        )

        st.altair_chart(grafico, use_container_width=True)
    else:
        st.error("No hay columnas numericas disponibles.")
