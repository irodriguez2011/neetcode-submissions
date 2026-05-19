class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # iterate through both nums1 and num2
        # as im checking nums1, dont move pointed until i scanned nums2
        # if i found the index of matching int in nums, add it to list

        mapping = []
        i = 0
        j = 0

        # for i, num in enumerate(nums2):
           
        while i < len(nums1) and j < len(nums2):
            print(f'nums2: {nums2[j]},{j}, nums1: {nums1[i]},{i}')
            if nums2[j] != nums1[i]:
                j += 1
            
            else:
                mapping.append(j)
                i += 1
                j = 0
        
        return mapping

