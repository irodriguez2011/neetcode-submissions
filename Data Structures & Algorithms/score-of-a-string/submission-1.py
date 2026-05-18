class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0

        ascii_values = [ord(char) for char in s]

        for i in range(len(ascii_values) -1 ):
            # print(ascii_values[i +1] )
            increment = abs(ascii_values[i] - (ascii_values[i +1] ))
            score += increment

        return score