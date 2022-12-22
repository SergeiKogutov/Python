
while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    operation = input("Что сделать? (+, -, *, /): ")
    resolt = 0

    if operation == "-":
        resolt = a - b

    elif operation == "+":
        resolt = a + b

    elif operation == "*":
        resolt = a * b

    elif operation == "/":
        resolt = a / b

    print(f"ответ: {resolt}")
