import math
   
def simplify(pair):
    g = math.gcd(pair[0], pair[1])
    return (pair[0]//g, pair[1]//g)
    
n = int(input("введите наибольший заменатель дроби: "))
t = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        pair = simplify((i, j))
        t.append(pair)
result = list(set(t))
for i in sorted(result, key = lambda x: x[0]/x[1]): 
    print(str(i[0]) + "/" + str(i[1]))