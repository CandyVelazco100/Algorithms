class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[False] * 9 for _ in range(9)]
        rows = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                if cell_value == ".":
                    continue
                
                num = int(cell_value) - 1
                box_index = (i // 3) * 3 + j // 3

                if cols[i][num] or rows[j][num] or boxes[box_index][num]:
                    return False
                cols[i][num] = True
                rows[j][num] = True
                boxes[box_index][num] = True
        return True
