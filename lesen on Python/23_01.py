import random 
def zd0():
    numbers = list(random.randint(1, 10) for _ in range(random.randint(3, 7)))
    print(numbers)
    set_numbers = list(set(numbers))
    if len(numbers) == len(set_numbers):
        print(f'в списке {numbers} нет повторяющихся элиментов.')
    else:
        print(f'в списке {numbers} есть повторяющиеся элименты.')

def zd1():
    x = str(random.randint(10000, 99999))
    y = str(random.randint(10000, 99999))

    print (x)
    print (y)
    count = 0
    for i in range(0, len(x)):
        if x[i] in y:
            count +=1    
    if len(x) == count and set(x) == set(y):
        print('цифры совпадают')
    else:
        print('цифры несовпадают')

operation = input('введите выражение: ')
print(f'ответ = {eval(operation)}')