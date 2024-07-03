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

def check_size(node):
    if node.is_virtual_node():
        return 0
    temp=check_size(node.left)+check_size(node.right)+1
    if temp!= node.size:
        print("probelm with ", node.key,". size should be ",temp," but its ",node.size)

    return temp

def check_height(node):
    if node.is_virtual_node():
        return -1
    temp=max(check_height(node.left),check_height(node.right))+1
    if temp!= node.height:
        print("probelm with ", node.key,". height should be ",temp," but its ",node.height)
    #else:
     #   print("the height of the node with key:", node.key," is",temp)
    return temp

def get_successor(node):
    dontAskWhy=node
    if node.right.is_real_node():
        nodi=node.right
        while nodi.left.is_real_node():
            nodi=nodi.left
        return nodi
    else:
        while node.parent!=None:
            if node==node.parent.left:
                return node.parent
            node=node.parent
    while dontAskWhy.left.is_real_node():
        dontAskWhy=dontAskWhy.left
    return dontAskWhy.left

def check_successor(node, p = False):
    while node.left.is_real_node():
        node=node.left
    while(node.is_real_node()):
        realSucc=get_successor(node)
        maybeSucc=node.successor
        if p:
            if realSucc.is_virtual_node() and maybeSucc.is_virtual_node() :
                print("analyzing ", node.key, ". successor should be virtual node and it is so")
            elif (realSucc.is_virtual_node()) and (maybeSucc.is_real_node()):
                print("analyzing ", node.key,". node successor is", maybeSucc.key, "altough it needs to be virtual")
            elif (realSucc.is_real_node() and maybeSucc.is_virtual_node()):
                print("analyzing ", node.key,". node successor is Virtual altough it needs to be", realSucc.key)
            else:
                print("analyzing ", node.key, ". successor shold be", realSucc.key," and its", maybeSucc.key)
        if realSucc!=maybeSucc:

            print("probelm with successor of ", node.key,". successor shold be", realSucc.key," but its", maybeSucc.key)
            return
        node=maybeSucc

def visualy_check_maxRange(Tree,a,b):
    lst = Tree.avl_to_array()
    print(' '.join(map(str, lst)))
    node=Tree.max_range(a,b)
    print("max is", node.value, "in node ",node.key)

def check_balanced(node):
    if node.is_virtual_node():
        return True
    heightL=node.left.height
    heightR=node.right.height
    a = heightL - heightR
    t = a in (0,1,-1)
    balanced =  t and check_balanced(node.left) and check_balanced(node.right)
    if not balanced:
        print(node.key,"is not balanced")
    return balanced
T0=AVLTree()
for i in range(1):
    T0.insert(i,"i")
T0.delete(T0.root)


T1=AVLTree()
n=10000
for i in range(n):
    T1.insert(i,"")
    T1.insert((2*n)-i,"")
for i in range(0,n,3):

    T1.delete(T1.search(i))
    T1.delete(T1.search((2*n)-i))







T2=AVLTree()
for i in range (n):
    T2.insert(i,"")


T3=AVLTree()
T3.insert(15,"a")
T3.insert(8,"a")
T3.insert(22,"c")
T3.insert(4,"")
T3.insert(11,"d")
T3.insert(20,"z")
T3.insert(24,"")
T3.insert(2,"")
T3.insert(9,"b")
T3.insert(12,"e")
T3.insert(18,"a")
T3.insert(13,"f")
T3.insert(10,"c")
T3.insert(11.5,"c")
T3.insert(23,"g")
T3.delete(T3.search(2))
T3.delete(T3.search(4))






m=1000000
T5=AVLTree()
for i in range(m):
    T5.insert(i,"")
for i in range(0,m,3):
    T5.delete(T5.search(i))
for i in range(m,2*m,2):
    T5.insert(i,"")
for i in range(m,2*m,4):
    T5.delete(T5.search(i))



print("started")
check_height(T1.root)
check_height(T2.root)
check_height(T3.root)
check_height(T5.root)
check_size(T1.root)
check_size(T2.root)
check_size(T3.root)
check_size(T5.root)
check_successor(T1.root, False)
check_successor(T2.root,False)
check_successor(T3.root,False)
check_successor(T5.root,False)
check_balanced(T1.root)
check_balanced(T2.root)
check_balanced(T3.root)
check_balanced(T5.root)
print("completed")

# visualy_check_maxRange(T3,11,18)
# print("completed")