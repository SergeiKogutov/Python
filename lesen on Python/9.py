import random
random_list = list(random.randint(0, 11) for i in range(10))
print(random_list)
random_list = list(filter(lambda x: x > 5, random_list))
print(random_list)