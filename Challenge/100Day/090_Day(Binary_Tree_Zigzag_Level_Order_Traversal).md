# Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

### Example 1:

<img width="277" height="302" alt="image" src="https://github.com/user-attachments/assets/62ef1e12-2996-440c-8e88-19e6542b20d0" />


    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

### Example 2:

    Input: root = [1]
    Output: [[1]]

### Example 3:

    Input: root = []
    Output: []
 

## Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        mp = {}
        
        def dfs(level, node):
            if node is None:
                return
            
            if level not in mp:
                mp[level] = []

            mp[level].append(node.val)
            
            dfs(level+1,node.left)
            dfs(level+1,node.right)
            
        dfs(0,root)
        ans = []

        for key,j in mp.items():
            if key % 2 == 0:
                ans.append(j)
            else:
                ans.append(j[::-1])


        return ans
                


```
