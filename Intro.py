import streamlit as st
from PIL import Image
st.title("Portafolio de Sebastián Villa Hernández")

st.write(f"En esta pagina encontraras las aplicaciones desplegadas en streamlit, indicado por el titulo de la clase en la que se hizo")
col1, col2, col3, col4 = st.columns(4)

with col1:
 
 st.subheader("Vectores y Matrices")
 image = Image.open('Vectores.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace encontraras la app de las frutas desplegada en streamlit") 
 url = "https://clase2pa-frutas.streamlit.app/"
 st.write(f" [Frutas]({url})")

 st.subheader("Calculo aplicado, gradiente.")
 image = Image.open('Gradiente.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace tendremos un descenso de gradiente interactivo") 
 url = "https://clase3paminimo.streamlit.app/"
 st.write(f" [Gradiente interactivo]({url})")

 st.subheader("Lógica, Big-O y Vectorización")
 image = Image.open('Bigo.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos tenemos un detector de anomalias el cual usa Lógica y Big-O") 
 url = "https://clase4pa.streamlit.app/"
 st.write(f" [Detector]({url})")

with col2: 
 st.subheader("Preparación de datos")
 image = Image.open('Prep.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que recoge datos, los procesa y nos lo muestra") 
 url = "https://clase5pa26agosto.streamlit.app/"
 st.write(f" [Preparación de datos]({url})")

 st.subheader("Aplicación Preparación de datos")
 image = Image.open('AplicacionPrep.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos una estacion de CORNARE de agua la cual nos mostrara datos sobre el nivel del agua") 
 url = "https://clase6pa-redagua.streamlit.app/"
 st.write(f" [Estación]({url})")

 st.subheader("Regresión Lineal")
 image = Image.open('Regresion.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicación que busca mostrarnos el uso de la Regresión Lineal") 
 url = "https://clase7-pa.streamlit.app/"
 st.write(f" [Regresión Lineal]({url})")


with col3: 
 st.subheader("Series de Tiempo.")
 image = Image.open('Tiempo.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que busca mostrarnos como usar una serie de tiempo usando ARIMA") 
 url = "https://clase-8-pa-series-tiempo.streamlit.app/"
 st.write(f" [Series Tiempo]({url})")

 st.subheader("Predicción y modelado de la calidad de aire.")
 image = Image.open('Aire.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicacion que busca predecir la calidad del aire usando una estacion de CORNARE, subiendo un archivo con los datos") 
 url = "https://clase-9-aire.streamlit.app/"
 st.write(f" [Predictor Aire]({url})")
 
 st.subheader("Predicción de sensacion termica con IoT")
 image = Image.open('Termica.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicación que busca predecir la sensación termica, conectandose a una base de datos externa") 
 url = "https://clase10-pa.streamlit.app/"
 st.write(f" [Predictor Termico]({url})")

with col4:
 st.subheader("De la regresión lineal a la logísitica.")
 image = Image.open('RDL.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicación que busca predecir si en los siguientes dias llovera") 
 url = "https://clase11pa.streamlit.app/"
 st.write(f" [Predictor Lluvia]({url})")

 st.subheader("Clasificación Knn")
 image = Image.open('KNN.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicación que clasifica el suelo segun sus datos vecinos") 
 url = "https://clase-13-tierra.streamlit.app/"
 st.write(f" [KNN Suelos]({url})")

