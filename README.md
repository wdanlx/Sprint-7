# Sprint-7
proyecto de sprint 7


Esta es una aplicación web interactiva desarrollada en Python utilizando **Streamlit**, **Pandas** y **Plotly**. La aplicación permite explorar y analizar un conjunto de datos de anuncios de venta de coches en Estados Unidos de manera rápida y visual.

## Funcionalidades principales

- **Visualización interactiva de datos:** Permite analizar la distribución de las características del conjunto de datos mediante gráficos dinámicos de Plotly.
- **Histograma del kilometraje:** Mediante una casilla de verificación, el usuario puede generar un histograma para observar la distribución de millas recorridas (`odometer`) por los vehículos.
- **Gráfico de dispersión:** Ofrece un diagrama de dispersión para analizar la relación entre el kilometraje y el precio de venta (`price vs. odometer`).
- **Interfaz dinámica:** Diseñada con casillas de verificación (*checkboxes*) que permiten activar o desactivar las visualizaciones de forma persistente y simultánea.

## Estructura del Proyecto

```text
├── notebooks/
│   └── EDA.ipynb          # Notebook de Jupyter para el Análisis Exploratorio de Datos
├── vehicles_env/          # Entorno virtual de Python
├── .gitignore             # Archivo para ignorar archivos no deseados (ej. entorno virtual)
├── app.py                 # Código principal de la aplicación Streamlit
├── vehicles_us.csv        # Conjunto de datos de vehículos
└── README.md              # Descripción y documentación del proyecto
