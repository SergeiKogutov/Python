import random
import datetime

def new_item():
    new_name = input("Введите имя и фамилию контакта:")
    new_nomer = input("Введите номер контакта (без пробелов):")
    data = open('spravochnick.txt', mode = 'a', encoding='utf-8')
    data.write(new_name + " " + new_nomer)
    data.write("\n")
    data.close()


def print_spravochnick():
    data = open('spravochnick.txt', mode = 'r', encoding='utf-8')
    spravochnick = data.readlines()
    data.close()
    for i in spravochnick: print(i, end='')

def item_search():
    item_name = input("Введите имя или фамилию контакта:")
    data = open('spravochnick.txt', mode = 'r', encoding='utf-8')
    spravochnick = data.readlines()
    data.close()
    for i in spravochnick:
        if item_name.lower() in i.lower(): print(i, end='')
