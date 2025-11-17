# Примеры мультисписка, очереди, дека и приоритетной очереди на Python

from queue import Queue, PriorityQueue
from collections import deque
import heapq


def example_multilist():
    print("=== МУЛЬТИСПИСОК (вложенный список) ===")
    groups = [
        ["Иван", "Петя"],
        ["Маша", "Катя"],
        ["Дима", "Саша"]
    ]
    print("Исходный мультисписок:", groups)

    # Пример обхода мультисписка
    all_names = []
    for group in groups:
        for name in group:
            all_names.append(name)

    print("Все имена в одном списке:", all_names)
    print()


def example_queue():
    print("=== ОЧЕРЕДЬ (Queue) ===")
    q = Queue()

    # Добавление элементов в очередь
    q.put("task1")
    q.put("task2")
    q.put("task3")

    # Извлечение элементов в порядке FIFO
    while not q.empty():
        current = q.get()
        print("Обрабатывается:", current)
    print()


def example_deque():
    print("=== ДЕК (collections.deque) ===")
    d = deque()

    # Добавляем элементы в оба конца
    d.append("справа_1")
    d.append("справа_2")
    d.appendleft("слева_1")

    print("Состояние дека:", d)

    # Удаляем элементы с обоих концов
    left = d.popleft()
    right = d.pop()
    print("Удалён слева:", left)
    print("Удалён справа:", right)
    print("Итоговое состояние дека:", d)
    print()


def example_priority_queue_queue():
    print("=== ПРИОРИТЕТНАЯ ОЧЕРЕДЬ (queue.PriorityQueue) ===")
    pq = PriorityQueue()

    # Чем меньше число, тем выше приоритет
    pq.put((2, "средний приоритет"))
    pq.put((1, "высокий приоритет"))
    pq.put((3, "низкий приоритет"))

    while not pq.empty():
        priority, item = pq.get()
        print(f"priority={priority}, item={item}")
    print()


def example_priority_queue_heapq():
    print("=== ПРИОРИТЕТНАЯ ОЧЕРЕДЬ (heapq) ===")
    customers = []
    # heappush создаёт min-heap
    heapq.heappush(customers, (2, "Harry"))
    heapq.heappush(customers, (3, "Charles"))
    heapq.heappush(customers, (1, "Riya"))
    heapq.heappush(customers, (4, "Stacy"))

    while customers:
        print(heapq.heappop(customers))
    print()


if __name__ == "__main__":
    example_multilist()
    example_queue()
    example_deque()
    example_priority_queue_queue()
    example_priority_queue_heapq()
