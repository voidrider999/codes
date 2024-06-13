import random
names = ['Vlad', 'Nik', 'Sam', 'Johan']
numplayers = int(input('Число игроков: '))
players = []
for _ in range(numplayers):
    i = random.randint(0, len(names) - 1)
    name = names[i]
    player = [name, 0]
    players.append(player)

rounds = int(input('Число раундов: '))
for _ in range(rounds):
    for player in players:
        print(player)
        number = random.randint(0, 3)
        pnumber = random.randint(0, 3)
        if pnumber == number:
            player[1] += 1
        else:
            print(player[0], 'проиграл')
print(player[0], 'победил')
print(player)   
