// Примеры мультисписка, очереди, дека и приоритетной очереди на C++

#include <iostream>
#include <vector>
#include <queue>
#include <deque>

int main() {
    using std::cout;
    using std::endl;

    // === МУЛЬТИСПИСОК (std::vector<std::vector<int>>) ===
    cout << "=== МУЛЬТИСПИСОК (vector<vector<int>>) ===" << endl;
    std::vector<std::vector<int>> matrix = {
        {1, 2},
        {3, 4}
    };

    cout << "Матрица:" << endl;
    for (const auto& row : matrix) {
        for (int x : row) {
            cout << x << " ";
        }
        cout << endl;
    }
    cout << endl;

    // === ОЧЕРЕДЬ (std::queue<int>) ===
    cout << "=== ОЧЕРЕДЬ (std::queue<int>) ===" << endl;
    std::queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);

    while (!q.empty()) {
        cout << "Обрабатывается: " << q.front() << endl;
        q.pop();
    }
    cout << endl;

    // === ДЕК (std::deque<int>) ===
    cout << "=== ДЕК (std::deque<int>) ===" << endl;
    std::deque<int> d;
    d.push_back(2);   // справа
    d.push_back(3);
    d.push_front(1);  // слева

    cout << "Состояние дека: ";
    for (int x : d) {
        cout << x << " ";
    }
    cout << endl;

    int left = d.front();
    d.pop_front();
    int right = d.back();
    d.pop_back();

    cout << "Удалён слева: " << left << endl;
    cout << "Удалён справа: " << right << endl;
    cout << "Итоговое состояние дека: ";
    for (int x : d) {
        cout << x << " ";
    }
    cout << endl << endl;

    // === ПРИОРИТЕТНАЯ ОЧЕРЕДЬ (std::priority_queue<int>) ===
    cout << "=== ПРИОРИТЕТНАЯ ОЧЕРЕДЬ (std::priority_queue<int>) ===" << endl;
    std::priority_queue<int> pq; // max-heap по умолчанию

    pq.push(5);
    pq.push(20);
    pq.push(1);
    pq.push(15);

    while (!pq.empty()) {
        cout << "Следующий элемент: " << pq.top() << endl;
        pq.pop();
    }

    return 0;
}
