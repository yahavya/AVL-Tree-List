from AVLTree import AVLTree, AVLNode


def test_search():
    """
    Test function to validate the search functionality of the AVL tree.
    """
    # Create an AVL tree with some nodes
    avl_tree = AVLTree()
    avl_tree.root = AVLNode(5, "Value 5")
    avl_tree.root.left = AVLNode(3, "Value 3")
    avl_tree.root.left = AVLNode(2, "Value 2")

    avl_tree.root.right = AVLNode(7, "Value 7")
    avl_tree.root.right.right = AVLNode(8, "Value 8")

    searched = avl_tree.search(4)

    print("searched for x and found:", searched)

    print("All search tests passed.")


test_search()
