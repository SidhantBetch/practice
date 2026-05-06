# 🐦‍🔥 Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

### 🕖 Example 1:

            1
          /   \
         2     2
        / \   / \
       3   4 4   3
    
    Input: root = [1,2,2,3,4,4,3]
    Output: true
    
### 🕖 Example 2:

            1
          /   \
         2     2
          \     \
           3     3
    
    Input: root = [1,2,2,null,3,null,3]
    Output: false
     

## 🎡 Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

---------------------------------------------------------------------------------------------------------------------

# 🚐 Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            Lnode, Rnode = stack.pop()

            if Lnode is None and Rnode is None:
                continue

            if Lnode is None or Rnode is None:
                return False

            if Lnode.val != Rnode.val:
                return False

            stack.append((Lnode.left, Rnode.right))
            stack.append((Lnode.right, Rnode.left))

        return True
```
