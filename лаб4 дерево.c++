// Бинарное дерево поиска: вставка, обход и поиск пути от корня к узлу.

#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node(int k) : key(k), left(nullptr), right(nullptr) {}
};

Node* insertBST(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->key)
        root->left = insertBST(root->left, key);
    else if (key > root->key)
        root->right = insertBST(root->right, key);
    return root;
}

void inorder(Node* root, vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);
    result.push_back(root->key);
    inorder(root->right, result);
}

bool findPath(Node* root, int target, vector<int>& path) {
    if (!root) return false;
    path.push_back(root->key);
    if (root->key == target) return true;
    if (findPath(root->left, target, path) || findPath(root->right, target, path))
        return true;
    path.pop_back();
    return false;
}

int main() {
    // Пример дерева
    int values[] = {12, 6, 3, 2, 9, 7, 10, 15};
    Node* root = nullptr;
    for (int x : values) {
        root = insertBST(root, x);
    }

    vector<int> res;
    inorder(root, res);
    cout << "Симметричный обход дерева: ";
    for (int x : res) cout << x << " ";
    cout << "\n";

    int target = 7;
    vector<int> path;
    if (findPath(root, target, path)) {
        cout << "Путь от корня к узлу " << target << ": ";
        for (int x : path) cout << x << " ";
        cout << "\n";
    } else {
        cout << "Узел " << target << " не найден\n";
    }

    return 0;
}
