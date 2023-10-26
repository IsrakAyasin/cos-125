#task1
x=-5
while x<=5:
    print(x)
    x+=1

for i in range(-5,6):
    print(i)

#task2-1
count=0
for i in range(10):
    for i in range(5):
        count+=1
print(count)

#task2-2
x=0
count=0
while x<4:
    y=0
    while y<8:
        count+=1
        y+=1
    x+=1
    
print(count)

L = ["A", "B", "C", "D", "E"]
#task2-3
x=0
while x<len(L):
    print(L[x])
    x+=1
#task2-4
for i in L:
    print(i)


#task3-1
mylist = [2, 11, 12, 45, 52, 808, 7, 68, 91, 1013]
count=0
for i in mylist:
    if i%2==0:
        mylist[count]=i//2
    count+=1
print(mylist)

#task3-2
first_names = ["Lisa", "Bob", "Carl", "Mohammed", "Vlad", "Aina"]
last_names = ["Smith", "Zhang", "Karlson", "Lee", "Numan", "Musa"]
x=0
while x<len(first_names):
    print(first_names[x]+" "+last_names[x])
    x+=1

#task3-3
x=0
y=x+2
while x<len(first_names):
    if(y<len(first_names)):
        print(first_names[y]+" "+last_names[x])
        y+=1
    else:
        print(first_names[y-6]+" "+last_names[x])
        y+=1
    x+=1

#task4-1
alist = [4, 5, 88, 32, 99, 88, 73, 68, 91, 1024]
x=0
while x<len(alist):
    while alist[x]%2==0:
        alist[x]=alist[x]//2
    x+=1
print(alist)

#task4-2
pm=int(input("Give me a number:"))
for i in range(2,pm+1):
    c=0
    for j in range(2,i-1):
        if(i%j==0):
            c+=1
    if c==0:
        print(i)