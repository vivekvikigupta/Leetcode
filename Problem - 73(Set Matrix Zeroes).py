class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # space complexity of solution is O(no._of_colums)
        r = len(matrix)
        c = len(matrix[0])
        col_zero = [False] * c
        # going through every element of matrix and storing the boolean values in col_zero list
        for row in range(r):
            for col in range(c):
                if matrix[row][col] == 0:
                    col_zero[col] = True

        for row in range(r):
            # after starting of a row we consider that it does not contain any zero
            contains_zero = False
            for col in range(c):
                if matrix[row][col] == 0:  # if contains zero we mark the row and break
                    contains_zero = True
                    break
            for col in range(c):  # again restarting to visit each element of that row
                if contains_zero or col_zero[col]:
                    matrix[row][col] = 0


