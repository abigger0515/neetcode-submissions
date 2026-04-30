class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = defaultdict(set)
        for i in range(9):
            # check row
            row = set()
            for r in range(9):
                row_val = board[i][r]
                if row_val == ".":
                    continue
                if row_val in row:
                    return False
                row.add(row_val)

            # check col
            col = set()
            for c in range(9):
                col_val = board[c][i]
                if col_val == ".":
                    continue
                if col_val in col:
                    return False
                col.add(col_val)


            # check box
            for j in range(9):
                # print(i//3, j//3)
                # [[0, 0], [0, 1], [0, 2]],
                # [[1, 0], [1, 1], [1, 2]],
                # [[2, 0], [2, 1], []]
                box_val = board[i][j]
                if box_val == ".":
                    continue
                if box_val in box[(i//3, j//3)]:
                    return False
                box[(i//3, j//3)].add(box_val)
        
        return True
        