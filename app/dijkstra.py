from collections import defaultdict, deque
from .importar_excel import distance_list, route_name, vor_name_end, vor_name_ini

#clase Graph donde almacena la red de nodos, caminos y distancias

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):              #funcion que añade nodo
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):       #funcion que añade camino
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance



# algoritmo para encontrar camino mas corto

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

#devuelve una lista con los puntos vor visitados y el aeropuerto de salida y destino

def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    route = list(full_path)

    return route

#igual que shortest_path pero devuelve la distancia recorrida

def dist_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    distance = visited[destination]
 
    return distance


if __name__ == '__main__':
    graph = Graph()

    i = 0

    for node in vor_name_ini:           #generamos los nodos (vor)
        
        graph.add_node(vor_name_ini[i])
        i += 1
    
    i = 0
    for edge in route_name:             #generamos los caminos que existen entre nodos (no se puede ir de cualquier nodo a cualquier nodo)
        
        graph.add_edge(vor_name_ini[i], vor_name_end[i], distance_list[i])
        i += 1
