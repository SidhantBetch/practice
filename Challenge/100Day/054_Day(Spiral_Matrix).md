# 🤦🏻 Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

 

### 📚 Example 1:

      1 ➡️ 2 ➡️ 3
                ⬇️
      4 ➡️ 5    6
     ⬆️        ⬇️
      7 ⬅️ 8 ⬅️ 9
    
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

### 📚 Example 2:

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

## 🚐 Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

-------------------------------------------------------------------------------------------------------------------

# ⚓ Solution
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        frow = 0
        lrow = len(matrix)

        fcolumn = 0
        lcolumn = len(matrix[0])

        count = 0
        total = len(matrix) * len(matrix[0])

        while count < total:

            # Left → Right
            for i in range(fcolumn, lcolumn):
                ans.append(matrix[frow][i])
                count += 1

            frow += 1

            if count == total:
                break

            # Top → Bottom
            for i in range(frow, lrow):
                ans.append(matrix[i][lcolumn - 1])
                count += 1

            lcolumn -= 1

            if count == total:
                break

            # Right → Left
            for i in range(lcolumn - 1, fcolumn - 1, -1):
                ans.append(matrix[lrow - 1][i])
                count += 1

            lrow -= 1

            if count == total:
                break

            # Bottom → Top
            for i in range(lrow - 1, frow - 1, -1):
                ans.append(matrix[i][fcolumn])
                count += 1

            fcolumn += 1

        return ans
```
