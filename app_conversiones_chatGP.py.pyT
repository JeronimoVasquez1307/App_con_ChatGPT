import streamlit as st

# Título y descripción de la app
st.title("App de Conversión de Medidas")
st.write("Esta app te permite realizar conversiones de medidas en diferentes categorías.")

# Selección de categoría
categoria = st.selectbox("Selecciona una categoría de medida:", [
    "Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad",
    "Área", "Energía", "Presión", "Tamaño de Datos"
])

# Conversiones disponibles por categoría
conversiones = {
    "Temperatura": [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ],
    "Longitud": [
        "Pies a metros",
        "Metros a pies",
        "Pulgadas a centímetros",
        "Centímetros a pulgadas"
    ],
    "Peso/Masa": [
        "Libras a kilogramos",
        "Kilogramos a libras",
        "Onzas a gramos",
        "Gramos a onzas"
    ],
    "Volumen": [
        "Galones a litros",
        "Litros a galones",
        "Pulgadas cúbicas a centímetros cúbicos",
        "Centímetros cúbicos a pulgadas cúbicas"
    ],
    "Tiempo": [
        "Horas a minutos",
        "Minutos a segundos",
        "Días a horas",
        "Semanas a días"
    ],
    "Velocidad": [
        "Millas por hora a kilómetros por hora",
        "Kilómetros por hora a metros por segundo",
        "Nudos a millas por hora",
        "Metros por segundo a pies por segundo"
    ],
    "Área": [
        "Metros cuadrados a pies cuadrados",
        "Pies cuadrados a metros cuadrados",
        "Kilómetros cuadrados a millas cuadradas",
        "Millas cuadradas a kilómetros cuadrados"
    ],
    "Energía": [
        "Julios a calorías",
        "Calorías a kilojulios",
        "Kilovatios-hora a megajulios",
        "Megajulios a kilovatios-hora"
    ],
    "Presión": [
        "Pascales a atmósferas",
        "Atmósferas a pascales",
        "Barras a libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a bares"
    ],
    "Tamaño de Datos": [
        "Megabytes a gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a megabytes",
        "Terabytes a petabytes"
    ]
}

# Mostrar las conversiones disponibles según la categoría seleccionada
if categoria in conversiones:
    st.subheader(f"Conversiones de {categoria}")
    tipo_conversion = st.selectbox("Selecciona un tipo de conversión:", conversiones[categoria])
    st.write(f"Has seleccionado la conversión: {tipo_conversion}")
else:
    st.write("Selecciona una categoría válida.")
