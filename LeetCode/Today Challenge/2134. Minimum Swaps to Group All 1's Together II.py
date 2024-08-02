2134. Minimum Swaps to Group All 1's Together II
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_ones = nums.count(1)
        count_numbers = len(nums)
        prefix_sum = ((count_numbers << 1) + 1) * [0]

        for i in range((count_numbers << 1)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i % count_numbers]
            max_ones_found = 0

            end_index = i + count_ones - 1
            if end_index < (count_numbers << 1):
                max_ones_found = max(max_ones_found, prefix_sum[end_index + 1] - prefix_sum[i])
      
        return count_ones - max_ones_found

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCount = nums.count(1)

        nums = nums + nums

        maxOnesInWindow = 0
        currentOnesInWindow = 0

        for i in range(len(nums)):
            if i >= oneCount:
                currentOnesInWindow -= nums[i - oneCount]
            currentOnesInWindow += nums[i]
            maxOnesInWindow = max(maxOnesInWindow, currentOnesInWindow)
        
        minSwap = oneCount - maxOnesInWindow
        return minSwap
