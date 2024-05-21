import random

pos = []
neg = []
for _ in range(10):
    num = random.randint(-5, 5)
    print(num)
    if num > 0:
        pos += [num]
    elif num < 0:
        neg += [num]
print(pos)
print(neg)