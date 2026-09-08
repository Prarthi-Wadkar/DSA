nums = [1, 2, 3, 4, 5, 4]

def duplicate_nums(nums):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
num = duplicate_nums(nums)
print(num)
