from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree():
    """
    Constructs the Binary Tree from Assessment 3.3 (Diagram 1):
    Level 0: S
    Level 1: O, L
    Level 2: A, T, O, R
    Level 3: I, O
    """
    root = Node("S")
    root.left = Node("O")
    root.right = Node("L")

    root.left.left = Node("A")
    root.left.right = Node("T")

    root.right.left = Node("O")
    root.right.right = Node("R")

    root.left.left.left = Node("I")
    root.left.left.right = Node("O")

    return root


def bfs(root):
    """Breadth-First Search (Level Order Traversal)."""
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result


def dfs_preorder(node, result=None):
    """Depth-First Search (Preorder Traversal: Root, Left, Right)."""
    if result is None:
        result = []

    if node is None:
        return result

    result.append(node.value)
    dfs_preorder(node.left, result)
    dfs_preorder(node.right, result)

    return result


if __name__ == "__main__":
    tree_root = build_binary_tree()

    bfs_result = bfs(tree_root)
    dfs_result = dfs_preorder(tree_root)

    print("Diagram 1: Binary Tree Traversals")
    print("BFS (Level Order):", "-".join(bfs_result))
    print("DFS (Preorder):   ", "-".join(dfs_result))