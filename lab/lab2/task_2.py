x=0.1
if x>1:
    x=1
elif x<-1:
    x=-1
else:
    x=0
print(x)

y=15
if y>10 and y<20:
    print("Yes")
else:
    print("NO")

a=1
b=1
c=1
if a==b and a==c:
    print("Correct")
else:
    print("Incorrenct")

t=5.00
if t==int(t):
    t=int(t)
print(t)
i=0
j=0
k=1
if ((i!=0 and j==0)and k==0):
    print(True)
elif ((i==0 and j!=0)and k==0):
    print(True)
elif ((i==0 and j==0)and k!=0):
    print(True)
else:
    print(False)


