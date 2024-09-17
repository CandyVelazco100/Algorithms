Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
  
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        count_list = sorted(counts.items(), key=lambda x:x[1],reverse = True)
        sorted_list = dict(count_list[:k])
        return [num for num in sorted_list]
