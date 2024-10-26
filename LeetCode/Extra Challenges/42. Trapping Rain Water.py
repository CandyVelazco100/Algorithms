Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        right_max = left_max = water = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
        return water
