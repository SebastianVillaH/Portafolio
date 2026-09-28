import streamlit as st
from PIL import Image

st.title("Portafolio de Sebastián Villa Hernández")

st.write("En esta pagina encontraras las aplicaciones desplegadas en streamlit, indicado por el titulo de la clase en la que se hizo")

proyectos = [
    ("Vectores y Matrices", "Vectores.jpg", "En la siguiente enlace encontraras la app de las frutas desplegada en streamlit", "https://clase2pa-frutas.streamlit.app/", "Frutas"),
    ("Preparación de datos", "Prep.png", "En la siguiente veremos una aplicación que recoge datos, los procesa y nos lo muestra", "https://clase5pa26agosto.streamlit.app/", "Preparación de datos"),
    ("Series de Tiempo.", "Tiempo.jpg", "En la siguiente veremos una aplicación que busca mostrarnos como usar una serie de tiempo usando ARIMA", "https://clase-8-pa-series-tiempo.streamlit.app/", "Series Tiempo"),
    ("De la regresión lineal a la logísitica.", "RDL.jpg", "En la siguiente enlace veremos una aplicación que busca predecir si en los siguientes dias llovera", "https://clase11pa.streamlit.app/", "Predictor Lluvia"),
    ("Calculo aplicado, gradiente.", "Gradiente.jpg", "En la siguiente enlace tendremos un descenso de gradiente interactivo", "https://clase3paminimo.streamlit.app/", "Gradiente interactivo"),
    ("Aplicación Preparación de datos", "AplicacionPrep.jpg", "En la siguiente enlace veremos una estacion de CORNARE de agua la cual nos mostrara datos sobre el nivel del agua", "https://clase6pa-redagua.streamlit.app/", "Estación"),
    ("Predicción y modelado de la calidad de aire.", "Aire.png", "En la siguiente enlace veremos una aplicacion que busca predecir la calidad del aire usando una estacion de CORNARE, subiendo un archivo con los datos", "https://clase-9-aire.streamlit.app/", "Predictor Aire"),
    ("Clasificación Knn", "KNN.jpg", "En la siguiente enlace veremos una aplicación que clasifica el suelo segun sus datos vecinos", "https://clase-13-tierra.streamlit.app/", "KNN Suelos"),
    ("Lógica, Big-O y Vectorización", "Bigo.png", "En la siguiente enlace veremos tenemos un detector de anomalias el cual usa Lógica y Big-O", "https://clase4pa.streamlit.app/", "Detector"),
    ("Regresión Lineal", "Regresion.jpg", "En la siguiente enlace veremos una aplicación que busca mostrarnos el uso de la Regresión Lineal", "https://clase7-pa.streamlit.app/", "Regresión Lineal"),
    ("Predicción de sensacion termica con IoT", "Termica.jpg", "En la siguiente enlace veremos una aplicación que busca predecir la sensación termica, conectandose a una base de datos externa", "https://clase10-pa.streamlit.app/", "Predictor Termico"),
]

COLUMNAS = 3

for i in range(0, len(proyectos), COLUMNAS):
    cols = st.columns(COLUMNAS, gap="large")
    for col, (titulo, img, desc, url, etiqueta) in zip(cols, proyectos[i:i + COLUMNAS]):
        with col:
            st.markdown(f"#### {titulo}")
            st.image(Image.open(img), use_container_width=True)
            st.write(desc)
            st.markdown(f"[{etiqueta}]({url})")
    st.divider()

