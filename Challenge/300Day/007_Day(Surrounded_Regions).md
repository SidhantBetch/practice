# Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

### Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

<img width="773" height="333" alt="image" src="https://github.com/user-attachments/assets/5c073c91-4b2a-48b5-a3a1-734b4f6ffc57" />


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

### Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

## Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def solve(self, board):

        row = len(board)
        col = len(board[0])

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            
            if board[r][c] != "O":
                return

            board[r][c] = "S"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)

        for j in range(col):
            dfs(0,j)
            dfs(row-1,j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                elif board[i][j] == "S":
                    board[i][j] = "O"
```
