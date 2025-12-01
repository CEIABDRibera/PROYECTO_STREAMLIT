import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualizacion Avanzada con Streamlit")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    columnas = df.select_dtypes("number").columns.tolist()
    columna = st.selectbox("Selecciona columna numerica:", columnas)

    tipo = st.selectbox(
        "Selecciona tipo de grafico:",
        ["Altair Scatter", "Histograma (Matplotlib)", "Boxplot (Seaborn)"]
    )

    if tipo == "Altair Scatter":
        grafico = alt.Chart(df).mark_circle(size=60).encode(
            x=columna,
            y=columna
        )
        st.altair_chart(grafico, use_container_width=True)

    elif tipo == "Histograma (Matplotlib)":
        fig, ax = plt.subplots()
        ax.hist(df[columna], bins=20)
        st.pyplot(fig)

    elif tipo == "Boxplot (Seaborn)":
        fig, ax = plt.subplots()
        sns.boxplot(data=df, y=columna, ax=ax)
        st.pyplot(fig)
