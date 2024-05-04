import hashlib

while True:
    fname = input('Введите имя файла: ')
    if len(fname) == 0:
        exit()
    f = open(fname)
    s = f.read()
    f.close()
    
    h = hashlib.sha256()
    h.update(s.encode())
    print(h.hexdigest())
