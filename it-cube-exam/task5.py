import random

nums = []
for _ in range(10):
    nums += [random.randint(1, 10)]
print(nums)
boundary = int(input('Пороговое значение: '))

res = []
for num in nums:
    if num < boundary:
        res += [boundary]
    else:
        res += [num]
print(res)