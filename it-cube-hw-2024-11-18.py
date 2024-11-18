s = input('Введите строку: ')
print('1.', s[0], s[-1])

print()
print('2.')
for i in range(len(s)):
    if i % 2 == 1:
        print(s[i])
print()

print('3.', s.count('+'))
print('4.', len(s))
print('5.', s[::-1])
print('6.', s[::-2])

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for v in vowels:
    s = s.replace(v, '?')
print('7.', s)
