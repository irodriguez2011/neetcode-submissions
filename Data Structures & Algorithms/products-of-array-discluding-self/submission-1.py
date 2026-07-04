class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums = [1,2,4,6]
        #left = [1,1,1,1]
        #right = [1,1,1,1]

        left = [1] * len(nums)
        right = [1] * len(nums)
 
        for i in range(1, len(nums)):

            left[i] = left[i - 1] * nums[i - 1]
        
        # we don't start loop at index 0 because by default left[0] will be 1
        # because there is nothing to left of index 0
        for i in range(len(nums) -  2, -1, -1):
            print(i)
            right[i] = right[i +1] * nums[i +1]

        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = left[i] * right[i]

        return result


        