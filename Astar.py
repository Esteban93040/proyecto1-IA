import math

def distancebystart (latStart, lonStart, latDest,lonDest):
    r = 6371.0

    latStart = math.radians(latStart) 
    lonStart = math.radians(lonStart) 
    latDest = math.radians(latDest) 
    lonDest = math.radians(lonDest) 

    dlat= latDest-latStart
    dlon= lonDest-lonStart

    a=math.sin(dlat/2)**2 + math.cos(latStart)*math.cos(latDest)*math.sin(dlon/2)**2
    c= 2* math.asin(math.sqrt(a))

    distance= r*c

    return distance

# Grafo con ciudades
ciudades = {
    'Bogota': {'latitud': 4.7110, 'longitud': -74.0721},
    'Medellin': {'latitud': 6.2442, 'longitud': -75.5812},
    'Cali': {'latitud': 3.4516, 'longitud': -76.5320},
    'Barranquilla': {'latitud': 10.9685, 'longitud': -74.7813},
    'Cartagena': {'latitud': 10.3910, 'longitud': -75.4794},
    'Bucaramanga': {'latitud': 7.1193, 'longitud': -73.1227},
    'Pereira': {'latitud': 4.8143, 'longitud': -75.6946},
    'Santa Marta': {'latitud': 11.2408, 'longitud': -74.1990},
    'Ibague': {'latitud': 4.4389, 'longitud': -75.2322},
    'Manizales': {'latitud': 5.0703, 'longitud': -75.5138},
    'Pasto': {'latitud': 1.2136, 'longitud': -77.2811},
    'Villavicencio': {'latitud': 4.1420, 'longitud': -73.6266},
    'Neiva': {'latitud': 2.9273, 'longitud': -75.2819},
    'Armenia': {'latitud': 4.5339, 'longitud': -75.6811},
    'Cucuta': {'latitud': 7.8891, 'longitud': -72.4967},
    'Popayan': {'latitud': 2.4448, 'longitud': -76.6147},
    'Monteria': {'latitud': 8.7479, 'longitud': -75.8814},
    'Sincelejo': {'latitud': 9.3047, 'longitud': -75.3978},
    'Tunja': {'latitud': 5.5353, 'longitud': -73.3678},
    'Riohacha': {'latitud': 11.5444, 'longitud': -72.9072}
}

#grafo con rutas
grafo = {
    'Bogota': {"Ibague", "Villavicencio", "Tunja", "Bucaramanga"},
    
    "Ibague": {"Bogota", "Armenia", "Neiva"},
    
    "Armenia": {"Ibague", "Pereira", "Cali"},
    
    "Pereira": {"Armenia", "Manizales"},
    
    "Manizales": {"Pereira", "Medellin"},
    
    "Medellin": {"Manizales", "Monteria"},
    
    "Cali": {"Popayan", "Armenia"},
    
    "Popayan": {"Cali", "Pasto"},
    
    "Pasto": {"Popayan"},
    
    "Neiva": {"Ibague"},
    
    "Villavicencio": {"Bogota"},
    
    "Tunja": {"Bogota", "Bucaramanga"},
    
    "Bucaramanga": {"Bogota", "Cucuta", "Tunja"},
    
    "Cucuta": {"Bucaramanga"},
    
    "Barranquilla": {"Cartagena", "Santa Marta", "Sincelejo"},
    
    "Cartagena": {"Barranquilla", "Sincelejo", "Monteria"},
    
    "Santa Marta": {"Barranquilla", "Riohacha"},
    
    "Riohacha": {"Santa Marta"},
    
    "Sincelejo": {"Monteria", "Cartagena", "Barranquilla"},
    
    "Monteria": {"Sincelejo", "Cartagena", "Medellin"}
}

# Heurística h(n): distancia en línea desde un punto hasta el destino+
def crear_heuristica(ciudades_dict, ciudad_destino):
    """Calcula la distancia de cada ciudad al destino"""
    h = {}
    lat_dest = ciudades_dict[ciudad_destino]['latitud']
    lon_dest = ciudades_dict[ciudad_destino]['longitud']
    
    for ciudad, coords in ciudades_dict.items():
        h[ciudad] = distancebystart(
            coords['latitud'], 
            coords['longitud'], 
            lat_dest, 
            lon_dest
        )
    
    return h

def a_star(start, goal):
    open_set = {start}
    came_from = {}
    g = {city: float('inf') for city in graph}
    g[start] = 0
    f = {city: float('inf') for city in graph}
    f[start] = h[start]

    while open_set:
        # nodo con menor f
        current = min(open_set, key=lambda x: f[x])
        if current == goal:
            # reconstruir camino
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g[goal]

        open_set.remove(current)
        for neighbor, cost in graph[current].items():
            tentative_g = g[current] + cost
            if tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + h[neighbor]
                open_set.add(neighbor)

    return None, float('inf')

camino, costo = a_star("Arad", "Bucarest")
print("Camino:", camino)
print("Costo:", costo)

