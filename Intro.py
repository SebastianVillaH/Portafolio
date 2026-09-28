import streamlit as st
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def cargar_imagen(nombre):
    ruta = BASE_DIR / nombre
    if not ruta.exists():
        archivos = {f.name.lower(): f for f in BASE_DIR.iterdir() if f.is_file()}
        ruta = archivos.get(nombre.lower(), ruta)
    return Image.open(ruta)

def tarjeta(titulo, imagen, ancho, descripcion, url, etiqueta):
    st.subheader(titulo)
    st.image(cargar_imagen(imagen), width=ancho)
    st.write(descripcion)
    st.write(f"[{etiqueta}]({url})")

st.title("Portafolio de Sebastián Villa Hernández")

st.write("En esta pagina encontraras las aplicaciones desplegadas en streamlit, indicado por el titulo de la clase en la que se hizo")
col1, col2, col3, col4 = st.columns(4)

with col1:
    tarjeta("Vectores y Matrices", "Vectores.jpg", 190,
            "En la siguiente enlace encontraras la app de las frutas desplegada en streamlit",
            "https://clase2pa-frutas.streamlit.app/", "Frutas")
    tarjeta("Calculo aplicado, gradiente.", "Gradiente.jpg", 200,
            "En la siguiente enlace tendremos un descenso de gradiente interactivo",
            "https://clase3paminimo.streamlit.app/", "Gradiente interactivo")
    tarjeta("Lógica, Big-O y Vectorización", "Big-o.jpg", 200,
            "En la siguiente enlace veremos tenemos un detector de anomalias el cual usa Lógica y Big-O",
            "https://clase4pa.streamlit.app/", "Detector")

with col2:
    tarjeta("Preparación de datos", "Prep.jpg", 200,
            "En la siguiente veremos una aplicación que recoge datos, los procesa y nos lo muestra",
            "https://clase5pa26agosto.streamlit.app/", "Preparación de datos")
    tarjeta("Aplicación Preparación de datos", "AplicacionPrep.jpg", 190,
            "En la siguiente enlace veremos una estacion de CORNARE de agua la cual nos mostrara datos sobre el nivel del agua",
            "https://clase6pa-redagua.streamlit.app/", "Estación")
    tarjeta("Regresión Lineal", "Regresion.jpg", 200,
            "En la siguiente enlace veremos una aplicación que busca mostrarnos el uso de la Regresión Lineal",
            "https://clase7-pa.streamlit.app/", "Regresión Lineal")

with col3:
    tarjeta("Series de Tiempo.", "Tiempo.jpg", 190,
            "En la siguiente veremos una aplicación que busca mostrarnos como usar una serie de tiempo usando ARIMA",
            "https://clase-8-pa-series-tiempo.streamlit.app/", "Series Tiempo")
    tarjeta("Predicción y modelado de la calidad de aire.", "Aire.jpg", 200,
            "En la siguiente enlace veremos una aplicacion que busca predecir la calidad del aire usando una estacion de CORNARE, subiendo un archivo con los datos",
            "https://clase-9-aire.streamlit.app/", "Predictor Aire")
    tarjeta("Predicción de sensacion termica con IoT", "Termica.jpg", 200,
            "En la siguiente enlace veremos una aplicación que busca predecir la sensación termica, conectandose a una base de datos externa",
            "https://clase10-pa.streamlit.app/", "Predictor Termico")

with col4:
    tarjeta("De la regresión lineal a la logísitica.", "RDL.jpg", 200,
            "En la siguiente enlace veremos una aplicación que busca predecir si en los siguientes dias llovera",
            "https://clase11pa.streamlit.app/", "Predictor Lluvia")
    tarjeta("Clasificación Knn", "KNN.jpg", 200,
            "En la siguiente enlace veremos una aplicación que clasifica el suelo segun sus datos vecinos",
            "https://clase-13-tierra.streamlit.app/", "KNN Suelos")
