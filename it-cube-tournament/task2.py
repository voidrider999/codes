while True:
    num1 = int(input('Введите первое число: '))
    if num1 > 0:
        num2 = int(input('Введите второе число: '))
        if num2 > 0:
            break
    print('Введите положительное число!')

print(num1, '+', num2, '=', num1 + num2)
print(num1, '-', num2, '=', num1 - num2)
print(num1, '*', num2, '=', num1 * num2)
print(num1, '/', num2, '=', num1 / num2)
