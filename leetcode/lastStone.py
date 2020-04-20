from typing import List

def lastStoneWeight(self, stones: List[int]) -> int:
        count = len(stones)
        if count == 1:
            return stones[0]
        elif count == 2:
            return abs(stones[0]-stones[1])
        
        while(count > 1):
            maxi_1 = max(stones)
            stones.remove(maxi_1)
            if len(stones) != 1:
                maxi_2 = max(stones)
            else:
                maxi_2 = stones[0]
            stones.remove(maxi_2)
            new_stone = abs(maxi_1 - maxi_2)
            if (new_stone != 0):
                stones.append(new_stone)
                count -=1
            else:
                count -=2
        if len(stones) == 0:
            return 0
        return stones[0]