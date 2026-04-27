class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // var count that will
        // [1,2,3,1,2,3]

        //let count = 0
        let sortedArr = nums.sort()

        for (let i = 0; i < sortedArr.length; i++){
             console.log(nums[i],nums[i+1])
            if (nums[i] == nums[i+1]) {
                //count++
                return true
            }
        } 
    return false;
    }
}
