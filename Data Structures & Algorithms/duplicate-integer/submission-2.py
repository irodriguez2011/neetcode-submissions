class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_items = set()

        for n in nums:
            if n not in unique_items:
                unique_items.add(n)
            else:
                return True
        return False