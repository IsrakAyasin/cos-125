quote = "Most of the good programmers do programming "+ \
"not because they expect to get "+ \
"paid or get adulation by the public, "+ \
"but because it is fun to program."
#task1-a
print(quote[12:29])
#task1-b
half=len(quote)//2
print(quote[:half])
#task1-c
print(quote[:-11]+quote[-1])
#task1-d
x=quote.split()
i=0
print(x[::2])

#task1-e
for i in x:
    if i[0] == "p":
        print(i)
    
#task2-a
import random

print(random.randint(0,10))

#task2-b
print(random.choice(x))

#task2-c
random.shuffle(x)
print(x)
