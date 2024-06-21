# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        if self.value == None:
            return False
        return True


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None

    """searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""

    def search(self, key):
        """helper function: gets a node and key, recursively searches for node with this key in tree
        @type node: AVLNode, key: int
        @param key: a key to be searched
        @rtype AVLNode if node is in tree, else None
        @returns: node corresponding to key
        """

        def searchRec(node, key):
            if not node.is_real_node():
                return None
            elif node.key > key:
                return searchRec(node.left, key)
            elif node.key < key:
                return searchRec(node.right, key)
            else:
                return node

        if self.root==None:                            #deal with empty tree
            return None
        return searchRec(self.root, key)               

    """inserts a new node into the dictionary with corresponding key and value

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, key, val):
        new_node=AVLNode(key,val)
        new_node.size=1
        node=self.root
        if node==None:
            self.root=new_node
            vir_node=AVLNode(None,None)
            vir_node.size=0
            self.root.left=vir_node
            self.root.right=vir_node
        
        else:      
            while (node.right.is_real_node() and node.key<key) or ((node.left.is_real_node() and node.key>key)):
                if node.key<key:
                    node=node.right
                elif node.key>key:
                    node=node.left
            if node.key>key and (not node.left.is_real_node()):
                virtual_node=node.left
                node.left=new_node
                new_node.left=virtual_node
                new_node.right=virtual_node
                new_node.parent=node
            elif node.key<key and (not node.right.is_real_node()):
                virtual_node=node.right
                node.right=new_node
                new_node.left=virtual_node
                new_node.right=virtual_node
                new_node.parent=node
    
        return -1

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):
        return -1

    """returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

    def avl_to_array(self):
        """helper function: gets a node and lst, recursively fill the list with tuples of key,value sorted by the key
        @type node: AVLNode, lst: list
        @base case: reached virtual node
        @returns: doesn't return anything. just filling the list
        """

        def avl_to_arrayRec(node, lst):
            if not node.is_real_node():
                return lst
            avl_to_arrayRec(node.left, lst)
            lst.append((node.key,node.value))
            avl_to_arrayRec(node.right, lst)

        sortedArray = []
        avl_to_arrayRec(self.root, sortedArray)
        return sortedArray

    """returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""

    def size(self):
        return self.root.size

    """compute the rank of node in the dictionary

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary to compute the rank for
	@rtype: int
	@returns: the rank of node in self
	"""

    # If we go up to the right, don't do anything
    def rank(self, node):
        counter = 0
        curr = node
        while curr.parent != None:  # Keep going up to the root
            if curr.parent.key < curr.key:
                counter += (
                    1 + curr.parent.left.size
                )  # If we go up to the left, add parent's left sub-tree + 1 to the counter
            curr = curr.parent
        counter += 1 + curr.left.size
        return counter

    """finds the i'th smallest item (according to keys) in the dictionary

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: AVLNode
	@returns: the node of rank i in self
	"""

    def select(self, i):
        def selectRec(node,i):
            n=node.left.size                           #assuming size of a virtual node is 0         
            #print(n)
            if n>=i:                                    #means the left son has at least i nodes
                return selectRec(node.left, i)         #go search the i'th in the left branch
            
            elif n+1==i:                               #means this node if the i'th, so return it                             
                return node
            else:                                      #means i>n+1
                return selectRec(node.right, i-n-1)    #return the i-n-1 item in the right branch which is the i'th in the tree
        
        
        if self.root==None:                            #deal with empty tree
            return None
        
        node_temp=selectRec(self.root,i)
        return node_temp

    """finds the node with the largest value in a specified range of keys

	@type a: int
	@param a: the lower end of the range
	@type b: int
	@param b: the upper end of the range
	@pre: a<b
	@rtype: AVLNode
	@returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
	"""

    def max_range(self, a, b):
        return None

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return self.root
