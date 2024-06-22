player = {'hp': 3, 'x': 5, 'y': 5}
enemies = [{'x': 7, 'y': 5}]
while True:
    print(player)
    move = input('Enter move(up/down/left/right): ')
    if move == 'up':
        player['y'] -= 1
    elif move == 'down':
        player['y'] += 1
    elif move == 'left':
        player['x'] -= 1
    elif move == 'right':
        player['x'] += 1
    else:
        continue
    if player['x'] > 10 or player['y'] < 0 or player['x'] < 0 or player['y'] > 10:
        print('Escaped')
        break
