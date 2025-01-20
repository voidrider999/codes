import random
l = []
n = random.randint(3, 7)
for i in range(n):
    g = random.randint(1, 100)
    l.append(g)
print('Список:', l)
print(len(l))
print(l[-1])
print(l[::-1])
if 17 in l and 5 in l:
    print('YES')
else:
    print('NO')
print(l[1:-1])
