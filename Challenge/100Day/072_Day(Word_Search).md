# Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

### Example 1:

<img width="322" height="242" alt="image" src="https://github.com/user-attachments/assets/5d04544f-b6c2-4df8-9bfd-ce5d3f370aed" />


    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

### Example 2:

<img width="322" height="242" alt="image" src="https://github.com/user-attachments/assets/203bc856-31d7-4d4b-9379-07534811f33a" />

    
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

### Example 3:

<img width="322" height="242" alt="image" src="https://github.com/user-attachments/assets/e8916e0f-ca73-42a6-99be-6e2b1a3298b5" />

    
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
 

## Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

--------------------------------------------------------------------------------------------------------------------------

# solution
```python
class Solution:
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            if index == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "*"

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            board[r][c] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

    ```
