# Grafo con costos reales (distancias)
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

# Heurística h(n): distancia en línea recta a Bucarest
h = {
    'Arad': 366, 'Bucarest': 0, 'Craiova': 160, 'Dobreta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80,
    'Vaslui': 199, 'Zerind': 374
}

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