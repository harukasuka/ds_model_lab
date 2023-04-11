
with open('D:/Політех/4 курс/ДМ/1/lab4/matrix4.txt', 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]


print("Матриця ваг")
for row in matrix:
    print(row)


def bfs(graph, start, end, parent):

    num_vertices = len(graph)

    # Ініціалізуйте список для відстеження відвіданих вершин та чергу для зберігання вершин, які необхідно відвідати.
    visited = [False] * num_vertices
    queue = [start]

    # Позначити стартовий вузол як відвіданий.
    visited[start] = True

    while queue:
        u = queue.pop(0)

        for v, val in enumerate(graph[u]):
            if not visited[v] and val > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == end:
                    return True

    return False


def ford_fulkerson_alg(graph, source, sink):

    num_vertices = len(graph)

    parent = [-1] * num_vertices
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        max_flow += path_flow

    return max_flow



source = 0
sink = 7
print(f"Максимальний потік дорівнює {ford_fulkerson_alg(matrix, source, sink)}")