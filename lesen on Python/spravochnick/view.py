
def create_menu():
    print('1. Новая запись')
    print('2. Вывести весь список')
    print('3. Найти по имени')

def input_number():
    print('Введите пункт меню: ')

def print_print_spravochnick(spravochnick):
    for i in spravochnick: print(i, end='')

def print_item_search(i):
    return f'{i}'