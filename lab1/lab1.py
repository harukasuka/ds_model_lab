# зчитування з файлу
with open('matrix1.txt', 'r') as f:
    l = [[int(num) for num in line.split(' ')] for line in f]

adjMatrix = l
setMatrix = []
# фінальна матриця ребер
finalmatr = []
# наповнення головної матриці
for i in range(0, len(adjMatrix)):
    setMatrix.append([i])


# Обхід наших груп початково окрема вершина е окрема група
def combine(e):
    e0 = -1
    e1 = -1
    for i in range(0, len(setMatrix)):
        # перевірка наявності в матриці
        if e[0] in setMatrix[i]:
            e0 = i
        if e[1] in setMatrix[i]:
            e1 = i
    setMatrix[e0] += setMatrix[e1]
    del setMatrix[e1]


print("Стартове групування: " + str(setMatrix))
# цикл виконується поки матриця не одна група
while (len(setMatrix) > 1):
    edges = []
    for component in setMatrix:
        m = [999, [0, 0]]
        for vertex in component:
            for i in range(0, len(adjMatrix[0])):
                if i not in component and adjMatrix[vertex][i] != 0:
                    # Перевірка на мінімальні ребра
                    if (m[0] > adjMatrix[vertex][i]):
                        m[0] = adjMatrix[vertex][i]
                        m[1] = [vertex, i]
        # Якщо ребро менше
        if (m[1][0] > m[1][1]):
            m[1][0], m[1][1] = m[1][1], m[1][0]
        # Якщо його нема
        if (m[1] not in edges):
            edges.append(m[1])

    for e in edges:
        combine(e)
    finalmatr.append(edges)
    print("Дуги: " + str(edges) + "Групи: " + str(setMatrix))

for each in finalmatr:
    for edge in each:
        print("Ребро:" + str(edge))


