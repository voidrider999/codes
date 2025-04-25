# script:  python

from math import pi, sin, cos

R = 10
S = 2 * R + 2

def draw_pyramid(xl, yt, a):
    xr = xl + S
    yb = yt + S
    xc = xl + S/2
    yc = yt + S/2
    x = R * cos(a) + xc
    y = R * sin(a) + yc

    tri(x, y, xl, yb, xl, yt, 1)
    tri(x, y, xl, yt, xr, yt, 2)
    tri(x, y, xr, yt, xr, yb, 3)
    tri(x, y, xr, yb, xl, yb, 4)
    pix(int(x), int(y), 12)
    #pix(int(xc), int(yc), 12)

def TIC():
    t = time() / 1000
    cls(0)
    for y in range(0, 136, S + 1):
        for x in range(0, 240, S + 1):
            w = (x + 5) * (y + 5) / 1000 + 1 # rad/s
            a = w * t
            draw_pyramid(x, y, a)

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

