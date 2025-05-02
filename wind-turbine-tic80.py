# script:  python

from math import cos, sin, pi
import random

SWING = 2 * pi / 3

turbines = []
dx = 0
y0 = 20
h0 = 20
vh = 0.3
for yc in range(20, 120, 35):
    dy = yc - y0
    dh = dy * vh
    h = h0 + dh
    for xc in range(10, 230, 40):
        w = 10
        xc += dx
        t = {
            'xc': xc,
            'yc': yc,
            'r': 0.7 * h,
            'yb': yc + h,
            'ym': yc + h/2,
            'xl': xc - w/2,
            'xr': xc + w/2,
            'a': random.uniform(0, pi),
        }
        turbines.append(t)
    dx += 10

def draw_turbine(t, rot, color):
    t['a'] += rot
    a, r = t['a'], t['r']
    xc, yc = t['xc'], t['yc']
    xl, xr = t['xl'], t['xr']
    yb, ym = t['yb'], t['ym']
    for i in range(3):
        x = r * cos(a + i * SWING) + xc
        y = r * sin(a + i * SWING) + yc
        line(xc, yc, x, y, color)

    tri(xc, yc, xl, yb, xr, yb, color)
    line(xc, yc, xc, ym, color)

wind = 1
yhor = 35
rsun = 5
xsun = 0
ysun = yhor
vxsun = 5
vysun = 2

def TIC():
    global wind, xsun, ysun

    if btnp(0):
        wind += 1
    if btnp(1):
        wind -= 1
    if wind > 10:
        wind = 10
    if wind < -10:
        wind = -10
    if abs(wind) == 9:
        poke(0x3ffa, random.randint(-1, 1))
    elif abs(wind) == 10:
        poke(0x3ffa, random.randint(-2, 2))
    else:
        poke(0x3ffa, 0)

    va = pi / 3 * wind 
    dt = 1/60
    rot = va * dt

    xsun += vxsun * dt
    if xsun > 480:
        xsun = 0
        ysun = yhor
    rising = 1 if xsun < 120 else -1
    ysun -= rising * vysun * dt

    if ysun > yhor + rsun:
        color_sky = 9
        color_grass = 7
        color_turbine = 13
    else:
        color_sky = 10
        color_grass = 6
        color_turbine = 12

    cls(color_sky)
    circ(int(xsun), int(ysun), rsun, 4)
    rect(0, yhor, 240, 136, color_grass)
    for t in turbines:
        draw_turbine(t, rot, color_turbine)

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

