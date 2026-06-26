# Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

### Example 1:

<img width="901" height="222" alt="image" src="https://github.com/user-attachments/assets/5059ffd7-668a-4c3b-b2b8-69924aebd423" />


    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

### Example 2:

    Input: n = 1
    Output: [[1]]
 

## Constraints:
- 1 <= n <= 8

--------------------------------------------------------------------------------------------------------------------------------------------

# Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            trees = []

            for rootVal in range(start, end + 1):
                leftTrees = build(start, rootVal - 1)
                rightTrees = build(rootVal + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(rootVal)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)

            
```
