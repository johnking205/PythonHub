#Two Sum
class Solution:
    def twoSum(self, nums, target):
        d = [] * len(nums)
        i = 0
        for num in nums:
            if target - num in d:
                return d.index(target-num), i
            d.append(num)
            i += 1
x = Solution()
print(x.twoSum([3,2,4],6))