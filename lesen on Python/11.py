import random
random_list = list(random.randint(0, 10) for i in range(10))
result = list(map(lambda x: random_list.count(x) > 1, random_list))
random_list1 = list(set(random_list))
print(random_list)
print(f'количество повторяющихся элиментов {result.count(True)}')
print(f'уникальные элименты {random_list1}')  