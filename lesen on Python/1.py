def zadacha():
    n = int(input("Введите число N: "))
    my_list = []
    for i in range(n + 1):
        my_list.append((-3) ** i)
    return my_list


print(zadacha())
