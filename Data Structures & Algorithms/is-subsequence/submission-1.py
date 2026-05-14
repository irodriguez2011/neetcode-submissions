class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #while iterating on s i need to check 
        #characters in t
        #one pointer on s and another pointer on t
        # s = node
        # t = neetcode

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return i == len(s)
            
        