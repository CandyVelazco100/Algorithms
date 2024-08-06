1508. Range Sum of Sorted Subarray Sums
You are given the array nums consisting of n positive integers. 
You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. 
Since the answer can be a huge number return it modulo 109 + 7.

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_sums = []

        # Calculate the sum of every contiguous subarray and store it into subarray_sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]  # Add the current element to the sum
                sub_sums.append(current_sum) # Append the current sum to the list
        
        sub_sums.sort()
        mod = 10**9 + 7
        # Compute the sum of the elements from the 'left' to 'right' indices
        # Note: The '-1' adjustment is required because list indices in Python are 0-based
        range_sum = sum(sub_sums[left-1 : right]) % mod

        return range_sum
