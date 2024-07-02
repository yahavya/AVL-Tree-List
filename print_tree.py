
## Written by Amitai Cohen 
## adjustment for AVL Trees by Eviatar, Yaron, and ChatGPT

from AVLTree import AVLTree, AVLNode

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # Print the textual representation returned by trepr
    for row in trepr(t.root, bykey):
        print(row)

def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t is None:
        return ["#"]  # Represent None as '#'

    if not t.is_real_node:
        return []  # Skip virtual nodes

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))

def conc(left, root, right):
    """Return a concatenation of textual representations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1]) if left else 0
    rwid = len(right[-1]) if right else 0
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    if left and right:
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")
    elif left:
        ls = leftspace(left[0])
        result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " ")
    elif right:
        rs = rightspace(right[0])
        result.append(rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i] if left else lwid * " "
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i] if right else rwid * " "
        else:
            row += rwid * " "

        result.append(row)

    return result

def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    if row:
        i = len(row) - 1
        while i >= 0 and row[i] == " ":
            i -= 1
        return i + 1
    else:
        return 0

def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    if row:
        i = 0
        while i < len(row) and row[i] == " ":
            i += 1
        return i
    else:
        return 0


t = AVLTree()


# for i in range(10):
#     print("changes", t.insert(i, "i"))
#     printree(t)
#     print()

printree(t)
print(t.insertAtMax(4, "a"))
printree(t)
print(t.insertAtMax(3, "a"))
printree(t)
print(t.insertAtMax(2, "a"))
printree(t)
print(t.insertAtMax(1, "a"))
printree(t)



# for i in range(1,21):
#     t.insert(i, "i")

# for i in range(1,21):
#     print(t.rank(t.search(i))) 


# def check_height(node):
#     if node.is_virtual_node():
#         return -1
    
#     height = 1 + max(check_height(node.left), check_height(node.right))
#     if height != node.height:
#         print("KEY IS", node.key, "WRONG HEIGHT IS", node.height)
#     return height   

def check_size(node):
    if node.is_virtual_node():
        return 0
    
    size = 1 + check_size(node.left) + check_size(node.right)
    if size != node.size:
        print("KEY IS", node.key, "WRONG SIZE IS", node.size)
    return size

def check_height(node):
    if node.is_virtual_node():
        return -1
    temp=max(check_height(node.left),check_height(node.right))+1
    if temp!= node.height:
        print("probelm with ", node.key,". height should be ",temp," but its ",node.height)
    #else:
     #   print("the height of the node with key:", node.key," is",temp)
    return temp

#t.delete(t.search(5))
# check_height(t.root)
# check_size(t.root)
# print(t.root.height)
# print(t.root.size)
# printree(t)
# print("left side size", t.root.left.size)
# print("right side size",t.root.right.size)
# print("root size",t.root.size)
# printree(t)



#printree(t)



