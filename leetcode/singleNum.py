class Solution:
    def singleNumber(self, nums) -> int:
        out=0
        for i in range(len(nums)):
            out  ^= nums[i]
        return out

if __name__ == "__main__":
    s= Solution()
    out = s.singleNumber([4,1,2,1,2])
    print(out)