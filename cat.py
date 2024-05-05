import sys

if len(sys.argv) != 2:
    exit(0)

f = open(sys.argv[1])
print(f.read())