# Recover Binary Search Tree

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

### Example 1:

<img width="422" height="302" alt="image" src="https://github.com/user-attachments/assets/3b39ef02-aee0-49b4-b422-99f11e1461f5" />

    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

### Example 2:

<img width="581" height="302" alt="image" src="https://github.com/user-attachments/assets/0f4bcb24-957c-4540-9010-99237b07dc47" />

    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

## Constraints:
- The number of nodes in the tree is in the range [2, 1000].
- -231 <= Node.val <= 231 - 1

----------------------------------------------------------------------------------------------------------------------------------------------

# Solution
```python
class Solution:
    def recoverTree(self, root):

        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev.val > node.val:

                if self.first is None:
                    self.first = self.prev

                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val
```
 
