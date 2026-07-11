class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for num, count in count.items():
            if count > target:
                return num