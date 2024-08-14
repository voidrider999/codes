import random

N = 3

bombs = random.choices('-B', k=N)
bombs = ''.join(bombs)
print(bombs)
field = '*' * N
print(field)
exit()
while True:
    print(field)
    cell = int(input(f'Выберите ячейку от 1 до {N}:'))
    assert cell >= 1 and cell <= N
