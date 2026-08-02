class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num -1 not in nums_set:
                current_length = 1
                next_num = num + 1

                while next_num in nums_set:
                    current_length += 1
                    next_num += 1

                longest = max(longest, current_length)

        return longest

        