class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need to go through list and find complement of target
        #as i lopp add the difference  to the map if its not there
        # if complement is already there return list

        ans = []
        map = {}

        for n in range(len(nums)):
          diff = target - nums[n]
          if diff not in map:
            map[nums[n]] = n
          else:
             return [map[diff], n]
  
