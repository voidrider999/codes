s = input('Введите слово: ')
res = ''
for i in range(len(s) // 2):
    j = -(i + 1)
    pair = s[i] + s[j]
    res += pair
if len(s) % 2 == 1:
    mid = s[len(s) // 2]
    res += mid
print(res)
