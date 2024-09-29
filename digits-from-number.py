x = int(input('Enter positive number: '))
digits = []
while x > 0:
    digits.append(x % 10)
    x //= 10
digits.reverse()
print(digits)
