from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for i in strs:
            sortedWord = "".join(sorted(i))
            
            if sortedWord not in out:
                out[sortedWord] = [i,]
            else:
                out[sortedWord].append(i)
        result = []
        for j in out.values():
            result.append(j)
        return result
        