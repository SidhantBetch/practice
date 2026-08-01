# Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

### Example 1:

    Input: root = [1,null,2,3]
    
    Output: [1,2,3]

Explanation:

<img width="254" height="335" alt="image" src="https://github.com/user-attachments/assets/a597a7ce-fc64-4ec7-8d35-9992590d04cd" />



### Example 2:

    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    
    Output: [1,2,4,5,6,7,3,8,9]

Explanation:

<img width="524" height="428" alt="image" src="https://github.com/user-attachments/assets/afaf1caf-7b3b-45bc-8692-ff5ff1c96925" />


### Example 3:

    Input: root = []
    
    Output: []


## Example 4:

    Input: root = [1]
    
    Output: [1]

 

## Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

---------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def backtraking(node):
            if node is None:
                return
            
            ans.append(node.val)
            backtraking(node.left)
            backtraking(node.right)
        
        backtraking(root)
        
        return ans

```
