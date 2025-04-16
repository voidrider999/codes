# script:  python

from math import pi, sin, cos, floor

a = 0

def TIC():
    global a

    r = 10
    s = 2 * r + 2
    xc = 120
    yc = 70
    xl = xc - s/2
    xr = xc + s/2
    yt = yc - s/2
    yb = yc + s/2
    

    dt = 1/60
    w = pi / 6 * 4
    rot_a = dt * w
    a += rot_a
    x = r * cos(a) + xc
    y = r * sin(a) + yc
    cls(0)
    pix(floor(x), floor(y), 12)
    pix(xc, yc, 12)
    tri(x, y, xl, yb, xl, yt, 1)
    tri(x, y, xl, yt, xr, yt, 2)
    tri(x, y, xr, yt, xr, yb, 3)
    tri(x, y, xr, yb, xl, yb, 4)

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

