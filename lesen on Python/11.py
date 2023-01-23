import random
random_list = list(random.randint(0, 10) for i in range(10))
check_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in random_list:
    check_list[random_list[i]]+=1   
print(random_list)       
print(check_list)