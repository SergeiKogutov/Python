import time
resolt = 0
x = True
while x:
    a = float(input("Введите первое число: "))
    operation = input("Что сделать? (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    
    if operation == "-":
        resolt = a - b

    elif operation == "+":
        resolt = a + b

    elif operation == "*":
        resolt = a * b

    elif operation == "/":
        resolt = a / b

    else:
        print("неварное действие")

    print(f"ответ: {resolt}")

    exit_now = input("вы хотите выйти: ")

    if exit_now == 'да':
        print('Good day')
        x = False
    else:
        print("жду новую задачу.")

print("програма закроется через 5 секунд...")

time.sleep(5)
