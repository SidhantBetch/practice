# Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

### Example 1:

<img width="432" height="302" alt="image" src="https://github.com/user-attachments/assets/040ddfd5-5992-4731-b2ba-a102de88c6a7" />


    Input: root = [3,9,20,null,null,15,7]
    Output: 2

### Example 2:

    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5
 

## Constraints:
- The number of nodes in the tree is in the range [0, 105].
- -1000 <= Node.val <= 1000

----------------------------------------------------------------------------------------------------------------------------------------------

# Soluton
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def find(node, level):

            if node is None:
                return float('inf')

            # leaf node
            if node.left is None and node.right is None:
                return level

            left = find(node.left, level + 1)
            right = find(node.right, level + 1)

            return min(left, right)

        return find(root, 1)
```
