import time 

def function1(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j
    return test

T1=0
for i in range (0,5):
   start = time.time()
   function1(50)
   end = time.time()
   T1 += (end-start)
T1=(T1/5)

T2=0
for i in range (0,5):
   start = time.time()
   function1(100)
   end = time.time()
   T2 += (end-start)
T2=(T2/5)

T3=0
for i in range (0,5):
   start = time.time()
   function1(200)
   end = time.time()
   T3 += (end-start)
T3=(T3/5)

T4=0
for i in range (0,5):
   start = time.time()
   function1(300)
   end = time.time()
   T4 += (end-start)
T4=(T4/5)

T5=0
for i in range (0,5):
   start = time.time()
   function1(500)
   end = time.time()
   T5 += (end-start)

import matplotlib.pyplot as plt
x_axis=[50,100,200,300,500]
T=[T1,T2,T3,T4,T5]
plt.plot(x_axis, T, marker='o', linestyle ='--', color='b', label='Square')
plt.ylabel('Average time (seconds)')
plt.xlabel('Iput size (n)')
plt.show()