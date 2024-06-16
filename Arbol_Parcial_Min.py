import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph, start):
    
    mst = []  # Lista para almacenar las aristas del MST
    visited = set()  # Conjunto para rastrear los nodos visitados
    edges = []  # Cola de prioridad para seleccionar la arista de menor peso
    heapq.heappush(edges, (0, start, start))  # Iniciar con el nodo inicial
    total_cost = 0  # Costo total del MST

    print(f"Estado inicial:")
    print(f"Visitados: {visited}")
    print(f"Cola de prioridad: {edges}")
    print("-" * 50)

    while edges:
        cost, frm, to = heapq.heappop(edges)  # Obtener la arista de menor peso
        if to in visited:
            continue  # Si el nodo ya fue visitado, saltar a la siguiente iteración

        visited.add(to)  # Marcar el nodo como visitado
        if frm != to:
            mst.append((frm, to, cost))  # Agregar la arista al MST
            total_cost += cost  # Actualizar el costo total

        # Explorar las aristas adyacentes del nodo actual
        for neighbor, weight in graph[to].items():
            if neighbor not in visited:
                heapq.heappush(edges, (weight, to, neighbor))

        # Imprimir el estado actual
        print(f"Visitando nodo: {to}")
        print(f"Visitados: {visited}")
        print(f"Cola de prioridad: {edges}")
        print("-" * 50)

    return mst, total_cost

def draw_graph(graph, ax, positions, mst_edges=None):
    """
    Función para dibujar el grafo usando NetworkX y Matplotlib.

    Parámetros:
    - graph: Un diccionario que representa el grafo.
    - ax: El eje de Matplotlib donde se dibujará el grafo.
    - positions: Un diccionario que contiene las posiciones de los nodos.
    - mst_edges: Lista de aristas que forman el MST (opcional).
    """
    G = nx.Graph()  # Crear un grafo vacío
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)  # Agregar las aristas al grafo

    nx.draw(G, positions, with_labels=True, node_color='lightblue', node_size=700, font_size=10, ax=ax)  # Dibujar nodos y aristas
    labels = nx.get_edge_attributes(G, 'weight')  # Obtener etiquetas de las aristas
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels, ax=ax)  # Dibujar etiquetas de las aristas

    if mst_edges:
        mst_edges_list = [(frm, to) for frm, to, weight in mst_edges]
        nx.draw_networkx_edges(G, positions, edgelist=mst_edges_list, edge_color='blue', width=2, ax=ax)  # Resaltar las aristas del MST

# Definir el grafo como un diccionario
graph = {
    'A': {'B': 8, 'G': 9, 'H': 10, 'I': 6, 'J': 12, 'K': 3},
    'B': {'A': 8, 'C': 10, 'E': 2, 'K': 7},
    'C': {'B': 10, 'D': 9, 'K': 5},
    'D': {'C': 9, 'E': 13, 'F': 12},
    'E': {'B': 2, 'D': 13, 'F': 10},
    'F': {'D': 12, 'E': 10, 'G': 8},
    'G': {'A': 9, 'E': 6, 'F': 8, 'H': 7},
    'H': {'A': 10, 'G': 7, 'I': 3},
    'I': {'A': 6, 'H': 3, 'J': 10},
    'J': {'A': 12, 'I': 10, 'K': 8},
    'K': {'A': 3, 'B': 7, 'C': 5, 'J': 8}
}

# Definir las posiciones de los nodos en un plano 2D
positions = {
    'A': (-1, 2),
    'B': (0, 0),
    'C': (-5, 0),
    'D': (-5, -3),
    'E': (0.5, -1),
    'F': (2, -3),
    'G': (4, 1),
    'H': (3.5, 3.5),
    'I': (1.5, 5),
    'J': (-5.5, 5),
    'K': (-3, 1.5)
}

# Ejecutar el algoritmo de Prim
mst, total_cost = prim(graph, 'A')
print("Árbol de Expansión Mínimo:", mst)
print("Costo Total:", total_cost)

# Crear la figura y los ejes para los gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Dibujar el grafo original
draw_graph(graph, ax1, positions)
ax1.set_title("Grafo Original")

# Dibujar el Árbol de Expansión Mínimo
draw_graph(graph, ax2, positions, mst_edges=mst)
ax2.set_title("Árbol de Expansión Mínimo con Algoritmo de Prim")

# Mostrar los gráficos
plt.show()
