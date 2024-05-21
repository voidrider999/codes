import random

nums = []
for _ in range(10):
    nums += [random.randint(1, 100)]

print(nums)
remaining = []
removed = []
for num in nums:
    if num > 35 and num < 65:
        removed += [num]
    else:
        remaining += [num]
print(remaining)
print(removed)        