import random


def greedy_vertex_cover(edges):
    """
    Жадный алгоритм для задачи о вершинном покрытии.
    edges: список рёбер в виде пар (u, v)
    Возвращает множество вершин покрытия.
    """
    cover = set()
    remaining = edges.copy()

    # Пока есть ребра
    while remaining:
        # Берём первое ребро
        u, v = remaining[0]

        # Добавляем обе вершины в покрытие
        cover.add(u)
        cover.add(v)

        # Удаляем все рёбра, инцидентные u или v
        new_remaining = []
        for (a, b) in remaining:
            if a != u and a != v and b != u and b != v:
                new_remaining.append((a, b))
        remaining = new_remaining

    return cover


def create_graph_from_edges(edges):
    """
    Создаёт граф (словарь смежности) из списка рёбер.
    """
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph


def unique_edges(graph):
    """
    Возвращает уникальные рёбра (u < v)
    """
    edges = set()
    for u in graph:
        for v in graph[u]:
            if u < v:
                edges.add((u, v))
            elif v < u:
                edges.add((v, u))
    return sorted(edges)


def display_graph_info(graph):
    """
    Печатает количество вершин, рёбер и списки.
    """
    vertices = sorted(graph.keys())
    edges = unique_edges(graph)
    print(
        f"Количество вершин: {len(vertices)} "
        f"Количество ребер: {len(edges)} "
        f"Вершины: {vertices} "
        f"Ребра: {edges}"
    )


def variant_graph_edges():
    """
    Рёбра графа варианта 1 (цикл из 10 вершин)
    """
    return [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
        (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)
    ]


def input_graph():
    """
    Меню выбора способа ввода графа.
    """
    print("\n" + "=" * 50)
    print("ВВОД ДАННЫХ ГРАФА")
    print("=" * 50)
    print("1 - Использовать граф по варианту (цикл из 10 вершин)")
    print("2 - Ввести рёбра вручную")
    print("3 - Сгенерировать случайный граф")

    while True:
        choice = input("Ваш выбор (1-3): ").strip()
        if choice == "1":
            edges = variant_graph_edges()
            print("Выбран граф по варианту.")
            return create_graph_from_edges(edges)
        elif choice == "2":
            return create_graph_from_edges(input_manual_edges())
        elif choice == "3":
            return create_graph_from_edges(generate_random_graph())
        else:
            print("Ошибка ввода.")


def input_manual_edges():
    edges = []
    print("\nВведите рёбра (например: 0 1). end — завершить.")
    while True:
        s = input("> ").strip()
        if s == "end":
            break
        try:
            u, v = map(int, s.split())
            edges.append((u, v))
        except:
            print("Ошибка.")
    return edges


def generate_random_graph():
    import random
    print("\nГенерация случайного графа.")
    n = int(input("Количество вершин: "))
    m = int(input("Количество рёбер: "))

    vertices = list(range(n))
    possible_edges = []

    for i in range(n):
        for j in range(i + 1, n):
            possible_edges.append((i, j))

    m = min(m, len(possible_edges))
    return random.sample(possible_edges, m)


def solve(graph):
    print("\n" + "=" * 50)
    print("ИНФОРМАЦИЯ О ГРАФЕ")
    print("=" * 50)
    display_graph_info(graph)

    edges = unique_edges(graph)
    cover = greedy_vertex_cover(edges)

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 50)
    print("Покрытие вершин:", sorted(cover))
    print("Размер покрытия:", len(cover))
    print(f"Доля вершин в покрытии: {len(cover) / len(graph) * 100:.1f}%")
    print()


def main():
    print("=" * 60)
    print("ЖАДНЫЙ АЛГОРИТМ ВЕРШИННОГО ПОКРЫТИЯ")
    print("=" * 60)

    while True:
        graph = input_graph()
        solve(graph)

        again = input("Продолжить? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
