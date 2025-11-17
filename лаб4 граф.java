// Взвешенный граф + алгоритм Дейкстры.

import java.util.*;

public class лаб4_граф {

    static class Edge {
        int to;
        int weight;
        Edge(int t, int w) {
            to = t;
            weight = w;
        }
    }

    public static int[] dijkstra(List<List<Edge>> graph, int start) {
        int n = graph.size();
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.add(new int[]{0, start});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0];
            int v = cur[1];
            if (d > dist[v]) continue;

            for (Edge e : graph.get(v)) {
                int nd = d + e.weight;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    pq.add(new int[]{nd, e.to});
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        // 0..5 соответствуют A..F
        int n = 6;
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        // утилита для добавления неориентированного ребра
        java.util.function.BiConsumer<int[], Integer> add =
                (arr, w) -> {
                    int u = arr[0], v = arr[1];
                    graph.get(u).add(new Edge(v, w));
                    graph.get(v).add(new Edge(u, w));
                };

        add.accept(new int[]{0,1}, 4);  // A-B
        add.accept(new int[]{0,2}, 7);  // A-C
        add.accept(new int[]{1,3}, 2);  // B-D
        add.accept(new int[]{1,4}, 8);  // B-E
        add.accept(new int[]{2,3}, 2);  // C-D
        add.accept(new int[]{2,4}, 5);  // C-E
        add.accept(new int[]{3,4}, 1);  // D-E
        add.accept(new int[]{3,5}, 4);  // D-F
        add.accept(new int[]{4,5}, 11); // E-F
        add.accept(new int[]{1,5}, 8);  // B-F

        int start = 0; // A
        int[] dist = dijkstra(graph, start);

        char[] name = {'A','B','C','D','E','F'};
        System.out.println("Кратчайшие расстояния от вершины A:");
        for (int i = 0; i < n; i++) {
            System.out.println("  до вершины " + name[i] + ": " + dist[i]);
        }
    }
}
