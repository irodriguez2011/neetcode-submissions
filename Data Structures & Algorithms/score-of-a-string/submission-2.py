class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0

        # ascii_values = [ord(char) for char in s]

        #O(1) space complexity

        for i in range(len(s) -1 ):
            current_char = ord(s[i])
            next_char = ord(s[i+1])
            
            score += abs(current_char - next_char)

        return score