import random

def generate_adjacency_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j] = matrix[j][i] = random.randint(0, 1)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(val) for val in row))

def depth_first_search(graph, start_vertex, visited):
    visited[start_vertex] = True
    print("Посещаем вершину:", start_vertex)

    for vertex in range(len(graph)):
        if graph[start_vertex][vertex] == 1 and not visited[vertex]:
            depth_first_search(graph, vertex, visited)

# Получаем размерность графа от пользователя
n = int(input("Введите размерность графа: "))

# Генерируем матрицу смежности
adj_matrix = generate_adjacency_matrix(n)

# Выводим матрицу на экран
print("\nМатрица смежности:")
print_matrix(adj_matrix)

# Стартовая вершина для обхода графа
start_vertex = int(input("Введите стартовую вершину для обхода: "))

# Инициализируем список посещенных вершин
visited = [False] * n

print("\nРезультат обхода графа в глубину:")
depth_first_search(adj_matrix, start_vertex, visited)