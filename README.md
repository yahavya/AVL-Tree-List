# AVL-Tree-List:

This repository contains the implementation of a List using an AVL and Rank Tree data structures in Python. 

## About
Lists are a abstract data type (ADT) in computer science. The two classic ways to implement a list are the array and the linked list. 
While each one has its own advantages, each has some operations with the slow Θ(n) time complexity.

By using a self-balancing tree structure – such as an AVL tree, it is possible to implement a list that can access and modify single elements in just Θ(log n) worst-case time, where n is the current size of the list.

## Description

## The AVLTreeList class has the following methods:

1. empty: Returns True if the list is empty, otherwise returns False.
2. retrieve(i): Returns the value of the element at index i if it exists, otherwise returns None.
3. insert(s, i): Inserts an element with value s into the list at position i (assuming there are at least i elements). 
Returns the total number of AVL tree balancing operations required to maintain balance during the repair phase.
4. delete(i): Deletes the element at index i in the list (if it exists). 
Returns the total number of AVL tree balancing operations required to maintain balance during the repair phase.
5. length(): Returns the number of elements in the list.
6. first(): Returns the value of the first element in the list or None if the list is empty.
7. last(): Returns the value of the last element in the list or None if the list is empty.
8. listToArray(): Returns an array containing the elements of the list in index order, or an empty array if the list is empty.
9. split(i): Takes an index i that exists in the list. Splits the list into two sublists: before index i and after index i.
10. concat(lst): Takes a list and concatenates it to the end of the current list.
11. heightDifference(lst): Takes a list and returns the absolute difference in heights between the merged AVL trees when the two lists are concatenated. 
This operation should run in logarithmic time complexity.
12. search(val): Returns the first index in the list where the value val appears, or 1 - if it does not exist.


## The AVLNode class has the following methods:

getHeight – Returns the height of the node, or 1 − if the node is virtual.
getValue – Returns the info of the node or None if the node is virtual.
getLeft – Returns the left child of the node or None if it does not exist.
getRight – Returns the right child of the node or None if it does not exist.
getParent – Returns the parent of the node or None if it does not exist.
isRealNode – Returns TRUE if the node represents a real node in the tree (i.e., a node that is not virtual).

* Each function's worst case time complexity is detailed both in the code and in a separate document. 
