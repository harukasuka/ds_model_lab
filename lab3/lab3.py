import numpy as np

def connectivity_matrix(matrix):
    # Матриця зв'язності базується на матриці ваг
    con_matrix = np.where(matrix > 0, 1, 0)
    print("\nМатриця зв'язності:")
    print(con_matrix)
    return con_matrix

def output(matrix, path):
    weight = 0
    print(" Ребро : Вага ребра ")
    for i in range(num_nodes):
        u, v = path[i], path[(i+1)%num_nodes]
        print(f" {u+1} - {v+1} : {matrix[u][v]}")
        weight += matrix[u][v]
    print("\n Сумарна вага шляху:", weight, "\n")

def hamilton(k, con_matrix, c, path, start_node):
    is_hamiltonian = False
    for v in range(num_nodes):
        if con_matrix[v, path[k-1]] or con_matrix[path[k-1], v]:
            if k == num_nodes and v == start_node:
                is_hamiltonian = True
            elif c[v] == -1:
                c[v] = k
                path[k] = v
                next_node = k + 1
                is_hamiltonian = hamilton(next_node, con_matrix, c, path, start_node)
                if not is_hamiltonian:
                    c[v] = -1
            else:
                continue
    return is_hamiltonian

def find_hamiltonian_cycle(con_matrix, start_node):
    print("\nГамільтоновий цикл:")
    c = np.full(num_nodes, -1, dtype=int)
    path = np.zeros(num_nodes, dtype=int)
    path[0] = start_node
    c[start_node] = start_node

    if hamilton(1, con_matrix, c, path, start_node):
        pass
    else:
        print("Розв'язків немає")

    return path


filename = 'matrix3.txt'
matrix = np.loadtxt(filename)
print(matrix)
num_nodes = len(matrix)
con_matrix = connectivity_matrix(matrix)
path = find_hamiltonian_cycle(con_matrix, start_node=0)
output(matrix, path)