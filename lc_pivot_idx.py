from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        else:
            for i in range(len(nums)):
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
                elif i == len(nums) - 1:
                    return -1