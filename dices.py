import random

names = ['Vlad', 'Nikita', 'Sam', 'Johan', 'Ann']
numplayers = int(input('Введите число игроков: '))
players = []
used_names = {}
for _ in range(numplayers):
    i = random.randint(0, len(names) - 1)
    name = names[i]
    if name in used_names:
        used_names[name] += 1
        name += str(used_names[name])
    else:
        used_names[name] = 1
    player = [name, 0]
    players.append(player)

rounds = int(input('Введите число раундов: '))
for _ in range(rounds):
    winner = random.randint(0, len(players) - 1)
        player[1] += 1
    print(player[0], 'wins')
    
