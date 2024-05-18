nums = []
while True:
    s = input('Введите число: ')
    if s == '':
        break
    if s.isdigit():
        nums.append(int(s))
    else:
        if s[0] == '-' and s[1:].isdigit():
            nums.append(int(s))
        else:
            print('Не число!')

res = []
for num in nums:
    if num < 0:
        res += [-1]
    elif num > 0:
        res += [1]
    else:
        res += [0]
print(res)