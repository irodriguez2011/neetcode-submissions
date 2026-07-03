class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // var count that will

        let count = 0

        for (let i = 0; i < nums.length; i++){ 
            if (nums[i] == nums[i+1]) {
                count++
                return true
            }
        } 
    return false;
    }
}
