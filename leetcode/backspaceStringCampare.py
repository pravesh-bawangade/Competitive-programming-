class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_l = ""
        T_l = ""
        
        for i in S:
            if i != "#":
                S_l = S_l+i
            elif i == "#":
                S_l = S_l[0:-1]
        
        for i in T:
            if i != "#":
                T_l = T_l+i
            elif i == "#":
                T_l = T_l[0:-1]
        
        if S_l == T_l:
            return True
        else:
            return False