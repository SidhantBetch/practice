# Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

### Example 1:

<img width="641" height="241" alt="image" src="https://github.com/user-attachments/assets/9a9edd8b-e30d-427f-b6f1-e9722bd1b563" />

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]


### Example 2:

<img width="791" height="241" alt="image" src="https://github.com/user-attachments/assets/293d3c14-34c3-4d67-98e9-391bd305362e" />
    
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -231 <= matrix[i][j] <= 231 - 1

------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        stack = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i, j))
        
        while stack:
            i,j = stack.pop()

            for k in range(0,n):
                matrix[i][k] = 0
            for l in range(m):
                matrix[l][j] = 0
```
