a = [34, 54, 2]
print(a[0])
print(a[2])
b = [100, 40, 61, 0]
print(b[-1])
print(b[0:2])
print(b[2:-1])
print(b[1:1000])
print(b[0:])
print(b[0:3])
print(b[:])
print(b[::2])
print(b[0:3:2])
print(b[::-1])
b[2] = 45
print(b[2])
b[2:5] = 40, 50
print(b)
a = [123, 1, 3]
d = a # A в данном случае сыллка.
d[1] = 100
print(d)
print(a)
a = [1, 2, 3]
d = a[:] # Чтобы A не менялось.
d[1] = 100
print(d)
print(a)


