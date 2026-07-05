class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_counter = {}

        for num in nums:
            if num not in num_counter:
                num_counter[num] = 0
            num_counter[num] += 1

        sorted_nums = sorted(num_counter.items(), key=lambda x:x[1], reverse=True)
        top_k = sorted_nums[:k]

        return [pair[0] for pair in top_k]