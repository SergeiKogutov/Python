import model
import view

def select(number):
    if number == 1:
        new_name = input("Введите имя и фамилию контакта:")
        new_nomer = input("Введите номер контакта (без пробелов):")
        print(model.new_item(new_name, new_nomer))
    elif number == 2:
        print(view.print_print_spravochnick(model.print_spravochnick()))
    elif number == 3:
        item_name = input("Введите имя или фамилию контакта:")
        print(view.print_item_search(model.item_search(item_name)))