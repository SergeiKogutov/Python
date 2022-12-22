import random
import time

ege = input("введите ваш возрост: ")
name = input("введите ваше имя и фамилию: ")

if int(ege) < 18:
    print(f"Уважаемый {name} в доступе отказано по причине не соответсвия требованиям возраста!")
    print("игра закроется через 5 секунд...")
    time.sleep(5)
elif int(ege) >= 18:
    print(f"Уважаемый {name} доступ разрешён!")

    random_number = random.randint(1, 5)
    user_number = 0

    while int(user_number) != random_number:

        user_number = input("угадай число (от 1 до 5): ")

        if int(user_number) == random_number:
            print("вы угадали!")
            print(f"да это было число {random_number}")
            print("игра закроется через 5 секунд...")


        else:
            print("Вы не угадали :(")

print("хорошего дня...")

time.sleep(5)