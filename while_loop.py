s = input('enter: ')
while len(s) > 0:
    print(len(s), s)
    s = input('enter: ')

while True:
    s = input('enter: ')
    if len(s) == 0:
        break
    print(len(s), s)

num = int(input('Введите число: '))
while num < 100:
    print(num)
    num = int(input('Введите число: '))