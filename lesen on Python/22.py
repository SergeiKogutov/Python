import random
import matplotlib.pyplot as plt
apartments = list(random.randint(100,300) for _ in range(15))
prices = list(random.randint(3000000,20000000) for _ in range(15))
price_per_square_meter = []
for i in range(15):
    res = ((prices[i]/apartments[i])/1000).__round__()
    price_per_square_meter.append(res)

print(apartments)
print(prices)
print(price_per_square_meter)
result =[]
for i in range(15):
    if price_per_square_meter[i] <= 50:
        result.append(f'дом {apartments[i]}кв/м, стоимость кв/м {price_per_square_meter[i]} тысяч руб. ')
result = list(set(result))
for i in result:
    print(i)

x = apartments
y = price_per_square_meter

fig, ax = plt.subplots()
ax.bar(x, y, color = 'red')

fig.set_facecolor('floralwhite')
ax.set_facecolor('seashell')

plt.show()