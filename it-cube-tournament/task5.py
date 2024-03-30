line = input('Введите строку: ')
counters = {}
for c in line:
    if c in counters:
        counters[c] += 1
    else:
        counters[c] = 1

letters = sorted(counters.keys())
for c in letters:
    print(c, counters[c])
