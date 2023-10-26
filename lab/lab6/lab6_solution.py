#################################
# LAB 6 Solution
# ZSH
##################################

# If you need a module, import at the top of the file. Not inside functions.
# or deep in the code. This way you can see which modules a file uses, i.e.,
# know it's "dependencies". Or what it relies upon.
import random


########################
# TASK 1
########################

########################
# A
########################
print("\n1A")
def BuildRandomList(N, R):
    nlist = []
    for i in range(N):
        x = random.randint(1,R)
        nlist.append(x)
    return nlist


# Test it
randlist = BuildRandomList(20,10)
print(randlist)

########################
# B
########################
print("\n1B")

# This is the version asked for by the lab task. That you build a new list
# from the list passed in without duplicates.
def PruneList(alist):
    new_list = []
    for element in alist:
        if element not in new_list:
            new_list.append(element)
    return new_list

# This is the harder task which many of you tried (because you didn't read
# the instructions) which removes duplicates from a list.
def PruneListInPlace(alist):
    i = 0
    while i < len(alist):
        while alist.count(alist[i]) > 1:
            alist.remove(alist[i])
        i+=1


mylist = [1,2,3,4,1,4,3,2,1,4,3]

print(f"The original list is {mylist}")

# Builds a new list.
pruned_list = PruneList(mylist)
print(f"Pruned list is: {pruned_list}")

# Alters the original list
PruneListInPlace(mylist)
print(f"mylist is now: {mylist}")

# Question for you: why do the two pruned lists differ in their order?


########################
# C
########################
print("\n1C")

randlist = BuildRandomList(20,10)
print(f"The random list is {randlist}.")
pruned_randlist = PruneList(randlist)
print(f"The pruned random list is {pruned_randlist}.")


########################
# D
########################
print("\n1D")

def CutAndPaste(L, i):
    return L[i:] + L[:i]


xlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
zlist = CutAndPaste(xlist, 5)
print(f"zlist is {zlist}.")



########################
# TASK 2
########################


########################
# A
########################
print("\n2A")


def Print2Dlist(alist):
    for x in alist:
        for y in x:
            print(y,end="")
        print()

mylist = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
Print2Dlist(mylist)


########################
# B
########################
print("\n2B")

def Copy2DList(alist):
    newlist = []
    for x in alist:
        l = []
        for y in x:
            l.append(y)
        newlist.append(l)
    return newlist


mylist = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
copyofmylist = Copy2DList(mylist)
Print2Dlist(copyofmylist) # Use the print function
print("\nChange copyofmylist[0][0] to 0")
copyofmylist[0][0] = 0
print("\nThe copy of mylist has changed.")
Print2Dlist(copyofmylist)
print("\nBut the original mylist has not.")
Print2Dlist(mylist)


#########################
# C
#########################
print("\n2C")

def Slice2DList(L, rc, index):
    if rc=='c':
        s = []
        for x in L:
            s.append(x[index])
        return s
    elif rc == 'r': # Trivial case
        return L[index]

mylist = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
aslice = Slice2DList(mylist, 'c', 1)
print(f"A column slice of the list at index 1 \n{aslice}")
bslice = Slice2DList(mylist,'r',2)
print(f"A row slice of the list at index 2 \n{bslice}")

##########################
# D
##########################3
print("\n2D")


# This function swaps elements from each end of the list
# and works toward to the middle.
def ReverseList(L):
    s = 0
    e = len(L)-1
    while s < e:

        # Swap rows
        tmp = L[s]
        L[s] = L[e]
        L[e] = tmp
        
        # Swap the row elements of s
        for i in range(len(L[s])//2):
            tmp = L[s][i]
            L[s][i] = L[s][-(i+1)]
            L[s][-(i+1)] = tmp

        # Swap the row elements of e
        for i in range(len(L[e])//2):
            tmp = L[e][i]
            L[e][i] = L[e][-(i+1)]
            L[e][-(i+1)] = tmp

        # Shift s and e toward the middle.
        s += 1
        e -= 1


mylist = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
ReverseList(mylist)
print("The reverse of mylist is:")
Print2Dlist(mylist)

