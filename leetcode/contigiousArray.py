from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        subarray, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count += -1
            if count == 0:
                subarray = i+1
            if count in dic:
                subarray=max(subarray, i-dic[count])
            else:
                dic[count]=i
        return subarray
        
            
        