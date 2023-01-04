def exercise1(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


def exercise2(n):
    return max(n, key=int)


def exercise3(attack, defence):
    defence['health'] -= attack['damage']
    return f'{attack["name"]} атаковал {defence["name"]}. Был нанесён урон - {attack["damage"]}. Осталось здоровья - {defence["health"]}'


def exercise4(attack, defence):
    defence['health'] -= attack['damage'] / defence['armor']
    return f'{attack["name"]} атаковал {defence["name"]}. Был нанесён урон - {attack["damage"] / defence["armor"]}. Осталось здоровья - {defence["health"]}'


print(exercise1('Василий', 21, 'Москва'))

print(exercise2(input().split()))

player = {'name': input('Введите имя игрока '), 'health': 120, 'damage': 40}
enemy = {'name': input('Введите имя злодея '), 'health': 100, 'damage': 50}
print(exercise3(player, enemy))

player = {'name': input('Введите имя игрока '), 'health': 120, 'damage': 40, 'armor': 1.2}
enemy = {'name': input('Введите имя злодея '), 'health': 100, 'damage': 50, 'armor': 1.1}
print(exercise4(enemy, player))