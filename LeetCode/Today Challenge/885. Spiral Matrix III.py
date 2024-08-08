885. Spiral Matrix III
You start at the cell (rStart, cStart) of an rows x cols grid facing east. 
The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. 
Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). 
Eventually, we reach all rows * cols spaces of the grid.
  
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        ans = [[rStart, cStart]]
        i = 0

        while len(ans) < rows * cols:
            for _ in range(i // 2 + 1):
                rStart += dy[i % 4]
                cStart += dx[i % 4]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            i += 1  # Esto debe estar dentro del bucle while
        
        return ans
