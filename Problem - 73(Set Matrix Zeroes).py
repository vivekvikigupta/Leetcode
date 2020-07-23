class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        if r == 0 or c == 0:
            return
        f_row_zero = False
        f_col_zero = False
        for i in range(r):
            if matrix[i][0] == 0:
                f_col_zero = True
                break
        for j in range(c):
            if matrix[0][j] == 0:
                f_row_zero = True
                break
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if f_row_zero:
            for j in range(c):
                matrix[0][j] = 0
        if f_col_zero:
            for i in range(r):
                matrix[i][0] = 0
