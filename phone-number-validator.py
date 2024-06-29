number = input('Enter phone number: ')
if len(number) != 12:
    print(False)
    exit()
if number[0] != '+':
    print(False)
    exit()
if number[1] != '7':
    print(False)
    exit()
if not number[2:].isdigit():
    print(False)
    exit()
print(True)
