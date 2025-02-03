h = int(input('Высота елки: ')) 
n = 1
spaces = h - 1
for i in range(h):
    print(' ' * spaces + '^' * n)
    n += 2
    spaces -= 1
print(' ' * (h - 2) + '|||')
