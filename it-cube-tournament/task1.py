while True:
    num1 = int(input('Введите трехзначное число: '))
    if num1 >= 100 and num1 <= 999:
        break

num2 = str(num1)
num2 = num2[2] + num2[1] + num2[0]
num2 = int(num2)
print(num1 * num2)
