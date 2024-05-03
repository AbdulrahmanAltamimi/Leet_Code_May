from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for num in range(len(nums)):
            if len(nums)<2:
                return -1
            large = nums[-1]

            for i in range(len(nums)-1):
                if nums[i] == large*-1:
                    return large
            nums = nums[:-1]

 



print(Solution().findMaxK([-10,8,6,7,-2,-7]))
