# Простое бинарное дерево поиска: вставка, обход и поиск пути от корня к узлу.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert_bst(root, key):
    """Вставка ключа в бинарное дерево поиска."""
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    elif key > root.key:
        root.right = insert_bst(root.right, key)
    # если равен – не вставляем дубликаты
    return root


def inorder_traversal(root):
    """Симметричный обход дерева (left, root, right)."""
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.key)
        dfs(node.right)

    dfs(root)
    return result


def find_path(root, target):
    """
    Поиск пути от корня к узлу со значением target.
    Возвращает список ключей на пути или None.
    """
    path = []

    def dfs(node):
        if node is None:
            return False
        path.append(node.key)
        if node.key == target:
            return True
        if dfs(node.left) or dfs(node.right):
            return True
        path.pop()
        return False

    if dfs(root):
        return path
    return None


if __name__ == "__main__":
    # Пример дерева, похожий на методичку
    values = [12, 6, 3, 2, 9, 7, 10, 15]
    root = None
    for v in values:
        root = insert_bst(root, v)

    print("Симметричный обход дерева:", inorder_traversal(root))

    target = 7
    path = find_path(root, target)
    if path:
        print(f"Путь от корня к узлу {target}:", path)
    else:
        print(f"Узел {target} не найден")
