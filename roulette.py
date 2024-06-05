import random

names = ['Nik', 'Vlad', 'Sam', 'John', 'Bob', 'Pet']
players = []
num = int(input('Enter number of players: '))
for _ in range(num):
    i = random.randint(0, len(names) - 1)
    name = names[i]
    cash = random.randint(100, 1000)
    player = {'name': name, 'cash': cash}
    players.append(player)
print(players)

rounds = int(input('Enter rounds: '))
bet_types = ['big-small', 'red-black', 'number']
for r in range(rounds):
    print('*' * 20)
    for player in players:
        if player['cash'] <= 0:
            continue

        bet = random.randint(1, player['cash'])
        print(player['name'], 'bets', bet)
        
        num = random.randint(0, 36)
#        print('Roulette gives', num)

#        i = random.randint(0, len(bet_types) - 1)
#        bet_type = bet_types[i]
#        if bet_type == 'big-small':
#            c = random.randint(0, 1)
        
        win = random.randint(0, 1)
        if win == 1:
            player['cash'] += bet
            print(player['name'], 'wins')
        else:
            player['cash'] -= bet 
            print(player['name'], 'loses')
print(players)    
