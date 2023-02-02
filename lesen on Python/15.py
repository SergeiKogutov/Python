import numpy as np
import random
arr = [[random.randint(10, 50) for _ in range (1, 5)], [random.randint(10, 50) for _ in range (1, 5)],\
       [random.randint(10, 50) for _ in range (1, 5)], [random.randint(10, 50) for _ in range (1, 5)]]
b = np.asarray(arr)
for i in arr:
    print(i)
res = []
for i in arr:
    if sum(i) > np.trace(b):
        res.append(i)

print(f'сумма элиментов в строках {res} превосходит сумму элиментов диагонали {np.diagonal(b)} = {np.trace(b)}')
