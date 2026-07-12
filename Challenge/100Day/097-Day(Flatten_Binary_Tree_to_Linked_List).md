# Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

### Example 1:

<img width="1021" height="461" alt="image" src="https://github.com/user-attachments/assets/98f9de24-e22f-4b2f-bae9-06e4ce2a1c32" />


    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

### Example 2:

    Input: root = []
    Output: []

### Example 3:

    Input: root = [0]
    Output: [0]
 

## Constraints:
- The number of nodes in the tree is in the range [0, 2000].
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        ans = []
        def backtrack(node):
            nonlocal ans

            if node is None:
                return

            if node in ans:
                return
            
            ans.append(node)
            
            backtrack(node.left)
            backtrack(node.right)
        backtrack(root)
        
        temp = root
        for i in ans:
            temp.right = i
            temp.left = None
            temp = temp.right
            temp.right = None
        
        


        
```
