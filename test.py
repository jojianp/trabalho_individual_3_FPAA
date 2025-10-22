import unittest
from main import find_hamiltonian_path

class TestHamiltonianPath(unittest.TestCase):

    def test_grafo_5_vertices_com_caminho(self):
        """Testa um grafo de 5 vértices que possui caminho hamiltoniano"""
        graph = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(len(path), 5)
        self.assertEqual(len(set(path)), 5)

    def test_grafo_sem_caminho_hamiltoniano(self):
        """Testa um grafo que não possui caminho hamiltoniano (desconexo)"""
        graph = [
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],  
            [0, 0, 0, 1, 1],  
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(path, [])

    def test_grafo_9_vertices_projeto(self):
        """Testa o grafo principal de 9 vértices do projeto"""
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
        self.assertEqual(len(path), 9)
        self.assertEqual(len(set(path)), 9)

    def test_grafo_3_vertices_completo(self):
        """Testa um grafo completo com 3 vértices"""
        graph = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(len(path), 3)
        self.assertEqual(len(set(path)), 3)

    def test_grafo_isolado_sem_caminho(self):
        """Testa um grafo com vértices isolados"""
        graph = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        path = find_hamiltonian_path(graph)
        self.assertEqual(path, [])

    def test_caminho_valido_arestas(self):
        """Verifica se o caminho encontrado possui arestas válidas"""
        graph = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ]
        path = find_hamiltonian_path(graph)
        
        if path:
            for i in range(len(path) - 1):
                self.assertEqual(graph[path[i]][path[i + 1]], 1)

if __name__ == "__main__":
    unittest.main()