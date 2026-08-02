# Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

### Example 1:

    Input: root = [1,null,2,3]
    
    Output: [3,2,1]

Explanation:

<img width="254" height="335" alt="image" src="https://github.com/user-attachments/assets/9f1d0c6f-31c0-4b36-b870-dad5012967a1" />


### Example 2:

    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    
    Output: [4,6,7,5,2,9,8,3,1]

Explanation:

<img width="524" height="428" alt="image" src="https://github.com/user-attachments/assets/81b5d170-b26c-4c66-a18f-b945e529d702" />


### Example 3:

    Input: root = []
    
    Output: []


### Example 4:

    Input: root = [1]
    
    Output: [1]

 

## Constraints:
- The number of the nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def postorder(node):
            if node is None:
                return

            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)
        
        postorder(root)
        return ans

```
