num = input('Введите номер телефона: ')
if len(num) != 12 or num[0] != '+' or num[1] != '7':
    print(False)
    exit()
print(num[2:].isdigit())
