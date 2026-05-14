class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Input: s = "node", t = "neetcode"
        # need to iterate through s to see if the characters in s
        # are also in t
        # if they are in t, they have to be there disturbing the original positions
        #t 
        #while s is less then t i can stay on s

        i= 0
        j= 0 

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1

        return i == len(s)
            
