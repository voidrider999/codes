a = [12, 43, 51]
a.append(16)
print(a) # [12, 43, 51, 16]
a.clear()
print(a) # []
a = [1, 2, 3]
b = a.copy()
print(b) # [1, 2, 3]
b = a[:]
print(b) # [1, 2, 3]
b.append(12)
b.append(12)
print(b) # [1, 2, 3, 12, 12]
print(b.count(12)) # 2
print(b.index(12, 3)) # 3
print(b.index(12, 3, 5)) # 3
c = 12 in b[3:5]
print(c) # True
b.insert(0, 1)
print(b) # [1, 1, 2, 3, 12, 12]
print(b.pop()) # 12
print(b.pop(3)) # 3
b.remove(12)
print(b) # [1, 1, 2]
b.reverse()
print(b) # [2, 1, 1]
