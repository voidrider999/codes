a = [12, 43, 51]
a.append(16) # 12, 43, 51, 16
print(a)
a.clear()
print(a)
a = [1, 2, 3]
b = a.copy() # 1, 2, 3
print(b)
b = a[:] # 1, 2, 3
print(b)
b.append(12) # 1, 2, 3, 12
b.append(12) # 1, 2, 3, 12, 12
print(b)
print(b.count(12)) # 2
print(b.index(12, 3)) # 3, первый параметр - что искать, второй - с какого индекса искать
print(b.index(12, 3, 5)) # 3, третий параметр - каким индексом закончить поиск
c = 12 in b[3:5]
print(c) # True
c = b.insert(0,1)
print(c) # None
print(b.pop()) # 12
print(b.pop(3)) # 3
print(b.remove(12)) # 1, 2, 3
print(b.reverse()) # 3, 2, 1
