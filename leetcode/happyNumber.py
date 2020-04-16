class Solution:
    def isHappy(self, n: int) -> bool:
        def numSquareSum(n): 
            squareSum = 0 
            while(n): 
                squareSum += (n % 10) * (n % 10)
                n = int(n / 10) 
            return squareSum
        
        seen = set()
        while numSquareSum(n) not in seen:
            addition = numSquareSum(n)
            if addition == 1:
                return True
            else:
                seen.add(addition)
                n = addition
        return False
    