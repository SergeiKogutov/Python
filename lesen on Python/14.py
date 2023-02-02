# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

arr = [[random.randint(1, 5) for _ in range (random.randint(20, 30))], [random.randint(1, 5) for _ in range (random.randint(20, 30))],\
       [random.randint(1, 5) for _ in range (random.randint(20, 30))] ,[random.randint(1, 5) for _ in range (random.randint(20, 30))]]
res = []
for i in arr:
    print(i, end=' ')
    print(f' Среднее арифметическое = {mean(i).__round__(1)}')
    res.append(mean(i).__round__(1))

pos_max = [i for i,x in enumerate(res) if x == max(res)]

print(f'у { pos_max[0] + 1} группы наилучший средний бал {max(res)}')