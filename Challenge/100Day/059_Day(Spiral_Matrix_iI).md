# 🐦‍🔥 Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

### 🎡 Example 1:

  1 ➡️  2 ➡️  3 
              ⬇️
   8 ➡️ 9     4
  ⬆️         ⬇️
   7 ⬅️ 6 ⬅️ 5


    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

### 🎡 Example 2:

    Input: n = 1
    Output: [[1]]
 

## 🤦🏻 Constraints:
- 1 <= n <= 20

------------------------------------------------------------------------------------------------------------------

# 🍟 Solution
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        count = 1
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(count)
                count += 1
            ans.append(temp[:])
        
        trow = 0
        brow = n-1
        rcol = n-1
        lcol = 0
        count = 1

        
        while(trow <= brow and lcol <= lcol):
            # work on top row
            for j in range(lcol,rcol+1):
                if ans[trow][j] != count:
                    ans[trow][j] = count
                count += 1
            trow += 1
            if trow > brow:
                break
            
            # work on Right Column
            for j in range(trow,brow+1):
                if ans[j][rcol] != count:
                    ans[j][rcol] = count
                count += 1
            rcol -= 1
            if lcol > rcol:
                break

            # work on bootm row
            for j in range(rcol,lcol-1,-1):
                if ans[brow][j] != count:
                    ans[brow][j] = count
                count += 1
            brow -= 1
            if trow > brow:
                break

            # work on left column
            for j in range(brow,trow-1,-1):
                if ans[j][lcol] != count:
                    ans[j][lcol] = count
                count += 1
            lcol += 1
            if lcol > rcol:
                break
            
        
        return ans
```
