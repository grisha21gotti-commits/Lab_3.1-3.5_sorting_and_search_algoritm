// Бинарное дерево поиска: вставка, обход и поиск пути от корня к узлу.

class TreeNode {
    int key;
    TreeNode left;
    TreeNode right;

    TreeNode(int key) {
        this.key = key;
    }
}

public class лаб4_дерево {
    public static TreeNode insertBST(TreeNode root, int key) {
        if (root == null) return new TreeNode(key);
        if (key < root.key) {
            root.left = insertBST(root.left, key);
        } else if (key > root.key) {
            root.right = insertBST(root.right, key);
        }
        return root;
    }

    public static void inorder(TreeNode root, java.util.List<Integer> res) {
        if (root == null) return;
        inorder(root.left, res);
        res.add(root.key);
        inorder(root.right, res);
    }

    public static boolean findPath(TreeNode root, int target, java.util.List<Integer> path) {
        if (root == null) return false;
        path.add(root.key);
        if (root.key == target) return true;
        if (findPath(root.left, target, path) || findPath(root.right, target, path))
            return true;
        path.remove(path.size() - 1);
        return false;
    }

    public static void main(String[] args) {
        int[] values = {12, 6, 3, 2, 9, 7, 10, 15};
        TreeNode root = null;
        for (int v : values) {
            root = insertBST(root, v);
        }

        java.util.List<Integer> res = new java.util.ArrayList<>();
        inorder(root, res);
        System.out.println("Симметричный обход дерева: " + res);

        int target = 7;
        java.util.List<Integer> path = new java.util.ArrayList<>();
        if (findPath(root, target, path)) {
            System.out.println("Путь от корня к узлу " + target + ": " + path);
        } else {
            System.out.println("Узел " + target + " не найден");
        }
    }
}
