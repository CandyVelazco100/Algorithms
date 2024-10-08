Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
    
            anagrams[key].append(s)
        return list(anagrams.values())
        
