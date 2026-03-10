# Buenos Aires Subway Route Optimizer 🚇

## Overview

This project is a graphical application for the Buenos Aires subway system (Subte) that calculates the optimal route between two selected stations using the **A* (A-star) search algorithm**.

The application models a subset of the subway network as a graph where stations are nodes and connections are edges. The algorithm computes the most efficient path between two stations considering factors such as travel distance, transfers, schedules, and train frequency.

The project demonstrates the practical implementation of heuristic search algorithms applied to real-world transportation networks.


---

## Features

### Route Optimization
- Computes the most efficient path between two stations.
- Considers travel distance, schedules, train frequency, and transfers.

### Graphical User Interface
- Built using **Tkinter**.
- Allows users to select origin and destination stations.
- Displays the calculated route visually.
- Highlights the stations included in the selected path.

### Travel Information
- Estimated travel duration
- Estimated arrival time
- Number of transfers required

---

## Project Structure
```text
buenos-aires-subway-route-optimizer
│
├── src/
│ ├── app.py # Main application entry point
│ │
│ ├── data/ # Subway data and interface helpers
│ │ ├── estaciones_buenos_aires_contildes.csv
│ │ ├── elementos_apoyo_interfaz.py
│ │ └── init.py
│ │
│ ├── logic/ # Graph construction and A* algorithm
│ │ ├── codigo_aestrella.py
│ │ ├── grafo.py
│ │ └── init.py
│
├── assets/ # Images and graphical resources
│ ├── icons/
│ │ └── logo_subte.ico
│ │
│ └── images/
│ ├── fondo.jpg
│ ├── logo_subte.png
│ ├── train_no_background.png
│ └── interfaz.png

│
├── docs/
│ └── Memoria.pdf # Project report
│
├── README.md
├── requirements.txt
└── LICENSE
```
---

## Technologies Used

- Python
- NetworkX
- Pandas
- NumPy
- Matplotlib
- Tkinter
- Datetime

  
---


# Project
Graphical application that computes optimal routes between selected Buenos Aires subway stations using the A* search algorithm. The system models a subset of the network as a weighted graph and considers distance, transfers, schedules, and train frequency for efficient path planning.

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt

```
## Running the Application

From the root of the repository run:

```bash
python src/app.py
```

## Example Usage

1. Select the origin station.
2. Select the destination station.
3. Choose the desired departure time.
4. The application computes the optimal route using the A* algorithm.
5. The interface displays the optimal route, travel time, and number of transfers.

## Screenshots

Main application interface:

![Application Interface](assets/images/interfaz.png)
--- 
## Authors

- Diego J. García Callejas
- Pablo de Tarso Pedraz García
- Manuel Arce Losada
- Pedro Álvaro Martínez Gutiérrez
- Mario Martín Muñoz
- Héctor Fernández Cano 
