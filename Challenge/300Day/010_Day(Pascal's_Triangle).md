# Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

<img width="260" height="240" alt="image" src="https://github.com/user-attachments/assets/3ad99cfa-320a-4678-8091-941b3c9d7f4b" />


### Example 1:

    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
### Example 2:

    Input: numRows = 1
    Output: [[1]]
 

## Constraints:
- 1 <= numRows <= 30

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        def pascal(level):
            if numRows == level:
                return
            
            temp = []
            
            for i in range(level+1):
                if i == 0:
                    temp.append(1)
                
                if i > 0 and i < level:
                    val = ans[level- 1][i-1] + ans[level-1][i]
                    temp.append(val)
                
                if i == level-1:
                    temp.append(1)

            ans.append(temp[:])
            pascal(level + 1)

        pascal(0)
        
        return ans
```
