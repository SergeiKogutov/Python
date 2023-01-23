import random
random_list = list(random.randint(0, 11) for i in range(10))
print(random_list)
Arr = [random_list[0]]
for i in random_list:
    if i > max(Arr):
        Arr.append(i)
print(Arr)