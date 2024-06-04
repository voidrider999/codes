ships = {}
while True:
    ship = input('Введите название корабля: ')
    if ship == '':
        break
    if ship not in ships:
        ships[ship] = 1
    else:
        if len(ship) < 6:
            ships[ship] += 1
        else:
            ships[ship] *= 2
print(ships)
