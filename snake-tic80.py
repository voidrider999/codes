# script:  python
import random

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

snake = [
    {'xc': 14, 'yc': 8},
    {'xc': 15, 'yc': 8},
    {'xc': 16, 'yc': 8},
]
new = {'xc': random.randint(5, 25), 'yc': random.randint(2, 6)}
speed = 4 # cells/sec
direction = RIGHT
dist = 0

def TIC():
    global dist, direction, new, speed

    if btnp(0):
        direction = UP
    elif btnp(1):
        direction = DOWN
    elif btnp(2):
        direction = LEFT
    elif btnp(3):
        direction = RIGHT

    dist += speed * 1/60    
    if dist >= 1:
        dist -= 1
        for i in range(len(snake) - 1):
            cell = snake[i]
            nxt = snake[i + 1]
            cell['xc'] = nxt['xc']
            cell['yc'] = nxt['yc']
        
        head = snake[-1]
        if direction == UP:
            head['yc'] -= 1
        elif direction == DOWN:
            head['yc'] += 1
        elif direction == LEFT:
            head['xc'] -= 1
        elif direction == RIGHT:
            head['xc'] += 1

        if head['xc'] > 29:
            head['xc'] = 0
        elif head['xc'] < 0:
            head['xc'] = 29
        elif head['yc'] > 16:
            head['yc'] = 0
        elif head['yc'] < 0:
            head['yc'] = 16

        for i in range(len(snake) - 1):
            cell = snake[i]
            if head['xc'] == cell['xc'] and head['yc'] == cell['yc']:
                trace(str(head) + ' ' + str(cell))
                speed = 0
                break

        if head['xc'] == new['xc'] and head['yc'] == new['yc']:
            speed *= 1.1
            snake.insert(0, new)
            while True:
                new = {
                    'xc': random.randint(0, 29),
                    'yc': random.randint(0, 16),
                }
                new_is_good = True
                for cell in snake:
                    dist_x = abs(new['xc'] - cell['xc'])
                    dist_y = abs(new['yc'] - cell['yc'])
                    if dist_x <= 3 and dist_y <= dist_y:
                        new_is_good = False
                        break
                if new_is_good:
                    break

    cls(1)
    spr(1, new['xc'] * 8, new['yc'] * 8)
    for cell in snake:
        spr(0, cell['xc'] * 8, cell['yc'] * 8)

# <TILES>
# 000:3333333332222223322222233222222332222223322222233222222333333333
# 001:444444444aaaaaa44aaaaaa44aaaaaa44aaaaaa44aaaaaa44aaaaaa444444444
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

