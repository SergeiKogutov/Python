# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
from random import uniform

n = int(input('Введите размер списка: '))
list = []
for i in range(n):
    f = uniform(0, 9)
    list.append(round(f, 2))

minimum = list[0]
maximum = 0
for i in range(len(list)):
    
    if maximum < list[i]:
        maximum = list[i]
    if minimum > list[i]:
        minimum = list[i]
x = (maximum - int(maximum)) - (minimum - int(minimum))

print(list)
print(maximum, minimum)
print(round(x,2))