// Взвешенный граф + алгоритм Дейкстры.

#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    // Пример графа: 0..5 соответствуют A..F
    int n = 6;
    vector<vector<pair<int,int>>> graph(n);
    auto add_edge = [&](int u, int v, int w) {
        graph[u].push_back({v, w});
        graph[v].push_back({u, w}); // неориентированный
    };

    // A(0), B(1), C(2), D(3), E(4), F(5)
    add_edge(0, 1, 4); // A-B
    add_edge(0, 2, 7); // A-C
    add_edge(1, 3, 2); // B-D
    add_edge(1, 4, 8); // B-E
    add_edge(2, 3, 2); // C-D
    add_edge(2, 4, 5); // C-E
    add_edge(3, 4, 1); // D-E
    add_edge(3, 5, 4); // D-F
    add_edge(4, 5, 11); // E-F
    add_edge(1, 5, 8); // B-F

    int start = 0; // A
    vector<int> dist(n, INF);
    dist[start] = 0;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, v] = pq.top();
        pq.pop();
        if (d > dist[v]) continue;
        for (auto [to, w] : graph[v]) {
            if (dist[v] != INF && dist[v] + w < dist[to]) {
                dist[to] = dist[v] + w;
                pq.push({dist[to], to});
            }
        }
    }

    char name[] = {'A','B','C','D','E','F'};
    cout << "Кратчайшие расстояния от вершины A:\n";
    for (int i = 0; i < n; ++i) {
        cout << "  до вершины " << name[i] << ": " << dist[i] << "\n";
    }

    return 0;
}
