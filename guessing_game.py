import random

secret = random.randint(1, 100)
print('Отгадай число от 1 до 100')
while True:
    s = input('Введите число: ')
    if len(s) == 0:
        break
    num = int(s)
    if num == secret:
        print('Вы угадали')
        break
    if secret > num:
        print('Загаданное число больше')
    if secret < num:
        print('Загаданное число меньше') 