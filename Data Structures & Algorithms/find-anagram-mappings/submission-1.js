class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number[]}
     */
    anagramMappings(nums1, nums2) {

    // create an empty object and this object is going to store the indices of nums2
    // ex: {50: 0, 12:1,32:2,...}
    // loop over nums2 once
    // then we loop over nums1 and check the value of hash[nums[i]
    // this should return index of second object
    // push the value of that hash into an array and return it

    const array = []
    const hash = {}

    for (let i = 0; i <nums2.length;i++){
        hash[nums2[i]] = i
    }

    for(let i=0; i < nums1.length; i++){
        array.push(hash[nums1[i]])
    }

    return array

    }
}
