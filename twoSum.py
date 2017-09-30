#Two Sum

def twoSum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-1):
            if nums[i] + nums[j] == target and i != j:
                return([i, j])

print(twoSum([2,7,11,15],9))