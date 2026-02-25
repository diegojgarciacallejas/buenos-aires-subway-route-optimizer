import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import time

VELOCIDAD_MEDIA=400  #metros por minuto
df_coordenas = pd.read_csv(
    os.path.join(BASE_DIR, 'data', 'estaciones_buenos_aires_contildes.csv'),
    usecols=["Estacion", "Longitud", "Latitud", "Linea"],
    index_col=["Estacion"]
)

line_colors = {
     # Ponemos los colores de las líneas
    "A": "lightblue",    
    "B": "red",              
    "C": "darkblue",      
    "D": "green",         
    "E": "purple"         
}

Horarios_inicio_dict = {  # Horarios de inicio de las líneas
    "A": {"L-V": time(5, 30), "S": time(6, 0), "D": time(8, 0)},
    "B": {"L-V": time(5, 30), "S": time(6, 0), "D": time(8, 0)},
    "C": {"L-V": time(5, 30), "S": time(6, 0), "D": time(8, 0)},
    "D": {"L-V": time(5, 30), "S": time(6, 0), "D": time(8, 0)},
    "E": {"L-V": time(5, 30), "S": time(6, 0), "D": time(8, 0)},
}
Horarios_inicio_df=pd.DataFrame(Horarios_inicio_dict)
Frecuencias_dict={   # Frecuencias de las líneas
    "A": {"L-V": 3, "S": 7, "D": 8},
    "B": {"L-V": 3, "S": 7, "D":8.5},
    "C": {"L-V": 3, "S": 6, "D": 7.5},
    "D": {"L-V": 3, "S": 7, "D": 7},
    "E": {"L-V": 4.30, "S": 8.35, "D": 8.35},
}
Frecuencias_df=pd.DataFrame(Frecuencias_dict)


Horario_fin_dict = {# Horarios de cierre de las líneas
    "A": {"L-V": time(23, 30), "S": time(23, 30), "D": time(22, 32)},
    "B": {"L-V": time(23, 30), "S": time(23, 30), "D": time(22, 32)},
    "C": {"L-V": time(23, 30), "S": time(23, 30), "D": time(22, 32)},
    "D": {"L-V": time(23, 30), "S": time(23, 30), "D": time(22, 32)},
    "E": {"L-V": time(23, 30), "S": time(23, 30), "D": time(22, 32)}
}

Horarios_fin_df= pd.DataFrame(Horario_fin_dict)

def creacion_grafo()-> nx.Graph:
    G = nx.Graph()
    # Representacion de la linea A
    G.add_edge('Alberti', 'Pasco', color= line_colors['A'], weight=232/VELOCIDAD_MEDIA)
    G.add_edge('Pasco', 'Congreso',color= line_colors['A'],weight=528/VELOCIDAD_MEDIA)
    G.add_edge('Congreso', 'Sáenz Peña',color= line_colors['A'],weight=567/VELOCIDAD_MEDIA)
    G.add_edge('Sáenz Peña', 'Lima',color= line_colors['A'],weight=382/VELOCIDAD_MEDIA)
    G.add_edge('Lima', 'Piedras',color= line_colors['A'],weight=365/VELOCIDAD_MEDIA)
    G.add_edge('Piedras', 'Perú',color= line_colors['A'],weight=383/VELOCIDAD_MEDIA)
    G.add_edge('Perú', 'Plaza de Mayo',color= line_colors['A'],weight=313/VELOCIDAD_MEDIA)


    # Representacion de la linea B
    G.add_edge('Pasteur', 'Callao B', color= line_colors['B'],weight=647/VELOCIDAD_MEDIA)
    G.add_edge('Callao B', 'Uruguay', color= line_colors['B'],weight=508/VELOCIDAD_MEDIA)
    G.add_edge('Uruguay', 'Carlos Pellegrini', color= line_colors['B'],weight=504/VELOCIDAD_MEDIA)
    G.add_edge('Carlos Pellegrini', 'Florida', color= line_colors['B'],weight=646/VELOCIDAD_MEDIA)
    G.add_edge('Florida', 'Leandro N.Alem', color= line_colors['B'],weight=388/VELOCIDAD_MEDIA)


    # Representaacion de la linea C
    G.add_edge('Constitución', 'San Juan', color= line_colors['C'],weight=698/VELOCIDAD_MEDIA)
    G.add_edge('San Juan', 'Independencia C', color= line_colors['C'],weight=517/VELOCIDAD_MEDIA)
    G.add_edge('Independencia C', 'Moreno', color= line_colors['C'],weight=641/VELOCIDAD_MEDIA)
    G.add_edge('Moreno', 'Avenida de Mayo', color= line_colors['C'],weight=361/VELOCIDAD_MEDIA)
    G.add_edge('Avenida de Mayo', 'Diagonal Norte', color= line_colors['C'],weight=560/VELOCIDAD_MEDIA)
    G.add_edge('Diagonal Norte', 'Lavalle', color= line_colors['C'],weight=379/VELOCIDAD_MEDIA)
    G.add_edge('Lavalle', 'General San Martín', color= line_colors['C'],weight=791/VELOCIDAD_MEDIA)
    G.add_edge('General San Martín', 'Retiro', color= line_colors['C'],weight=761/VELOCIDAD_MEDIA)


    # Representacion de la linea D
    G.add_edge('Facultad de Medicina', 'Callao D',color= line_colors['D'],weight=400/VELOCIDAD_MEDIA)
    G.add_edge('Callao D', 'Tribunales',color= line_colors['D'],weight=924/VELOCIDAD_MEDIA)
    G.add_edge('Tribunales', '9 de Julio',color= line_colors['D'],weight=489/VELOCIDAD_MEDIA)
    G.add_edge('9 de Julio', 'Catedral',color= line_colors['D'],weight=621/VELOCIDAD_MEDIA)

    # Representacion de la linea E
    G.add_edge('Pichincha', 'Entre Ríos', color= line_colors['E'],weight=498/VELOCIDAD_MEDIA)
    G.add_edge('Entre Ríos', 'San José', color= line_colors['E'],weight=560/VELOCIDAD_MEDIA)
    G.add_edge('San José', 'Independencia E', color= line_colors['E'],weight=770/VELOCIDAD_MEDIA)
    G.add_edge('Independencia E', 'Belgrano', color= line_colors['E'],weight=690/VELOCIDAD_MEDIA)
    G.add_edge('Belgrano', 'Bolívar', color= line_colors['E'],weight=491/VELOCIDAD_MEDIA)

    # Representacion de los transbordos
    G.add_edge('Independencia C', 'Independencia E',weight=4)
    G.add_edge('Bolívar', 'Perú',weight=4)
    G.add_edge('Bolívar', 'Catedral',weight=4)
    G.add_edge('Perú', 'Catedral',weight=4)
    G.add_edge('Avenida de Mayo', 'Lima',weight=4)
    G.add_edge('Diagonal Norte', '9 de Julio',weight=4)
    G.add_edge('9 de Julio', 'Carlos Pellegrini',weight=4)

    return G

def dibujar_grafo(G:nx.Graph):
    np.random.seed(30)
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)  # Cambiar a un layout más intuitivo

    # Dibujar las aristas con los colores asignados
    edges = G.edges(data=True)

    # Extraer colores de cada arista utilizando el atributo 'color'
    colors = [edge[2]['color'] if 'color' in edge[2] else 'black' for edge in edges]  # Color o negro por defecto

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=8, font_weight="bold", edge_color=colors)
    plt.title("Grafo del Subte de Buenos Aires")
    plt.show()
