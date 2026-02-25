from logic.grafo import *
import networkx as nx
from typing import List
import math
from datetime import time, timedelta,date, datetime

DIAS_SEMANA = ['L-V', 'L-V', 'L-V', 'L-V', 'L-V', 'S', 'D'] # Ponemos los días de la semana para usarlos en una funcion 
G=creacion_grafo()  # Creamos el grafo

def calcular_heuristica_entredos ( current:str,target:str)->float:
    RADIO_TIERA=6378100  # Necesitamos el radio de la Tierra para calcular la heurística
    if current == target: # Si el inicio es igual al destino la heurística será 0
        return 0
    # Calculamos los datos para aplicar la fórmula
    longitud_current:float=math.radians(df_coordenas.loc[current]["Longitud"])
    longitud_target:float=math.radians(df_coordenas.loc[target]["Longitud"])
    latitud_current:float=math.radians(df_coordenas.loc[current]["Latitud"])
    latitud_target:float=math.radians(df_coordenas.loc[target]["Latitud"])
    dif_lon:float=longitud_target - longitud_current
    dif_lat:float=latitud_target - latitud_current
    interior:float= math.sqrt(math.sin(dif_lat/2)**2+ math.cos(latitud_current)*math.cos(latitud_target)*math.sin(dif_lon/2)**2)
    #Calculamos la distancia
    distancia:float= 2*RADIO_TIERA*math.asin(interior)
    # Devolvemos la heurística expresadda en minutos 
    return distancia//VELOCIDAD_MEDIA

#Funcion que devuelve el dia de la ficha elegidad
def calcular_fecha(fecha:date)->str:
        #Devuelve dia accediendo al indice que devuelve weekday en la lista DIAS_SEMANA
        nombre_dia:str = DIAS_SEMANA[fecha.weekday()]
        return nombre_dia

#Funcion que devuelve el tiempo que esperamos en la estacion indicada 
def tiempo_espera_en_estacion(hora_llegada:time, nombre_estacion:str,fecha:str)->int:
    linea_metro:str=df_coordenas.loc[nombre_estacion,"Linea"]
    frecuencia:float =Frecuencias_df.loc[fecha,linea_metro]  
    horario_inicio:time=Horarios_inicio_df.loc[fecha,linea_metro]
    horario_fin:time=Horarios_fin_df.loc[fecha,linea_metro]
    # Verificamos si la línea está operativa
    if not (horario_inicio <= hora_llegada <= horario_fin):
        return None  # Tren fuera de servicio
    # Calvualmos la hora a la que llegamos y la hora de inicio del servicio en minutos 
    minutos_llegada:int = hora_llegada.hour * 60 + hora_llegada.minute
    minutos_inicio:int = horario_inicio.hour * 60 + horario_inicio.minute
    # Calculamos los minutos que llevamos desde que se inicio el servicio
    minutos_desde_inicio:int = minutos_llegada - minutos_inicio
    # Dividimos por la frecueencia de ese dia y ese dato se lo restamos a la frecuencia para saber cuanto tenemos que esperar
    tiempo_espera:int = (frecuencia - (minutos_desde_inicio % frecuencia)) % frecuencia
    #Devuelve el tiempo de espera 
    return tiempo_espera

def calcular_camino(inicio:str, fin:str  )->List[str]: # Aplicamos el algoritmo A*
    camino:List[str]= nx.astar_path(G,inicio, fin, heuristic=calcular_heuristica_entredos, weight="weight")
    return camino  

#Funcion que calcula la hora de llegada dada la hora de inicio y el tiempo del trayecto
def hora_llegada(hora:time,tiempo:int)->datetime:
    hora_actual:datetime = datetime.combine(datetime.today(), hora) 
    hora_delta:datetime = hora_actual + timedelta(minutes=tiempo)
    return hora_delta.time()


def numero_transbordos(camino: list) -> List[tuple]: # Devolvemos lista de tuplas de transborodos
    #Creamos la lista vacia 
    num_transbordos=[]
    ultima_columna = df_coordenas.iloc[:, -1]  # Última columna del DataFrame
    
    for i in range(len(camino) - 1):  # Recorrer hasta el penúltimo elemento
        if ultima_columna[camino[i]] != ultima_columna[camino[i + 1]]:
            num_transbordos.append((camino[i],camino[i+1]))

    return num_transbordos

#Funcion que devuelve el tiempo que tarda el trayecto teniendo en cuenta las frecuencias de todas las lineas
#Recibe la hora de llegada, el dia y el camino a recorrer
def calcular_tiempo_camino(Hora:time,fecha:str,camino:List[str])->int:
    #Calculas el tiempo que hay que esperar en la estacion 
    tiempo_espera_inicio:int=tiempo_espera_en_estacion(Hora,camino[0],fecha)
    #Si el tiempo de espera es None significa que estamos fuera del horario establecido 
    if tiempo_espera_inicio is None:
        return None
    #Actualizamos la hora y sumamos el tiempo que va pasando
    tiempo_actual:datetime = datetime.combine(datetime.today(), Hora) + timedelta(minutes=int(tiempo_espera_inicio))
    tiempo_total:int = tiempo_espera_inicio
    #Hacemos la  misma accion durante todo el camino
    for i in range(1,len(camino)):
        nodo_A:str=camino[i-1]
        nodo_B:str=camino[i]
        arista =G.get_edge_data(nodo_A,nodo_B)
        tiempo_segmento=arista.get('weight')
        tiempo_total += tiempo_segmento

        tiempo_actual += timedelta(minutes=int(tiempo_segmento))
        if i < len(camino) - 1:  # No es el último nodo
            nodo_siguiente:str = camino[i + 1]
            color_actual:str = G[nodo_A][nodo_B].get('color', None)
            color_siguiente:str = G[nodo_B][nodo_siguiente].get('color', None)
            
            if color_actual != color_siguiente:  # Si cambia la línea, hay un transbordo
                # Calculos tiempo de espera para el siguiente tren de la nueva linea de metro
                tiempo_espera_transbordo = tiempo_espera_en_estacion(tiempo_actual.time(), nodo_B, fecha)
                if tiempo_espera_transbordo is None:
                    return None     #Si el tiempo de espera es None significa que estamos fuera del horario establecido 

                tiempo_total += tiempo_espera_transbordo
                tiempo_actual += timedelta(minutes=int(tiempo_espera_transbordo))
        
    #Agisnamos todo a una variable final 
    tiempo_final = (tiempo_total) 
    return tiempo_final + (len(camino)-2)*0.5