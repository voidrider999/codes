import sys

if len(sys.argv) != 3:
    print(sys.argv[0], 'SET1 SET2')
    exit(1)

set1, set2 = sys.argv[1:]
if len(set1) != len(set2):
    print('SET1 and SET2 must be of the same length')
    exit(1)

if len(set1) == 0:
    print('SET1 and SET2 must be non-empty')
    exit(1)

for line in sys.stdin:
    line = line.rstrip('\n') 
