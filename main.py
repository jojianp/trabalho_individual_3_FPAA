def find_hamiltonian_path(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0
    
    if not backtrack(graph, path, 1):
        return []
    
    return path

def backtrack(graph, path, pos):
    if pos == len(graph):
        return True
    
    for v in range(len(graph)):
        if is_valid(v, graph, path, pos):
            path[pos] = v
            if backtrack(graph, path, pos + 1):
                return True
            path[pos] = -1
    
    return False

def is_valid(v, graph, path, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def main():
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
    
    print("Matriz de adjacência:")
    for row in graph:
        print(row)
    
    path = find_hamiltonian_path(graph)
    
    if path:
        print("Caminho Hamiltoniano encontrado:")
        print(" -> ".join(map(str, path)))
    else:
        print("Não existe Caminho Hamiltoniano")

if __name__ == "__main__":
    main()