# Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

### Example 1:

<img width="277" height="302" alt="image" src="https://github.com/user-attachments/assets/ebc1cc4b-4d8c-422b-ab48-9f8bda1f3f90" />


    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

### Example 2:

    Input: root = [1]
    Output: [[1]]

### Example 3:

    Input: root = []
    Output: []
 

## Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```PYTHON
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mp = {}

        def dfs(level, node):
            if node is None:
                return
            
            if level not in mp:
                mp[level] = []
            
            mp[level].append(node.val)

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)
        ans = []
        for i in range(len(mp)-1,-1,-1):
            ans.append(mp[i])

        return ans
```
