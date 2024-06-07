used_names = {}
while True:
    name = input('Введите имя: ')
    if name == '':
        break
    if name not in used_names:
        used_names[name] = 1
    else:
        used_names[name] += 1
        name += str(used_names[name])
    print(name)
print(used_names)

