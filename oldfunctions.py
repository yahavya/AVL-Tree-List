"""find_criminal receives a pointer to the newly added node,
        searches for a criminal node in the tree, BF >= 1 or BF <= -1, and returns a pointer to the node.
    """
    # def find_criminal(self, node):
    #     while node is not None: # iterate until we reach the root
    #         BF = node.left.height - node.right.height # calculate balance factor
    #         if BF not in (-1,1,0): # if BF is not 0 or 1 or -1, we have a criminal
    #             return node
    #         node = node.parent # move to the parent node
    #     return None  # if we reach the root and haven't found a criminal, return None
        
"""
    balance receives the criminal node and rebalances the tree 
    returns the number of rebalancing operations required to balance the tree.
"""
    # def balance(self, node):
        
    #     if node == None:
    #         return
    #     #node is real
    #     BF = node.left.height - node.right.height #calculate balance factor
    #     if BF == 2: #tree is left heavy
    #         leftBF = node.left.left.height - node.left.right.height
    #         if leftBF == 1 or leftBF == 0: #left child with balance factor 1, meaning child tree is also left heavy, rotate right to fix
    #             self.rotate_right(node)
    #             return 1

    #         elif leftBF == -1: #left child with balance factor -1, meaning child tree is right heavy, rotate left then right to fix
    #             self.rotate_left(node.left)
    #             self.rotate_right(node)
    #             return 2

    #     elif BF == -2: #tree is right heavy
    #         rightBF = node.right.left.height - node.right.right.height
    #         if rightBF == 1: #right child with balance factor 1, meaning child tree is left heavy, rotate right then left to fix
    #             self.rotate_right(node.right)
    #             self.rotate_left(node)
    #             return 2
    #         elif rightBF == -1 or rightBF == 0: #right child with balance factor -1, meaning child tree is also right heavy, rotate left to fix
    #             self.rotate_left(node)
    #             return 1
    #     else: #balance factor is ok, and return is irrelevant
    #         return -1

"""update_height receives a pointer to the newly added node
        updates all heights in its path to the root.
"""
    
    # def update_height(self, node):
    #     height_changed = 0
    #     while node != None:
    #         new_height = 1 + max(node.left.height, node.right.height)  # Calculate new height based on children heights
    #         if new_height != node.height:  # If the height has changed
    #             height_changed +=1
    #             node.height = new_height  # Update the height
    #         node = node.parent  # Move to the parent node
    #     return height_changed


"""update_size receives a pointer to the newly added node
        updates all sizes in its path to the root.
"""
    # def update_size(self, node):
    #     curr_node = node

    #     while curr_node != None:
    #         curr_node.size = curr_node.left.size + curr_node.right.size + 1
    #         curr_node = curr_node.parent