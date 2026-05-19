class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = -1

        while i >= -len(s) and s[i].isspace():
            i -= 1

        end = i
        print(f'end: {end}')
        while i >= -len(s) and not s[i].isspace():
             i -= 1
        print(f'end - i: {end} - {i}')
        return end - i