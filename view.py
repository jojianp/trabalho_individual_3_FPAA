import networkx as nx
import matplotlib.pyplot as plt
import os
from main import find_hamiltonian_path

def draw_hamiltonian_path(graph, path):
    G = nx.Graph()
    n = len(graph)
    
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
            node_size=700, font_size=14)
    
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                              edge_color='darkorange', width=4)
    
    plt.title("Grafo com Caminho Hamiltoniano" if path else "Grafo", 
              fontsize=16, pad=20)
    plt.axis('off')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_dir, 'assets', 'figura.png')
    plt.savefig(assets_path, dpi=300, bbox_inches='tight')
    
    plt.show()

if __name__ == "__main__":
    graph = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],  
    [1, 0, 1, 0, 1, 0, 0, 0, 0],  
    [0, 1, 0, 0, 0, 1, 0, 0, 0],  
    [1, 0, 0, 0, 1, 0, 1, 0, 0],  
    [0, 1, 0, 1, 0, 1, 0, 1, 0],  
    [0, 0, 1, 0, 1, 0, 0, 0, 1],  
    [0, 0, 0, 1, 0, 0, 0, 1, 0],  
    [0, 0, 0, 0, 1, 0, 1, 0, 1],  
    [0, 0, 0, 0, 0, 1, 0, 1, 0]   
    ]
    
    path = find_hamiltonian_path(graph)
    draw_hamiltonian_path(graph, path)