import random

def zadacha0():
    data = open('random.txt', mode='a', encoding='utf-8')
    for i in range(10):
        number = random.randint(1, 100)
        data.write(str(number) + ', ')
    data.write('\n')
    data.close

def tuple_index_change(index):
    random_tuple=tuple(random.randint(0, 5) for i in range(5))
    print(random_tuple)
    random_list=list(random_tuple)
    random_list[index - 1]=random.randint(100, 999)
    print(random_list)
    random_tuple=tuple(random_list)
    print(random_tuple)

# index = 2
# tuple_index_change(index)

def zadacha_2():
    # Задача 2. Актёров разделили на списки по трём качествам 
    # «умные», «красивые», «сильные». На главную роль нужен 
    # актёр обладающий всеми тремя качествами. Определите, 
    # сколько есть претендентов на главную роль.

    # Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
    # Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
    # Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад
    beauty = 'Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян'
    strong = 'Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад'
    smart = 'Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад'

    beauty = set(beauty.split())
    strong = set(strong.split())
    smart = set(smart.split())

    result = beauty.intersection(smart).intersection(strong)
    print(result)

def zadacha_3():
    random_list = list(random.randint(1, 20) for i in range(10))
    print(random_list)
    random_list = set(random_list)
    print(random_list)
    random_list = list(random_list)
    print(random_list)

def zadacha_4():
    import math
    area_whole = 50 * 30
    area_flowers = 16 * 7 * 4
    fountain = math.pi * 5**2
    area_plate = area_whole - (area_flowers + fountain)
    print(area_plate)
