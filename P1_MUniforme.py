"""
RECORRIDO EN METODO UNIFORME
INTEGRANTES:
CALDERON GUEVARA CESAR YAIR
GARCIA ZUÑIGA LUIS JUSTO
MACEDA PATRICIO FERNANDO
El metodo uniforme (uniform cost search) elige el camino
que tiene el menor costo en ruta
"""

import collections
import math

# Clase que servirá para mapear las ciudades
class MapaCiudades:
    def __init__(self):
        self.ciudad = set()
        self.caminos = collections.defaultdict(list)
        self.costo = {}
    # Metodo para agregar ciudades
    def agregar_ciudad(self, ciudad):
        self.ciudad.add(ciudad)
    # Metodo para agregar conexiones entre ciudades
    def agregar_camino(self, ciudad_origen, ciudad_destino, costo):
        if ciudad_origen == ciudad_destino:
            print("AVISO: La ciudad origen y ciudad destino son iguales.")
            print("No se agregó el camino.")
        self.caminos[ciudad_origen].append(ciudad_destino)      # Se agrega un camino
        self.costo[(ciudad_origen, ciudad_destino)] = costo     # Se agrega el costo del camino

# Comienza la ejecucion del codigo
Romania = MapaCiudades()        # Creando mapa de Romania
# Agregando CIUDADES
Romania.agregar_ciudad("Arad")
Romania.agregar_ciudad("Bucharest")
Romania.agregar_ciudad("Craiova")
Romania.agregar_ciudad("Dobreta")
Romania.agregar_ciudad("Eforie")
Romania.agregar_ciudad("Fagaras")
Romania.agregar_ciudad("Giurgiu")
Romania.agregar_ciudad("Hirsova")
Romania.agregar_ciudad("Iasi")
Romania.agregar_ciudad("Lugoj")
Romania.agregar_ciudad("Mehadia")
Romania.agregar_ciudad("Neamt")
Romania.agregar_ciudad("Oradea")
Romania.agregar_ciudad("Pitesti")
Romania.agregar_ciudad("Rimnicu Vilcea")
Romania.agregar_ciudad("Sibiu")
Romania.agregar_ciudad("Timisoara")
Romania.agregar_ciudad("Urziceni")
Romania.agregar_ciudad("Vaslui")
Romania.agregar_ciudad("Zerind")

# Agregando caminos entre ciudades (Se registra de ida y vuelta)
Romania.agregar_camino("Oradea","Sibiu",151)
Romania.agregar_camino("Sibiu","Oradea",151)

Romania.agregar_camino("Oradea","Zerind",71)
Romania.agregar_camino("Zerind","Oradea",71)

Romania.agregar_camino("Zerind","Arad",75)
Romania.agregar_camino("Arad","Zerind",75)

Romania.agregar_camino("Arad","Sibiu",140)
Romania.agregar_camino("Sibiu","Arad",140)


Romania.agregar_camino("Arad","Timisoara",118)
Romania.agregar_camino("Timisoara","Arad",118)

Romania.agregar_camino("Timisoara","Lugoj",111)
Romania.agregar_camino("Lugoj","Timisoara",111)

Romania.agregar_camino("Lugoj","Mehadia",70)
Romania.agregar_camino("Mehadia","Lugoj",70)

Romania.agregar_camino("Mehadia","Dobreta",75)
Romania.agregar_camino("Dobreta","Mehadia",75)

Romania.agregar_camino("Dobreta","Craiova",120)
Romania.agregar_camino("Craiova","Dobreta",120)

Romania.agregar_camino("Sibiu","Fagaras",99)
Romania.agregar_camino("Fagaras","Sibiu",99)

Romania.agregar_camino("Sibiu","Rimnicu Vilcea",80)
Romania.agregar_camino("Rimnicu Vilcea","Sibiu",80)

Romania.agregar_camino("Fagaras","Bucharest",211)
Romania.agregar_camino("Buchaerst","Fagaras",211)

Romania.agregar_camino("Rimnicu Vilcea","Pitesti",97)
Romania.agregar_camino("Pitesti","Rimnicu Vilcea",97)

Romania.agregar_camino("Rimnicu Vilcea","Craiova",146)
Romania.agregar_camino("Craiova","Rminicu Vilcea",146)

Romania.agregar_camino("Craiova","Pitesti",138)
Romania.agregar_camino("Pitesti","Craiova",138)


Romania.agregar_camino("Bucharest","Giurgiu",90)
Romania.agregar_camino("Giurgiu","Bucharest",90)

Romania.agregar_camino("Bucharest","Urziceni",85)
Romania.agregar_camino("Urziceni","Bucharest",85)

Romania.agregar_camino("Urziceni","Hirsova",98)
Romania.agregar_camino("Hirsova","Urziceni",98)

Romania.agregar_camino("Hirsova","Eforie",86)
Romania.agregar_camino("Eforie","Hirsova",86)

Romania.agregar_camino("Urziceni","Vaslui",152)
Romania.agregar_camino("Vaslui","Urziceni",152)

Romania.agregar_camino("Vaslui","Iasi",92)
Romania.agregar_camino("Iasi","Vaslui",92)

Romania.agregar_camino("Iasi","Neamt",87)
Romania.agregar_camino("Neamt","Iasi",87)

# Funcion para resolver un recorrido dado un mapa
def recorre_mapa(mapa,ciudad_inicio,ciudad_final):
    if ciudad_inicio not in mapa.ciudad: # Comprobamos si existe ciudad_inicio
        print("ERROR: '{}' no se encuentra en el mapa!".format(ciudad_inicio))
        return
    elif ciudad_final not in mapa.ciudad:  # Comprobamos si existe ciudad_final
        print("ERROR: '{}' no se encuentra en el mapa!".format(ciudad_final))
        return
    elif ciudad_inicio == ciudad_final: # Si las ciudades son iguales
        print("AVISO: La ciudad de inicio y ciudad destino son iguales!")
        return

"""
    # Comenzando la iteracion del algoritmo
    ciudades_recorridas = []
    costo_total = 0
    #while ciudad_inicio != ciudad_final: # Mientras no hayamos llegado a ciudad_final
    #    ciudades_recorridas.append(ciudad_inicio)
    #    costo_total += costo_total
    #    ciudad_inicio,costo_total = metodo_uniforme(mapa,ciudad_inicio) # Regresamos la nueva ciudad y su costo
    metodo_uniforme(mapa,ciudad_inicio)   
    
def metodo_uniforme(mapa,ciudad_actual):
    # dos dicc
    ciudades_visitadas = set()
    frontera = dict.fromkeys(list(mapa.ciudad), math.inf) #Ciudades con valor inf
    explorado = dict.fromkeys(list(mapa.ciudad), None) # Ciudades con valor none
    #delta[ciudad_actual] = 0 # Para la ciudad donde nos encontremos
    while ciudades_visitadas != mapa.ciudad:

    #return (ciudad_actual,costo)



#recorre_mapa(Romania,"Eforie","Urziceni")
#print(Romania.caminos)

#Playground
#delta = dict.fromkeys(list(Romania.ciudad), math.inf)
#print("DELTA\n",delta)
#previo = dict.fromkeys(list(Romania.ciudad), None)
#print("PREVIO\n",previo)
#print(Romania.ciudad)
#delta["Zerind"] = 0
#print(delta)
"""
