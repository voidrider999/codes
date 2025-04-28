import sys

sys.stdin.readline()
for line in sys.stdin:
    word = line.rstrip()
    #print(line)
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)
