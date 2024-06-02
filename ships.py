ships = {}
while True:
    ship = input('Введите название корабля: ')
    if ship == '':
        break
    if ship not in ships:
        ships[ship] = 1
    else:
        ships[ship] += 1
print(ships)
