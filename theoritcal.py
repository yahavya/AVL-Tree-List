from random import shuffle
import random
from AVLTree import AVLTree, AVLNode

def check(lst):
    t = AVLTree()
    changes_sum = 0 # balancing operations
    steps_sum = 0 # distance from max
    switches_sum = 0 # how many switches until ordered
    for i in lst:
        (changes, steps, switches) = t.insertAtMax(i, "i")
        changes_sum += changes
        steps_sum += steps
        switches_sum += switches
        # print(changes, steps, switches)
    
    print(changes_sum + steps_sum, switches_sum)


# lst = [i for i in range(1111*32, 0, -1)]
lst = [i for i in range(1,1111*32)]
#random.shuffle(lst)

check(lst)
        
