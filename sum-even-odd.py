nums = []
while True:
    s = input('enter number: ')
    if s == '':
        break
    if s.isdigit():
        nums.append(int(s))
    else:
        if s[0] == '-' and s[1:].isdigit():
            nums.append(int(s))
        else:
            print('not a number!')
print(nums)

sum_odd = 0
sum_even = 0
for num in nums:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print('even', sum_even)
print('odd', sum_odd)


