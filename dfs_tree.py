class TreeNode:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


def create_tree():
    # Builds the Assessment 3.5 tree for Solatorio, John Wave
    n_left = TreeNode("N", left=TreeNode("A"), right=TreeNode("T"))
    s_right = TreeNode("S", left=TreeNode("O"), right=TreeNode("R"))
    o_left = TreeNode("O", left=n_left, right=s_right)

    o_mid = TreeNode("O", left=TreeNode("I"), right=TreeNode("O"))
    l_right = TreeNode("L")
    h_right = TreeNode("H", left=o_mid, right=l_right)

    return TreeNode("J", left=o_left, right=h_right)


def preorder(node):
    if not node:
        return []
    return [node.label] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.label] + inorder(node.right)


def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.label]


def main():
    root = create_tree()
    print("Preorder :", " -> ".join(preorder(root)))
    print("Inorder  :", " -> ".join(inorder(root)))
    print("Postorder:", " -> ".join(postorder(root)))


if __name__ == "__main__":
    main()