import random 

# random_list = list(random.randint(1, 101) for i in range(15))
# print(random_list)
# random_list = list(filter(lambda x: not x % 5, random_list))
# print(random_list)

y = 2345
# x = y
# res = []
# while(x > 0):
#     res.append(x%10)
#     x //= 10
# res = list(map(lambda x: x + 10, res))
# print(y)
# print(res)

# num = 9876487382
# result = list(int(el)+10 for el in str(num))
# print(result)

# Задача 3. Имеется информация о том, телефонами каких 
# компаний сейчас торгуют магазины. Определите те компании, 
# чьи телефоны присутствуют в каждом магазине.


data = open('phone.txt', mode='r', encoding='utf-8')
list_ = data.readlines()
data.close()

set1 = set(list_[1].split(', '))
set2 = set(list_[3].split(', '))
set3 = set(list_[5].split(', '))

print(set1.intersection(set2).intersection(set3))

def zadacha0():
    def mult(num):
        return num % 5 == 0

    fun = lambda num: num % 5 == 0
    # Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
    # Заполните список случайным образом числами от 1 до 100.

    length = 15
    numbers = list(random.randint(1,100) for _ in range(length))
    print(numbers)
    for el in numbers:
        if mult(el):
            print(el, end = ' ')
    print()

    result = filter(lambda num: num % 5 == 0, numbers)
    print(result) 
    result = list(result)
    print(result)

def zadacha3():
    # Задача 3. Имеется информация о том, телефонами каких компаний сейчас торгуют магазины. 
    # Определите те компании, чьи телефоны присутствуют в каждом магазине.

    data = open('phones.txt', mode = 'r', encoding='utf-8')
    phones = data.readlines()
    data.close()

    shop_f = set(phones[1].replace('\n', '').split(', '))
    shop_s = set(phones[3].removesuffix('\n').split(', '))
    shop_t = set(phones[5].removesuffix('\n').split(', '))
    print(shop_f)
    print(shop_s)
    print(shop_t)
    
    result = shop_f.intersection(shop_s).intersection(shop_t)
    print(result)

def bin_convertor(number):
    result = ''
    while number > 0:
        digit = number % 2
        result = str(digit) + result
        number //= 2
    return result

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

enum_alphabet = enumerate(alphabet)
enum_alphabet = list(enum_alphabet)

alphabet_dictionary = {}

for count, letter in enum_alphabet:
    bin_num = bin_convertor(count)
    code = '0' * (6 - len(bin_num)) + str(bin_num)
    alphabet_dictionary[code] = letter
print(alphabet_dictionary)

data = open('animals.txt')
animals_bin = data.readlines()
data.close()

for animal in animals_bin:
    animal = animal.removesuffix('\n')
    #print(animal)
    for index in range(0, len(animal), 6):
        code = animal[index:index+6]
        print(alphabet_dictionary[code], end = '')
    print()