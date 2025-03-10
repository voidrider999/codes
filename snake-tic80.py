# script:  python

snake = [
    {'xc': 14, 'yc': 8},
    {'xc': 15, 'yc': 8},
    {'xc': 16, 'yc': 8},
]
speed = 4 # cells/sec
dist = 0

def TIC():
    global dist

    dist += speed * 1/60    
    if dist >= 1:
        dist -= 1
        for i in range(len(snake) - 1):
            cell = snake[i]
            nxt = snake[i + 1]
            cell['xc'] = nxt['xc']
            cell['yc'] = nxt['yc']
        
        head = snake[-1]
        head['xc'] += 1

    cls(1)
    for cell in snake:
        spr(0, cell['xc'] * 8, cell['yc'] * 8)

# <TILES>
# 000:3333333332222223322222233222222332222223322222233222222333333333
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

