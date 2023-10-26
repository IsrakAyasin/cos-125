
import random
def BuildRandomList(N,times):
    list=[]
    for i in range(times):
        list.append(random.randint(1,N))
    return(list)
BuildRandomList(10,9)

def PruneList(list):
    newList=[]
    for i in list:
        if i not in newList:
            newList.append(i)

    return newList
PruneList([1,2,2,3,1,1,4,4])

#print(PruneList(BuildRandomList(10,9)))

def RemoveAll(L,e):
    for i in L:
        if str(i) in str(e):
            L.remove(i)
    
    print(L)

#RemoveAll([0,1,2,3,2,34,4,2],2)

def CutAndPaste(L,i):
    print(L[i:]+L[:i])
#CutAndPaste([0,1,2,3,4,5,6,7,8,9,10],5)

def Print2DList(twoDList):
    for i in twoDList:
        for j in i:
            print(j,end="")
        print("")  
#Print2DList([[9,8,7],[6,5,4],[3,2,1]])

def Copy2DList(tList):
    list=tList
    tList=[1,2]
    print(tList)
    print(list)
#Copy2DList([[9,8,7],[6,5,4],[3,2,1]])

def RemoveAll(L,e):
    for i in L:
        for j in i:
            if str(e) in str(j):
                L.remove(i)
    print(L)
RemoveAll([[9,8,7],[6,5,4],[3,2,1],[2,3,4],[6,7,8]],6)

def slice2dlist(L,rc,index)