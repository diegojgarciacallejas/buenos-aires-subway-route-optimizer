# Aplicación Subte Buenos Aires

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una **aplicación gráfica para el metro de Buenos Aires (subte)** que calcula el trayecto óptimo entre dos estaciones utilizando el algoritmo de búsqueda **A\***. 
El objetivo principal es proporcionar una herramienta interactiva y eficiente que permita a los usuarios planificar sus trayectos considerando diversos factores como distancias, transbordos, horarios y frecuencia de trenes.

La aplicación incluye:

- **Algoritmo A***: Optimizado para calcular rutas considerando múltiples variables.
- **Interfaz gráfica de usuario (GUI)**: Intuitiva y fácil de usar, creada con Tkinter.
- **Visualización de rutas**: Muestra claramente estaciones, transbordos y caminos elegidos.

## Características Principales

1. **Optimización de trayectos**:
   - Determina la ruta más eficiente entre dos estaciones.
   - Considera parámetros como horarios, frecuencias y distancias.

2. **Interfaz gráfica**:
   - Selección de estaciones de origen y destino mediante menús desplegables.
   - Visualización de la ruta en el mapa.
   - Resaltado dinámico de estaciones en el trayecto.

3. **Información adicional**:
   - Duración del viaje.
   - Hora de llegada estimada.
   - Cantidad de transbordos necesarios.
4. **Memoria**
   - Explicación del transcurso del proyecto y ademas descripcion de como realizar el ejecutable o de como realizar la ejecucion sin el ejecutable, incluyendo también un drive donde se puede encontrar el proyecto con el ejecutable.

## Las carpetas entregadas y utlizadas en el pryecto son las siguientes:

1. **Assets**:
   - Contiene imágenes y elementos usados para construir la interfaz gráfica.
   - También contiene el logo de nuestra aplicación llamada "subte".

2. **Data**:
   - Contiene el csv con las coordenadas de cada estación, que será utilizado en el algoritmo.
   - Contiene el main.
   - Contiene un diccionario utilizado para ubicar cada botón en su lugar en la interfaz gráfica.

3. **logic**:
   - Por un lado incluye la construcción del grafo con todas las estaciones, los horarios y las frecuencias.
   - Por otro lado incluye el código utilizado para implementar el algoritmo A*, con las funciones utilizadas para su uso.

4. **app**:
   - Código usado para crear la interfaz gráfica


## Requisitos

- Librerías utilizadas:
  - `NetworkX`
  - `Matplotlib`
  - `NumPy`
  - `Pandas`
  - `Tkinter`
  - `Datetime`
  - `Math`
  - `Typing`


