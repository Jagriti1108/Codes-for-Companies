import numpy as np

x = int(input())
lst = []
for i in range(x):
    array = list(map(int, input().split()))
    arrayele = list(map(int, input().split()))

    q = (len(arrayele))
    s=0
    for j in range(q):
        for p in range(j+1 , q):
            # print(arrayele[j], arrayele[p], array[1])
            if (arrayele[j] + arrayele[p] == array[1]):
                s=s+1
    if(s>0):
        lst.append('YES')
    else:
        lst.append('NO')

print(*lst, sep ="\n")
