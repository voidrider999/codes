from sys import stdin

_, k = [int(s) for s in stdin.readline().split()]
pts = [int(s) for s in stdin.readline().split()]
pts_k = pts[k - 1]
n = 0
for p in pts:
    if p > 0 and p >= pts_k:
        n += 1
print(n)
