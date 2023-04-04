n = int(input())
players = {}
for i in range(n):
    name = input()
    if name in players:
        print(players[name])
    else:
        print("not set")
        name = input()
        size = input()
        players[name] = size
print(players)
