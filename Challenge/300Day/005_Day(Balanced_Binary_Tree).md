# Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

 

### Example 1:

<img width="342" height="221" alt="image" src="https://github.com/user-attachments/assets/3819cea4-c7a7-422b-9ccd-e51866427850" />
    
    Input: root = [3,9,20,null,null,15,7]
    Output: true

### Example 2:

<img width="452" height="301" alt="image" src="https://github.com/user-attachments/assets/4f6e992c-feaf-4b87-8ed1-6162219296ca" />
    
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

### Example 3:
    
    Input: root = []
    Output: true
 

## Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -104 <= Node.val <= 104

----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if node is None:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1
        

```
