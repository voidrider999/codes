import random
print(random.randint(0, 10000), 'Людей следят за игрой')
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
    print('*' * 20)
    for player in players:
        print('===', 'Игрок:', player[0], 'Побед:', player[1], '===')
        number = random.randint(1, 3)
        print('Шарик в наперстке:', number)
        pnumber = random.randint(1, 3)
        print('Выбор игрока:', pnumber)
        if pnumber == number:
            player[1] += 1
            print(player[0], 'выиграл')
        else:
            print(player[0], 'проиграл')
print('+' * 20)
for player in players: 
    print(player[0],':',player[1])     
print(random.randint(0, 9999), 'Досмотрели до конца')
