840. Magic Squares In Grid
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals 
all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(grid, i, j):
            s = "".join(str(grid[i + dx][j + dy]) for dx, dy in [(0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)])
            return grid[i][j] % 2 == grid[i+2][j+2] % 2 == 0 and (s in '4381672943816729' or s in '9276183492761834')

        return sum(is_magic(grid, i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if len({grid[i+dx][j+dy] for dx in range(3) for dy in range(3)}) == 9)
