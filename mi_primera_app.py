
import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por “Jerónimo Vásquez González”.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Imprimir el mensaje de bienvenida
    mensaje = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje)
