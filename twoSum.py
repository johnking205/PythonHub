#Two Sum problem from LeetCode
class Solution:
    def twoSum(self, nums, target):
        """
        Create an empty list of the same length as the input
        This prevents false match if input list item is half the target
        """
        d = [] * len(nums)
        i = 0 #keeps track of the index for the current list item

        """
        For each list item in the input list, check if target minus
        said list item is equal to one of the stored numbers in d.
        In other words, check if current list item plus any of the
        previous list items (stored in d) equals the target. d is a 
        list that will store all of the input list members that 
        have already been checked. 
        """
        for num in nums:
            if target - num in d:
                return d.index(target-num), i
            d.append(num)
            i += 1
x = Solution()
print(x.twoSum([3,2,4],6))