
// Примеры мультисписка, очереди, дека и приоритетной очереди на Java

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.PriorityQueue;

public class lab_1_2 {
    public static void exampleMultilist() {
        System.out.println("=== МУЛЬТИСПИСОК (ArrayList<ArrayList<Integer>>) ===");
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();

        ArrayList<Integer> row1 = new ArrayList<>();
        row1.add(1);
        row1.add(2);

        ArrayList<Integer> row2 = new ArrayList<>();
        row2.add(3);
        row2.add(4);

        matrix.add(row1);
        matrix.add(row2);

        System.out.println("Матрица: " + matrix);

        System.out.print("Обход элементов: ");
        for (ArrayList<Integer> row : matrix) {
            for (Integer x : row) {
                System.out.print(x + " ");
            }
        }
        System.out.println("\n");
    }

    public static void exampleQueue() {
        System.out.println("=== ОЧЕРЕДЬ (Queue<String>) ===");
        Queue<String> queue = new LinkedList<>();

        queue.add("task1");
        queue.add("task2");
        queue.add("task3");

        while (!queue.isEmpty()) {
            String current = queue.poll(); // извлекает из головы очереди
            System.out.println("Обрабатывается: " + current);
        }
        System.out.println();
    }

    public static void exampleDeque() {
        System.out.println("=== ДЕК (Deque<Integer>) ===");
        Deque<Integer> deque = new ArrayDeque<>();

        deque.addLast(10);   // добавление справа
        deque.addLast(20);
        deque.addFirst(5);   // добавление слева

        System.out.println("Состояние дека: " + deque);

        Integer left = deque.removeFirst();
        Integer right = deque.removeLast();

        System.out.println("Удалён слева: " + left);
        System.out.println("Удалён справа: " + right);
        System.out.println("Итоговое состояние дека: " + deque);
        System.out.println();
    }

    public static void examplePriorityQueue() {
        System.out.println("=== ПРИОРИТЕТНАЯ ОЧЕРЕДЬ (PriorityQueue<Integer>) ===");

        PriorityQueue<Integer> pq = new PriorityQueue<>(); // min-heap

        pq.offer(20);
        pq.offer(5);
        pq.offer(15);
        pq.offer(1);

        while (!pq.isEmpty()) {
            System.out.println("Следующий элемент: " + pq.poll());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        exampleMultilist();
        exampleQueue();
        exampleDeque();
        examplePriorityQueue();
    }
}
