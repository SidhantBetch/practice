# Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

### Example 1:

<img width="277" height="302" alt="image" src="https://github.com/user-attachments/assets/a0e1b855-a7e8-4c97-88b2-7c82ebc44e63" />

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

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
```python
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        mp = defaultdict(list)
        
        def dfs(node,level):
            if node is None:
                return
            
            mp[level].append(node.val)

            dfs(node.left,level+1)
            dfs(node.right,level+1)

        dfs(root,0)
        
        ans = []

        for key, lst in mp.items():
            ans.append(lst[:])

        return ans

            

            

```
