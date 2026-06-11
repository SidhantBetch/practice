# Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

### Example 1:

<img width="322" height="242" alt="image" src="https://github.com/user-attachments/assets/28c9c8d3-1025-47b6-a076-c13de373165b" />


    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

### Example 2:

<img width="322" height="242" alt="image" src="https://github.com/user-attachments/assets/bdd01ed9-d79f-4a09-a114-148f694e074f" />


    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
 

## Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -104 <= matrix[i][j], target <= 104

--------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])*len(matrix) 
        print("left: ",left,"& right: ",right)
        print("while:-")
        

        while(left < right):
            mid = (left + right) // 2

            y = mid % len(matrix[0])
            x = mid // len(matrix[0])
            
            if matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                return True
            print("left: ",left,"& right: ",right,"matrix: ",matrix[x][y])
        
        return False
```
