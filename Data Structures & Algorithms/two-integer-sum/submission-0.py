class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need to go through list and add each value togther to see if it
        #equal the target
        #while im one index .. loop through the other index and add
        #to see if it matches the target
        ans = []
        prev_map = {}

        
        for n in range(len(nums)):
          diff = target - nums[n]
          if diff not in prev_map:
            print('diff', diff)
            prev_map[nums[n]] = n
            print('prevmap', prev_map)
          else:
             return [prev_map[diff], n]
  
