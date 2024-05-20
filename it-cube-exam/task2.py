nums = []
while True:
    s = input('Введите число: ')
    if s == '':
        break
    if s.isdigit():
        nums += [int(s)]
    else:
        if s[0] == '-' and s[1:].isdigit():
            nums += [int(s)]
        else:
            print('Не число!')

pos = 0
neg = 0
zero = 0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print(pos, neg, zero)
    