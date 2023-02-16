import numpy as np
import matplotlib.pyplot as plt

# A = [1743, 1648, 1650, 1622, 1581, 1490]
# B = [743, 648, 711, 780, 805, 846]

def zd0(A):
    delta_A = []
    for i in range(len(A) - 1):
        delta_A.append(A[i+1]-A[i])
    avg_a = sum(delta_A)/len(delta_A)
    last_a = A[-1]
    for i in range(10):
        last_a += avg_a
        A.append(last_a)

# zd0(B)
# zd0(A)

# plt.plot(A)
# plt.plot(B)
# plt.show()
def zd1():
    a = [4, 6, 10, 4, 2, 8, 10, 7, 1, 5]
    b = [3, 3, 10, 5, 10, 10, 4, 3, 6, 1]
    c = [2, 2, 1, 1, 3, 7, 9, 9, 2, 8]
    def invers(arr):
        for i in range(len(arr)):
            arr[i] = arr[i] * -1
    invers(a)
    invers(b)
    invers(c)
    ax = plt.subplot(131, projection='polar')
    plt.plot(a, 'ro')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_ticklabels(['8', '6', '4', '2'])
    bx = plt.subplot(132, projection='polar')
    plt.plot(b, 'bo')
    bx.get_xaxis().set_visible(False)
    bx.get_yaxis().set_ticklabels(['8', '6', '4', '2'])
    cx = plt.subplot(133, projection='polar')
    plt.plot(c, 'go')
    cx.get_xaxis().set_visible(False)
    cx.get_yaxis().set_ticklabels(['8', '6', '4', '2'])
    plt.show()

def zd2():
    # Задача 1. Проверьте, существует ли связь между данными, 
    # приведёнными в таблице.Выполните задание с помощью 
    # графика и библиотеки numpy.
    x = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    y = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    z = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

    matrik = [x, y, z]
    result = np.corrcoef(matrik)
    print(result)
    plt.plot(x, 'g')
    plt.plot(y, 'r')
    plt.plot(z, 'b')
    plt.show()

def zd3():
    numbers = [np.random.randint(1,10) for i in range(5)]
    num_av = np.mean(numbers)
    print(numbers)
    numbers = list(set(numbers))    
    print(num_av)
    x = int(input('введите число: '))
    delta = [np.abs(number - x) for number in numbers]
    min = np.argmin(delta)
    print(numbers[min])

def zd4():
    size = (4, 4)
    numbers = np.random.randint(1, 12, size)
    print(numbers)
    numbers_dict = {}
    for row in numbers:
        for num in row:
            if num in numbers_dict.keys():
                numbers_dict[num] += 1
            else:
                numbers_dict[num] = 1
    print(numbers_dict)


zd4()