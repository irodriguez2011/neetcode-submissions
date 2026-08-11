class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    # m is the number of valid elements in num2
    #and we know n elements that are equal to 0 are are placeholders for the numners in nums2
    # we need one pointer that points to the largest element in nums1
    # m-1 represent the largest valid number in nums1
    # [10,20,20,40,0,0]

        last_valid = m - 1  # 3 - the last valid elment in nums1
        current = m + n - 1 # 5 - points to current position we are filling
        nums2_index = n - 1 # 2 - starts at last index of nums2
   
    # in nums1

        while nums2_index >= 0:
            if last_valid >= 0 and nums1[last_valid] > nums2[nums2_index]:
                nums1[current] = nums1[last_valid]
                last_valid -= 1
            else:
                nums1[current] = nums2[nums2_index]
                nums2_index -= 1
            
            current -= 1




        