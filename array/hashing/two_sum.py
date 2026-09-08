nums = [1,2,4,6]
target = 10

def two_sum(target, nums):
    seen = {}

    for i in range(len(nums)):
        current = nums[i]
        needed = target - current

        if needed in seen:
            return[seen[needed], i]

        seen[current] = i   

sum = two_sum(target, nums)

print(sum)