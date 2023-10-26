def recsum(n):
    if n==1:
        return 1
    else:
        return n+recsum(n-1)
print(recsum(5))

def rec(n):
    if n<4:
        return n
    else:
        return 1+rec(n-4)
print(rec(36))

def rec1(n):
    if len(n)==1:
        return []
    else:
        return [rec1(n[(len(n)//2):] + rec1(n[:(len(n)//2)]))]
#print(rec1([1,2,3,4,5,6]))
