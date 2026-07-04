from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # take each string and compare it with others to see if 
        #they are an anagram
        # for quick lookup a hashmap would be best. 
        # order doesn't matter so maybe we can use a set

        groups = {}

        for word in strs:
            sorted_key = "".join(sorted(word))

            if sorted_key not in groups:
                groups[sorted_key] = []

            groups[sorted_key].append(word)

        return list(groups.values())


        
        