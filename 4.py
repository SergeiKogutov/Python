import random
number=random.randint(1,100)
user_number = None
while '=' != user_number:
    print('Ваше число: ',number)
    user_number = input ('Подскажи пожалуйста символами > , < или = загаданное тобой число: ')

    if user_number=='>':
        number+=1
    elif user_number=='<':
        number-=1
    else:
        print('Удача, мое второе имя!!!')