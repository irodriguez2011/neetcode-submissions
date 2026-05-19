class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
     #Faster execution time

        s = s.rstrip()
        i = len(s) -1
        word_length = 0

        while i >= 0 and not s[i].isspace():
            word_length +=1
            i -= 1

        return word_length
