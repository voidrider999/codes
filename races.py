import random

nracers = int(input('Number of racers: '))
names = ['Vlad', 'Nik', 'Sam', 'Johan', 'Pat', 'Drew']
racers = []
used_names = {}
for _ in range(nracers):
    i = random.randint(0, len(names) - 1)
    name = names[i]
    if name not in used_names:
        used_names[name] = 1
    else:
        used_names[name] += 1
        name += str(used_names[name])
    racers.append({'name': name, 'wins': 0})

rounds = int(input('Enter number of rounds: '))
for i in range(rounds):
    print('Round', i + 1)
    winning = random.randint(0, len(racers) - 1)
    winner = racers[winning]
    winner['wins'] += 1
    print(winner['name'], 'wins')
print('*' * 10)
print(racers)
