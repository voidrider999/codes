from sys import stdin

def one_i_j():
    for i, line in enumerate(stdin):
        row = line.rstrip().split()
        for j, elt in enumerate(row):
            if elt == '1':
                return i, j

i, j = one_i_j()
n = abs(i - 2) + abs(j - 2)
print(n)
