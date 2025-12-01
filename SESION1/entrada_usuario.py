import streamlit as st

st.title("Ejemplo de entrada de usuario")

nombre = st.text_input("Introduce tu nombre:")
edad = st.number_input("Introduce tu edad:", min_value=0, max_value=120)

if st.button("Mostrar saludo"):
    st.write("Hola", nombre, "tienes", edad, "años.")
