grades = [4, 5, 3, 4, 5]
print(grades) # 4, 5, 3, 4, 5
d1 = 26
print(d1) # 26
d2 = 30
print(d2) # 30
july = [30, 40, 27, 24, 25, 35]
print(july) # 30, 40, 27, 24, 25, 35
u = ['a', 320, 45.2, True, [True, False]]
print(u) # 'a', 320, 45.2, True, [True, False] 
b = []
print(type(b)) # <class 'list'>
print(len([1, 2, 3])) # 3
print(len(b)) # 0
print([100, 1000, 10000] + ['a', 'b', 'c']) # 100, 100, 10000,  'a', 'b', 'c'
print([3] in grades) # False
print([2] in grades) # False
w = [4, 20, 100, -20]
print(max(w)) # 100
print(min(w)) # -20
print(sum(w)) # 104
print(sorted(w)) # -20, 4, 20, 100
print(sorted(w, reverse=True)) # 100, 20, 4, -20
print([100, 200] > [34, 400]) # True
print([100, 200] < [101, 400]) # True
print([30, 40] == [30, 40]) # True
print([40, 50] == ['a', 40, 50]) # False 
print(sum(grades)/len(grades)) # 4.2
