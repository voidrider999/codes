from sys import stdin

nums = [int(s) for s in stdin.readline().split('+')]
nums.sort()
nums = [str(n) for n in nums]
print('+'.join(nums))
