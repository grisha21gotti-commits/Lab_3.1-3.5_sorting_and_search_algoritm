# Взвешенный граф + алгоритм Дейкстры.

import heapq


def dijkstra(graph, start):
    """
    graph: dict[вершина] -> dict[сосед] = вес
    start: начальная вершина
    Возвращает словарь кратчайших расстояний.
    """
    distances = {v: float("inf") for v in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_vertex = heapq.heappop(queue)
        if current_dist > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            dist = current_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(queue, (dist, neighbor))

    return distances


if __name__ == "__main__":
    # Пример графа как в методичке (A-F)
    graph = {
        'A': {'B': 4, 'C': 7},
        'B': {'A': 4, 'D': 2, 'E': 8},
        'C': {'A': 7, 'D': 2, 'E': 5},
        'D': {'B': 2, 'C': 2, 'E': 1, 'F': 4},
        'E': {'C': 5, 'D': 1, 'F': 11},
        'F': {'B': 8, 'D': 4, 'E': 11}
    }

    start = 'A'
    distances = dijkstra(graph, start)

    print(f"Кратчайшие расстояния от вершины {start}:")
    for v in sorted(graph.keys()):
        print(f"  до вершины {v}: {distances[v]}")
