# import random
# number=random.randint(1,100)
# user_number = None
# while '=' != user_number:
#     print('Ваше число: ',number)
#     user_number = input ('Подскажи пожалуйста символами > , < или = загаданное тобой число: ')

#     if user_number=='>':
#         number+=1
#     elif user_number=='<':
#         number-=1
#     else:
#         print('Удача, мое второе имя!!!')

data = '2 3 4 5 7 8'.split()
print(data)
res = list(map(int, data))
print(res)
res = list(filter(lambda x: not x % 2, res))
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)