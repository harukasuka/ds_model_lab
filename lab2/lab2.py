with open('matrix2.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(' ')] for line in f]

print("Матриця з файлу")
for m in matrix:
    print(m)


def sum_edges(matrix):
    total_weight = 0
    matrix_length = len(matrix)
    for i in range(matrix_length):
        for j in range(i, matrix_length):
            total_weight += matrix[i][j]
    return total_weight

print(f"Загальна вага з непарними вершинами: {sum_edges(matrix)}")

def dijkstra(matrix, source, dest):# Алгоритм дейкстри для знаходження шляху
    shortest = [0] * len(matrix)
    selected = [source]
    graph_length = len(matrix)
    inf = float("inf")
    min_sel = inf
    for i in range(graph_length):
        if i == source:
            shortest[source] = 0
        else:
            if matrix[source][i] == 0:
                shortest[i] = inf
            else:
                shortest[i] = matrix[source][i]
                if shortest[i] < min_sel:
                    min_sel = shortest[i]
                    ind = i

    if source == dest:
        return 0

    selected.append(ind)
    while ind != dest:
        for i in range(graph_length):
            if i not in selected:
                if matrix[ind][i] != 0:
                    if matrix[ind][i] + min_sel < shortest[i]:
                        shortest[i] = matrix[ind][i] + min_sel
        temp_min = float("inf")

        for j in range(graph_length):
            if j not in selected:
                if shortest[j] < temp_min:
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]


    def get_odd_vertices(graph):#Вершини по індексам
        degrees = [0] * len(graph)
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] != 0:
                    degrees[i] += 1

        print(f"Степені для кожної вершини: {degrees}")
        odd_vertices = [i for i in range(len(degrees)) if degrees[i] % 2 != 0]
        print('Непарні вершини:', odd_vertices)
        return odd_vertices


    def gen_pairs(odd_vertices):# Генеруються  унікальні пари по індексам
        pairs = []
        for i in range(len(odd_vertices) - 1):
            pairs.append([])
            for j in range(i + 1, len(odd_vertices)):
                pairs[i].append([odd_vertices[i], odd_vertices[j]])

        return pairs


    #Розв'язок задачі
    def Postman_sol(matrix):
        odds = get_odd_vertices(matrix)
        if (len(odds) == 0):
            return sum_edges(matrix)
        pairs = gen_pairs(odds)
        l = (len(pairs) + 1) // 2

        pairings_sum = []

        def get_pairs(pairs, done=[], final=[]):

            if (pairs[0][0][0] not in done):
                done.append(pairs[0][0][0])

                for i in pairs[0]:
                    f = final[:]
                    val = done[:]
                    if (i[1] not in val):
                        f.append(i)
                    else:
                        continue

                    if (len(f) == l):
                        pairings_sum.append(f)
                        return
                    else:
                        val.append(i[1])
                        get_pairs(pairs[1:], val, f)

            else:
                get_pairs(pairs[1:], done, final)

        get_pairs(pairs)
        min_sums = []

        for i in pairings_sum:
            s = 0
            for j in range(len(i)):
                s += dijkstra(matrix, i[j][0], i[j][1])
            min_sums.append(s)

        added_dis = min(min_sums)
        postman_dis = added_dis + sum_edges(matrix)
        return postman_dis


print('Задача листоноші з парними вершинами:', Postman_sol(matrix))
