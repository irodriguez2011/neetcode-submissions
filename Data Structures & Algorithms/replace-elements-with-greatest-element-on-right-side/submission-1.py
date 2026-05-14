class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # variable to stay on index that we are replacing
        # another variable as pointer to search for the greatest element

        n = len(arr)

        for i in range(n - 1):
            arr[i] =  max(arr[i+1:])
        arr[-1] = -1
        return arr
                