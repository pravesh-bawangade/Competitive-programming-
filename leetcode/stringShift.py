from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def leftShift(s):
            s = s[1:]+s[0] 
            return s
        def rightShift(s):
            s = s[-1]+s[0:-1]
            return s
        for i in shift:
            # Direction - left
            if i[0] == 0:
                for i in range(i[1]):
                    s = leftShift(s)
            # Direction - right
            elif i[0] == 1:
                for i in range(i[1]):
                    s = rightShift(s)
        return s

if __name__ == "__main__":
    a = Solution()
    print(a.stringShift(s = "abc",shift=[[0,1],[1,2]]))