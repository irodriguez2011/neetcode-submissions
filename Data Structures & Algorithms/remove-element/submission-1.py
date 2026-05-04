class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            #look through the array for the val we want to remove
            #while loops to check that val in the array, continue looping
            #use remove() to remove occurrences
            #Input: nums = [1,1,2,3,4], val = 1
            
            # while val in nums:
            #      nums.remove(val)
                
            # return len(nums)
            # i iterates through list and checks for val
            #Input: nums = [1,1,2,3,4], val = 1
            # nums = [0,1,2,2,3,0,4,2], val = 2
            #[0,1,3]
            k = 0
            for i in range(len(nums)):
                if nums[i]!= val:
                    nums[k] = nums[i]
                    print(nums)
                    k +=1

            return k



