# Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

### Example 1:

<img width="277" height="302" alt="image" src="https://github.com/user-attachments/assets/127b47f3-ca88-42b6-ad57-ca0240049a1c" />


    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]

### Example 2:

    Input: inorder = [-1], postorder = [-1]
    Output: [-1]
 

## Constraints:
- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of unique values.
- Each value of postorder also appears in inorder.
- inorder is guaranteed to be the inorder traversal of the tree.
- postorder is guaranteed to be the postorder traversal of the tree.

-----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])

        sep = inorder.index(postorder[-1])

        left_size = sep

        root.left = self.buildTree(
            inorder[:sep],
            postorder[:left_size]
        )

        root.right = self.buildTree(
            inorder[sep+1:],
            postorder[left_size:-1]
        )

        return root
```
