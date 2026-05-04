class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            #look through the array for the val we want to remove
            #while loops to check that val in the array, continue looping
            #use remove() to remove occurrences
            #Input: nums = [1,1,2,3,4], val = 1
            
            while val in nums:
                 nums.remove(val)
                
            return len(nums)
