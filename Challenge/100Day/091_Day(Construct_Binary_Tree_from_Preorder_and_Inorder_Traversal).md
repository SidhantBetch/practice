# Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

### Example 1:

<img width="277" height="302" alt="image" src="https://github.com/user-attachments/assets/d123a39b-639d-4c9d-8920-5266f2b87870" />


    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

### Example 2:

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]
 

## Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        sep = inorder.index(preorder[0])

        root.left = self.buildTree(
            preorder[1:sep+1],
            inorder[:sep]
        )

        root.right = self.buildTree(
            preorder[sep+1:],
            inorder[sep+1:]
        )

        return root
```
