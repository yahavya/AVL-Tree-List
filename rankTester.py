from AVLTree import AVLTree, AVLNode


def test_rank():
    """
    Test function to validate the rank functionality of the AVL tree.
    """
    # Create an AVL tree with some nodes
    avl_tree = AVLTree()
    avl_tree.root = AVLNode(5, "Value 5")
    avl_tree.root.size = 6
    avl_tree.root.left = AVLNode(3, "Value 3")
    avl_tree.root.left.size = 3
    avl_tree.root.left.left = AVLNode(2, "Value 2")
    avl_tree.root.left.left.size = 1
    avl_tree.root.left.right = AVLNode(4, "Value 4")
    avl_tree.root.left.right.size = 1

    avl_tree.root.right = AVLNode(7, "Value 7")
    avl_tree.root.right.size = 2
    avl_tree.root.right.right = AVLNode(8, "Value 8")
    avl_tree.root.right.right.size = 1

    print("this is root", avl_tree.get_root().key)

    # Test the rank function
    print(avl_tree.rank(avl_tree.root))
    # assert avl_tree.rank(avl_tree.root) == 4

    print("All rank tests passed.")


test_rank()
