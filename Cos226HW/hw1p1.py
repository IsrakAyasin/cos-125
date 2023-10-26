def function2(array1,array2):
    n = len(array1)
    test = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(j+1):
                total+= array1[k]
        if array2[j]==total:
            test+= 1
    return test
print(function2([1, 2, 3],[2, 3, 5]))