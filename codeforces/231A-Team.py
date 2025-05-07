from sys import stdin

stdin.readline()
n = 0
for line in stdin:
    line = line.rstrip()
    digits = line.split()
    ones = digits.count('1')
    if ones >= 2:
        n += 1
print(n)
