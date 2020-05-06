from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = {0:1}
        n = len(nums)
        count = 0
        s = 0
        for num in nums:
            s += num
            if s-k in sum:
                count += sum[s-k]
            if s in sum:
                sum[s]+=1
            else:
                sum[s] = 1
        return count