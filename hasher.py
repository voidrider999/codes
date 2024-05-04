import hashlib

while True:
    s = input('Введите строку: ')
    if len(s) == 0:
        exit(0)
    h = hashlib.sha256()
    h.update(s.encode())
    print(h.hexdigest())