You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
  
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        R, C = len(matrix), len(matrix[0])
        low, high = 0, R * C - 1

        while low <= high:
            mid = (low + high) // 2
            r, c = mid // C, mid % C

            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
