# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

n = int(input('Введите размер списка: '))
list1 = []
list2 = []

for i in range(n):
    list1.append(randint(0, 9))

for i in range(len(list1)):
    while i < len(list1)/2 and n > len(list1)/2:
        n = n - 1
        a = list1[i] * list1[n]
        list2.append(a)
        i += 1

print(list1)
print(list2)