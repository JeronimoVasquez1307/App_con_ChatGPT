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

# Diccionario de fórmulas de conversión
formulas = {
    "Celsius a Fahrenheit": lambda celsius: celsius * 9/5 + 32,
    "Fahrenheit a Celsius": lambda fahrenheit: (fahrenheit - 32) * 5/9,
    "Celsius a Kelvin": lambda celsius: celsius + 273.15,
    "Kelvin a Celsius": lambda kelvin: kelvin - 273.15,
    "Pies a metros": lambda pies: pies * 0.3048,
    "Metros a pies": lambda metros: metros / 0.3048,
    "Pulgadas a centímetros": lambda pulgadas: pulgadas * 2.54,
    "Centímetros a pulgadas": lambda centimetros: centimetros / 2.54,
    "Libras a kilogramos": lambda libras: libras * 0.453592,
    "Kilogramos a libras": lambda kilogramos: kilogramos / 0.453592,
    "Onzas a gramos": lambda onzas: onzas * 28.3495,
    "Gramos a onzas": lambda gramos: gramos / 28.3495,
    "Galones a litros": lambda galones: galones * 3.78541,
    "Litros a galones": lambda litros: litros / 3.78541,
    "Pulgadas cúbicas a centímetros cúbicos": lambda pulgadas3: pulgadas3 * 16.3871,
    "Centímetros cúbicos a pulgadas cúbicas": lambda centimetros3: centimetros3 / 16.3871,
    "Horas a minutos": lambda horas: horas * 60,
    "Minutos a segundos": lambda minutos: minutos * 60,
    "Días a horas": lambda dias: dias * 24,
    "Semanas a días": lambda semanas: semanas * 7,
    "Millas por hora a kilómetros por hora": lambda mph: mph * 1.60934,
    "Kilómetros por hora a metros por segundo": lambda kph: kph * 0.277778,
    "Nudos a millas por hora": lambda nudos: nudos * 1.15078,
    "Metros por segundo a pies por segundo": lambda mps: mps * 3.28084,
    "Metros cuadrados a pies cuadrados": lambda metros2: metros2 * 10.7639,
    "Pies cuadrados a metros cuadrados": lambda pies2: pies2 / 10.7639,
    "Kilómetros cuadrados a millas cuadradas": lambda km2: km2 * 0.386102,
    "Millas cuadradas a kilómetros cuadrados": lambda mi2: mi2 / 0.386102,
    "Julios a calorías": lambda julios: julios / 4.184,
    "Calorías a kilojulios": lambda calorias: calorias * 0.004184,
    "Kilovatios-hora a megajulios": lambda kwh: kwh * 3.6,
    "Megajulios a kilovatios-hora": lambda mj: mj / 3.6,
    "Pascales a atmósferas": lambda pascales: pascales / 101325,
    "Atmósferas a pascales": lambda atm: atm * 101325,
    "Barras a libras por pulgada cuadrada": lambda barras: barras * 14.5038,
    "Libras por pulgada cuadrada a bares": lambda psi: psi / 14.5038,
    "Megabytes a gigabytes": lambda mb: mb / 1024,
    "Gigabytes a Terabytes": lambda gb: gb / 1024,
    "Kilobytes a megabytes": lambda kb: kb / 1024,
    "Terabytes a petabytes": lambda tb: tb / 1024,
}

# Mostrar las conversiones disponibles según la categoría seleccionada
if categoria in conversiones:
    st.subheader(f"Conversiones de {categoria}")
    tipo_conversion = st.selectbox("Selecciona un tipo de conversión:", conversiones[categoria])
    
    if tipo_conversion in formulas:
        valor_entrada = st.number_input(f"Ingrese el valor en {tipo_conversion.split(' a ')[0]}:")
        valor_convertido = formulas[tipo_conversion](valor_entrada)
        st.write(f"El valor convertido es: {valor_convertido:.2f} {tipo_conversion.split(' a ')[1]}")
    else:
        st.write("Seleccione una conversión válida.")
else:
    st.write("Selecciona una categoría válida.")

