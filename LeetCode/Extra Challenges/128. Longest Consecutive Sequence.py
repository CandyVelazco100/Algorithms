Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecs = set()
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        length = 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] - sorted_nums[i] == 1:
                length += 1
            else:
                consecs.add(length)
                length = 1
        consecs.add(length)
        return max(consecs)
