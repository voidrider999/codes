import random

nums = []
for _ in range(10):
    nums.append(random.randint(-5, 5))
print(nums)

min_num = nums[0]
for num in nums:
    if num < min_num:
        min_num = num
print(min_num)
