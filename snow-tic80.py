# script:  python

from math import floor
from random import uniform, randint, choice

FLAKES_NUM = 1000
flakes = []
for i in range(FLAKES_NUM):
    xdir = choice([1, -1])
    swing = randint(2, 4)
    flake = {
        'xbase': i / FLAKES_NUM * 240,
        'y': randint(0, 135),
        'vy': uniform(10, 15), # pix/sec
        'swing': swing,
        'vx': xdir * uniform(5, 10), # pix/sec
        'xloc': uniform(-swing, swing),
    }
    flakes.append(flake)

frames = 0

def TIC():
    global frames

    frames += 1
    cls(13)
    dt = 1/60
    for flake in flakes:
        dist_y = dt * flake['vy']
        flake['y'] += dist_y
        if flake['y'] >= 136:
            flake['y'] -= 136 

        dist_x = dt * flake['vx']
        flake['xloc'] += dist_x
        swing = flake['swing']
        if flake['xloc'] >= swing or flake['xloc'] <= -swing:
            flake['vx'] = -flake['vx']
        xglob = flake['xbase'] + flake['xloc']

        pix(floor(xglob), floor(flake['y']), 12)

    if frames % 5 != 0:
        return 
        
    vbank(1)
    x = randint(0, 239)
    y = 135
    while pix(x, y) == 12:
        y -= 1
        if y == 0:
            break
    tri(x, y, x - 16, y + 8, x + 16, y + 8, 12)
    vbank(0)

# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
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

