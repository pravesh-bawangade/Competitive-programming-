from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_till = global_max = nums[0]
        for i in nums[1:]:
            total_till = max(i, total_till+i)
            global_max = max(global_max, total_till)
        return global_max
