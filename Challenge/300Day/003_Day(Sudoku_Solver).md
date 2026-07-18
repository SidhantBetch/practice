# Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

### Example 1:

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/e0e09bc6-da62-4c3b-b133-a6ae7a1f9c64" />


    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/e1d00460-5e8d-4902-9852-8a6841ccc0f5" /> 

## Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.

----------------------------------------------------------------------------------------------

# Solution
```Python
class Solution:
    def solveSudoku(self, board):

        def possible(row, col, num):

            # row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # 3x3 box
            sr = row - row % 3
            sc = col - col % 3

            for i in range(sr, sr+3):
                for j in range(sc, sc+3):
                    if board[i][j] == num:
                        return False

            return True


        def solve():

            min_options = 10
            target = None
            choices = None

            # Find cell with minimum choices
            for i in range(9):
                for j in range(9):

                    if board[i][j] == ".":

                        possible_nums = []

                        for num in "123456789":
                            if possible(i, j, num):
                                possible_nums.append(num)

                        if len(possible_nums) == 0:
                            return False

                        if len(possible_nums) < min_options:
                            min_options = len(possible_nums)
                            target = (i, j)
                            choices = possible_nums


            # Sudoku completed
            if target is None:
                return True


            row, col = target

            # Try choices
            for num in choices:

                board[row][col] = num

                if solve():
                    return True

                # backtrack
                board[row][col] = "."

            return False


        solve()
```
