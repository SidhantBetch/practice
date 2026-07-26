# Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


<img width="260" height="240" alt="image" src="https://github.com/user-attachments/assets/d5f02510-2f59-4f4d-84af-efba3ce93fe2" />

 

### Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]

### Example 2:

    Input: rowIndex = 0
    Output: [1]

### Example 3:

    Input: rowIndex = 1
    Output: [1,1]
 

## Constraints:
- 0 <= rowIndex <= 33

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = []

        def pascal(level):

            if level > rowIndex:
                return

            temp = []

            for i in range(level + 1):

                if i == 0 or i == level:
                    temp.append(1)
                else:
                    temp.append(ans[level-1][i-1] + ans[level-1][i])

            ans.append(temp)

            pascal(level + 1)

        pascal(0)

        return ans[-1]
```
