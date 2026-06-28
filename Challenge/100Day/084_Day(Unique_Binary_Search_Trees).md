# Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

### Example 1:

<img width="901" height="222" alt="image" src="https://github.com/user-attachments/assets/763a8a86-556b-49a5-b03a-5417419528f2" />

    Input: n = 3
    Output: 5

### Example 2:

    Input: n = 1
    Output: 1
 

## Constraints:
- 1 <= n <= 19

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def numTrees(self, n: int):

        memo = {}

        def count(start, end):
            if start >= end:
                return 1

            if (start, end) in memo:
                return memo[(start, end)]

            ans = 0

            for root in range(start, end + 1):
                left = count(start, root - 1)
                right = count(root + 1, end)

                ans += left * right

            memo[(start, end)] = ans
            return ans

        return count(1, n)

```
