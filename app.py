"""

#Codigo basico 1

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Título principal de la aplicación
st.header('Cuadro de mandos de vehículos')

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón para el histograma
build_histogram = st.button('Construir histograma')

if build_histogram:  # al hacer clic en el botón
    # Escribir un mensaje en la aplicación
    st.write(
        'Creando un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma con Plotly
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del kilometraje")

    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)


#codigo mejorado 1

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de venta de coches')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Añadir un título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)


#codigo con los dos botones


import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de venta de coches')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# --- BOTÓN 1: HISTOGRAMA ---
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico
    st.plotly_chart(fig_hist, use_container_width=True)


# --- BOTÓN 2: GRÁFICO DE DISPERSIÓN ---
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para precio vs. kilometraje')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])
    fig_scatter.update_layout(
        title_text='Precio vs. Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )

    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
"""


import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de venta de coches')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# --- CASILLA DE VERIFICACIÓN 1: HISTOGRAMA ---
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla está marcada
    # Escribir un mensaje en la aplicación
    st.write('Construir un histograma para la columna odómetro')

    # Crear un histograma utilizando plotly.graph_objects
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico
    st.plotly_chart(fig_hist, use_container_width=True)


# --- CASILLA DE VERIFICACIÓN 2: GRÁFICO DE DISPERSIÓN ---
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si la casilla está marcada
    # Escribir un mensaje en la aplicación
    st.write('Construir un gráfico de dispersión para precio vs. kilometraje')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])
    fig_scatter.update_layout(
        title_text='Precio vs. Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )

    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
